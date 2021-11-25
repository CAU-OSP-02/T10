# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
image draw_box:
        "drawBox.png"
        yalign .4

image lots:
        "lots.png"
        xalign .5
        yalign .4
        linear 1.0 yalign .25

image period_0 = Text("0교시", size=25, color="#000000", xpos=75, ypos=75)
image period_1 = Text("1교시", size=25, color="#000000", xpos=75, ypos=75)        # 임시-교시 표기

image BG hallway a = "hallway.png"
image BG classroom1 a = "classroom1.png"
image BG classroom2 a = "classroom2.png"


# 게임에서 사용할 캐릭터를 정의합니다.
define n = Character()                                                            # 나레이션
define e = Character('ENFP', color="#FF5E00")
define f = Character('INFP', color="#4374D9")
define t =Character('INTP', color="#998A00")
define s = Character('ISFP', color="#2F9D27")
define ht = Character('담임 선생님', color="#353535")
define et = Character('영어 선생님', color="#353535")
define mt = Character('수학 선생님', color="#353535")

##호감도 창

define persistent.love = [0, 0, 0, 0]

init:
    screen stat_overlay:

        frame:
            padding (15,15)
            align(1.0, 0.0)
            xmaximum 250
            ymaximum 250
            vbox:
                text "INTP{space=15}[persistent.love[0]]" size 16
                bar:
                    value persistent.love[0]
                    range 100
                    style "fixed_bar"
                text " " size 3

                text "ENFP{space=15}[persistent.love[1]]" size 16
                bar:
                    value persistent.love[1]
                    range 100
                    xalign 0.0
                    style "fixed_bar"
                text " " size 3

                text "INFP{space=15}[persistent.love[2]]" size 16
                bar:
                    value persistent.love[2]
                    range 100
                    xalign 0.0
                    style "fixed_bar"
                text " " size 3

                text "ISFP{space=15}[persistent.love[3]]" size 16
                bar:
                    value persistent.love[3]
                    range 100
                    xalign 0.0
                    style "fixed_bar"
                text " " size 3

init -5 python:
    style.fixed_bar = Style(style.default)
    style.fixed_bar.xmaximum = 200
    style.fixed_bar.ymaximum = 15
    style.fixed_bar.left_gutter = 0
    style.fixed_bar.right_gutter = 0
    style.fixed_bar.left_bar = Frame("images/bar_full.png", 0, 0)
    style.fixed_bar.right_bar = Frame("images/bar_empty.png", 0, 0)



