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

    def __del__(self):
        print("player deleted")

    def __str__ (self):
        return  f'{self.name} - plyes-{self.icon} (player is a {PLAYER_TYPES[self.type]})'





class GameBord:
    def __init__(self, size, game_sqrs = [], game_map = [], empty_i = [], flat = []):
        self.size = size
        self.game_sqrs = game_sqrs
        self.game_map = game_map
        self.empty_i = empty_i
        self.flat = flat
        for i in range(size):
            self.flat += ['_' for x in range(size)]
        for row in range(size * 2 + 2):
            self.game_sqrs.append(['_' for x in range(size)])    
        for row in range(size):    
            for col in range(size):    
                self.empty_i.append([row,col])
        # create map of rwos , col's and diagonals     
        for row in range(size):
            self.game_map.append([y + row * size for y in range(size)])
        for row in range(size):
            self.game_map.append([y for y in range(row,size*size,size)])
        self.game_map.append([y for y in range(0,size*size,size+1)])
        self.game_map.append([y for y in range(size-1,size*size -1,size-1)])

    def __del__(self):
        print("game bord deleted")

    def reset(self):
        self.flat.clear()
        self.game_map.clear()
        self.game_sqrs.clear()
        self.empty_i.clear()
        for i in range(self.size):
            self.flat += ['_' for x in range(self.size)]
        for row in range(self.size * 2 + 2):
            self.game_sqrs.append(['_' for x in range(self.size)])    
        for row in range(self.size):    
            for col in range(self.size):    
                self.empty_i.append([row,col])
        # create map of rwos , col's and diagonals     
        for row in range(self.size):
            self.game_map.append([y + row * self.size for y in range(self.size)])
        for row in range(self.size):
            self.game_map.append([y for y in range(row,self.size*self.size,self.size)])
        self.game_map.append([y for y in range(0,self.size*self.size,self.size+1)])
        self.game_map.append([y for y in range(self.size-1,self.size*self.size -1,self.size-1)])


    def play_move(self, cur_plyr, row, col):
        move_success = False
        self.flat.clear()
        for i in range(self.size):
            self.flat += [x for x in self.game_sqrs[i]]
        if  0 <= row < self.size and  0 <= col < self.size and cur_plyr in PLAYER_ICON and [row,col] in self.empty_i:
            move_success = True
            self.flat[row * self.size + col] = cur_plyr
            self.empty_i.remove([row,col])
            map_i = self.size * 2 + 2
            for r1 in range(map_i):
                for c1 in range(self.size):
                    self.game_sqrs[r1][c1] = self.flat[self.game_map[r1][c1]]                    
        return move_success

    def check_bord(self, cur_plyr):
        for vic in self.game_sqrs:
            if vic.count(cur_plyr) >= self.size:
                return cur_plyr
        return None


    def find_win_bloc_move(self,cur_plyr):
        oppnt = PLAYER_ICON[0] if cur_plyr == PLAYER_ICON[1] else PLAYER_ICON[0]
        for i , g1 in  enumerate(self.game_sqrs) :
            if g1.count(cur_plyr) == (self.size - 1) and g1.count(FREE_SPC) == 1:
                return i , g1.index(FREE_SPC)
        for i , g1 in  enumerate(self.game_sqrs) :
            if g1.count(oppnt) == (self.size - 1) and g1.count(FREE_SPC) == 1:
                return i , g1.index(FREE_SPC)
        return None, None

# display Board genaral        
    
def disp_board(bord:GameBord):
    for row in range(bord.size):
        print(f' |  {"  |  ".join([sq for sq in bord.game_sqrs[row]])}  |')  
        print(f'\n')


