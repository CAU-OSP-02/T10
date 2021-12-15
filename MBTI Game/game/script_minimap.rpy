label start:

    show screen gameUI
    "test"
    return

label shoppingmall_pressed:
    call shoppingmall
    return

label theater_pressed:
    scene bg theater
    "Theater was pressed"
    return

label PCroom_pressed:
    scene bg PCroom
    "PC room was pressed"
    return

label concert_pressed:
    call concert
    return