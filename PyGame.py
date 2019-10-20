import pygame
from pygame.display import set_caption
from colors import *
pygame.init()

x1 = 0  # координата х
y1 = 0  # координата y
d = 30  # длина квадрата
w = 0  # ширина квадрата
WIN_WIDTH = 500
WIN_HEIGHT = 340
clock = pygame.time.Clock()
set_caption('TAB TO SCREEN FOR GAME, mn1v.prodj')
los = int(1)
clicks = 'Кликов: '

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
back_int = 0
fi_int = 0
pygame.display.update()
while True:
    backgr = (WHEAT, WHEAT1, WHEAT2, WHEAT3, WHEAT4)
    hero = (WHEAT4, WHEAT, WHEAT1, WHEAT2, WHEAT3)
    sc.fill(backgr[back_int])
    for i in pygame.event.get():
        if i.type == pygame.MOUSEBUTTONDOWN:
            text = clicks + str(los)
            set_caption(text)
            los += 1
        if i.type == pygame.QUIT:
            exit()
    pygame.draw.rect(sc, hero[fi_int], (x1, y1, d, w))  # рисуем квадрат
    pygame.display.update()

    if x1 == WIN_WIDTH:  # если кооснулось правой стенки то
        k = -2  # движение в обратную сторону
        x1 += k
        back_int += 1
        fi_int += 1
        if fi_int == 4:
            fi_int = 0
        if back_int == 4:
            back_int = 0
    elif x1 == 0:  # движение влево после того как координата х = 0
        k = 2
        x1 += k
        back_int += 1
        fi_int += 1
        if fi_int == 4:
            fi_int = 0
        if back_int == 4:
            back_int = 0
    else:  # движение в правую сторону от левой стенки
        x1 += k
    pygame.time.delay(10)
