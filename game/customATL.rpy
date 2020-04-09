transform fadeout:
    on replaced:
        alpha 1.0
        linear 0.5 alpha 0.0

transform fadein:
    alpha 0.0
    linear 0.5 alpha 1.0

transform door01:
    "bg door01" with fade
    0.5
    "bg door02" with dissolve

image bg door:
    contains door01

label opendoor:
    show bg door
    pause 1.5
    return

transform hall01:
    "bg hall01" with fade
    0.5
    "bg hall02" with dissolve
    1
    "bg hall03" with dissolve

image bg hall:
    contains hall01

label gohall:
    show bg hall
    pause 3
    return

screen swordGame(sword_mini_game):
    add sword_mini_game
