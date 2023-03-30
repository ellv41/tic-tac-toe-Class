PLAYER_TYPES = {"C":"Computer", "H":"Human"}
PLAYER_ICON = ['X','O']
FREE_SPC = '_'



class Player:
    def __init__(self, name, type, icon, win_count = 0, game_open = 0):
        self.type = type
        self.name = name
        self.icon = icon
        self.win_count = win_count
        self.game_open = game_open

    def __str__ (self):
        return  f'{self.name} - plyes-{self.icon} (player is a {PLAYER_TYPES[self.type]})'




class GameBord:
    def __init__(self, size, game_sqrs = [], game_map = [], empty_i = []):
        self.size = size
        self.game_sqrs = game_sqrs
        self.game_map = game_map
        self.empty_i = empty_i
        for row in range(size):
            self.game_sqrs.append(['_' for x in range(size)])    
        # create map of rwos , col's and diagonals     
        for row in range(size):
            self.game_map.append([y + row * size for y in range(size)])
        for row in range(size):
            self.game_map.append([y for y in range(row,size*size,size)])
        self.game_map.append([y for y in range(0,size*size,size+1)])
        self.game_map.append([y for y in range(size-1,size*size -1,size-1)])



    # def disp_board(self):
    def __str__(self):
        print(f'\nGame Board Tic Tac Toe\n')
        for row in range(self.size):
            print(f' |  {"  |  ".join([sq for sq in self.game_sqrs[row]])}  |')  
            print(f'\n')


    def play_move(self, cur_plyr, row = 0, col = 0):
        if  0 <= row < self.size and  0 <= col < self.size and cur_plyr in PLAYER_ICON:
            if self.game_sqrs[row][col] == '_': self.game_sqrs[row][col] = cur_plyr
            self.empty_i.clear()
            for r1 in self.game_map:
                for sq_idx in r1:
                    row1 = sq_idx // self.size 
                    col1 = sq_idx % self.size 
                    if row1 == row and col == col1: self.game_sqrs[row1][col1] = cur_plyr
                    if self.game_sqrs[row1][col1] == FREE_SPC : self.empty_i.append([row1,col1])
        return None

    def check_bord(self, cur_plyr):
        for vic in self.game_sqrs:
            if vic.count(cur_plyr) >= self.size:
                return cur_plyr
        return None


    def find_win_bloc_move(self,cur_plyr):
        for i , g1 in  enumerate(self.game_sqrs) :
            if g1.count(cur_plyr) == self.size - 1 and g1.count(FREE_SPC) == 1:
                return i , g1.index(FREE_SPC)
        return None, None
    