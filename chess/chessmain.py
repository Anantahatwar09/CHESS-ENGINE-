import pygame as p
import os
from chessengine import gamestate, move

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ = WIDTH // DIMENSION
MAX_FPS = 15
IMAGES = {}


def load_images():
    pieces = ["wp", "wr", "wn", "wb", "wk", "wq", "bp", "br", "bn", "bb", "bk", "bq"]
    image_directory = "C:/Users/anant/OneDrive/Desktop/AI project/chess/img"
    for piece in pieces:
        image_path = os.path.join(image_directory, piece + ".png")
        IMAGES[piece] = p.transform.scale(p.image.load(image_path), (SQ, SQ))


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    gs = gamestate()
    validmoves = gs.getvalidmoves()
    movemade = False #flag variable for when a move is made 
    load_images()
    running = True
    sqselected = ()
    player_click = []

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0] // SQ
                row = location[1] // SQ

                if sqselected == (row, col):
                    sqselected = ()
                    player_click = []
                else:
                    sqselected = (row, col)
                    player_click.append(sqselected)
                if len(player_click) == 2:
                    chess_move = move(player_click[0], player_click[1], gs.board)
                    print(chess_move.chessnotation())
                    if  chess_move in validmoves:
                        gs.makemove(chess_move)  
                    sqselected = ()
                    player_click = []
            
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undomoves()
                    
                    

        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


def draw_game_state(screen, gs):
    draw_board(screen)
    draw_pieces(screen, gs.board)


def draw_board(screen):
    colors = [p.Color('white'), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2]
            p.draw.rect(screen, color, p.Rect(c * SQ, r * SQ, SQ, SQ))


def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c * SQ, r * SQ, SQ, SQ))


if __name__ == "__main__":
    main()
