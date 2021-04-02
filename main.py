xy = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
# Set default LED position to be the middle
count = 0


def on_button_pressed_a():
    global count
    
    basic.clear_screen()

    # Check if count is -1 and if it is wrap around to 25
    if (count == -1):
        count = 25
    else:
        --count

def on_button_pressed_b():
    global count  
    
    basic.clear_screen()

    # Check if count is 25 and if it is wrap around to 0
    if (count == 25):
        count = 0
    else:
        ++count
pass

def main():
    global count

    input.on_button_pressed(Button.A, on_button_pressed_a)
    input.on_button_pressed(Button.B, on_button_pressed_b)
    
    # Iterate all the possible LEDs 
    # and turn it on if the count is up to that LED from origin 0,0 in the top left corner.
    for y in range(5):
        for x in range(5):
            for i in range(count):
                led.plot(i % 5, i / 5)
            
        
    
basic.forever(main)