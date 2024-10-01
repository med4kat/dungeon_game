#!/usr/bin/env python
# coding: utf-8

# In[1]:


from RDGen import generate_rooms, connect_rooms
from colorama import init, Fore, Style
import os


# Initialize colorama
init()

# Define parameters
num_rooms = 10
min_width = 4
max_width = 8
min_height = 4
max_height = 8
grid_width = 50
grid_height = 25
door_chance = 0.3

# Generate the dungeon
grid, rooms = generate_rooms(
    num_rooms=num_rooms,
    min_width=min_width,
    max_width=max_width,
    min_height=min_height,
    max_height=max_height,
    grid_width=grid_width,
    grid_height=grid_height
)

# Connect the rooms
connect_rooms(
    grid=grid,
    rooms=rooms,
    door_chance=door_chance
)

# Define cell representations with colors
cell_symbols = {
    'W': Fore.GREEN + '#' + Style.RESET_ALL,     # Walls
    '.': Fore.WHITE + '.' + Style.RESET_ALL,     # Rooms
    '#': Fore.CYAN + '.' + Style.RESET_ALL,      # Corridors
    '+': Fore.YELLOW + '+' + Style.RESET_ALL,    # Doors
}


# In[2]:


# Add a player
player_symbol = Fore.RED + '@' + Style.RESET_ALL

# Calculate the center of the first room manually
first_room = rooms[0]
player_x = first_room['x'] + first_room['width'] // 2
player_y = first_room['y'] + first_room['height'] // 2


# Function to display the grid with the player
def display_grid():
    
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen when not in jupyter
    
    for y, row in enumerate(grid):
        line = ''
        for x, cell in enumerate(row):
            if x == player_x and y == player_y:
                line += player_symbol
            else:
                line += cell_symbols.get(cell, ' ')
        print(line)


# Function to check if the player can move to the next position
def can_move(x, y):
    return grid[y][x] in ['.', '#', '+']  # Player can walk on rooms, corridors, and doors

# Main game loop
while True:
    display_grid()
    move = input("Move (WASD): ").lower()

    new_x, new_y = player_x, player_y

    if move == 'w' and can_move(player_x, player_y - 1):
        new_y -= 1
    elif move == 's' and can_move(player_x, player_y + 1):
        new_y += 1
    elif move == 'a' and can_move(player_x - 1, player_y):
        new_x -= 1
    elif move == 'd' and can_move(player_x + 1, player_y):
        new_x += 1

    if can_move(new_x, new_y):
        player_x, player_y = new_x, new_y






