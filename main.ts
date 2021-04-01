let xy = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
let count = 0
basic.forever(function main() {
    
    input.onButtonPressed(Button.A, function on_button_pressed_a() {
        
        //  Check if count is 0 and if it is wrap around to 24
        if (count == 0) {
            count = 24
        } else {
            --count
        }
        
    })
    input.onButtonPressed(Button.B, function on_button_pressed_b() {
        
        //  Check if count is 24 and if it is wrap around to 0
        if (count == 24) {
            count = 0
        } else {
            ++count
        }
        
    })
    //  Iterate all the possible LEDs 
    //  and turn it on if the count is up to that LED from origin 0,0 in the top left corner.
    for (let x = 0; x < 5; x++) {
        for (let y = 0; y < 5; y++) {
            // TODO
            
        }
    }
})
