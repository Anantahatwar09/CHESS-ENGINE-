import pygame as p
import os
from chessengine import gamestate

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ = WIDTH // DIMENSION
MAX_FPS = 15
IMAGES = {}

def loadimg():
    pieces = ["wp", "wr", "wn", "wb", "wk", "wq", "bp", "br", "bn", "bb", "bk", "bq"]
    image_directory = "C:/Users/anant/OneDrive/Desktop/AI project/chess/img"  # Use forward slashes
    for piece in pieces:
        image_path = image_directory + "/" + piece + ".png"  # Use forward slashes
        IMAGES[piece] = p.transform.scale(p.image.load(image_path), (SQ, SQ))

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    gs = gamestate()
    loadimg()
    running = True

    while running:  # Main game loop
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        drawgamestate(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

def drawgamestate(screen, gs):
    drawboard(screen)
    drawpieces(screen, gs.board)

def drawboard(screen):
    colors = [p.Color('white'), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2]
            p.draw.rect(screen, color, p.Rect(c * SQ, r * SQ, SQ, SQ))

def drawpieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            peice = board[r][c]
            if peice != "--":
                screen.blit(IMAGES[peice],p.Rect(c * SQ, r * SQ, SQ, SQ))
            

if __name__ == "__main__":
    main()
