# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
attempts = 0
success  = 0
run = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    if (t == 0):
        return "0:00:0"
    tenths  = t % 10
    seconds = t / 10
    minutes = seconds / 60
    seconds = seconds - (minutes * 60)
    if (seconds < 10):
        seconds = '0' + str(seconds)
    return str(minutes) + ':' + str(seconds) + '.' + str(tenths)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global run, time
    run = True
    stopwatch.start()

def stop_handler():
    global attempts, run, success
    if (run == True):
        attempts += 1
        if (time % 10 == 0):
            success += 1
            
    run = False
    stopwatch.stop()
    
def reset_handler():
    global attempts, run, success, time
    run = False
    stopwatch.stop()
    attempts = 0
    success = 0
    time = 0
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global run, time
    if (run == True):
        time += 1

# define draw handler
def draw_handler(canvas):
    display_time = format(time)
    reflex_result = str(success) + '/' + str(attempts)
    canvas.draw_text(display_time, [100,100], 24, 'White')
    canvas.draw_text(reflex_result, [280,16], 16, 'White')
    
# create frame
frame = simplegui.create_frame('Stop Watch', 300, 300)

# register event handlers
frame.set_draw_handler(draw_handler)

stopwatch = simplegui.create_timer(100, timer_handler)

start = frame.add_button('Start', start_handler, 200)
stop  = frame.add_button('Stop' , stop_handler , 200)
reset = frame.add_button('Reset', reset_handler, 200)

# start frame
frame.start()

# Please remember to review the grading rubric
