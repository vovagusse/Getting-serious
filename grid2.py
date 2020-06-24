GAME = True #game status iteriable
f = [] #field or grid
player_pos = [0, 0]
DEFAULT_PLAYER = 'O'
DEFAULT_EMPTY_GRID_ELEMENT = '-'

def main():
    num = get_value()
    make_a_grid(num, f)
    make_player(f)
    while GAME == True:
        render_field(f, num)
        move_value = move_input()
        move_on_f(f, move_value)

def make_player(f):
    f[player_pos[0]][player_pos[1]] = DEFAULT_PLAYER

def render_field(f, num):
    for x in f:
        tmp = ''
        for y in x:
            if y == DEFAULT_PLAYER:
                tmp += DEFAULT_PLAYER
            else:
                tmp += DEFAULT_EMPTY_GRID_ELEMENT
        print(tmp)
        tmp = ''
    
    

def move_input():
    return str.lower(input('Where to move?(type "HELP" to see commands list, "END" to end the program) Type here: '))

def move_on_f(f, move_value):
    if move_value == 'end':
        GAME = False
    elif move_value == 'right':
        player_pos[0] += 1
        x = player_pos[1]
        y = player_pos[0]
        f[x][y] = DEFAULT_PLAYER
        f[x][y - 1] = DEFAULT_EMPTY_GRID_ELEMENT

    elif move_value == 'up':
        pass
    elif move_value == 'down':
        player_pos[1] += 1
        x = player_pos[1]
        y = player_pos[0]
        f[x][y] = DEFAULT_PLAYER
        f[x - 1][y] = DEFAULT_EMPTY_GRID_ELEMENT

    elif move_value == 'help':
        print('------------------------------------------------------')
        print(''' Help - commands you can use in the program are: \n    Movement: "up", "down", "left", "right";  \n    Misc: "end", "help"  ''')
        print('------------------------------------------------------')
    elif move_value == 'left':
        pass
    else:
        print('------------------------------------------------------')
        print('error, type help to see commands list')
        print('------------------------------------------------------')

def make_a_grid(num, f):
    for x in range(num):
        f.append([])
        for y in range(num):
            # print(f'x currently equals {x}, y currently is {y}')
            # print(f'range(num) = {range(num)}')
            f[x].append('-')
            # print(f)
    

def get_value():
    num = int(input('Grid side length: '))
    return num

main()
