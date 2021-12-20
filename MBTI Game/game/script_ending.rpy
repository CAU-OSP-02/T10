
label ending:
    show screen stat_overlay
    scene bg platform with slowfade
    play music "audio/bgm chat.mp3" fadein 1 fadeout 1
    show e_norm with dissolve
    e "이야 벌써 헤어질 시간이네?"
    hide screen stat_overlay
    p "벌써? 난 하루가 꽤 길었는데;;"
    e "맞아 오늘 진짜 많은 일이 있었어."
    e "참 보람찬 하루였다!"
    p "ㅋㅋㅋㅋ 그려 조심히 들어가고!"
    e "엉야! 너도 조심히 들어가~ 빠이!"
    hide e_norm with dissolve



    hide screen placeUI with dissolve

    scene bg subway with Dissolve(1.0)
    scene bg room with Dissolve(1.0)

    "ENFP와 헤어지고 숙소로 돌아왔다."
    "아무래도 한 번에 지구인 친구를 사귀는 데 성공한 것 같다.\n난 엄청난 인…싸?란 게 아닐까? {w}나중에 또 같이 놀자고 연락해봐야겠다."

    $ show_messenger()

    $ msg ("오늘 재밌었다 ㅎㅎ")
    $ msg ("다음에 또 언제 시간 괜찮아?")

    if friendship < 20:
        $ msg ("음… 잘 모르겠네. 연락하면 시간 생각해 볼게.", who=1, status='online')
        $ msg ("", who=1, status='offline')
        pause
        $ hide_messenger()
        "괜…찮다는 건가? 응? 그런 거야?…"

    if 20 <= friendship < 60:
        $ msg ("오 ㅋㅋ 언젠지는 모르겠지만 다음에는 조금 더 일찍 만나서 놀자 ㅎㅎ", who=1, status='online')
        pause
        $ hide_messenger()
        "며칠을 기다려봤지만 답장이 없다..."

    if 60 <= friendship:
        $ msg ("난 언제든지 시간 되지~ 없어도 시간은 만들어서 논다!", who=1, status='online')
        pause
        $ hide_messenger()
        "며칠을 기다려봤지만 답장이 없다..."

    if friendship < 20:
        scene bg ending_sad with flashbulb
        show e_sad
        
        with dissolve
        
        "{i}당신은 ENFP와 정말 안 맞는 것 같군요. 하지만 노력은 해봐야 하지 않겠어요? 힘내요, 외계인!{/i}"

    if 20 <= friendship < 80:
        scene bg ending_normal with flashbulb
        show e_norm
        
        with dissolve
        
        "{i}당신은 ENFP와 친하다고도, 안 친하다고도 할 수 없는... 그런 친구가 되었습니다.\n어쩔 수 없죠, 뭐. 분발하자고요, 외계인!{/i}"

    if 80 <= friendship:
        scene bg ending_happy with flashbulb
        show e_happy
        
        with dissolve
        
        "{i}당신은 ENFP와 둘도 없는 친구가 되었습니다. 축하합니다, 외계인!{/i}"

    
    return
