"""
A recursive loop search of tic tac toe game permutations in a few lines of Python code
"""
permutations=[]
def decide_game_outcome(game:list):
    "Either log an ended game or make the next move"
    if get_result(game)=='In Progress':
        for next_move in get_all_moves_left(game):
            new_game=list(game)
            new_game[next_move]=get_next_player(game)
            decide_game_outcome(new_game)
    else:
        permutations.append(game)
def get_result(game:list) -> str:
    "Someone won, it is a draw or still in progress"
    for check_win in ((0,1,2),(0,3,6),(0,4,8),(1,4,7),(2,4,6),(2,5,8),(3,4,5),(6,7,8)):
        if (len(game) >= max(check_win) and
            game[check_win[0]]==game[check_win[1]]==game[check_win[2]]):
            return str(game[check_win[1]]) + ' wins'
    if len(get_all_moves_left(game))==0:
        return 'draw'
    return 'In Progress'
def get_all_moves_left(game:list) -> list:
    "make a list of possible next moves on an in progress game"
    next_moves=[]
    for move in game:
        if str(move)!='O' and str(move)!='X':
            next_moves.append(move)
    return next_moves
def get_next_player(game:list) -> str :
    "noughts ‘O’ plays first then crosses ‘X’ and so on..."
    if game.count('X')<game.count('O'):
        return 'X'
    return 'O'
if __name__=='__main__':
    first_game=[0,1,2,3,4,5,6,7,8]
    decide_game_outcome(first_game)
    who_won=tuple(get_result(game) for game in permutations)
    print('total games:',len(who_won))
    print('first player wins:',who_won.count('O wins'))
    print('second player wins:',who_won.count('X wins'))
    print('draw:',who_won.count('draw'))
    
