import random

import os

CELLS = [ 
    (0,1),(1,0),(2,0),(3,0),(4,0),(5,0),
    (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),
    (0,2),(1,2),(2,2),(3,2),(4,2),(5,2),
    (0,3),(1,3),(2,3),(3,3),(4,3),(5,3),
    (0,4),(1,4),(2,4),(3,4),(4,4),(5,4),
    (0,5),(1,5),(2,5),(3,5),(4,5),(5,5)
]  
        
def clear_screen():

    os.system('cls' if os.name == 'nt' else 'clear')
    

def get_locations():
        
    return random.sample(CELLS, 3)

def move_player(player, move):
    
    x, y = player
    
    if move == 'LEFT':
        x-=1
    if move == 'RIGHT':
        x+=1
    if move == 'UP':
        y-=1
    if move == 'DOWN':
        y+=1    
        
    return x, y
    
    # get player location
    # if move == LEFT, x - 1
    # if move == RIGHT, x + 1
    # if move == UP, y - 1
    # if move == DOWN, y + 1

def get_moves(player):
    
    moves = ['LEFT','RIGHT','UP','DOWN']
    
    x, y = player
    
    if x==0:
        
        moves.remove('LEFT')
        
    if x==5:
        
        moves.remove('RIGHT')
        
    if y==0:
        
        moves.remove('UP')
        
    if y==5:
        moves.remove('DOWN')    
               
    return moves

def draw_map(player):
    
    print(' _'*5)
    
    tile = "|{}"
    
    for cell in CELLS:
        x, y = cell
        
        if x<5:
            line_end = ""
            
            if cell == player:
                
                output = tile.format('X')
            
            else:
                
                output = tile.format('_')    

        else:
            
            line_end = "\n"
            
            if cell == player:
                
                output = tile.format('X|')  
                
            else:
                
                output = tile.format('_|')    
    
    
        print(output,end=line_end)
        
def gameloop():
    
    monster, player, door = get_locations()
    
    playing = True
    
    while playing:
        
        clear_screen()

        draw_map(player)
        
        valid_moves = get_moves(player)
        
        print('You are currently in room {}'.format(player))
        
        print('You can move {}'.format(", ".join(valid_moves)))
        
        print('Enter QUIT to quit')
    
        move = input('> ')
       
        move = move.upper()
       
        if move == 'QUIT':
            
            print('\n ** See you in the next Game **\n')
           
        
            break
    
        if move in valid_moves:
        
            player = move_player(player, move)
            
            if player == monster:
                
                print('\n** Oh no! The Monster got you, Better luck next time! **\n')
                
                playing = False   
            
            if player == door:
                
                print('\n** You escaped! Congratulations! **\n')
                
                playing = False 
                
        
        else:
        
            input('\n ** Walls are hard! Dont run into them! **\n')
        
    else:
        
        if input('Play Again? [Y/n]').lower() != 'n':
            
            gameloop()
            

clear_screen()

print('Welcome to Dungeon Game!')

input('Press return to start!')

clear_screen()

gameloop()

        
        
    
    
    
    
    



















# draw grid   
# pick random location for player
# pick random location for exit door
# pick random location for the monster
# draw player in the grid
# take input for movement
# move player, unless invalid move(past edges of grid)
# check for win/loss
# clear screen and redraw grid








        # (0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10),
        # (1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),
        # (2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(2,10),
        # (3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(3,9),(3,10),
        # (4,0),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8),(4,9),(4,10),
        # (5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10),
        # (6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(6,8),(6,9),(6,10),
        # (7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),(7,8),(7,9),(7,10),
        # (8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8),(8,9),(8,10),
        # (9,0),(9,1),(9,2),(9,3),(9,4),(9,5),(9,6),(9,7),(9,8),(9,9),(9,10),
        # (10,0),(10,1),(10,2),(10,3),(10,4),(10,5),(10,6),(10,7),(10,8),(10,9),(10,10)
        