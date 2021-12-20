label concert:
    scene bg concert with slowfade
    show screen placeUI with dissolve
    play music "audio/bgm chat.mp3" fadein 1 fadeout 1
    show screen stat_overlay
    show e_happy with dissolve
    e "어! MB경기장??? 오늘 밤에 있는 TI콘서트 말하는거지? 대박 너 티켓팅 성공했어?"
    e "사실 내가 TI 완전 팬인데 이번에 티켓팅 실패해서 못 가게 됐거든ㅠㅠ"
    hide e_happy
    p "이 세계의 아이돌은 어떨지 궁금했거든 너랑 같이 가려고 2장 티켓팅했다."
    p "후훗, 한장은 암시장에서 구한거지만"
    show e_happy
    e "와 진짜 친구야ㅠㅠ 사랑한다 너 아니면 어쩔뻔했냐ㅠㅠ 티켓값 지금 보내줄게!"
    hide e_happy
    $friendship += 20
    
    p "굿굿"
    
    p "{i}근데 TI는 무슨 아이돌인지 잘 모르겠다 ENFP에게 물어보자{/i}"

    menu:
        "근데 TI는 뭐하는 애들이냐? 내가 모르는거 보니까 듣보잡인거같은데?ㅋㅋㅋㅋ":
            $friendship -= 20
            show e_awk
            e "우씨 나 완전 팬이라고 했잖아! 우리 TI무시하지 말아줄레? 그래도 표사줬으니까 알려줄게 TI는 6년 전에 있었던 MBTI 서바이벌 프로그램에서 나온 아이돌이야."
            e "총 16명인데 다들 개성이 다 달라! 이번에 하는게 5주년 콘서튼데 진짜 시간 빨리간다."
            e "나 그 프로그램 본지가 엇그제 같은데. 이 그룹에 나랑 같은 이름인 애도 있음!"
            hide e_awk
        "너 진짜 TI좋아하는구나 표사길 잘했네 표 보니까 5주년 써있던거 같은데 오래한 아이돌이네. 넌 언제부터 팬이었어?":
            $friendship +=20
            show e_happy
            e "맞아 5년차 아이돌이고 이번에 5주년으로 콘서트하는 거야!"
            e "TI에 대해 조금 소개하자면 TI는 6년 전에 있었던 MBTI서바이벌 프로그램에서 나온 아이돌이야. 나 그 프로그램 본지가 엇그제 같은데."
            e "총 16명인데 다들 개성이 다 달라! 이번에 하는게 5주년 콘서튼데 진짜 시간 빨리간다. "
            e " 이 그룹에 나랑 같은 이름인 애도 있음! "
            hide e_happy
    

    p "아 그래? 이름이 ENFP인 아이돌도 있구나~"
    
    show e_happy
    e "응! 걔는 내 차애고 내 최애는 ISTP야!>< 너무 잘생겼어 나 지갑에 포카 있잖아~ 한번 봐봐ㅋㅋㅋㅋ"
    hide e_happy

    show e_norm with dissolve
    p "너 콘서트 몇시에 하는지 알아?"

    e "6시!"
    hide e_norm
    menu:
        "그럼 지금 3시니까 시간 많네~ 여기저기 돌아다녀보자!":
            show e_happy
            e "꺄~ 신난다!"
            $friendship += 20
            hide e_happy
        "지금은 3시라서 시간 생각보다 없어 티켓뽑고, 굿즈사고, 사진찍고, 화장실 가고, \n우리는 스텐딩석이니까 줄기다려서 표 확인 받고 다 해야함 내가 최적의 동선을 짜왔으니 걱정 하지말어!":
            show e_sad
            e "3시간이면 충분한거 같은데ㅠㅠ 알았어. 그렇게 하자...."
            $friendship -= 20
            hide e_sad
            
    
   

    ##굿즈판매소 줄 기다리기
    show e_norm with dissolve
    e "와 사람 진짜 많다ㄷㄷ 너 말대로 빠릿빠릿하게 욺직이길 잘했네."
    
    p "..."
    p "너 시간 계산은 해봤냐ㅋㅋㅋ"
    e "아닠ㅋㅋ 운명에 맡기는거지~"
    e "아 근데 줄 기다리는데 너무 힘들다ㅠㅠ 언제 사람이 빠질까..."
    hide e_norm
    menu:
        "아까 시간 확인 해봤는데 한 사람당 2분정도 걸리네. 앞에 28명 남았으니까, 56분만 참어. 나도 지쳐서 짜증난다.":
            show e_sad
            e "ㅠㅠ 알았어 징징거리지 않을게..."
            $friendship -= 20
            hide e_sad
        "흠.. 우리 그럼 기다리는 동안 끝말잇기나 할레?":
            show e_happy
            e "오~ 똑똑한데? 좋아! 3글자로 쿵쿵따하자!"
            $friendship += 20
            hide e_happy
    show text "잠시 후" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve
    

    ##콘서트장 앞
    show e_norm
    e "음냐~ 콘서트 이제 1시간 남았네"
    
    p "맞아 얼마 안남았어"
    e "으아 떨린다! OO이 얼굴 볼 생각하니까 너무 좋아ㅠㅠ"
    e "직캠말고 직접 두눈으로 보는 날이 오다니!"
    e "어? 저기봐! 저기서도 굿즈 판다"
    hide e_norm
    menu:
        "흠... 친구야 여기 바가지만 조심하고 꼭 사고싶은것만 사자!":
            show e_happy
            e "ㅎㅎ 나도 알고 있지 구경만할껴~"
            $friendship += 20
            hide e_happy
        "야 너 바보냐? 콘서트장 앞에서 파는 것들 불량인데다 바가지나 씌우고 별로야 그냥 사지마":
            show e_awk
            e "칫 구경만 할꺼거든!"
            $friendship -= 20
            hide e_awk
    
    p "그럼 다행이고 ^^"

    ##콘서트장 앞 대기줄
    show text "콘서트 시작 30분 전" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve
    ti "여러분~! 콘서트 때 우리 오빠들을 위한 깜짝 이벤트가 있습니다~ 떼창 꼭 같이 해주시고 지금 나눠드리는 5주년 단콘 축하해 우리 사랑 영원해"
    ti "판플렛 꼭 흔들어주세요! 감사합니다~"
    show e_happy
    e "[player_name], 너 떼창곡 뭔지 알아? 다른 곡들은? 응원법 알려줄까?"
    hide e_happy
    menu:
        "됐어. 그냥 따라 부르면 되지ㅋㅋ":
            show e_sad
            e "아 왜ㅠㅠ 그럼 떼창곡만 알려줄게. 여기 후렴 부분에 우리 사랑 영원해~"
            e "가사만 잘 따라하면 쉽게 따라올 수 있을 거야"
            $friendship -= 20
            hide e_sad
        "오! 그럼 지금 시간 없으니까 떼창곡만 알려주라.":
            show e_happy
            e "굿 초이스~ 그럼 떼창곡만 알려줄게. 여기 후렴부분에 우리 사랑 영원해~"
            e "가사 자주 나오니까 꼭 외우고 우리 꼭 다시 만나~ 여기 부분에서"
            e "음정 키업 되니까 주의하면 돼!"
            $friendship += 20
            hide e_happy
    
    ##
    show text "그렇게 콘서트가 잘 마무리된 후..." at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve
    
    show e_happy
    e "야야 마지막에 앵콜노래 나올 때 봤어? OO이가 나 보고 하트 날려줬어ㅠㅠㅠㅠ"
    e "나 심장 멎을 것만 같아"
    hide e_happy
    menu:
        "욜~ 어떻게 너의 최애가 딱 너 앞으로 오더라. 기분 째지겠넼ㅋㅋㅋ":
            show e_happy
            e "진짜루ㅠㅠ 오늘 진짜 너 덕분에 잘 놀았다!"
            $friendship += 20
            hide e_happy
        "ㅋㅋㅋ야 너한테 했겠냐. 옆에 다른 애들한테 한 거겠지 착각하기는 쯪쯪":
            show e_awk
            e "진짜 너무하네 아 그렇다고 해주면 되지 뭘 그렇게 딱 잡아서 아니라고 하냐! 칫..."
            $friendship -= 20
            hide e_awk
    
    ##콘서트장 앞
    show e_norm
    e "이제 헤어질 시간이네~ 오늘 싸인포카도 얻고, 최애한테 하트도 받고 너무 행복한 시간이었다!"
   
    p "흠.. 나는 완전 잊혀진 거같군ㅋㅋㅋㅋㅋ"
    e "아! 아니야! 진짜 까먹은거 아니얔ㅋㅋㅋ"
    e "잠시만 나 화장실 좀 갔다올게! 좀만 기다려줘"
    p "그려 빨리 갔다와 밤 되니까 춥다."
    hide e_norm
    show text "자자~ 5주년 콘서트 기념 무료 나눔합니다~" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve
    show text "선착순으로 가져가시면 됩니다! 먼저 가져가는 사람이 임자!" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve
    p "무료 나눔? 선착순? 이거 다 털릴 텐데"
    p "빨리 가서 ENFP꺼 챙겨야겠다."

    call speedgame
    scene image "bg white.png"
    p "왔어?"
    show e_norm with dissolve
    e "응! 어? 손에 그건 뭐야? 뭔가 엄청 많이 들고있네?"
    hide e_norm
    p "자, 널 위한 선물이다."
    show e_happy
    e "우와 고마워! 헐? 이건 뭐야 굿즈들이 가득? 어떻게 구했어?"
    hide e_happy
    menu:
        "오다 주웠다.":
            show e_happy
            e "앜ㅋㅋㅋㅋ 고맙다! 이쁜 거 많네~ㅎㅎㅎ"
            $friendship += 20
            hide e_happy
        "어이 세상엔 공짜가 없다는거 알지?":
            show e_sad
            e "엥? 아까는 선물이라며ㅠㅠ 얼마나 산 거야...?"
            $friendship -= 20
            hide e_sad
            p "ㅋㅋㅋ 농담이야"
    hide screen stat_overlay

    $ is_visited += 1                                                           # 장소마다 스크립트 마지막에 추가

    if is_visited == 4:                                                         # 4곳 모두 방문 시 엔딩으로, 아니면 맵으로 돌아감
        jump ending
    else:
        jump minimap

label speedgame:
    scene black
    # 게임 화면 객체로 채우기
    $ InitGame("bg white", 3.0, (0, 300), "img0", (150, 300), "img1", (300, 300), "img2", (0, 150), "img3", (150, 150), "img4", (300, 150), "img5", (0,0), "img6", (150,0), "img7")

    #게임 화면
    $ GameAsBG()
    with dissolve
    #게임 시작
    $ res = StartGame()

    #다시 배경으로 표시(이미 발견한건 제외)
    $ GameAsBG()

    #게임 결과 확인
    if oRes:
        "나이스! 싹다 모았다~"
    else:
        "아~ 까비ㅠㅠ"
    return
