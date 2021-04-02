let xy = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
//  Set default LED position to be the middle
let count = 12
function plotLeds() {
    let j: number;
    for (let i = 0; i < xy.length; i++) {
        if (i <= count / 5) {
            if (i == (count - count % 5) / 5) {
                //  (count - (count % 5) ) / 5) is equal to the integer part of the division
                for (j = 0; j < count % 5; j++) {
                    led.plot(j, i)
                }
            } else {
                for (j = 0; j < xy[i].length; j++) {
                    led.plot(j, i)
                }
            }
            
        }
        
    }
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.clearScreen()
    
    count -= 1
    if (count <= 0) {
        count = 25
    }
    
    plotLeds()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.clearScreen()
    
    ++count
    if (count >= 26) {
        count = 1
    }
    
    plotLeds()
})
