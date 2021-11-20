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


    return
