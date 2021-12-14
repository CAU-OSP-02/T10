# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
image heart:
         "heart.png"
         size(30,30)
image empty_heart:
         "emptyheart.png"
         size(30,30)


# 게임에서 사용할 캐릭터를 정의합니다.
define n = Character()                                                            # 나레이션
define e = Character('ENFP', color="#FF5E00")
define f = Character('INFP', color="#4374D9")
define t =Character('INTP', color="#998A00")
define s = Character('ISFP', color="#2F9D27")
define ti = Character('TI팬클럽회장', color="#353535")
#친밀도
define friendship = 0
##친밀도 창
init:
    screen stat_overlay:

        frame:
            padding (15,15)
            align(1.0, 0.0)
            xmaximum 250
            ymaximum 250
            vbox:
                text "친밀도" size 16 
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

    
label concert:
                show e with dissolve
                e "어! MB경기장??? 오늘 밤에 있는 TI콘서트 말하는거지? 대박 너 티켓팅 성공했어?"
                e "사실 내가 TI 완전 팬인데 이번에 티켓팅 실패해서 못 가게 됐거든ㅠㅠ"
                hide e
                f "이 세계의 아이돌은 어떨지 궁금했거든 너랑 같이 가려고 2장 티켓팅했다."
                f "후훗, 한장은 암시장에서 구한거지만"
                show e
                e "와 진짜 친구야ㅠㅠ 사랑한다 너 아니면 어쩔뻔했냐ㅠㅠ 티켓값 지금 보내줄게!"
                hide e
                $friendship += 20
                show screen stat_overlay
                f "굿굿"
                hide screen stat_overlay
                n "근데 TI는 무슨 아이돌인지 잘 모르겠다 ENFP에게 물어보자"
        
                menu:
                    "근데 TI는 뭐하는 애들이냐? 내가 모르는거 보니까 듣보잡인거같은데?ㅋㅋㅋㅋ":
                        $friendship -= 20
                        show e
                        e "우씨 나 완전 팬이라고 했잖아! 우리 TI무시하지 말아줄레? 그래도 표사줬으니까 알려줄게 TI는 6년 전에 있었던 MBTI서바이벌 프로그램에서 나온 아이돌이야."
                        e "총 16명인데 다들 개성이 다 달라! 이번에 하는게 5주년 콘서튼데 진짜 시간 빨리간다."
                        e "나 그 프로그램 본지가 엇그제 같은데. 이 그룹에 나랑 같은 이름인 애도 있음!" 
                    "너 진짜 TI좋아하는구나 표사길 잘했네 표 보니까 5주년 써있던거 같은데 오래한 아이돌이네. 넌 언제부터 팬이었어?":
                        $friendship +=20
                        show e
                        e "맞아 5년차 아이돌이고 이번에 5주년으로 콘서트하는거야! TI에 대해 조금 소개하자면 TI는 6년 전에 있었던 MBTI서바이벌 프로그램에서 나온 아이돌이야. 나 그 프로그램 본지가 엇그제 같은데."
                        e "총 16명인데 다들 개성이 다 달라! 이번에 하는게 5주년 콘서튼데 진짜 시간 빨리간다. "
                        e " 이 그룹에 나랑 같은 이름인 애도 있음! "
                show screen stat_overlay

                f "아 그래? 이름이 ENFP인 아이돌도 있구나~"
                hide screen stat_overlay
                e "응! 걔는 내 차애고 내 최애는 ISTP야!>< 너무 잘생겼어 나 지갑에 포카 있잖아~ 한번 봐봐ㅋㅋㅋㅋ"
                hide e
        
                ## 지하철 배경사진
                f "너 콘서트 몇시에 하는지 알아?"

                show e with dissolve 
                e "6시!"
                hide e
                menu:
                     "그럼 지금 3시니까 시간 많네~ 여기저기 돌아다녀보자!":
                        e "꺄~ 신난다!"
                        $friendship += 20
                        show e
                     "지금은 3시라서 시간 생각보다 없어 티켓뽑고, 굿즈사고, 사진찍고, 화장실 가고, 우리는 스텐딩석이니까 줄기다려서 표 확인 받고 다 해야함 내가 최적의 동선을 짜왔으니 걱정 하지말어!":
                        e "3시간이면 충분한거 같은데ㅠㅠ 알았어. 그렇게 하자...."
                        $friendship -= 20
                        show e
                show screen stat_overlay
                hide e
                ##굿즈판매소 줄 기다리기
                show e with dissolve
                e "와 사람 진짜 많다ㄷㄷ 너 말대로 빠릿빠릿하게 욺직이길 잘했네."
                hide screen stat_overlay
                f "..."
                f "너 시간 계산은 해봤냐ㅋㅋㅋ"
                e "아닠ㅋㅋ 운명에 맡기는거지~"
                e "아 근데 줄 기다리는데 너무 힘들다ㅠㅠ 언제 사람이 빠질까..."
                hide e
                menu:
                       "아까 시간 확인 해봤는데 한 사람당 2분정도 걸리네. 앞에 28명 남았으니까, 56분만 참어. 나도 지쳐서 짜증난다.":
                           e "ㅠㅠ 알았어 징징거리지 않을게..."
                           $friendship -= 20
                           show e
                       "흠.. 우리 그럼 기다리는 동안 끝말잇기나 할레?":
                           e "오~ 똑똑한데? 좋아! 3글자로 쿵쿵따하자!"
                           $friendship += 20
                           show e
                n "..."
                hide e with dissolve
                show screen stat_overlay
                ##콘서트장 앞
                e "음냐~ 콘서트 이제 1시간 남았네"
                hide screen stat_overlay
                f "맞아 얼마 안남았어"
                e "으아 떨린다! ISTP얼굴 볼 생각하니까 너무 좋아ㅠㅠ"
                e "직캠말고 직접 두눈으로 보는 날이 오다니!"
                e "어? 저기봐! 저기서도 굿즈 판다"
                menu:
                    "흠... 친구야 여기 바가지만 조시하고 꼭 사고싶은것만 사자!":
                        e "ㅎㅎ 나도 알고 있지 구경만할껴~"
                        $friendship += 20
                    "야 너 바보냐? 콘서트장 앞에서 파는 것들 불량인데다 바가지나 씌우고 별로야 그냥 사지마":
                        e "칫 구경만 할꺼거든!"
                        $friendship -= 20
                show screen stat_overlay
                f "그럼 다행이고 ^^"
                ##콘서트장 앞 대기줄
                n "30분 전"
                ti "여러분~! 콘서트 때 우리 오빠들을 위한 깜짝 이벤트가 있습니다~ 떼창 꼭 같이 해주시고 지금 나눠드리는 5주년 단콘 축하해 우리 사랑 영원해"
                ti "판플렛 꼭 흔들어주세요! 감사합니다~"
                e "f야 너 떼창곡 뭔지 알아? 다른 곡들은? 응원법 알려줄까?"
                menu:
                        "됐어. 그냥 따라 부르면 되지ㅋㅋ":
                            e "아 왜ㅠㅠ 그럼 떼창곡만 알려줄게. 여기 후렴 부분에 우리 사랑 영원해~"
                            e "가사만 잘 따라하면 쉽게 따라올 수 있을 거야"
                            $friendship -= 20    
                        "오! 그럼 지금 시간 없으니까 떼창곡만 알려주라.":
                            e "굿 초이스~ 그럼 떼창곡만 알려줄게. 여기 후렴부분에 우리 사랑 영원해~"
                            e "가사 자주 나오니까 꼭 외우고 우리 꼭 다시 만나~ 여기 부분에서"
                            e "음정 키업 되니까 주의하면 돼!"
                            $friendship += 20
                show screen stat_overlay
                ##
                n "그렇게 TI콘서트가 무사히 마무리 되었다."
                hide screen stat_overlay
                e "야야 마지막에 앵콜노래 나올 때 봤어? ISTP가 나 보고 하트 날려줬어ㅠㅠㅠㅠ"
                e "나 심장 멎을 것만 같아"
                menu:
                    "욜~ 어떻게 너의 최애가 딱 너 앞으로 오더라. 기분 째지겠넼ㅋㅋㅋ":
                        e "진짜루ㅠㅠ 오늘 진짜 너 덕분에 잘 놀았다!"
                        $friendship += 20
                    "ㅋㅋㅋ야 너한테 했겠냐. 옆에 다른 애들한테 한 거겠지 착각하기는 쯪쯪":
                        e "진짜 너무하네 아 그렇다고 해주면 되지 뭘 그렇게 딱 잡아서 아니라고 하냐! 칫..."
                        $friendship -= 20
                show screen stat_overlay
                ##콘서트 앞
                e "이제 헤어질 시간이네~ 오늘 싸인포카도 얻고, 최애한테 하트도 받고 너무 행복한 시간들이었다!"
                hide screen stat_overlay
                f "흠.. 나는 완전 잊혀진거같군ㅋㅋㅋㅋㅋ"
                e "아! 아니야! 진짜 까먹은거 아니얔ㅋㅋㅋ"
                e "잠시만 나 화장실 좀 갔다올게! 좀만 기다려줘"
                f "그려 빨리 갔다와 밤 되니까 춥다."
                n "자자~ 5주년 콘서트 기념 무료 나눔합니다~"
                n "선착순으로 가져가시면 됩니다! 먼저 가져가는 사람이 임자!"
                f "무료 나눔? 선착순? 이거 다 털릴텐데"
                f "빨리 가서 ENFP꺼 챙겨야겠다."
                
                call speedgame  
                scene image "bg white.png"
                f "왔어?"
                show e with dissolve
                e "응! 어? 손에 그건 뭐야? 뭔가 엄청 많이 들고있네?"
                f "자, 널 위한 선물이다."
                e "우와 고마워! 헐? 이건 뭐야 굿즈들이 가득? 어떻게 구했어?"
                hide e
                menu:
                    "오다 주웠다.":
                        e "앜ㅋㅋㅋㅋ 고맙다! 이쁜거 많네~ㅎㅎㅎ"
                        $friendship += 20
                    "어이 세상엔 공짜가 없다는거 알지?":
                        e "엥? 아까는 선물이라며ㅠㅠ 얼마나 산거야...?"
                        $friendship -= 20
                        f "ㅋㅋㅋ 농담이야"
                show screen stat_overlay
                ##지하철 앞
                e "이야 벌써 헤어질 시간이네?"
                hide screen stat_overlay
                f "벌써? 난 하루가 꽤 길었는데;;"
                e "맞아 오늘 진짜 많은 일이 있었어."
                e "참 보람찬 하루였다!"
                f "ㅋㅋㅋㅋ 그려 조심히 들어가고!"
                e "엉야! 너도 조심히 들어가~ 빠이!"

                $friendship = 0

                return

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
