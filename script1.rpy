# 이미지 정의
image e = "e.png"
image f = "f.png"
image t = "t.png"
image s = "s.png"
image school = "school.png"                  #임시 학교 사진
image class = im.FactorScale("class.png", 2) #임시 배경 사진


# 캐릭터 정의 
define e = Character('ENFP', color="#c8ffc8")
define f = Character('INFP', color="c8ffc8")
define t =Character('INTP', color="c8ffc8")
define s = Character('ISFP', color="c8ffc8")
define a = Character('주인공', color="c8ffc8")
define b = Character('담임선생님', color="c8ffc8")
define c = Character('영어선생님', color="c8ffc8")
define d = Character('수학선생님', color="c8ffc8")


# 호감도 정의
init -99:
    $love_of_e = 0
init -99:
    $love_of_f = 0
init -99:
    $love_of_t = 0
init -99:
    $love_of_s = 0


# 게임이 시작
# 1교시 영어 - 행맨
label start:

  scene class #임시 교실 배경

  a "영어시간이네 열심히 해보자!"
  
  c "Hi hello~ How are you?"
 
  c "Today, we will introduce ourselves!" 
  
  show e  
  
  e "히익 영어라니 잘모르지만 열심히 해보자><"
  
  hide e with dissolve
  
  c "You guys have own number right?"
  
  c "Number 9! Please introduce yourself" 
  
  show t
  
  t "Hi my name is INTP. I like to solve problems with logic and analysis. I don't usually talk, but I do talk a lot about my interests. Thank you!"
  
  hide t with fade
  
  show e

  e "우와 영어 짱잘한다! t랑 친해지고 싶은걸~" 
  
  hide e with fade

  show s

  s "내 번호는 안불렸으면 좋겠다…."

  hide s
 
  c "Good job! Next… number 4!"
  
  show s
  
  s "Hi my name is ISFP. I like creative activities. Also I like playing with my friends. Thank you!"
  
  hide s

  c "Very good! Next...number 16!"

  show f

  f "Hi my name is INFP. I interacts well with people. Also I enjoy the challenge. Thank you!"

  hide f

  c "Good. Next..number 17!"

  show e

  e "Hi my name is ENFP. I enjoy trying different things. Also I get along well with friends. Thank you!"

  hide e

  c "Very good~. Now we know well each other."  

  a "나와 잘 맞는 친구는 누굴까??"

  menu:
    "INTP":
        $love_of_t = love_of_t + 1
        "INTP에 대한 호감도가 1상승했습니다."
    "ENFP":
        $love_of_e = love_of_e + 1
        "ENFP에 대한 호감도가 1상승했습니다."
    "INFP":
        $love_of_f = love_of_f + 1
        "INFP에 대한 호감도가 1상승했습니다."
    "ISFP":
        $love_of_s = love_of_s + 1
        "ISFP에 대한 호감도가 1상승했습니다."
  
  c "As you know, memorizing word is important so.."
  
  c "Let’s play Hangman game! If you give the correct answer, I will give you a prize."
 
  ## (행맨게임화면)
 
  c "The prize was applause. See you next time."


  return
