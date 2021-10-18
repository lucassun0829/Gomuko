import pygame
from gomuko.constants import WIDTH, HEIGHT, ROWS, COLS
from gomuko.board import Board


FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def round_pos(x,y):
        x = 50 * round(x/50)
        y = 50 * round(y/50)
        return(x,y)

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    # 1 = white move, 0 = black move
    turn = "White"
    board.draw_board(WIN)
    board.create_board()
    pygame.display.update()
    
    while(run):
        clock.tick(FPS)
        print(f"Its {turn} turn")

        round_start = True
        while(round_start):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    round_start=False
                    run = False 


                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    position = round_pos(position[0], position[1])
                    if(board.check_pos(position)):
                        print(position) #testing
                        
                        board.place_piece(WIN, position, turn)
                        if(board.check_five(position, turn)):
                            print(f"{turn} Win")
                            run = False

                        round_start=False
                        if(turn=="White"):
                            turn="Black"
                        else:
                            turn="White"
                    
                    else:
                        print("Space already taken, please pick another spot. ")
                        break
        
        pygame.display.update()

    pygame.quit()


main()
