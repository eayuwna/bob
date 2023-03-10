def on_button_pressed_a():
    global Stuff, Times_Fed, Age
    if Age <= 2 and Times_Fed >= 10:
        Stuff = 0
        music.play_melody("D E F G - - G - ", 388)
        basic.show_leds("""
            . . . . .
                        . . # # .
                        . . # # .
                        . . . . .
                        . . . . .
        """)
        music.play_melody("D E F A - - A - ", 388)
        basic.show_leds("""
            . . # # .
                        . # # # #
                        . # # # #
                        . . # # .
                        . . . . .
        """)
        music.play_melody("D E F B - - B - ", 388)
        basic.show_leds("""
            . . # # .
                        . # # . #
                        . # . # #
                        . . # # .
                        . . . . .
        """)
        music.play_melody("D E F C5 - - C5 - ", 388)
        basic.show_leds("""
            . . # # .
                        . # . . #
                        . # . . #
                        . . # # .
                        . . . . .
        """)
        music.play_melody("C - D - E - G G ", 388)
        basic.show_leds("""
            . # # # .
                        # . . . #
                        # . . . #
                        # . . . #
                        . # # # .
        """)
        music.play_melody("C5 B A B A B C5 C5 ", 388)
        Times_Fed = 0
        Age += 1
        Stuff = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Stuff, Direction2
    if Age == 2:
        Stuff = 0
        basic.show_string("Game!")
        for index in range(4):
            basic.show_leds("""
                . # # # .
                                # . . . #
                                # . # # #
                                # . # # #
                                . # # # .
            """)
            basic.show_leds("""
                . # # # .
                                # . . . #
                                # # # . #
                                # # # . #
                                . # # # .
            """)
        while not (input.button_is_pressed(Button.A)) or input.button_is_pressed(Button.B):
            basic.show_leds("""
                . # # # .
                                # . . . #
                                # . # . #
                                # . . . #
                                . # # # .
            """)
            basic.show_leds("""
                . # # # .
                                # . . . #
                                # . . . #
                                # . . . #
                                . # # # .
            """)
        if input.button_is_pressed(Button.A):
            Direction2 = 0
        else:
            Direction2 = 1
        if Math.random_boolean():
            basic.show_leds("""
                . # # # .
                                # . . . #
                                # . # # #
                                # . # # #
                                . # # # .
            """)
        else:
            basic.show_leds("""
                . # # # .
                                # . . . #
                                # # # . #
                                # # # . #
                                . # # # .
            """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Stuff
    Stuff = 0
    if Age <= 2:
        basic.show_string("Hungry:")
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        if Hungry < 10:
            basic.show_leds("""
                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
            """)
        if Hungry > 10:
            basic.show_leds("""
                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
                                . # # # .
            """)
        if Hungry > 30:
            basic.show_leds("""
                . . . . .
                                . . . . .
                                . . . . .
                                . # # # .
                                . # # # .
            """)
        if Hungry > 50:
            basic.show_leds("""
                . . . . .
                                . . . . .
                                . # # # .
                                . # # # .
                                . # # # .
            """)
        if Hungry > 70:
            basic.show_leds("""
                . . . . .
                                . # # # .
                                . # # # .
                                . # # # .
                                . # # # .
            """)
        if Hungry > 90:
            basic.show_leds("""
                . # # # .
                                . # # # .
                                . # # # .
                                . # # # .
                                . # # # .
            """)
        basic.pause(4000)
    Stuff = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    global Stuff, Hungry, Times_Fed
    if Age <= 2:
        Stuff = 0
        basic.show_string("Yummy!")
        music.play_melody("B - - B A E - - ", 388)
        basic.show_leds("""
            . # # # .
                        # # # # #
                        . # # # .
                        . # . # .
                        . # . # .
        """)
        basic.show_leds("""
            # # # # #
                        . # # # .
                        . # # # .
                        . # . # .
                        . # . # .
        """)
        basic.show_leds("""
            # # # # #
                        . # # # .
                        . # # # .
                        # # . # .
                        . . . # .
        """)
        Hungry = 0
        Stuff = 1
        Times_Fed += 1
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

Direction2 = 0
Times_Fed = 0
Stuff = 0
Hungry = 0
Age = 0
Age = 0
Hungry = 0
Stuff = 1
Times_Fed = 0

def on_forever():
    global Hungry
    if Stuff == 1:
        if Age == 0:
            basic.show_leds("""
                . . # . .
                                . # . # .
                                # . . . #
                                # . . . #
                                . # # # .
            """)
            basic.show_leds("""
                . . # . .
                                . # . # .
                                # . # . #
                                # . # . #
                                . # # # .
            """)
        if Age == 1:
            if Hungry < 70:
                basic.show_leds("""
                    . . # . .
                                        . . # . .
                                        # # # # #
                                        . . # . .
                                        . . # . .
                """)
                basic.show_leds("""
                    . . . . .
                                        . . # . .
                                        . # # # .
                                        . . # . .
                                        . . . . .
                """)
                Hungry += 1
            if Hungry >= 70:
                basic.show_leds("""
                    . # . # .
                                        . # . # .
                                        . # # # .
                                        . # # # .
                                        . # # # .
                """)
                basic.show_leds("""
                    . # . # .
                                        . # . # .
                                        . # # # .
                                        . # . # .
                                        . # . # .
                """)
                music.play_tone(262, music.beat(BeatFraction.WHOLE))
                Hungry += 1
        if Age == 2:
            if Hungry < 70:
                basic.show_leds("""
                    . # # # .
                                        # . . . #
                                        # . # # #
                                        # . # # #
                                        . # # # .
                """)
                basic.show_leds("""
                    . # # # .
                                        # . . . #
                                        # # # . #
                                        # # # . #
                                        . # # # .
                """)
                Hungry += 1
            if Hungry >= 70:
                basic.show_leds("""
                    . # # # .
                                        # . . . #
                                        # . . . #
                                        # . . . #
                                        . # # # .
                """)
                basic.show_leds("""
                    # # . # #
                                        # # . # #
                                        # # . # #
                                        # . # . #
                                        . # # # .
                """)
                music.play_tone(262, music.beat(BeatFraction.WHOLE))
                Hungry += 1
basic.forever(on_forever)
