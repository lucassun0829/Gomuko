import pygame
from .constants import BROWN, ROWS, COLS, WIDTH, HEIGHT

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
    
    def draw_board(self, win):
        win.fill(BROWN) 
        x_position = 0
        y_position = 0
        space_interval = HEIGHT//ROWS
        while(y_position<HEIGHT):
            pygame.draw.line(win, (0,0,0), 
                        (x_position,y_position), (x_position+800,y_position), 2)
            y_position+=space_interval

        y_position = 0
        while(x_position<WIDTH):
            pygame.draw.line(win, (0,0,0), 
                        (x_position,y_position), (x_position,y_position+800), 2)
            x_position+=space_interval
    
    def create_board(self):
        for x in range(ROWS):
            rows=[]
            for y in range(COLS+1):
                rows.append('x')
            self.board.append(rows)
    
    def update_board(self, position, color):
        x = position[0]//50
        y = position[1]//50
        if(color=="White"):
            self.board[y][x] = "1"
        else:
            self.board[y][x] = "0"

        pass
    def place_piece(self, win, position, color):
        self.update_board(position, color)
        if(color=="White"):
            color = (255, 255, 255)
        else:
            color = (0, 0, 0)
        pygame.draw.circle(win, color, position, 15)
    
    def representation(self):
        string=""
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                string+=self.board[x][y]
            string+="\n"
        return(string)


    def check_pos(self, position):
        x = position[0]//50
        y = position[1]//50
        return(self.board[y][x] == "x")
    
    def check_five(self, position, color):
        x = position[0]//50
        y = position[1]//50
        if(color=="White"):
            rep = "1"
        else:
            rep = "0"
        
        return(self.check_straight(x, y, rep) or self.check_up_down(x, y, rep)
                or self.check_rdiagonal(x, y, rep) or self.check_ldiagonal(x, y, rep))
    def check_straight(self, x, y, rep): 
        z = x                                                       
        left = False
        right = False
        count=1

        while(not left):
            if(self.board[y][x-1] == rep):
                count+=1
                x-=1
            else:
                left = True

        while(not right):
            if(self.board[y][z+1] == rep):
                count+=1
                z+=1
            else:
                right = True
        
        return(count>=5)
    
    def check_up_down(self, x, y, rep):
        z = y                                                       
        up = False
        down = False
        count=1

        while(not down):
            if(self.board[y+1][x] == rep):
                count+=1
                y+=1
            else:
                down = True

        while(not up):
            if(self.board[z-1][x] == rep):
                count+=1
                z-=1
            else:
                up = True
        
        return(count>=5)
    
    def check_rdiagonal(self, x, y, rep):
        w=x
        z=y
        up = False
        down = False
        count=1
        while(not down):
            if(self.board[y+1][x+1] == rep):
                count+=1
                y+=1
                x+=1
            else:
                down = True

        while(not up):
            if(self.board[z-1][w-1] == rep):
                count+=1
                z-=1
                w-=1
            else:
                up = True
        
        return(count>=5)
    
    def check_ldiagonal(self, x, y, rep):
        w=x
        z=y
        up = False
        down = False
        count=1
        while(not down):
            if(self.board[y-1][x+1] == rep):
                count+=1
                y-=1
                x+=1
            else:
                down = True

        while(not up):
            if(self.board[z+1][w-1] == rep):
                count+=1
                z+=1
                w-=1
            else:
                up = True
        return(count>=5)