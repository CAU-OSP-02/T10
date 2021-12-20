# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
image heart:
         "heart.png"
         size(30,30)
image empty_heart:
         "emptyheart.png"
         size(30,30)
image restaurant_menu = "restaurant_menu.png"

#친밀도 창
init:
    screen stat_overlay:

        frame:
            padding (15,15)
            align(1.0, 0.0)
            xmaximum 250
            ymaximum 250
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


# 여기에서부터 게임이 시작합니다.
label shoppingmall:

    show screen stat_overlay
    scene bg platform with slowfade
    show screen placeUI with dissolve
    play music "audio/bgm chat.mp3" fadein 1 fadeout 1

    show e_norm with dissolve
    e "쇼핑하러 갈까? 안 그래도 옷이 좀 필요하던 참이었는데~"
    p "좋아 좋아."

    menu:
        "일단 가게는 여기랑 여기 먼저 들러야 할 것 같아. 여기 옷들이 네 스타일이거든! \n그리고 점심은 1시쯤에 먹고 잠깐 쉬다가 그 주변에 있는 이 가게 가보자. \n동선은 이렇게 정하면 딱 맞을 것 같은데?":
            hide e_norm
            $friendship -= 20
            show e_sad
            e "계획이 너무 타이트한 것 같은데...ㅠㅠ"
            hide e_sad
        
        "들어가서 예쁜 옷들 보이면 왕창 다 구경하자! 사고 싶은 거 있으면 고민 말고 담기!":
            hide e_norm
            $friendship += 20
            show e_happy
            e "응! 진짜 재밌겠다... 신난다~"
            hide e_happy

    show e_norm
    p "그러면 우리 지금 가볼까?"
    hide e_norm with dissolve

    scene bg shoppingmall_1 with fade

    show e_norm with dissolve
    e "[player_name]! 내가 마음에 드는 옷들 골라왔는데 좀 봐줄래?"
    p "응. 보여줘봐."
    e "여기 두 벌인데, 나는 이게 쪼오끔 더 마음에 드는 것 같아. 예쁘긴 한데 살짝 얇아보여서 걱정이야."
    e "옆에 거가 좀 더 실용적으로 입을 수 있을 거 같긴 해."

    menu:
        "응, 네 말대로 조금 얇아보이긴 하네. 그런 면에서는 옆에 거가 더 나은 것 같기도 하고... \n근데 첫 번째 거가 예쁘긴 하다. 진짜 고민된다 ENFP야...":
            e "맞아맞아. 나 지금 완전 고민 중..."

        "난 두 번째 거가 더 나은 것 같은데? 이거 사!":
            hide e_norm
            $friendship += 0
            show e_sad
            e "근데 첫 번째 거가 더 예쁘단 말이지... ㅠㅠ"
            p "그래서 뭐 살지 골랐어?"

        "내가 말해줘도 어차피 너 원하는 거 살 거잖아. 맘대로 해~":
            hide e_norm
            $friendship -= 20
            show e_awk
            e "에이, 넌 뭐 말을 그렇게 하냐! 그래도 봐주면 좀 덧나냐..."
            p "그래서 뭐 살지 골랐어?"
            hide e_awk
            show e_sad

    e "아니... 아직도 못 골랐어..."
    hide e_sad
    show e_norm
    e "가게 아주머니께 여쭤볼까?"
    p "그러자!"
    hide e_norm with dissolve

    show so at left
    show e_sad at right
    with dissolve
    e "아주머니! 저 이 두 옷 중에 고민 중인데 어떤 게 더 나을까요?"
    so "학생 체형이나 요즘 날씨 같은 걸 고려했을 때는 두 번쨰 옷이 더 나아보이는데~?"
    e "아, 그런가요..."

    pause(1.0)

    hide e_sad
    show e_happy at right
    e "그냥 첫 번째 걸로 주세요!"
    hide so
    hide e_happy
    with dissolve

    show e_norm with dissolve
    menu:
        "결국에는 이거 샀구나! 잘했어. 잘 어울린다!":
            $friendship += 20
            e "아 정말? 다행이다. 아까 귀찮았을텐데 같이 고민해줘서 고마워..."
            hide e_norm with dissolve
        
        "으이구... 이 화상아. 결국 이거 살 거였으면서 뭘 그렇게 고민을 했어!":
            hide e_norm
            $friendship -= 20
            show e_sad
            e "그래도 고민이 되는 걸 어떡해..."
            hide e_sad with dissolve

    show e_norm with fade
    p "ENFP야 배 안 고파?"
    e "살짝 배고프다... 우리 뭐 먹을까? [player_name], 먹고 싶은 거 있어?"
    p "난 상관 없는데, 너는 뭐 먹고 싶은 거 있어?"
    e "음... 한 번 쭉 둘러볼까?"
    p "그래!"
    hide e_norm with dissolve

    scene bg restaurant with fade
    
    show restaurant_menu at truecenter with dissolve
    pause(2.0)
    show e_happy with dissolve
    e "여기 맛있어 보인다!"
    p "그래, 여기서 먹자."
    hide restaurant_menu with dissolve
    hide e_happy with dissolve

    show e_norm with fade
    p "ENFP, 벌써 메뉴 골랐어?"
    e "응. 나 이거 먹으려구!"

    menu:
        "어제는 이거 먹었으니까, 오늘은 이걸 먹어야 하나? 근데 이 음식점 추천메뉴가 저거던데... 저걸 먹어볼까?":
            hide e_norm
            show e_sad
            e "[player_name], 뭘 그리 고민해... 나 배고파, 빨리 시키자."
            p "아니, 어떤 걸 먹는 게 제일 이득일지 생각 중이야..."
            hide e_sad
            $friendship -= 20
            show e_awk
            e "어? 음식 먹을 때도 이득을 따져...? 맛있으면 된 거지..."
            hide e_awk
            show e_norm

        "난 이거 먹을래! 이게 제일 땡긴다 지금.":
            $friendship += 0
            e "그래. 나도 쪼금 나눠줄 거지? 내 것도 너 좀 줄게."

    e "근데 나 진짜 어릴 적부터 궁금했던 건데..."
    p "응, 뭔데?"
    e "진짜로 외계인이 존재할까?"

    menu:
        "글쎄... 별로 생각해본 적 없는데.":
            hide e_norm
            $friendship -= 20
            show e_sad
            e "아, 그렇구나... 그냥 항상 궁금했었어!"
            p "그럴 수 있지."
            hide e_sad

        "만약 외계인이 진짜로 존재한다면 나는 우주 여행하면서 그들과 교류해보고 싶어! 진짜 신기하겠다.":
            hide e_norm
            $friendship += 20
            show e_happy
            e "그럼 나는 너 옆에 따라가서 외계인 친구 만들어야지!"
            p "헉, 너무 좋은데?"
            hide e_happy

    show e_norm
    e "근데 내가 어제 고양이 영상을 봤는데, 이거 봐봐. 진짜 귀엽다?"
    p "오오, 완전 귀엽다. 나 앞으로 이 영상 주기적으로 찾아볼 듯."
    e "근데 이 옆에, 이 게임 영상 진짜 웃김! ㅋㅋㅋ ..."
    hide e_norm with dissolve

    show e_norm with fade
    e "나 예전부터 인테리어 소품 같은 거 사고 싶었는데 구경하러 가도 돼?"

    menu:
        "아 진짜? 뭐 사고 싶었는데?? 나도 요즘 그쪽에 관심 엄청 많거든!!":
            hide e_norm
            $friendship += 20
            show e_happy
            e "나 오르골 진짜 사고 싶었어... 요즘 유튜브로 계속 오르골 자장가 틀어놓고 잤거든."
            p "아 진짜~? 오르골 한 번도 사본 적 없는데, 궁금하다. 가보자 가보자!"
            hide e_happy with dissolve

        "인테리어 소품? 사서 뭐하게? 요즘 방 꾸미는 게 취미야?":
            $friendship += 0
            e "그건 아니고, 요즘 유튜브로 맨날 오르골 자장가 틀어놓고 잤거든. 실제로 사면 더 좋을 것 같아서."
            p "아 그렇구나. 그럼 가보자."
            hide e_norm with dissolve

        "인테리어 소품 사도 어차피 쓰지도 않을 거잖아~ 돈 아깝지 않아?":
            hide e_norm
            $friendship -= 20
            show e_sad
            e "그래도 예쁘잖아... 전시해놓고 두고두고 보면 좋을 것 같은데... ㅠㅠ"
            p "그래, 가보자."
            show e_sad with dissolve

    scene bg shoppingmall_2 with fade

    show e_norm at right with dissolve
    e "우와 이거 진짜 예쁘다! 음악도 귀엽고."

    show sm at left with dissolve
    sm "손님 여기 이것도 봐보세요. 지금 보시는 거는 노래가 저런 거라면, 그것과 세트로 만들어진 게 이거랍니다."
    e "아하, 이게 세트도 있구나. 사실 이 노래가 제가 진짜 좋아하는 애니메이션 OST거든요! 혹시 이 애니메이션 보셨어요?"
    sm "아, 당연히 봤죠~ 저도 이 애니메이션 진짜 좋아해요. 3번인가 돌려봤다니까요."
    e "진짜요? 거기서 캐릭터 누구 제일 좋아하세요?"
    sm "저는 그 중에,"
    hide e_norm
    hide sm
    with dissolve

    show e_norm with dissolve
    p "ENFP야. 거기서 뭐해. 이거 살 거야?"
    e "응! 이거랑 이것도 살 거야!"

    menu:
        "원래 하나만 사려던 거 아니었어? 충동적으로 사서 돈 너무 많이 쓰지 말고 하나만 사자.":
            hide e_norm
            $friendship -= 20
            show e_sad
            e "그래도 저거랑 세트여서 사고 싶은데...ㅠㅠ"
            hide e_sad
            show e_norm

        "원래 하나만 사려던 거 아니었어? 이것도 마음에 들었나보네?":
            $friendship += 0
            e "응. 마음 같아서는 이거저거 다 사고 싶은데 나도 내 딴에는 참는 거야."

    p "살 거 다 골랐으면 이제 갈까?"
    e "아, 나 지금 직원 분이랑 얘기하고 있었는데 잠시만..."

    menu: 
        "무슨 얘기를 그렇게 재미있게 하고 있었어~ 그럼 나는 저기서 저거 보면서 기다리고 있을게.":
            hide e_norm
            $friendship += 20
            show e_happy
            e "응! 기다려줘서 고마워!"
            hide e_happy with dissolve

        "직원 분이랑 할 얘기가 뭐 그리 많아~ 우리 얼른 가자. 나 조금 피곤해...":
            hide e_norm
            $friendship -= 20
            show e_sad
            e "아 그래..? 알겠어... 가자!"
            hide e_sad with dissolve

    hide screen stat_overlay
    hide screen placeUI with dissolve

    $ is_visited += 1                                                           # 장소마다 스크립트 마지막에 추가

    if is_visited == 4:                                                         # 4곳 모두 방문 시 엔딩으로, 아니면 맵으로 돌아감
        jump ending
    else:
        jump minimap