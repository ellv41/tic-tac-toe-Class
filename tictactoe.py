import random
from Classes import *


def computer_play(plyer,empty_i):
    pos = -1
    #crate a list postions of all empty squers 
    r1,c1 = board.find_win_bloc_move(plyer)
    if pos == -1: pos = random.choice(empty_i)
    return pos


def play_move(c_plyer, bord):
    legal = False
    index = -1
    s_size = [str(x+1) for x in range(bord.size+1)] 
    if opponent == COMPUTER:
        row, col = computer_play(plyer,bord.empty)
    else:
        while not legal:
            row = input(f'select row number  1-{bord.size} : ')
            col = input(f'select col number  1-{bord.size} : ')
            if row.isnumeric() and col.isnumeric() and row in s_size and col in s_size:
                row = int(row) - 1 
                col = int(col) - 1
                if bord.play_move(player.icon,row,col):
                    legal = True
                else:
                    print(f'select an empty place')
            else:
                if row in ('X', 'x') or col in ('X', 'x'):
                    return -1
                print(f'enter only numbers 1-{bord.size}')
                legal = False


########### main ######

player1 = Player("compi",'C', 'X')
player2 = Player("eli", 'H', 'O')
game1 = GameBord(3)

print(player1)
game1.play_move(player1.icon,1,1)

print('\n\n\n\n')
del game1
game2 = GameBord(4)
print(game2)


# player = PLAYER1
# opponent1 = input("for first opponent computer press C : ").upper()
# opponent2 = input("for first opponent computer press C : ").upper()

# # Games loop
# while True:
#     player = random.choice([PLAYER1,PLAYER2])
#     # player = PLAYER1
#     game_over = False
#     # start the game first move is  played by X (C)
#     reset_board()
#     game_status = 0
#     player_opens = player 
#     if player == PLAYER1: x_opens += 1
# # Single Game Loop        
#     while not game_over:
#         if display_lvl == 3:
#             print_bord()
#             print(f'player {player} your turn')
#         if GAME_BOARD.count(FREE_SPC) > 0:
#             if player == PLAYER1:
#                 game_status = play_move(player, opponent1)
#                 player = PLAYER2
#             else:
#                 game_status = play_move(player, opponent2)
#                 player = PLAYER1
#             if game_status in (PLAYER1, PLAYER2):
#                 if game_status == PLAYER1:
#                     win_x += 1
#                 else:
#                     win_O += 1    
#                 if display_lvl == 3:    
#                     print_bord()
#                     print(f'\n ****** And the Winner is ********* player-{game_status}')
#                 game_over = True
#         else:
#             if display_lvl == 3:
#                 print_bord()
#                 print(f'no more moves the board is full @@@@@@@ its a tie @@@@@@@@')                    
#             no_winer += 1
#             game_over = True
#         if game_status == -1:    
#             game_over = True
#     grade_moves(game_status)
#     GAME_DATA.clear()
#     game += 1
#     if not computer_playes:
#         if input('want another game press Y : ').upper() != 'Y':
#             break
#     else:
#         if display_lvl > 1:
#             print_bord()
#             print(f'\n Game Winer = {game_status} - player_opens = {player_opens}')
#             print('\n***********************************************************')
#             print(f'       END GMAE    Game :{game} of {num_games}')
#             print('***********************************************************')
#     if game >= num_games and computer_playes:
#         break
# print(f'\n**************** Games Sumery **************** \n\n Games Plyed = {num_games}\n')    
# print(f'X wins  =  {win_x} - x opens = {x_opens} times \nO wins  =  {win_O}\nno_winer = {no_winer}\n')  
# if computer_playes:
#     input('to close the program press Enter : X')

    
# # end Main
