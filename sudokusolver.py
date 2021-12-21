import sys
import pygame
from algo import solve
from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw()  # to hide the main window

pygame.init()
pygame.display.set_caption("Sudoku Solver")
clock = pygame.time.Clock()
size = width, height = 650, 550
screen = pygame.display.set_mode(size)
selected = (0, 0)
pygame.font.init()  # you have to call this at the start,
# if you want to use this module.
myfont = pygame.font.SysFont('Times New Roman', 22)


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

    # Draw Buttons
    pygame.draw.rect(screen, pygame.Color("lightgrey"), (500, 50, 100, 50))
    pytextsurface = myfont.render("Solve", False, (0, 0, 0))
    screen.blit(pytextsurface, (520, 60))
    pygame.draw.rect(screen, pygame.Color("lightgrey"), (500, 150, 100, 50))
    pytextsurface = myfont.render("Reset", False, (0, 0, 0))
    screen.blit(pytextsurface, (520, 160))


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if not solve(board):
                    messagebox.showinfo('Alert', 'No Solution Found')
            if event.unicode >= '0' and event.unicode <= '9':
                if selected[1] <= 8 and selected[0] <= 8:
                    num = ord(event.unicode) - ord('0')
                    board[selected[1]][selected[0]] = num
            if event.key == pygame.K_LEFT:
                selected = (selected[0] - 1, selected[1])
            if event.key == pygame.K_RIGHT:
                selected = (selected[0] + 1, selected[1])
            if event.key == pygame.K_DOWN:
                selected = (selected[0], selected[1] + 1)
            if event.key == pygame.K_UP:
                selected = (selected[0], selected[1] - 1)

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            x = x//50
            y = y // 50
            selected = (x, y)
            if selected[0] == 10 or selected[0] == 11:
                if selected[1] == 1:
                    if not solve(board):
                        messagebox.showinfo('Alert', 'No Solution Found')
                elif selected[1] == 3:
                    for i in range(0, 9):
                        for j in range(0, 9):
                            board[i][j] = 0

    drawGrid()
    pygame.display.flip()
    clock.tick(60)
