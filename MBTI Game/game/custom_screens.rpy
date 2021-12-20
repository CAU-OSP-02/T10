## 친밀도 창 ###################################################################
init:
    screen stat_overlay:

        frame:
            padding (15,15)
            xalign 1.0
            yalign 0.0
            xoffset -20
            yoffset 20
            vbox:
                text "친밀도" size 20
                bar:
                    value friendship
                    range 100
                    style "fixed_bar"
                text " " size 3

init -5 python:
    style.fixed_bar = Style(style.default)
    style.fixed_bar.xmaximum = 200
    style.fixed_bar.ymaximum = 30
    style.fixed_bar.left_gutter = 0
    style.fixed_bar.right_gutter = 0
    style.fixed_bar.left_bar = Frame("images/heart.png", 0, 0)
    style.fixed_bar.right_bar = Frame("images/emptyheart.png", 0, 0)

init python:
    res = False


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
            size 25
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
                        xalign .5
                        yalign .5
                        if i == "ENFP":
                            action Jump(i)
                        else:
                            action Notify("서비스 준비 중")


## 얼굴 선택 스크린 ##############################################################

screen choice_face():
    vbox:
        xalign 0.22 yalign 0.5
        spacing 23

        text "나는 어떻게 생겼을까?":
            size 23
            color "#ffffff"
            xalign 0.5

        grid 2 2:
            spacing 30
            xsize 100
            ysize 60

            imagebutton:
                idle "messenger/pic/1.png"
                hover im.MatrixColor("messenger/pic/1.png", im.matrix.brightness(-0.1))
                action Return("1")

            imagebutton:
                idle "messenger/pic/2.png"
                hover im.MatrixColor("messenger/pic/2.png", im.matrix.brightness(-0.1))
                action Return("2")

            imagebutton:
                idle "messenger/pic/3.png"
                hover im.MatrixColor("messenger/pic/3.png", im.matrix.brightness(-0.1))
                action Return("3")

            imagebutton:
                idle "messenger/pic/4.png"
                hover im.MatrixColor("messenger/pic/4.png", im.matrix.brightness(-0.1))
                action Return("4")
