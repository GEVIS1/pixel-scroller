let xy = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
//  Set default LED position to be the middle
let count = 0

basic.forever(function main() {
    
    input.onButtonPressed(Button.A, function on_button_pressed_a() {
        
        basic.clearScreen()
        //  Check if count is -1 and if it is wrap around to 25
        if (count == -1) {
            count = 25
        } else {
            --count
        }
        
    })
    input.onButtonPressed(Button.B, function on_button_pressed_b() {
        
        basic.clearScreen()
        //  Check if count is 25 and if it is wrap around to 0
        if (count == 25) {
            count = 0
        } else {
            ++count
        }
        
    })
    //  Iterate all the possible LEDs 
    //  and turn it on if the count is up to that LED from origin 0,0 in the top left corner.
    for (let y = 0; y < 5; y++) {
        for (let x = 0; x < 5; x++) {
            for (let i = 0; i < count; i++) {
                led.plot(i % 5, i / 5)
            }
        }
    }
})
