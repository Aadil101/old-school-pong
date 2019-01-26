#Lab 1 - Checkpoint
#Aadil Islam
#January 21, 2017
#CS 1

from cs1lib import *

#constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

#more constants, adjust as you please!
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 80
PADDLE_MOVEMENT = 5

#initial left/right paddle coordinates
l_x = 0
l_y = 0
r_x = WINDOW_WIDTH - PADDLE_WIDTH
r_y = WINDOW_HEIGHT - PADDLE_HEIGHT

#track state of directional keys
is_a_pressed = False
is_z_pressed = False
is_k_pressed = False
is_m_pressed = False

#identify a pressed key
def keypress(key):

    global is_a_pressed, is_z_pressed, is_k_pressed, is_m_pressed

    if key == 'a':
        is_a_pressed = True
    elif key == 'z':
        is_z_pressed = True
    elif key == 'k':
        is_k_pressed = True
    elif key == 'm':
        is_m_pressed = True
    else:
        print("Invalid input, try again.")

#identify when user lets go of key, or else paddle just keeps moving!
def keyrelease(key):

    global is_a_pressed, is_z_pressed, is_k_pressed, is_m_pressed

    if key == 'a':
        is_a_pressed = False
    elif key == 'z':
        is_z_pressed = False
    elif key == 'k':
        is_k_pressed = False
    elif key == 'm':
        is_m_pressed = False

def graphics():

    global l_y,r_y

    #create black background
    set_clear_color(0,0,0)
    clear()

    #if this key is pressed...
    if is_a_pressed:

        #...check if paddle is too close to top of window...
        if l_y >= PADDLE_MOVEMENT:

            #...if not too close, move up
            l_y -= PADDLE_MOVEMENT

    if is_z_pressed:

        #...check if paddle is too close to bottom of window...
        if (l_y + PADDLE_HEIGHT + PADDLE_MOVEMENT <= WINDOW_HEIGHT):

            # ...if not too close, move down
            l_y += PADDLE_MOVEMENT

    if is_k_pressed:

        #...check if paddle is too close to top of window...
        if r_y >= PADDLE_MOVEMENT:

            # ...if not too close, move up
            r_y -= PADDLE_MOVEMENT

    if is_m_pressed:

        # ...check if paddle is too close to bottom of window...
        if (r_y + PADDLE_HEIGHT + PADDLE_MOVEMENT <= WINDOW_HEIGHT):

            # ...if not too close, move down
            r_y += PADDLE_MOVEMENT

    set_fill_color(1,0,0)

    #draw red left paddle
    draw_rectangle(l_x,l_y,PADDLE_WIDTH,PADDLE_HEIGHT)

    # draw red right paddle
    draw_rectangle(r_x,r_y, PADDLE_WIDTH, PADDLE_HEIGHT)

start_graphics(graphics, 2400, key_press=keypress, key_release=keyrelease)