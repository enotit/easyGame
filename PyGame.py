import random

import pygame
from pygame.display import set_caption
from colors import *


def true(objectes, tf, inter, fiter):
    if objectes == tf:
        inter += 1
        return True, inter
    else:
        return False, fiter


def false(objectes, tf, inter, fiter):
    if objectes != tf:
        inter += 1
        return True, inter
    else:
        return False, fiter


def geo():
    f2 = pygame.font.Font(None, 60)
    sec = 4
    fen = 0
    bo = True
    ans = True
    lex = 0
    fig = str('')
    lex1 = 0
    trush = False
    tex = str('')
    set_caption('ГеоИгра')
    f1 = pygame.font.Font(None, 46)
    while sec:
        sec -= 1
        keys = pygame.key.get_pressed()
        pygame.display.update()
        sc.fill(MINT)
        texts = f2.render(str(sec), 1, RED1)
        sc.blit(texts, (500, 320))
        pygame.time.delay(600)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
            if keys[pygame.K_DOWN]:
                return
        pygame.time.delay(10)
    sc.fill(MINT)
    while bo:
        pygame.display.update()
        sc.fill(MINT)

        if ans:
            ran = random.randint(1, 4)
            lex = random.randint(0, 3)
            lex1 = random.randint(1, 3)
            if ran == 1:  # треугольник
                fig = 'треугольник'
                if lex == 0:
                    tex = 'треугольник'
                elif lex1 == 1:
                    tex = 'круг'
                elif lex1 == 2:
                    tex = 'квадрат'
                elif lex == 3:
                    tex = 'овал'
            elif ran == 2:  # круг
                fig = 'круг'
                if lex == 0:
                    tex = 'круг'
                elif lex1 == 1:
                    tex = 'треугольник'
                elif lex1 == 2:
                    tex = 'квадрат'
                elif lex == 3:
                    tex = 'овал'
            elif ran == 3:  # квадрат
                fig = 'квадрат'
                if lex == 0:
                    tex = 'квадрат'
                elif lex1 == 1:
                    tex = 'круг'
                elif lex1 == 2:
                    tex = 'треугольник'
                elif lex == 3:
                    tex = 'овал'
            else:  # овал
                fig = 'овал'
                if lex == 0:
                    tex = 'овал'
                elif lex1 == 1:
                    tex = 'круг'
                elif lex1 == 2:
                    tex = 'квадрат'
                elif lex == 3:
                    tex = 'квадрат'
            ans = False
        text1 = f1.render(tex, 1, RED1)
        sc.blit(text1, (350, 550))
        text2 = f1.render(str(fen), 1, RED1)
        sc.blit(text2, (10, 10))
        if fig == 'треугольник':
            pygame.draw.lines(sc, BLACK, True, [[400, 300], [700, 300], [400, 80]], 3)
        elif fig == 'круг':
            pygame.draw.circle(sc, BLACK, (500, 300), 100)
        elif fig == 'квадрат':
            pygame.draw.rect(sc, BLACK, (300, 180, 300, 275))
        elif fig == 'овал':
            pygame.draw.ellipse(sc, BLACK, (200, 250, 480, 300))
        textt = f1.render('Правда', 1, DARKOLIVEGREEN)
        sc.blit(textt, (850, 300))
        textf = f1.render('Ложь', 1, RED2)
        sc.blit(textf, (10, 300))
        keys = pygame.key.get_pressed()
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
            if keys[pygame.K_DOWN]:
                return
            elif keys[pygame.K_RIGHT]:
                ans = True
                if fig == tex:
                    fen += 1
            elif keys[pygame.K_LEFT]:
                if fig != tex:
                    fen += 1
                ans = True
    pygame.time.delay(1)

def main():
    lister = (DARKGREEN, GREEN1, GREEN1)
    cursorer = int(0)
    while 1:
        pygame.display.update()
        sc.fill(MINT)
        f21 = pygame.font.Font(None, 20)
        f2 = pygame.font.Font(None, 35)
        set_caption('Основное меню')
        text21 = f21.render('для выхода нажмите кнопку "вниз"', 1, TEAL)
        one_text = f2.render('геометрия', 1, lister[0])
        two_text = f2.render('математика', 1, lister[1])
        three_text = f2.render('настройки', 1, lister[2])
        sc.blit(text21, (0, 0))
        sc.blit(one_text, (150, 320)); sc.blit(two_text, (400, 320)); sc.blit(three_text, (650, 320))
        for i in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                return
            elif keys[pygame.K_RIGHT]:
                cursorer += 1
            elif keys[pygame.K_LEFT]:
                cursorer -= 1
            elif keys[pygame.K_UP]:
                if cursorer == 0:
                    geo()

            if i.type == pygame.QUIT:
                exit()

            if cursorer == 3:
                cursorer = 0
            elif cursorer == -1:
                cursorer = 2

            if cursorer == 0:
                lister = (DARKGREEN, GREEN1, GREEN1)
            elif cursorer == 1:
                    lister = (GREEN1, DARKGREEN, GREEN1)
            elif cursorer == 2:
                lister = (GREEN1, GREEN1, DARKOLIVEGREEN)
            pygame.display.update()
        pygame.time.delay(10)


pygame.init()
x1 = 0  # координата х
y1 = 0  # координата y
d = 30  # длина квадрата
w = 0  # ширина квадрата
WIN_WIDTH = 1000  # ширина
WIN_HEIGHT = 640  # высота
clock = pygame.time.Clock()
set_caption('READ SCREEN')
los = int(1)
clicks = 'NOT CLICK '

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
back_int = 0
fi_int = 0
pygame.display.update()
while 1:
    backgr = (WHEAT, WHEAT1, WHEAT2, WHEAT3, WHEAT4)
    hero = (WHEAT4, WHEAT, WHEAT1, WHEAT2, WHEAT3)
    sc.fill(backgr[back_int])
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render('Чтобы продолжить нажмите клавишу "вверх"', 1, TEAL)
    sc.blit(text1, (WIN_WIDTH // 2 - 280, WIN_HEIGHT // 2))
    text2 = f1.render('Чтобы выйти нажмите клавишу "вниз"', 1, SEPIA)
    sc.blit(text2, (WIN_WIDTH // 2 - 250, WIN_HEIGHT // 2 + 50))
    for i in pygame.event.get():
        keys = pygame.key.get_pressed()
        if i.type == pygame.MOUSEBUTTONDOWN:
            text = clicks + str(los) + 'x'
            set_caption(text)
            los += 1
        elif keys[pygame.K_UP]:
            main()
        elif keys[pygame.K_DOWN]:
            exit()
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
