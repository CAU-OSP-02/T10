label minimap:
    play music "audio/bgm map.mp3" fadein 1 fadeout 1
    call screen MapUI

label shoppingmall_pressed:
    call shoppingmall from _call_shoppingmall

label theater_pressed:
    call theater from _call_theater

label PCroom_pressed:
    call PCroom from _call_PCroom 

label concert_pressed:
    call concert from _call_concert