import pygame
import time

#Инициализация PyGame

pygame.init()

#Окно игры позиция

gameScreen = pygame.display.set_mode((400, 500))


#параметры окна

size = [500, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
#gameScreen.fill((0,0,255))
#pygame.display.flip()

#Цикл игры, выход из игры

#Цикл игры

runGame = True # флаг выхода из цикла игры

r = 0
g = 0
b = 0
con = 1

while runGame:
    gameScreen.fill((r,g,b))
    pygame.display.flip()
    
    time.sleep(0.01)
    if r < 255: r+=con 
    elif g < 255: g+=con
    elif b < 255: b+=con
    else: con = -con
#Отслеживание события: "закрыть окно"

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            runGame = False
            pygame.quit()
