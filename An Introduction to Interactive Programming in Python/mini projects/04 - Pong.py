# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
paddle1_pos = [[0, HEIGHT/2 - PAD_HEIGHT/2], [PAD_WIDTH, HEIGHT/2 - PAD_HEIGHT/2],
              [PAD_WIDTH, HEIGHT/2 + PAD_HEIGHT/2], [0, HEIGHT/2 + PAD_HEIGHT/2]]
paddle2_pos = [[WIDTH, HEIGHT/2 - PAD_HEIGHT/2], [WIDTH - PAD_WIDTH, HEIGHT/2 - PAD_HEIGHT/2],
              [WIDTH - PAD_WIDTH, HEIGHT/2 + PAD_HEIGHT/2], [WIDTH, HEIGHT/2 + PAD_HEIGHT/2]]
paddle1_vel = 0
paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction = 'RIGHT'):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == 'RIGHT':
        ball_vel[0] = random.randrange(120, 240) / 60
        ball_vel[1] = -random.randrange(60, 180) / 60
    elif direction == 'LEFT':
        ball_vel[0] = -random.randrange(120, 240) / 60
        ball_vel[1] = -random.randrange(60, 180) / 60

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball('RIGHT')

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if ((ball_pos[1] - BALL_RADIUS) <= 0) or ((ball_pos[1] + BALL_RADIUS) >= HEIGHT):
        ball_vel[1] = -ball_vel[1]
        
    if ((ball_pos[0] - BALL_RADIUS) <= PAD_WIDTH):
        spawn_ball('RIGHT')
    elif ((ball_pos[0] + BALL_RADIUS) >= WIDTH - PAD_WIDTH):
        spawn_ball('LEFT')
        
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, 'White', 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    for pos in paddle1_pos:
        if ((paddle1_pos[0][1] > 0) and (paddle1_vel < 0)) or (paddle1_pos[-1][1] < HEIGHT and paddle1_vel > 0):
            pos[1] += paddle1_vel
        else:
            if paddle1_vel < 0:
                paddle1_pos[1][1] = 0
            elif paddle1_vel > 0:
                paddle1_pos[0][1] = HEIGHT - PAD_HEIGHT
                paddle1_pos[1][1] = HEIGHT - PAD_HEIGHT
                
    for pos in paddle2_pos:
        if ((paddle2_pos[0][1] > 0) and (paddle2_vel < 0)) or (paddle2_pos[-1][1] < HEIGHT and paddle2_vel > 0):
            pos[1] += paddle2_vel
        else:
            if paddle2_vel < 0:
                paddle2_pos[1][1] = 0
            elif paddle2_vel > 0:
                paddle2_pos[0][1] = HEIGHT - PAD_HEIGHT
                paddle2_pos[1][1] = HEIGHT - PAD_HEIGHT
    
    # draw paddles
    canvas.draw_polygon(paddle1_pos, 2, 'White', 'White')
    canvas.draw_polygon(paddle2_pos, 2, 'White', 'White')
    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -10
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 10
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -10
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 10
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w'] or key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
