label start:
    "Welcome brave adventurer..."
    goto a01 start

label a01:

    trans bg a01

    if LastScreen == 'start':
        $TextBuffer = "You awaken in a small room smelling of rust. There are two doors in front of you, one to the west and one to the east."
    else:
        $TextBuffer = "Back at the room you awoke in, two doors lay before you. One to the west, the other to the east."

    "[TextBuffer]"

    menu:
        "head to the west.":
            call opendoor
            goto a04 a01

        "head to the east.":
            call opendoor
            goto a07 a01

        "Pull sword from stone.":
            window hide
            $ quick_menu = False
            $ TimesSwordGameAttempted += 1
            call screen swordGame( SwordMiniGame("sword", 250, 250, (30)))
            window show
            $ quick_menu = True
            if _return == True:
                $renpy.pause(1, hard = True)
            goto a01 a01

        "Open Inventory":
            call Inventory
            if _return == "test flag":
                "You did it!"
            goto a01 a01

label a04:

    trans bg a04

    if LastScreen == 'a01':
        $TextBuffer = "After heading west for some time you stop as the hallway veers to the north."
    elif LastScreen == 'a08':
        $TextBuffer = "After heading south for some time you stop as the hallway veers to the east."

    if GotOrbBlue == True:
        $TextBuffer += "To the east is the alter where the blue orb once lay."
    else:
        $TextBuffer += "To the east is a blue orb on top of an alter. You hear a faint humming comming from the orb."

    "[TextBuffer]"

    if GotOrbBlue == True:
        menu:
            "Head to the north.":
                call gohall
                goto a08 a04
            "Head to the east.":
                goto a01 a04
    else:
        menu:
            "Head to the north.":
                call gohall
                goto a08 a04
            "Head to the east.":
                goto a01 a04
            "Pick up the orb.":
                "As you touch the blue orb, a warm sensation hits your hand an start to travel up your body."
                "Got blue orb."
                $GotOrbBlue = True
                goto a04 a04

label a07:

    trans bg a07

    if LastScreen == 'a01':
        $TextBuffer = "You follow the hall to the east for some time before following it as it veers to the north. "
    elif LastScreen == 'a08':
        $TextBuffer == "You head to the east for some time before stopping as the path veers to the south. "

    if GotOrbGreen == False:
        $TextBuffer += "To the north sits a green orb on top of an alter."
    else:
        $TextBuffer += "To the north sits the alter where the green orb once lay."

    "[TextBuffer]"

    if GotOrbGreen == False:
        menu:
            "Pick up the orb.":
                "Energy courses though your vains as you pick up the orb."
                "Got orb."
                $GotOrbGreen = True
                goto a07 a07
            "Head to the west.":
                call gohall
                goto a08 a07
            "Head to the south.":
                goto a01 a07
    else:
        menu:
            "Head to the west.":
                call gohall
                goto a08 a07
            "Head to the south.":
                goto a01 a07

label a08:

    trans bg a08

    if LastScreen == 'a07':
        $TextBuffer = "After heading south "
    if LastScreen == 'a04':
        $TextBuffer = "After heading east "

    $TextBuffer += "you come to a large door to the north. Two circular alcoves sit beside the door, one on each side."

    "[TextBuffer]"

    if GotOrbGreen == True and GotOrbBlue == True:
        menu:
            "Head to the east":
                call gohall
                goto a07 a08
            "Head to the west":
                call gohall
                goto a04 a08
            "Insert orbs":
                "The orbs click into place, one in each of the alcoves."
                "The door slowly opens, as glorious sunlight blinds you."
                goto a09 a08
    else:
        menu:
            "Head to the east":
                call gohall
                goto a07 a08
            "Head to the west":
                call gohall
                goto a04 a08

label a09:

    trans bg a09
    "You are winner!!!"

return
