import random
import colorama
from colorama import Fore, Back, Style
import keyboard
from os import system, name
colorama.init()

movement = True

menu = ("""


""")

build = []

class Coordinates(object):
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = vel

player = Coordinates(50, 12, 1)
ghoul = Coordinates(48, 10, 1)
block = Coordinates(0, 0, 0)

def move_up():
    if player.y > 0:
        player.y -= player.vel
    else:
        player.y = player.y
    system('cls')
    draw_map()
def move_left():
    if player.x > 1:
        player.x -= player.vel
    else:
        player.x = player.x
    system('cls')
    draw_map()
def move_right():
    if player.x < 97:
        player.x += player.vel
    else:
        player.x = player.x
    system('cls')
    draw_map()
def move_down():
    if player.y < 19:
        player.y += player.vel
    else:
        player.y = player.y
    system('cls')
    draw_map()

def place_block():
    blockprompt = input(Fore.GREEN + """Place block Where? > """ + Fore.WHITE)
    menu = blockprompt
    if blockprompt == 'w':
        block.y = (player.y - 1)
        block.x = player.x
    if blockprompt == 'a':
        block.y = player.y
        block.x = (player.x - 1)
    if blockprompt == 'd':
        block.y = player.y
        block.x = (player.x + 1)
    if blockprompt == 's':
        block.y = (player.y + 1)
        block.x = player.x
    system('cls')
    draw_map()
    return block.x and block.y
    
def draw_map():
    width = 99
    height = 20
    def get_level_row():
        print(Fore.WHITE)
        return [' '] * width

    level = [get_level_row() for row in range(height)]


    ghoulwalk = random.randint(1, 4)
    if ghoulwalk == 1 and ghoul.x < 97:
        ghoul.x += 1
    if ghoulwalk == 2 and ghoul.x > 1:
        ghoul.x -= 1
    if ghoulwalk == 3 and ghoul.y < 19:
        ghoul.y += 1
    if ghoulwalk == 4 and ghoul.y > 1:
        ghoul.y -= 1
    x = ghoul.x
    y = ghoul.y
    level[y][x] = (Fore.RED + 'G' + Fore.WHITE)

    x = player.x
    y = player.y     
    level[y][x] = (Fore.GREEN +  '@' + Fore.WHITE)

    build.append(list((block.x, block.y)))
    for i in build:
        x = i[0]
        y = i[1]
        level[y][x] = '#'
                
    for x in range(0,1):
        for y in range(0,20):
            level[y][x] = '<'
    for x in range(98,99):
        for y in range(0,20):
            level[y][x] = '>'

    print('^' * width)

    for row in level:
        mapgen = print( ''.join(row))
   
    print(("v" * width) + menu)

draw_map()    

keyboard.add_hotkey("b", lambda: place_block())
                    
if movement:
    keyboard.add_hotkey("w", lambda: move_up())
    keyboard.add_hotkey("a", lambda: move_left())
    keyboard.add_hotkey("d", lambda: move_right())
    keyboard.add_hotkey("s", lambda: move_down())

while True:
    input()

