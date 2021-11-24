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

image period = Text("0교시", size=50, color="#000000", xpos=0.5, ypos=0.5)        # 임시-교시 표기


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

        scene bg white                                                                # 임시 배경

        n "오늘은 새 학기 첫 날이다. {p}우리 반 친구들은 어떤 애들일까?"

        # [화면 전환 추가]
        show period

        e "안뇽! 나는 ENFP야. 넌 이름이 뭐야?"
        $ player_name = renpy.call_screen("set_name", title="당신의 이름은?")
        $ player_name = player_name.strip() or '플레이어'
        $ p = Character(player_name, color="#ffffff")

        p "안녕! 내 이름은 [player_name](이)야."
        e "오늘 새 학기 첫날인데 정말 설레지? ㅋㅋ"
        p "응…."

        ## <종소리>
        # 0교시 조회 - 자리 바꾸기: 제비뽑기
        # 자리 배정 - 짝과 대화, 당번

        ht "모두 자리에 앉아라!"
        ht "자, 오늘은 첫날이니까 자리를 뽑을 거다. {p}뽑는 순서는 그냥 번호 순서대로 나오면 된다."
        hide period
        show draw_box
        call screen draw_button

        ## 뽑기 버튼 클릭 이벤트 ##
        label draw:
                show lots behind draw_box
                $ drawNumber = renpy.random.randint(1, 25)
                pause 1.7
                hide draw_box
                hide lots
                call screen draw_num(drawNumber)

        p "나는… [drawNumber]번이네."
        e "나는 17번인데, 까비!"
        s "휴, 쟤랑 짝은 안됐다. 다행이네."

        ## (자리 배치도 사진)
        ht "학교는 항상 깨끗해야 한다! {p}오늘 당번은 1, 2번이 하도록 하자."
        ht "아니다, 이번 주 1, 2번이 하고 담 주는 3, 4번이 하고 이렇게 쭉 가는 거다! 알겠지~!"
        ht "곧 종 치니까 빨리 화장실 갔다 오고 수업 준비하도록. 조회 끝."



        #1교시
        p "영어시간이네. 열심히 해보자!"
        et "Hello~ How are you guys?"
        et "Today, we will introduce ourselves!" 
        
        show e  
        e "히익, 영어라니 잘 모르지만 열심히 해보자 ><"
        hide e with dissolve
        
        et "You guys have your own numbers right?"
        et "Number 9! Please introduce yourself." 
        
        show t
        t "Hi my name is INTP. I like to solve problems with logic and analyze them. I'm not that talkative, but when it comes to my areas of interest I talk a lot. Thank you!"
        hide t with fade
        
        show e
        e "우와 영어 짱 잘한다! t랑 친해지고 싶은 걸~" 
        hide e with fade

        show s
        s "내 번호는 안 불렸으면 좋겠다…."
        hide s
        
        et "Good job! Next… number 4!"
        
        show s
        s "Hi my name is ISFP. I like creative activities. Also I like playing with my friends. Thank you!"
        hide s

        et "Very good! Next...number 16!"

        show f
        f "Hi my name is INFP. I interact well with people. Also, I enjoy challenging something. Thank you!"
        hide f

        et "Good. Next..number 17!"

        show e
        e "Hi my name is ENFP. I enjoy trying different things. Also, I get along well with people. Thank you!"
        hide e

        et "Very good~. Well, we had a little time to get to know our classmates."

        p "나와 잘 맞는 친구는 누굴까??"
       
        menu:
            "INTP":
                 $ persistent.love[0] +=10
                 "INTP에대한호감도가1상승했습니다."
            "ENFP":
                 $ persistent.love[1] +=10
                 "ENFP에대한호감도가1상승했습니다."
            "INFP":
                 $ persistent.love[2] +=10
                 "INFP에대한호감도가1상승했습니다."
            "ISFP":
                 $ persistent.love[3] +=10
                 "ISFP에대한호감도가1상승했습니다."

        show screen stat_overlay
        
        et "As you know, memorizing words is important so.."
        et "Let’s play the Hangman game! If your answer is correct, I will give you a prize."
        
        ## (행맨게임화면)
        
        et "The prize was a round of applause. See you next time."




        ##<종소리>(학교전체사진) 
    
        #2교시 수학 - 오목
        #모르는 문제가 있음
        
        mt "자리에 앉아라! 바로 수업 들어갈게 시간이 없단다."
        mt "교과서는 다들 들고 왔겠지? 16페이지 펴고, 다항식 들어간다~"
        
        e "하.. 이 쌤 빡세다ㅠㅠ 벌써 잠오는거 같은데?"
        f "역시 수학은 재밌군. 이번에 공부 열심히해서 만점 받아야지"
        s "첫날부터 수업이네, 책 안가지고 왔는데…"
        t "음 이게 저거니까... 오케이 이해됐다. 쉬운데?"

        mt "여기서 문제를 내도록 하지 9x^2 + 42x + 49를 인수분해 해보시오."

        p "아 어렵네..옆 친구한테 물어봐야겠다"
        p "혹시 이것 좀 알려줄 수 있어?"
        f "후훗. 이건 말이지 이렇게 이렇게 해서 답은(3x+7)제곱 이란다."
        
        mt "오늘 수업은 여기까지 하고 남은시간은 놀지 말고 짝이랑 오목 게임을 해보자." 
        
        ##(오목 게임 화면)
        
        return