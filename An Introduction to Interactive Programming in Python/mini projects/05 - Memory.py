# implementation of card game - Memory

import simplegui
import random

num_list = []
exposed = []
state = 0
current = 0
previous = 0
turns = 0

def new_game():
    global current, exposed, num_list, previous, state
    list1 = range(0,8)
    list2 = range(0,8)
    num_list = list1 + list2
    random.shuffle(num_list)
    exposed = [False] * 16
    state = 0
    current = None
    previous = None
    turns = 0
     
# define event handlers
def mouseclick(pos):
    global current, exposed, previous, state, turns
    clicked = pos[0]/50
    if not exposed[clicked]:
        if state == 0:
            state = 1
            current = clicked
        elif state == 1:
            state = 2
            previous, current = current, clicked
            turns += 1
        else:
            if (num_list[previous] != num_list[current]):
                exposed[current] = False
                exposed[previous] = False
            current = clicked
            state = 1
    
    if not exposed[clicked]:
        exposed[clicked] = True
    print state, current, previous
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    card_x = 0
    card_y = 0
    width = 50
    height = 100
    txt_x_pos = 20
    txt_y_pos = 60
    for idx, num in enumerate(num_list):
        if (exposed[idx]):
            canvas.draw_polygon([(card_x, card_y), 
                                 (card_x + width, card_y),
                                 (card_x + width, card_y + height), 
                                 (card_x, card_y + height)], 1, 'White')
            canvas.draw_text(str(num), [txt_x_pos, txt_y_pos], 20, 'White')
        else:
            canvas.draw_polygon([(card_x, card_y), 
                                 (card_x + width, card_y),
                                 (card_x + width, card_y + height), 
                                 (card_x, card_y + height)], 1, 'White', 'Green')
        card_x += 50
        txt_x_pos += 50
    label.set_text("Turns = " + str(turns))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric