label theater:

    scene bg box_office:
        xalign 0
    with slowfade
    show screen placeUI with dissolve
    play music "audio/bgm theater.mp3" fadeout 1
    show screen stat_overlay
    "우리는 영화를 보러 영화관에 왔다.{p}우리 행성에서도 지구 영화는 꽤 유명해서, 나도 몇 번 본 적이 있다."

    e "무슨 영화 볼래?"

    label choice_movie:
        menu:
            "컨저링":
                $ flag_movie = "conjuring"

                e "너 공포 영화 잘 봐?"
                menu:
                    "무섭긴 한데 좋아는 해.":
                        e "으아~ 긴장되네. 나도 너무 무서워."

                    "난 엄마 말고 무서운 게 없어.":
                        e "히익, 얼마나 무서우신 거야…"

            "조커":
                $ flag_movie = "joker"

                e "DC 영화네? 재밌으려나?"


            "7번방의 선물":
                $ flag_movie = "no.7"

                e "가족 영화라 편하게 보기 좋겠다."


            "자전차왕 엄복동":
                $ flag_movie = "ubd"

                e "뭐…? 진심이야?"
                menu:
                    "응. 꼭 보고 싶어.":
                        "ENFP의 표정이 안 좋은 것 같은데, 어디 아픈가?"
                        $ friendship -= 20

                    "농담이야.":
                        "ENFP의 표정이 갑자기 밝아졌다. 나만 알고 싶은 영화… 뭐 그런 건가?"
                        $ friendship += 20
        

    label popcorn:
        show bg box_office:
            linear 1.5 xalign 1.0

        window hide
        pause 1.6
        e "우리 팝콘 사자!"
        menu:
            "좋아!":
                p "넌 무슨 맛 먹을래? 난 카라멜."
                e "난 어니언! 콜라도 사자."
                $ friendship += 20

            "난 괜찮아.":
                p "난 영화 볼 때 팝콘 잘 안 먹어서. 너 먹고 싶으면 사."
                e "아… 그래? 그럼 팝콘 사올게. 좀만 기다려!"
                $ friendship -= 20
                menu:
                    "따라간다":
                        p "그래도 같이 가야지."
                        e "나중에 먹고 싶으면 내 거 좀 먹어도 돼. ㅎㅎ"
                        $ friendship += 20
                    "따라가지 않는다":
                        "팝콘 사 올 때까지 구경이나 해야겠다."
                        $ friendship -= 20
        

    label movie_start:
        scene bg theater with fade
        "상영관 내 조명이 어두워지고 영화가 시작됐다."

        if flag_movie == "conjuring":
            e "허억!!"
            "갑자기 귀신이 튀어나오는 장면에서 ENFP가 깜짝 놀라며 팝콘을 사방팔방 튀겨댔다.{w} 그 모습을 보며 든 생각은…"

            menu:
                "나도 무섭다. ㅠ":
                    $ flag_feedback = 1
                    "나도 놀랐지만 ENFP의 반응을 보니 왠지 안심이 된다."

                "웃기다.":
                    $ flag_feedback = 2
                    "좀 웃겼다…. ㅋ.. ㅋㅋ. 나중에 이걸로 놀려먹어야겠다."

                "너 때문에 더 놀랐다…":
                    $ flag_feedback = 3
                    "영화는 별로 안 무서운데 ENFP가 더 무섭다…"


        if flag_movie == "joker":
            "ENFP가 팝콘을 입에 넣은 채 영화에 매우 몰입하고 있다.{p}그 모습을 보며 든 생각은…"

            menu:
                "난 히어로물 기대했는데…":
                    $  flag_feedback = 1
                    "나도 놀랐지만 ENFP의 반응을 보니 왠지 안심이 된다."

                "이런 게 바로 띵작…?":
                    $ flag_feedback = 2
                    "좀 웃겼다…. ㅋ.. ㅋㅋ. 나중에 이걸로 놀려먹어야겠다."

                "내용이 너무 어둡지 않나?":
                    $ flag_feedback = 3
                    "영화는 별로 안 무서운데 ENFP가 더 무섭다…"


        if flag_movie == "no.7":
            "옆에서 훌쩍거리는 소리가 들려 돌아보니 ENFP가 울고 있다.{p}그 모습을 보며 든 생각은…"

            menu:
                "너도 나랑 같구나…?":
                    $  flag_feedback = 1
                    p "큽.. 크흡.."
                    "흐르는 콧물을 소매로 내리 훔쳤다. 너무 슬프다… 소매가 축축해졌지만 눈물이 멈추질 않는다."

                "이게 슬픈가?":
                    $ flag_feedback = 2
                    "이런 뻔한 신파물을 보면서 울다니… 이해가 안 간다."


        if flag_movie == "ubd":
            e "…"
            "어두운 상영관 내 사람들 발소리가 멈추지 않는다. ENFP의 표정은 상영관의 어둠보다 어둡다.{p}그 모습을 보며 든 생각은…"

            menu:
                "미안하다..":
                    $  flag_feedback = 1
                    "왜 이 영화를 골랐을까…. ENFP에게 사과해야겠다."

                "재밌는데 표정이 왜 저러지?":
                    $ flag_feedback = 2
                    "난 재밌는데 ENFP는 영화가 마음에 들지 않는 것 같다. 영화 취향이 좀 다른가 보다."

                "모른 척 하자.":
                    $ flag_feedback = 3
                    "내가 보자고 했는데, 좀 그렇다. 문득문득 ENFP의 시선이 느껴지지만, 애써 외면하기로 한다."


    label movie_end:
        scene bg box_office with fade

        # 컨저링
        if flag_movie == "conjuring":
            e "아… 진짜 무서웠다. 넌 영화 어땠어?"

            if flag_feedback == 1:
                p "나도…. 너무 놀라서 심장 아파."
                e "그치? 난 수녀귀신? 얼굴이 너무 무섭더라ㅠㅠ"
                $ friendship += 20

            if flag_feedback == 2:
                p "아 ㅋㅋ 네 반응이 너무 웃겨서 집중이 안됐어."
                e "우씨.. 나 때문에 웃었던 거였어!"
                $ friendship -= 20

            if flag_feedback == 3:
                p "영화는 그렇게 무서운 줄 모르겠던데…. 난 네 비명 때문에 놀랐어."
                e "으악 미안하다 ㅋㅋㅋ"
                $ friendship -= 20


        # 조커
        if flag_movie == "joker":
            e "연기 진짜 미쳤다. 넌 영화 어땠어?"

            if flag_feedback == 1:
                p "난 액션 영화인 줄 알고 고른 거라 좀 지루하더라."
                e "나도 처음엔 그런 줄 알았는데, 막상 보니 괜찮던데?"
                p "그래? 난 사실 무슨 얘기하고 싶은 건지 잘 모르겠어."
                $ friendship -= 20

            if flag_feedback == 2:
                p "돈이 안 아깝다는 게 바로 이런 거지. 진짜 가취있는 영화였다."
                e "진짜 인정. 그래서 ‘가취있기를’ 뜻이 뭐야?"
                $ friendship += 20

            if flag_feedback == 3:
                p "연기는 좋긴 한데 내용은 좀…. 범죄 미화하는 것 같기도 하고."
                e "음… 그렇게 볼 영화는 아니지 않아?"
                $ friendship -= 20


        # 7번방의 선물
        if flag_movie == "no.7":
            e "별 생각 없이 봤다가 울었네. 넌 영화 어땠어?"

            if flag_feedback == 1:
                p "예승이… 세일러문 가방…"
                "ENFP가 내 몰골을 보곤 이해했다는 듯 고개를 끄덕인다."
                e "그래… 그래 보여."
                $ friendship += 20

            if flag_feedback == 2:
                p "좀 억지스러워서 몰입이 잘 안 됐어."
                e "아 진짜? 배우들 너무 잘하던데.. 난 슬펐어. ㅠㅠ"
                $ friendship -= 20


        # 자전차왕 엄복동
        if flag_movie == "ubd":
            e "…. 영화 어땠어…?"

            if flag_feedback == 1:
                p "미안…. 처음 본 사이에 이러면 안 되는 거였는데…."
                e "음냐~ 잘 뻔 했어…."
                "이 영화는 분명 관객 수가 1UBD밖에 안 될 것이다."

            if flag_feedback == 2:
                p "재밌었어!!"
                e "뭐…?"
                $ friendship -= 20

            if flag_feedback == 3:
                p "아~ 팝콘 맛있었다."
                e "어? 어. 근데 이 영화 왜 보자고 해ㅆ..."
                p "팝콘은 역시 카라멜이지!"
                $ friendship -= 20

    hide screen placeUI with dissolve
    hide screen stat_overlay
    $ is_visited += 1                                                           # 장소마다 스크립트 마지막에 추가

    if is_visited == 4:                                                         # 4곳 모두 방문 시 엔딩으로, 아니면 맵으로 돌아감
        jump ending
    else:
        jump minimap
