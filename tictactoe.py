import random
from Classes import *

########## main ######

print(f'\nGame Tic Tac Toe\n')

# opponent = input("for playing against  computer press C : ").upper()
# if opponent == 'C':
#     player1 = Player("compi",'C', 'O')
#     print(player1)
# else:
#     name = input("player 1 enter your Name : ")
#     player1 = Player(name,'H', 'X')
#     print(player1)
# name = input("player 2 enter your Name : ")
# player2 = Player(name,'H', 'O')
# print(player2)

player1 = Player("compi",'C', 'O')
player2 = Player("ELI",'H', 'X')

bord_size = input("select bord size  3  or 4  or 5 if you dare : ")
bord_size = int(bord_size) if bord_size.isnumeric()  else 3

# Games loop
while True:
    player = random.choice(PLAYER_ICON)
    player = player1 if player == player1.icon else player2
    game_over = False
    game1 = GameBord(bord_size)
    s_size = [str(x + 1) for x in range(game1.size + 1)]
    game_status = 0
# Single Game Loop
    while not game_over:
        disp_board(game1)
        # print(game1.game_map)
        # print(game1.game_sqrs)
        print(game1.empty_i)
        if len(game1.empty_i) > 0:
            if player.type == 'C':
                r1, c1 = game1.find_win_bloc_move(player.icon)
                if r1 == None:
                    pos = random.choice(game1.empty_i)
                    r1 = pos[0]  
                    c1 = pos[1]
                game1.play_move(player.icon, r1, c1)
            else:
                print(f'player {player.name} your turn')
                legal = False
                index = -1
                while not legal:
                    row = input(f'select row number  1-{game1.size} : ')
                    col = input(f'select col number  1-{game1.size} : ')
                    if row.isnumeric() and col.isnumeric() and row in s_size and col in s_size:
                        row = int(row) - 1
                        col = int(col) - 1
                        if game1.play_move(player.icon, row, col):
                            legal = True
                        else:
                            print(f'select an empty place')
                    else:
                        print(f'enter only numbers 1-{game1.size}')
                        legal = False
            game_status = game1.check_bord(player.icon)
            player = player1 if player == player2 else player2
            if game_status in (PLAYER_ICON):
                disp_board(game1)
                print(f'\n ****** And the Winner is ********* player-{game_status}')
                game_over = True
        else:
            disp_board(game1)
            print(f'no more moves the board is full @@@@@@@ its a tie @@@@@@@@')
            game_over = True
    if input('want another game press Y : ').upper() != 'Y':
        break
    else:
        game1.reset()
        
        
  
# end Main
