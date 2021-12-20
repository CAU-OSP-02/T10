## 다른 장소로 이동하기 버튼 ####################################################
screen placeUI:
    imagebutton:
        xalign 0.0
        yalign 0.0
        xoffset 30
        yoffset 30
        auto "UI/minimap_%s.png"
        action ShowMenu("MapUI")


## 미니맵 스크린 ################################################################

screen MapUI():
    tag statusUI
    add "map/bg map.png"

    imagebutton:
        xalign 0.0
        yalign 0.0
        xoffset 30
        yoffset 30
        auto "UI/ending_%s.png"
        action Jump("ending")

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


## 이름 Input 스크린 ############################################################

screen set_name(title):
    frame:
        xpadding 30
        ypadding 30
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 15
            text title xalign 0.5
            input
            xalign 0.5



## 뷰포트 스크린 ################################################################

screen viewport_blog():
    side "c r":
         area (169, 50, 942, 530)

         viewport id "blog":
             mousewheel True

             add "blog.png"

         vbar value YScrollValue("blog")



## 유형 선택 버튼 스크린 #########################################################

screen choice_mbti():

    $ mbti = ['ISTJ', 'ISTP', 'ISFJ', 'ISFP', 'INTJ', 'INTP', 'INFJ', 'INFP', 'ESTJ', 'ESTP', 'ESFJ', 'ESFP', 'ENTJ', 'ENTP', 'ENFJ', 'ENFP']

    vbox:
        xalign 0.5 yalign 0.5
        spacing 25

        text "원하는 MBTI 유형을 선택하세요.":
            size 30
            color "#000000"
            xalign 0.5

        grid 4 4:
            spacing 25

            for i in mbti:
                frame:
                    xsize 100
                    ysize 60

                    textbutton "[i]":
                        text_size 25
                        xalign 0.5
                        yalign 0.5
                        if i == "ENFP":
                            action Jump(i)
                        else:
                            action Notify("서비스 준비 중")

