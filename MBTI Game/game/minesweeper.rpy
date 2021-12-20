default board = Board(9)

label start_minesweeper:
    menu:
        "게임판의 크기를 정해주세요."
        "9x9":
            $ board = Board(9)
        "12x12":
            $ board = Board(12)

    menu:
        "지뢰의 개수를 정해주세요."
        "10개":
            $ board.create_board(10)
        "20개":
            $ board.create_board(20)

    call screen minesweeper(board.dict)

label lost_minesweeper:
    show screen minesweeper(board.dict, True)

    "땡! 지뢰를 누르셨네요."
    hide screen minesweeper

    menu:
        "다시 도전해보시겠습니까?"

        "재도전":
            jump start_minesweeper

        "게임 끝내기":
            return     
            


label won_minesweeper:
    show screen minesweeper(board.dict, True)
    "축하합니다! 게임에서 이기셨어요:)"
    hide screen minesweeper


screen minesweeper(board, active=False):

    fixed:
        xoffset 450
        yoffset 150

        for key, tile in board.iteritems():
            button:
                style_prefix "minesweeper"
                idle_background "minesweeper_tile"
                insensitive_background Solid("#EEE")
                hover_background im.MatrixColor("minesweeper_tile.png", im.matrix.brightness(0.1))
                xsize 40
                ysize 40
                xpos tile.x * 40
                ypos tile.y * 40
                if active and tile.mine:
                    text "*"
                elif tile.cleared:
                    action None
                    if tile.number != 0:
                        text "[tile.number]" color "#555"
                elif tile.flag:
                    add "minesweeper_flag" xoffset -2
                action Function(tile.click_button)
                alternate Function(tile.flag_toggle)

    if active:
        button:
            xsize 450
            ysize 400
            xalign 0.35
            yalign 0.45
            background None 
            action Return()
    

init:
    style minesweeper_button is button:
        margin (0, 0)
        left_padding 13
        top_padding 7

init python:

    class Tile():
        def __init__(self, x, y, size):
            self.x = x
            self.y = y
            self.size = size
            self.mine = False
            self.flag = False
            self.cleared = False
            self.number = 0 

        def create_mine(self):
            self.mine = True
            self.cleared = None

        def flag_toggle(self):
            if self.flag:
                self.flag = False
            else:
                self.flag = True

        def click_button(self):
            if self.flag:
                pass
            elif self.mine:
                renpy.jump("lost_minesweeper")
            else:
                self.cleared = True

                if self.number == 0:
                    x = self.x
                    y = self.y

                    temp = []
                    for i in [-1, 0, 1]:
                        for j in [-1, 0, 1]:
                            if i != 0 or j != 0:
                                x1 = x+i
                                y1 = y+j
                                if x1 >=0 and y1 >=0 and x1 < self.size and y1 < self.size:
                                    temp.append(board.dict[(x1, y1)])

                    for i in temp:
                        if not i.cleared:
                            i.click_button()

                self.check_win()


        def check_win(self):
            temp = [value.cleared for key, value in board.dict.iteritems()]
            if False not in temp:
                renpy.jump("won_minesweeper")


    class Board():
        def __init__(self, size):
            self.size = size
            self.dict = {} 

        def create_board(self, mines):
            
            self.dict = {}
            for y in range(self.size):
                for x in range(self.size): 
                    index = (x, y)
                    self.dict[index] = Tile(x, y, self.size)

           
            count = 0
            while count < mines:
                x = renpy.random.randint(0, self.size-1)
                y = renpy.random.randint(0, self.size-1)
                if self.dict[(x, y)].mine:
                    continue
                else:
                    self.dict[(x, y)].create_mine()
                    count += 1

           
            for key, value in self.dict.iteritems():
                x, y = key

                temp = []
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if i != 0 or j != 0:
                            x1 = x+i
                            y1 = y+j
                            if x1 >=0 and y1 >=0 and x1 < self.size and y1 < self.size:
                                temp.append(board.dict[(x1, y1)])
                for i in temp:
                    if i.mine:
                        value.number += 1
