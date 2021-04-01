xy = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
count = 0


def on_button_pressed_a():
    global count
    
    # Check if count is 0 and if it is wrap around to 24
    if (count == 0):
        count = 24
    else:
        --count   
        

def on_button_pressed_b():
    global count  
    
    # Check if count is 24 and if it is wrap around to 0
    if (count == 24):
        count = 0
    else:
        ++count
        
def main():
    global count

    input.on_button_pressed(Button.A, on_button_pressed_a)
    input.on_button_pressed(Button.B, on_button_pressed_b)
    
    # Iterate all the possible LEDs 
    # and turn it on if the count is up to that LED from origin 0,0 in the top left corner.
    for x in range(5):
        for y in range(5):
            #TODO
            pass
            

       

basic.forever(main)