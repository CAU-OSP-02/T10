## Screen with Stats Button
screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/minimap_%s.png"
        action ShowMenu("MapUI")

## Stats UI
screen MapUI():
    tag statusUI
    add "map/bg map.png"

    imagebutton:
        xpos 388
        ypos 113
        idle "map/shoppingmall_idle.png"
        hover "map/shoppingmall_hover.png"
        action Jump("shoppingmall_pressed")

    imagebutton:
        xpos 59
        ypos 268
        idle "map/concert_idle.png"
        hover "map/concert_hover.png"
        action Jump("concert_pressed")

    imagebutton:
        xpos 1006
        ypos 323
        idle "map/PCroom_idle.png"
        hover "map/PCroom_hover.png"
        action Jump("PCroom_pressed")

    imagebutton:
        xpos 721
        ypos 48
        idle "map/theater_idle.png"
        hover "map/theater_hover.png"
        action Jump("theater_pressed")