# 여기에서부터 게임이 시작합니다.
label start:

        scene BG hallway a with dissolve                                                                # 임시 배경

        n "오늘은 새 학기 첫 날이다. {p}우리 반 친구들은 어떤 애들일까?"

        # [화면 전환 추가]
        show period_0 with dissolve
        scene BG classroom1 a with dissolve

        show e with dissolve
        e "안뇽! 나는 ENFP야. 넌 이름이 뭐야?"

        $ player_name = renpy.call_screen("set_name", title="당신의 이름은?")
        $ player_name = player_name.strip() or '플레이어'
        $ p = Character(player_name, color="#ffffff")

        p "안녕! 내 이름은 [player_name](이)야."
        e "오늘 새 학기 첫날인데 정말 설레지? ㅋㅋ"
        p "응…."
        hide e with dissolve

        ## <종소리>
        # 0교시 조회 - 자리 바꾸기: 제비뽑기
        # 자리 배정 - 짝과 대화, 당번

        show ht with dissolve
        ht "모두 자리에 앉아라!"
        ht "자, 오늘은 첫날이니까 자리를 뽑을 거다. {p}뽑는 순서는 그냥 번호 순서대로 나오면 된다."
        hide ht with dissolve
        hide period_0 with dissolve
        show draw_box with dissolve
        call screen draw_button with dissolve

        ## 뽑기 버튼 클릭 이벤트 ##
        label draw:
                show lots behind draw_box
                $ drawNumber = renpy.random.randint(1, 25)
                pause 1.7
                hide draw_box with dissolve
                hide lots with dissolve
                call screen draw_num(drawNumber) with dissolve

        p "나는… [drawNumber]번이네."
        $ e_drawNum = drawNumber + 2
        $ f_drawNum = drawNumber + 1
        $ t_drawNum = drawNumber - 3
        $ s_drawNum = drawNumber - 5

        show e with dissolve
        e "나는 [e_drawNum]번인데, 까비!"
        hide e with dissolve

        show s with dissolve
        s "휴, 쟤랑 짝은 안됐다. 다행이네."
        hide s with dissolve

        ## (자리 배치도 사진)
        show ht with dissolve
        ht "학교는 항상 깨끗해야 한다! {p}오늘 당번은 1, 2번이 하도록 하자."
        ht "아니다, 이번 주 1, 2번이 하고 담 주는 3, 4번이 하고 이렇게 쭉 가는 거다! 알겠지~!"
        ht "곧 종 치니까 빨리 화장실 갔다 오고 수업 준비하도록. 조회 끝."



        #1교시
        scene BG classroom2 a with fade
        show period_1 with dissolve

        p "영어시간이네. 열심히 해보자!"

        show et with dissolve
        et "Hello~ How are you guys?"
        et "Today, we will introduce ourselves!" 
        hide et with dissolve
        
        show e with dissolve
        e "히익, 영어라니 잘 모르지만 열심히 해보자 ><"
        hide e with dissolve
        
        show et with dissolve
        et "You guys have your own numbers right?"
        et "Number [t_drawNum]! Please introduce yourself." 
        hide et with dissolve
        
        show t with dissolve
        t "Hi my name is INTP. I like to solve problems with logic and analyze them. I'm not that talkative, but when it comes to my areas of interest I talk a lot. Thank you!"
        hide t with dissolve
        
        show e with dissolve
        e "우와 영어 짱 잘한다! t랑 친해지고 싶은 걸~" 
        hide e with dissolve

        show s with dissolve
        s "내 번호는 안 불렸으면 좋겠다…."
        hide s with fade
        
        show et with dissolve
        et "Good job! Next… number [s_drawNum]!"
        hide et with dissolve
        
        show s with dissolve
        s "Hi my name is ISFP. I like creative activities. Also I like playing with my friends. Thank you!"
        hide s with fade

        show et with dissolve
        et "Very good! Next...number [f_drawNum]!"
        hide et with dissolve

        show f with dissolve
        f "Hi my name is INFP. I interact well with people. Also, I enjoy challenging something. Thank you!"
        hide f with fade

        show et with dissolve
        et "Good. Next..number [e_drawNum]!"
        hide et with dissolve

        show e with dissolve
        e "Hi my name is ENFP. I enjoy trying different things. Also, I get along well with people. Thank you!"
        hide e with fade

        show et with dissolve
        et "Very good~. Well, we had a little time to get to know our classmates."
        hide et with dissolve

        p "나와 잘 맞는 친구는 누굴까??"
       
        menu:
            "INTP":
                 $ persistent.love[0] +=10
                 show t with dissolve
                 "INTP에 대한 호감도가 10 상승했습니다."
                 hide t with dissolve
            "ENFP":
                 $ persistent.love[1] +=10
                 show e with dissolve
                 "ENFP에 대한 호감도가 10 상승했습니다."
                 hide e with dissolve
            "INFP":
                 $ persistent.love[2] +=10
                 show f with dissolve
                 "INFP에 대한 호감도가 10 상승했습니다."
                 hide f with dissolve
            "ISFP":
                 $ persistent.love[3] +=10
                 show s with dissolve
                 "ISFP에 대한 호감도가 10 상승했습니다."
                 hide s with dissolve

        show screen stat_overlay with dissolve
        pause(2.0)
        hide screen stat_overlay with dissolve
        
        show et with fade
        et "As you know, memorizing words is important so.."
        et "Let’s play the Hangman game! If your answer is correct, I will give you a prize."
        hide et with dissolve
        
        ## (행맨게임화면)
        
        python:
            word = renpy.random.choice(["friend", "school", "english", "hangman"])
            letters = ""

            while True:
                isSuccess = True
                for w in word:
                    if w in letters:
                        renpy.say(n, "[w] ")
                    else:
                        renpy.say(n, "_ ")
                        isSuccess = False
                if isSuccess == True:
                    break

                letter = renpy.input ("Input letter >")
                if letter not in letters:
                    letters += letter


        show et with fade
        et "The prize was a round of applause. See you next time."
        hide et with dissolve

        return
