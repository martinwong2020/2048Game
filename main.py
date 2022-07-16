import random
import copy
#starting function that creates the board. main function that prints the board
def start_game():
    board=[
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
    start_state=True
    progress_board=generate_board(board,start_state)
    print("Movement Keys: ")
    print("Up: W or w")
    print("Down: S or s")
    print("Right: D or d")
    print("Left: A or a")
    print_board(board)

    Win=False
    Lost=False
    while Win==False and Lost==False:
        progress_board=game(progress_board)
        print_board(progress_board)
        
        result=win_or_lose(Win,Lost,progress_board)
        if(result[0]==True):
            Win=result[0]
            print("Winner")
        elif(result[1]==True):
            Lost=result[1]
            print("Sorry you lost. Try Again?")

#checks the user's move and merge/collapse based on input. Returns the new board where the values have shifted based on user's input.
def game(board):
    user_input=input("Player move: ").lower()
    if(user_input=="w"):
        new_board=collapse(board,"w")
        result=merge(new_board,"w")
        new_board=result[0]
    elif(user_input=="s"):
        new_board=collapse(board,"s")
        result=merge(new_board,"s")
        new_board=result[0]
    elif(user_input=="d"):
        new_board=collapse(board,"d")
        result=merge(new_board,"d")
        new_board=result[0]
    elif(user_input=="a"):
        new_board=collapse(board,"a")
        result=merge(new_board,"a")
        new_board=result[0]
    new_board=generate_board(new_board,False)
    return new_board

#Generates a board that puts a new value into a random location of the incoming board
def generate_board(board,start_state):
    if(start_state==True):
        limit=2
    elif(start_state==False):
        limit=1
    i=0
    if not any(0 in i for i in board):
        if(can_move(board)==True):
            print("Try another move.")
            return board
    else:
        while i<limit:
            row=random.randint(0,3)
            column=random.randint(0,3)
            if(board[row][column]==0):
                board[row][column]=2
                i+=1
    return board

#merges the value in the board if they are next to each other and of same value. Then also passes out a second argument that states that a merge has occurred.
def merge(board,move):
    merged=False
    if(move=="w"):
        for col in range(0,4):
            for row in range(0,3):
                if(board[row][col]==board[row+1][col] and board[row][col]!=0):
                    board[row][col]=board[row][col]*2
                    board[row+1][col]=0
                    merged=True
    elif(move=="s"):
        for col in range(0,4):
            for row in range(3,0,-1):
                if(board[row][col]==board[row-1][col] and board[row][col]!=0):
                    board[row][col]=board[row][col]*2
                    board[row-1][col]=0
                    merged=True
    elif(move=="d"):
        for row in range(0,4):
            for col in range(3,0,-1):
                if(board[row][col]==board[row][col-1] and board[row][col]!=0):
                    board[row][col]=board[row][col]*2
                    board[row][col-1]=0
                    merged=True
    elif(move=="a"):
        for row in range(0,4):
            for col in range(0,3):
                if(board[row][col]==board[row][col+1] and board[row][col]!=0):
                    board[row][col]=board[row][col]*2
                    board[row][col+1]=0
                    merged=True
    return collapse(board,move),merged

#collapses the board to remove the 0's in between the numbers based on the user's move   
def collapse(board,move):
    new_board=copy.deepcopy(board)
    if(move=="w"):
        for col in range(0,4):
            count=0
            for row in range(0,4):
                if(board[row][col]!=0):
                    new_board[count][col]=board[row][col]
                    count+=1
            for i in range(count,4):
                new_board[i][col]=0 
    elif(move=="s"): 
        for col in range(0,4):
            count=3
            for row in range(3,-1,-1):
                if(board[row][col]!=0):
                    new_board[count][col]=board[row][col]
                    count-=1
            for i in range(count,-1,-1):
                new_board[i][col]=0 
    elif(move=="d"):
        for row in range(0,4):
            count=3
            for col in range(3,-1,-1):
                if(board[row][col]!=0):
                    new_board[row][count]=board[row][col]
                    count-=1
            for i in range(count,-1,-1):
                new_board[row][i]=0
    elif(move=="a"):
        for row in range(0,4):
            count=0
            for col in range(0,4):
                if(board[row][col]!=0):
                    new_board[row][count]=board[row][col]
                    count+=1
            for i in range(count,4):
                new_board[row][i]=0
    return new_board

#checks if the user has won or lost the game and returns state of the win and lose variable
def win_or_lose(win,lose,board):
    if any(2048 in i for i in board):
        win=True
    if not any(0 in i for i in board):
        if(can_move(board)==False):
            lose=True
    return win, lose

#determines if the user can still move even when the board is filled.
def can_move(board):
    check_board=copy.deepcopy(board)
    moves=["w","a","s","d"]
    for i in range(0,4):
        result=merge(check_board,moves[i])
        if(result[1]==True):
            return True
    return False

#prints the game board in a readable way
def print_board(board):
    for i in range(0,4):
        print(board[i])


#calls the start function name
start_game()