input.onButtonPressed(Button.A, function () {
    if (Age <= 1 && Times_Fed >= 10) {
        Stuff = 0
        music.playMelody("D E F G - - G - ", 388)
        basic.showLeds(`
            . . . . .
            . . # # .
            . . # # .
            . . . . .
            . . . . .
            `)
        music.playMelody("D E F A - - A - ", 388)
        basic.showLeds(`
            . . # # .
            . # # # #
            . # # # #
            . . # # .
            . . . . .
            `)
        music.playMelody("D E F B - - B - ", 388)
        basic.showLeds(`
            . . # # .
            . # # . #
            . # . # #
            . . # # .
            . . . . .
            `)
        music.playMelody("D E F C5 - - C5 - ", 388)
        basic.showLeds(`
            . . # # .
            . # . . #
            . # . . #
            . . # # .
            . . . . .
            `)
        music.playMelody("C - D - E - G G ", 388)
        basic.showLeds(`
            . # # # .
            # . . . #
            # . . . #
            # . . . #
            . # # # .
            `)
        music.playMelody("C5 B A B A B C5 C5 ", 388)
        Times_Fed = 0
        Age += 1
        Stuff = 1
    }
})
input.onButtonPressed(Button.B, function () {
    Stuff = 0
    if (Age <= 1) {
        basic.showString("Hungry:")
        music.playTone(262, music.beat(BeatFraction.Whole))
        if (Hungry < 10) {
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                `)
        }
        if (Hungry > 10) {
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . # # # .
                `)
        }
        if (Hungry > 30) {
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . # # # .
                . # # # .
                `)
        }
        if (Hungry > 50) {
            basic.showLeds(`
                . . . . .
                . . . . .
                . # # # .
                . # # # .
                . # # # .
                `)
        }
        if (Hungry > 70) {
            basic.showLeds(`
                . . . . .
                . # # # .
                . # # # .
                . # # # .
                . # # # .
                `)
        }
        if (Hungry > 90) {
            basic.showLeds(`
                . # # # .
                . # # # .
                . # # # .
                . # # # .
                . # # # .
                `)
        }
        basic.pause(4000)
    }
    Stuff = 1
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    if (Age <= 1) {
        Stuff = 0
        basic.showString("Yummy!")
        music.playMelody("B - - B A E - - ", 388)
        basic.showLeds(`
            . # # # .
            # # # # #
            . # # # .
            . # . # .
            . # . # .
            `)
        basic.showLeds(`
            # # # # #
            . # # # .
            . # # # .
            . # . # .
            . # . # .
            `)
        basic.showLeds(`
            # # # # #
            . # # # .
            . # # # .
            # # . # .
            . . . # .
            `)
        Hungry = 0
        Stuff = 1
        Times_Fed += 1
    }
})
let Times_Fed = 0
let Stuff = 0
let Hungry = 0
let Age = 0
Age = 0
Hungry = 0
Stuff = 1
Times_Fed = 0
basic.forever(function () {
    if (Stuff == 1) {
        if (Age == 0) {
            basic.showLeds(`
                . . # . .
                . # . # .
                # . . . #
                # . . . #
                . # # # .
                `)
            basic.showLeds(`
                . . # . .
                . # . # .
                # . # . #
                # . # . #
                . # # # .
                `)
        }
        if (Age == 1) {
            if (Hungry < 70) {
                basic.showLeds(`
                    . . # . .
                    . . # . .
                    # # # # #
                    . . # . .
                    . . # . .
                    `)
                basic.showLeds(`
                    . . . . .
                    . . # . .
                    . # # # .
                    . . # . .
                    . . . . .
                    `)
                Hungry += 1
            }
            if (Hungry >= 70) {
                basic.showLeds(`
                    . # . # .
                    . # . # .
                    . # # # .
                    . # # # .
                    . # # # .
                    `)
                basic.showLeds(`
                    . # . # .
                    . # . # .
                    . # # # .
                    . # . # .
                    . # . # .
                    `)
                music.playTone(262, music.beat(BeatFraction.Whole))
                Hungry += 1
            }
        }
        if (Age == 2) {
            if (Hungry < 70) {
                basic.showLeds(`
                    . # # # .
                    # . . . #
                    # . # # #
                    # . # # #
                    . # # # .
                    `)
                basic.showLeds(`
                    . # # # .
                    # . . . #
                    # # # . #
                    # # # . #
                    . # # # .
                    `)
                Hungry += 1
            }
            if (Hungry >= 70) {
                basic.showLeds(`
                    . # # # .
                    # . . . #
                    # . . . #
                    # . . . #
                    . # # # .
                    `)
                basic.showLeds(`
                    # # . # #
                    # # . # #
                    # # . # #
                    # . # . #
                    . # # # .
                    `)
                music.playTone(262, music.beat(BeatFraction.Whole))
                Hungry += 1
            }
        }
    }
})
