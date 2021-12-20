init python:
    # 화면 중앙에 창
    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    #선언
    config.automatic_images_minimum_components = 1
    config.automatic_images = [' ', '_', '/']
    config.automatic_images_strip = ["images"]
    oXY = []
    oN = []
    oLen = 0
    maxLen = 0
    oBg = ""
    oLast = -1
    oTime = 0.0
    oMaxTime = 5.0
    needTimer = False
    oActive = False
    oRes = False

    # 게임 초기화 및 화면에 아이템 배치
    def InitGame(bg, time, *args):
        global oBg, oXY, oN, oLen, maxLen, oLast, oTime, oMaxTime, oActive, needTimer, oRes
        oXY = []
        oN = []
        oLen = 0
        oBg = bg
        oLast = -1
        oTime = time
        oMaxTime = time
        maxLen = 0
        oActive = True
        oRes = False
        if oTime > 0.0:
            needTimer = True
        for xy, obj_name in zip(args[0::2], args[1::2]):
            oXY.append(xy)
            oN.append(obj_name)
            maxLen += 1

    # 게임 실행
    def StartGame():
        global oActive
        oActive = True
        need = True
        while need:
            renpy.call_screen("game", _layer="master")
            need = oRes == False
            if needTimer and (oTime <= .0):
                need = False

    # 게임 화면을 비활성 배경으로 표시
    # 이미 찾은 항목은 표시되지 않습니다.
    def GameAsBG():
        global oActive
        oActive = False
        renpy.show_screen("game", _layer="master")

    # 항목 클릭 핸들러
    def o_click(i):
        global oLen, oRes
        if i >= 0:
            if oN[i]:
                temp = oN[i]
                oN[i] = ""
                oLen += 1
                renpy.play("audio/click.mp3", channel="sound") #sound to audio
                renpy.restart_interaction()
                if needTimer:
                    if oLen >= maxLen:
                        oRes = True
                else:
                    oRes = temp
    oClick = renpy.curry(o_click)

# 게임 화면, StartGame() 함수에서 실행
screen game:
    modal True
    if oActive and needTimer:
        timer 0.01 repeat True action [SetVariable("oTime", oTime-.01), If(oTime <= .0, true=[Return()])]
    add oBg
    for i in range(0, len(oN)):
        if oN[i]:
            imagebutton:
                focus_mask True
                pos(oXY[i])
                idle oN[i]
                hover oN[i]
                # 당신은 개체의 사진을 복제할 수 있습니다
                # "images / objectname_hover.png"라고 부릅니다.
                #그래픽 편집기에서 강조 표시
                # 위의 줄을 아래 줄로 바꿉니다.
                # 그런 다음 마우스를 올리면 강조 표시됩니다.
                # hover oN[i] + " hover"
                if oActive:
                    action [oClick(i), Return()]
                else:
                    action []
    if oActive and needTimer:
        # if oTime > .1:
            # text "[oTime]" align(.1, .1) size 48
        # else:
            # text "0.0" align(.1, .1) size 48
        bar value StaticValue(oTime, oMaxTime):
            align(.5, .001)
            xmaximum 400
            ymaximum 20
            left_bar Frame("slider_left.png", 10, 10)
            right_bar Frame("slider_right.png", 10, 10)
            thumb None
            thumb_shadow None
