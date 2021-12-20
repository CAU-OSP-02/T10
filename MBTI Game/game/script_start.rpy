# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
image e_norm = "ENFP_normal.png"
image e_happy = "ENFP_happy.png"
image e_sad = "ENFP_sad.png"
image e_awk = "ENFP_awkward.png"
image ti = "TI_Fan.png"
image so = "Shop_Owner.png"
image sm = "Shop_Manager.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define nv = nvl_narrator
define p = DynamicCharacter("player_name")
define e = Character("ENFP", color="#FFCCCC")
define ti = Character('TI팬클럽회장', color="#353535")
define so = Character('가게 아주머니', color="#ff9dd2")
define sm = Character('가게 종업원', color="9fff9d")

init:
    $ name = "player_name"

# 기타 정의
define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
define slowfade = Fade(.5,.2,.5)
define friendship = 0

# 여기에서부터 게임이 시작합니다.
label start:

    $ is_visited = 0

    scene bg space with dissolve
    play music "audio/bgm space.mp3" fadein 1 fadeout 1
    window hide

    nv """
    내가 사는 별은 OSP-2021이라 불리는, 몹시 아름다운 곳이다.
    {p}우리에게는 기잇 허브라고 하는 워프 기술이 있어, 
    \n누구나 쉽게 우주 여행을 갈 수 있다.
    \n요즘 가장 인기있는 여행지는 지구라는 외계 행성인데,
    지구인 친구를 사귀고 그걸 SNS에 인증하는 게 유행인 것 같다.
    \n부럽다... 나도 외계인 친구가 생기면 좋겠는데...
    {p}라고 생각하던 것도 잠시, 어느새 난 기잇 허브를 타고 있었다.
    """

    "{i}잠시 후 지구에 도착 예정입니다. 기잇 허브를 이용해 주셔서 감사합니다.{/i}"

    """
    아, 잠깐...{w}
    그러고 보니 지구에서는 내 멋진 이름 '깃풀애드커밋푸쉬'를 그대로 썼다간 좀 곤란할 것 같은데.
    {w}지구식 이름을 뭐라고 하지?
    """

    $ player_name = renpy.call_screen("set_name", title="이름 뭐로 할까?")
    $ player_name = player_name.strip() or '플레이어'
    $ name = player_name

    "[player_name]. 좋아. 내 원래 이름보다는 못하지만 나쁘지 않은 것 같다."

    scene bg cafe with slowfade
    play music "audio/bgm cafe.mp3" fadein 1 fadeout 1

    "지구에 와서 가장 처음 온 곳은 '카페'.\n지구인들의 일상에 녹아들기 위해서는 필수 코스라고 들었다."
    "음료 하나를 시켜서 앉은 나는 이제부터 '지구인 친구 사귀기' 플랜을 짜려고 한다.."

    "손님1" "야, 너 MBTI 뭐야?"
    "손님2" "나? 나 ISTJ."
    "손님1" "ISTJ.. 꼰대.. 정확하네."
    "손님2" "뭐? 내가 왜 꼰대야? 야, 넌 뭔데?"

    "MBTI..? ISTJ? 뭐야, 다른 외계 행성 이름인가? 그럼 저 사람들도 외계인?{p}검색해 봐야겠다."

    with flashbulb

    "어?"

    show screen viewport_blog
    window hide
    pause 5.0

    "이 앱 하나만으로도 지구인 친구를 사귈 수 있다고? 그럼 고민할 필요가 없지!"

    hide screen viewport_blog

    scene bg mbti with fade
    play music "audio/bgm map.mp3" fadeout 1

    call screen choice_mbti                                                     # MBTI 선택 화면
