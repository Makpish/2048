import random
from msvcrt import getch

def print_board(board,moves,score):
    for i in board:
            print("-------------------")
            print(" |",i[0],"|",i[1],"|",i[2],"|",i[3],"|")
    print("-------------------","Moves=",moves,"Score=",score)


def next_number():
    return random.choice([2,2,2,2,4,2,2,2,2,2])


def next_position(board):
    pos=[]
    for i in range(4):
        for j in range(4):
            if board[i][j]==' ':
                pos.append(i*10+j)
    return random.choice(pos),len(pos)

def up(board):
    x=0
    y=0
    for j in range(4):
        i=1
        z=-1
        while i<4:
            if board[i][j]==' ':
                i=i+1
                continue
            if i!=0 and board[i-1][j]==' ':
                board[i-1][j]=board[i][j]
                board[i][j]=' '
                i=i-2
                i=i+1
                x=1
                continue
            if i!=0 and board[i-1][j]!=board[i][j]:
                i=i+1
                continue
            if i!=0 and i>z and board[i-1][j]==board[i][j]:
                board[i-1][j]=board[i][j]*2
                y=y+board[i-1][j]
                board[i][j]=' '
                z=i
                #i=i+1
                i=i+1
                x=1
                continue
            i=i+1
    return x,y


def down(board):
    x=0
    y=0
    for j in range(4):
        i=2
        z=4
        while i>=0:
            if board[i][j]==' ':
                i=i-1
                continue
            if i!=3 and board[i+1][j]==' ':
                board[i+1][j]=board[i][j]
                board[i][j]=' '
                i=i+2
                i=i-1
                x=1
                continue
            if i!=3 and board[i+1][j]!=board[i][j]:
                i=i-1
                continue
            if i!=3 and i<z and board[i+1][j]==board[i][j]:
                board[i+1][j]=board[i][j]*2
                y=y+board[i+1][j]
                board[i][j]=' '
                z=i
                #i=i-1
                i=i-1
                x=1
                continue
            i=i-1
    return x,y

                    
def left(board):
    x=0
    y=0
    for i in range(4):
        j=1
        z=-1
        while j<4:
            if board[i][j]==' ':
                j=j+1
                continue
            if j!=0 and board[i][j-1]==' ':
                board[i][j-1]=board[i][j]
                board[i][j]=' '
                j=j-2
                j=j+1
                x=1
                continue
            if j!=0 and board[i][j-1]!=board[i][j]:
                j=j+1
                continue
            if j!=0 and j>z and board[i][j-1]==board[i][j]:
                board[i][j-1]=board[i][j]*2
                y=y+board[i][j-1]
                board[i][j]=' '
                z=j
                #j=j+1
                j=j+1
                x=1
                continue
            j=j+1
    return x,y


def right(board):
    x=0
    y=0
    for i in range(4):
        j=2
        z=4
        while j>=0:
            if board[i][j]==' ':
                j=j-1
                continue
            if j!=3 and board[i][j+1]==' ':
                board[i][j+1]=board[i][j]
                board[i][j]=' '
                j=j+2
                j=j-1
                x=1
                continue
            if j!=3 and board[i][j+1]!=board[i][j]:
                j=j-1
                continue
            if j!=3 and j<z and board[i][j+1]==board[i][j]:
                board[i][j+1]=board[i][j]*2
                y=y+board[i][j+1]
                board[i][j]=' '
                z=j
                #j=j-1
                j=j-1
                x=1
                continue
            j=j-1
    return x,y


board=[[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' ']]
nxt=next_number()
pos=next_position(board)
board[int(pos[0]/10)][int(pos[0]%10)]=nxt
nxt=next_number()
pos=next_position(board)
board[int(pos[0]/10)][int(pos[0]%10)]=nxt
moves=0
score=0
print_board(board,moves,score)
while True:
    c=ord(getch())
    if c==224:
        continue
    x=0
    y=0
    if c==80:
        x,y=down(board)
    if c==72:
        x,y=up(board)
    if c==75:
        x,y=left(board)
    if c==77:
        x,y=right(board)
    moves=moves+x
    score=score+y
    if x!=0:
        nxt=next_number()
        pos=next_position(board)
        if pos[1]==0:
            break
        board[int(pos[0]/10)][int(pos[0]%10)]=nxt
    print_board(board,moves,score)
    
