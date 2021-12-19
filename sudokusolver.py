import sys
import pygame
from algo import solve
from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw()  # to hide the main window

pygame.init()
pygame.display.set_caption("Sudoku Solver")
clock = pygame.time.Clock()
size = width, height = 650, 560
screen = pygame.display.set_mode(size)
selected = (0, 0)
pygame.font.init()  # you have to call this at the start,
# if you want to use this module.
myfont = pygame.font.SysFont('Arial', 22)


board = [
        [6, 0, 0, 0, 0, 2, 0, 0, 5],
        [2, 0, 1, 0, 0, 0, 3, 0, 8],
        [0, 0, 5, 0, 0, 3, 4, 0, 0],
        [0, 0, 4, 0, 2, 0, 1, 0, 0],
        [0, 0, 0, 5, 0, 1, 0, 0, 0],
        [0, 6, 0, 0, 4, 0, 0, 5, 0],
        [0, 0, 9, 4, 0, 0, 6, 0, 0],
        [8, 0, 2, 0, 0, 0, 9, 0, 1],
        [4, 0, 0, 2, 0, 0, 0, 0, 7]
]


def drawGrid():
    screen.fill(pygame.Color("white"))

    for i in range(0, 9):
        for j in range(0, 9):
            if board[j][i] != 0:
                textsurface = myfont.render(str(board[j][i]), False, (0, 0, 0))
                screen.blit(textsurface, (i*50 + 15, j*50 + 10))
            if (i, j) == selected:
                pygame.draw.rect(screen, pygame.Color("red"),
                                 (i * 50, j * 50, 50, 50), 1)
            else:
                pygame.draw.rect(screen, pygame.Color("grey"),
                                 (i * 50, j * 50, 50, 50), 1)

    pygame.draw.line(screen, pygame.Color("black"), (150, 0),
                     (150, 450), 2)
    pygame.draw.line(screen, pygame.Color("black"), (300, 0),
                     (300, 450), 2)
    pygame.draw.line(screen, pygame.Color("black"), (0, 150),
                     (450, 150), 2)
    pygame.draw.line(screen, pygame.Color("black"), (0, 300),
                     (450, 300), 2)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if not solve(board):
                    messagebox.showinfo('Alert', 'No Solution Found')
            elif event.key == pygame.MOUSEBUTTONDOWN:
                print("click")
    drawGrid()
    pygame.display.flip()
    clock.tick(60)
