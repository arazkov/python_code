from tkinter import Canvas
import random


def get_winner(GAME_STATE):
    if (GAME_STATE[0] == 'x' and GAME_STATE[1] == 'x' and GAME_STATE[2] == 'x' or
        GAME_STATE[3] == 'x' and GAME_STATE[4] == 'x' and GAME_STATE[5] == 'x' or
        GAME_STATE[6] == 'x' and GAME_STATE[7] == 'x' and GAME_STATE[8] == 'x' or
        GAME_STATE[0] == 'x' and GAME_STATE[3] == 'x' and GAME_STATE[6] == 'x' or
        GAME_STATE[1] == 'x' and GAME_STATE[4] == 'x' and GAME_STATE[7] == 'x' or
        GAME_STATE[2] == 'x' and GAME_STATE[5] == 'x' and GAME_STATE[8] == 'x' or
        GAME_STATE[0] == 'x' and GAME_STATE[4] == 'x' and GAME_STATE[8] == 'x' or
        GAME_STATE[6] == 'x' and GAME_STATE[4] == 'x' and GAME_STATE[2] == 'x'):
        return 'x_win'
    elif (GAME_STATE[0] == 'o' and GAME_STATE[1] == 'o' and GAME_STATE[2] == 'o' or
          GAME_STATE[3] == 'o' and GAME_STATE[4] == 'o' and GAME_STATE[5] == 'o' or
          GAME_STATE[6] == 'o' and GAME_STATE[7] == 'o' and GAME_STATE[8] == 'o' or
          GAME_STATE[0] == 'o' and GAME_STATE[3] == 'o' and GAME_STATE[6] == 'o' or
          GAME_STATE[1] == 'o' and GAME_STATE[4] == 'o' and GAME_STATE[7] == 'o' or
          GAME_STATE[2] == 'o' and GAME_STATE[5] == 'o' and GAME_STATE[8] == 'o' or
          GAME_STATE[0] == 'o' and GAME_STATE[4] == 'o' and GAME_STATE[8] == 'o' or
          GAME_STATE[6] == 'o' and GAME_STATE[4] == 'o' and GAME_STATE[2] == 'o'):
              return 'o_win'
    elif None not in GAME_STATE:
        return 'draw'

def move(i):
    if GAME_STATE[i] == None: 
        GAME_STATE[i] = 'x'
        if get_winner(GAME_STATE) != None:
            canvas.stroke_text(get_winner(GAME_STATE), 50, 50)
        GAME_STATE[get_bot_move(GAME_STATE)] = 'o'
        if get_winner(GAME_STATE) != None:
            canvas.stroke_text(get_winner(GAME_STATE),50, 50)

def get_bot_move(GAME_STATE):
    while True:
        i = random.randint(0, len(GAME_STATE)-1)
        if GAME_STATE[i] != 'x' and GAME_STATE[i] != 'o':
            break
    return i

def click(x, y):
    if x < cen and y < cen: 
        move(0)
    elif cen < x < 2 * cen and y < cen: 
        move(1)
    elif cen * 2 < x < 3 * cen and y < cen: 
        move(2)
    elif x < cen and cen < y < 2 * cen: 
        move(3)
    elif cen < x < 2 * cen and cen < y < 2 * cen:
        move(4)
    elif cen * 2 < x < 3 * cen and cen < y < 2 * cen: 
        move(5)
    elif x < cen and cen * 2 < y < 3 * cen: 
        move(6)
    elif cen < x < 2 * cen and cen *2 < y < 3 * cen: 
        move(7)
    else: 
        move(8)
    draw_state(GAME_STATE)

def kvad(coord, i):
    coordinate = [
        [cen/2, cen/2],[cen + cen/2, cen/2],[cen*2 + cen/2, cen/2],
        [cen/2, cen/2 + cen],[cen + cen/2, cen/2 + cen],[cen*2 + cen/2, cen/2 + cen],
        [cen/2, cen/2 + cen*2],[cen + cen/2, cen/2 + cen*2],[cen*2 + cen/2, cen/2 + cen*2],
        ]
    return coordinate[i][0] if coord == 'x' else coordinate[i][1]

def draw_x(i):
    canvas.set_color('blue')
    canvas.line_width(5)
    grad = 45
    for e in range(4):
        canvas.radius_line(kvad('x',i), kvad('y',i), grad, 40)
        grad += 90
        
def draw_o(i):
    canvas.set_color('green')
    canvas.line_width(5)
    canvas.circle(kvad('x',i), kvad('y',i), 30)
    
def draw_grid():
    canvas.radius_line(350/3, 0, 180, 350)
    canvas.radius_line(2*350/3, 0, 180, 350)
    canvas.radius_line(0, 350/3, 90, 350)
    canvas.radius_line(0, 2*350/3, 90, 350)
    canvas.draw()

def draw_state(GAME_STATE):
    for i in range(len(GAME_STATE)):
        if GAME_STATE[i] == 'x':
            draw_x(i)
        elif GAME_STATE[i] == 'o':
            draw_o(i)
    canvas.draw()

cen = 350/3    
GAME_STATE = [None, None, None, None, None, None, None, None, None]
draw_grid()
canvas.set_onclick(click)
canvas.listen()

