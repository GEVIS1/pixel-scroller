xy = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
# Set default LED position to be the middle
count = 12 

def on_button_pressed_a():
    basic.clear_screen()
    global count
    count -= 1
    if count <= 0:
        count = 25
    plotLeds()
 
def on_button_pressed_b():
    basic.clear_screen()
    global count
    ++count
    if count >= 26:
        count = 1
    plotLeds()
 
def plotLeds():
    for i in range(len(xy)):
        if i <= (count / 5):
            if i == ((count - (count % 5) ) / 5): # (count - (count % 5) ) / 5) is equal to the integer part of the division
                for j in range(count % 5):
                    led.plot(j, i)
            else:
                for j in range(len(xy[i])):
                    led.plot(j, i)
 
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)