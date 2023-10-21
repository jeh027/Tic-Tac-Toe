board = [
    ["-", "-", "-"],
    
    ["-", "-", "-"],
    
    ["-", "-", "-"]
]

user = True   #true refers to x otherwise o
turns = 0

def print_board(board):
    for row in board:
        for slot in row:
            print(slot, end = " ")
        print()
            

# check to see if number
def isnum(user_input):
    if user_input.isnumeric():
        return True  #boolean type
    else:
        print(user_input, "is not a valid response")
        return False


def bounds(user_input):
    output = int(user_input)
    if output < 10 and output > 0:
        return True
    else:
        print(output, "is an invalid input [1 - 10]")
        return False

#p1  NEED TO UNDERSTAND THIS
def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print("This position is already taken")
        return True
    else:
        return False
    

#p2  NEED TO UNDERSTAND THIS
def coordinates(user_input):
    row = int(user_input / 3)
    col = user_input
    if col > 2:
        col = int(col % 3)
    return (row, col)

#allow user to mark x and o
def addToboard(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user

#programs to change from x to o
def current_user(user):
    if user:
        return "x"
    else:
        return "0"


###

# This program check whether or not player has won
def iswin(user, board):
    if check_row(user, board):
        return True
    if check_col(user, board):
        return True
    if check_diag(user, board):
        return True
    return False  # return false if none of these criterions fit the board

#check horizontal rows
def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row:
            return True
    return False
                
#check vertical rows
def check_col(user, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != user:
                complete_col = False
                break
        if complete_col:
            return True
    return False


#check diagonal rows
def check_diag(user, board):
    #top left to bottom right
    if board[0][0] == user and board[1][1] == user and board[2][2] == user:
        return True
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user:
        return True
    else:
        return False


while turns < 9:   # 9 because the first loop is at zero
    active_user = current_user(user) # !!!
    print_board(board)   # call function for board
    user_input = input("Enter a position on the board: ")
    if isnum(user_input) == False:
        print("Try again!")
        continue # re run the loop from the beginning
    if bounds(user_input) == False:
        print("Try again!")
        continue
    user_input = int(user_input) - 1
    coords = coordinates(user_input)
    if istaken(coords, board):
        print("Try again!")
        continue
    addToboard(coords, board, active_user)
    if iswin(active_user, board):
        print(active_user, "won!")
        break
    
    turns += 1
    if turns == 9:
        print("Neither player has won; tie")
        break
 
    user = not user #False
        
        
        
        
        
    











