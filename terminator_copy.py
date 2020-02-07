from random import * 
# Init your variables here 
corners = [[0,0],[0,6],[6,0],[6,6]]
arround_center = [[2,3],[3,2],[3,4],[4,3]]
SIZE = 7
MIDDLE = 3
WIN = 5
# Put your bot name here
name = "Terminator_copy" 
# Player 'O' is max, in this case AI
def check_if_win_opponent(board, position, idplayer): 
    
    board[MIDDLE][MIDDLE] = idplayer  # Middle cell takes the color of the current player  
    board[position[0]][position[1]] = idplayer   
    directions = [([0, 1], [0, -1]), ([1, 0], [-1, 0]), ([-1, 1], [1, -1]), ([1, 1], [-1, -1])]
    for direction in directions:
            counter = 0
            for i in range(2):
                p = position[:]
                while 0 <= p[0] < SIZE and 0 <= p[1] < SIZE:
                    if board[p[0]][p[1]] == idplayer:
                        counter += 1
                    else:
                        break
                    p[0] += direction[i][0]
                    p[1] += direction[i][1]
            if counter >= WIN+1:
                board[position[0]][position[1]] = 0
                board[MIDDLE][MIDDLE] = 0
                return True
    board[position[0]][position[1]] = 0
    board[MIDDLE][MIDDLE] = 0
    return False
def check_if_win_player(board, position, idplayer): 
    
    board[MIDDLE][MIDDLE] = idplayer  # Middle cell takes the color of the current player  
    board[position[0]][position[1]] = idplayer   
    directions = [([0, 1], [0, -1]), ([1, 0], [-1, 0]), ([-1, 1], [1, -1]), ([1, 1], [-1, -1])]
    for direction in directions:
            counter = 0
            for i in range(2):
                p = position[:]
                while 0 <= p[0] < SIZE and 0 <= p[1] < SIZE:
                    if board[p[0]][p[1]] == idplayer:
                        counter += 1
                    else:
                        break
                    p[0] += direction[i][0]
                    p[1] += direction[i][1]
            if counter >= 4:
                board[position[0]][position[1]] = 0
                board[MIDDLE][MIDDLE] = 0
                return True
    board[position[0]][position[1]] = 0
    board[MIDDLE][MIDDLE] = 0
    return False

def choose_a_corner(available_cells):
    cornerstab =[]
    for a in corners:
        if a in available_cells:
            cornerstab.append(a)
    if len(cornerstab) != 0:
        return cornerstab[randint(0,len(cornerstab)-1)]
    else:
        pass
    
def choose_arround_center(available_cells):
    arroudtab = []
    for a in arround_center:
        if a in available_cells:
            arroudtab.append(a)
    if len(arroudtab) !=0 :
        return arroudtab[randint(0,len(arroudtab)-1)]
    else:
        return


def play(board, available_cells, player):
    playertab = []
    move = choose_a_corner(available_cells)
    arroud = choose_arround_center(available_cells)
    if player == 1:
        opponent = 2
    else: 
        opponent = 1
    for a in available_cells:
        if check_if_win_opponent(board,[a[0],a[1]],opponent) :
          return a
        elif check_if_win_opponent(board,[a[0],a[1]],player):
            return a
        elif check_if_win_player(board,[a[0],a[1]],player):
            playertab.append(a)

  
    if arroud != None:
        return arroud
    elif len(playertab) != 0:
        return playertab[randint(0,len(playertab)-1)]
    elif move != None:
        return move
    else:
        return available_cells[randint(0,len(available_cells)-1)]