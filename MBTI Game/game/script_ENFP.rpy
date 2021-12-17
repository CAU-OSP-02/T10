label ENFP:
    scene bg subway with fade
    play music "audio/bgm chat.mp3" fadeout 1

    p "○월 ○일. 드디어 앱에서 매칭된 친구와 만나기로 한 날이다.{p}일단 지하철역에서 만나기로 했는데…"

    $ unfreeze()

    $ messages = [] # list of all messages

    $ message_time = False # if True - get current time / or [hours, minutes] / or False
    $ in_history = True # add messages to history
    $ choice_number = True # default 1. choice1 / 2. choice2 / etc. / or False
    $ click_to_continue = False # if False - live mode messages
    $ time_to_send_pm = 2.0 # time to send picture message
    $ time_to_send_am = 2.0 # time to send audio message
    $ under_messenger = True # set False if you don't need a darker background under messenger

    $ typewriter = False # if False - you instantly send a message
    $ typewriter_speed = 2 # how fast you type

    $ interlocutor = "ENFP" # interlocutor's name
    $ interlocutor_online = True # interlocutor status
    $ interlocutor_typing = True # if False - interlocutor instantly sends a message
    $ interlocutor_extra_time = 2.0 # extra writing time
    $ interlocutor_typing_speed = 0.1 # default speed 0.1 * number of letters


    ## 스크립트 ##
    $ show_messenger()

    $ msg ("오늘 드디어 만나네!", who=1, status='online')
    $ msg ("근데 우리 어떻게 알아보지?", who=1, status='online')
    $ msg ("", choices={0:{'jump':'my_photo', 'name':"내 사진을 보내준다"}, 1:{'jump':'my_clothes', 'name':"내 옷차림을 말해준다"}, 2:{'jump':'your_photo', 'name':"사진을 보내줄 수 있냐고 물어본다"}, 3:{'jump':'your_clothes', 'name':"옷차림이 어떻냐고 물어본다"}})

    $ my_photo = False
    $ my_clothes = False
    $ your_photo = False
    $ your_clothes = False

label my_photo:
    python:
        my_photo = True
        msg (None, pic="raven")
        msg ("내 사진이야!")
        msg ("오! 내 사진은 프로필에 있어! 확인해 봐.", who=1)
    jump arrive

label my_clothes:
    python:
        my_clothes = True
        what_wear = renpy.input("내가 무슨 옷을 입고 있더라?")
        msg ("나 [what_wear] 입고 있어. 알아볼 수 있겠지?")
        msg ("오키! 그러면 금방 눈에 띄겠다.", who=1)
    jump arrive

label your_photo:
    python:
        your_photo = True
        msg ("혹시 네 사진 보내줄 수 있어?")
        msg ("그래! 내 프사랑 똑같긴 한데 내 사진이야.", who=1)
        msg (None, who=1, pic="raven")
    jump arrive

label your_clothes:
    python:
        your_clothes = True
        msg ("네가 옷 어떻게 입었는지 알려주면 될 것 같아.")
        msg ("음… 오늘은 무지개색 옷을 입었어. 보면 알 거야!", who=1)
    jump arrive


label arrive:
    pause
    $ hide_messenger()

    "{i}이번 역은 푸앙, 푸앙역입니다. 내리실 문은 오른쪽입니다.{/i}"

    scene bg platform with slowfade

    "도착했다."

    $ show_messenger()

    $ msg ("난 도착했다! 넌 어디쯤 왔어?", who=1)
    $ msg ("방금 역에 내렸어. 지금 어디 있어?")
    $ msg ("오~ 타이밍 딱 맞췄네. 난 지금 계단 바로 옆에!", who=1)

    pause 2.5
    $ hide_messenger()
    window hide

    # jump map                                                                  # 맵으로 이동                                                   
