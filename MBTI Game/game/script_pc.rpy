﻿#이미지
image e = im.FactorScale("e.png", 1)
image pc:
       "bg pc.jpg"
       size(1280, 720)
image heart:
         "heart.png"
         size(30,30)
image empty_heart:
         "emptyheart.png"
         size(30,30)

#캐릭터 정의
define p = Character()                                                            
define e = Character('ENFP', color="#FF5E00")

#친밀도
define friendship = 0

#친밀도 창
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

#대본
label pc:
  
  play music "bgm.mp3" loop volume 0.01

  show e with dissolve
  e "심심한데 피시방 가자!"
  p "피시방??"
  p "피시방이 뭐야?"
  e "엥 피시방을 모른다고!??"
  e "신기하네..음 돈내고 컴퓨터 사용하는 곳이야"
  p "아하 그래 가자 재밌겠다"
  hide e with dissolve
  
  scene bg
  
  show e with fade
  e "여기 담배 냄새 나니깐 저기 구석으로 가자"
  $friendship += 20
  show screen stat_overlay
  p "그래"
  e "우리 게임하자"
  hide screen stat_overlay
  e "무슨 게임하지...?"
  p "둘이 같이 할 수 있는거 하자"
  e "그럼 둘이 할 수 있는 피파하자"
  p "좋아"
  hide e with fade

  show e at right with dissolve
  e "아...이걸 지네"
  p "너무 쉽다 잘 좀 해봐"
  e "내가 실수 한거야!"
  e "다시 해 이길 수 있어"
  p "그래그래 내가 특별히 다시 해줄게^^"
  hide e with dissolve

  show e at right with fade
  e "거봐 다시하면 이긴다고 했지 ㅋㅋ"
  menu: 
      "오 잘하네":
        $friendship += 20
      "인정 못해 다시 해":
        $friendship += 20
      "노잼":
        $friendship -= 20
  show screen stat_overlay
  hide e with fade
  hide screen stat_overlay

  show e with fade
  e "흐아~ 이제 슬슬 배고프다"
  p "나도"
  e "그럼 우리 뭐 시켜먹자!"
  p "그래"
  p "응? 여기서 먹자고?"
  menu:
      "응 식당보다 맛있진 않지만 귀찮으니간 여기서 먹자":      
        e "맛있는 거 먹고 싶긴한데..."
        $friendship -= 20
      "피시방 밥 비싼데 밖에 나가서 맛있는 식당 찾아보자":
        e "좋다"
        $friendship += 20
  show screen stat_overlay
      
  e "밥 먹기 전에 내기하자"
  p "무슨 내기?"
  hide screen stat_overlay
  e "밥값 내기 어때?"
  menu:
      "좋다, 재밌겠다":
        e "무슨 게임으로 내기할까?"
        $friendship += 20
      "싫어..":
        e "오키..그럼 나가기 전에 게임 하나 하고 가자"
        $friendship -= 20
  show screen stat_overlay

  e "지뢰찾기 게임 어때?"
  p "지뢰찾기 게임이 뭐지??"
  hide screen stat_overlay
  p "어떻게 하는지 알려줘"
  e "그냥 지뢰가 없는 칸을 모두 찾아 클릭하면 되는 거야"
  e "생각보다 머리 많이 써야되는 게임이다"
  p "그럼 처음 해도 내가 이기겠는데??ㅋㅋㅋㅋㅋ"
  e "무슨소리야 당연히 내가 이기지 ㅋㅋㅋㅋㅋ"
  p "그럼 한번 해보자"
  hide e with fade
  
  show e with dissolve
  e "그럼 지뢰찾기 게임 시작한다. 마우스 오른쪽 버튼은 깃발 표시하는거야. 잘해봐^^"
  hide e with dissolve
  
  jump start_minesweeper

  $friendship = 0

  return

