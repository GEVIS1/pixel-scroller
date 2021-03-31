xy = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
# Set default LED position to be the middle
count = 12


def on_button_pressed_a():
    global count
    
    # Check if count is 0 and if it is wrap around to 24
    if (count == 0):
        count = 24
        pass
    else:
        --count   
        pass
    pass

def on_button_pressed_b():
    global count  
    
    # Check if count is 24 and if it is wrap around to 0
    if (count == 24):
        count = 0
        pass 
    else:
        ++count
        pass
pass

def main():
    global count
    basic.clear_screen()

    input.on_button_pressed(Button.A, on_button_pressed_a)
    input.on_button_pressed(Button.B, on_button_pressed_b)
    
    # Iterate all the possible LEDs 
    # and turn it on if the count is up to that LED from origin 0,0 in the top left corner.
    for y in range(5):
        for x in range(5):
            if (count == x + (y * 5)):
                led.plot(x, y)
                pass
            pass
        pass
    pass
basic.forever(main)