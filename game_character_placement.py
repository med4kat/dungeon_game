#!/usr/bin/env python
# coding: utf-8

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

# Add a player
player_symbol = Fore.RED + '@' + Style.RESET_ALL

# Calculate the center of the first room manually
first_room = rooms[0]

player_x = first_room['x'] + first_room['width'] // 2
player_y = first_room['y'] + first_room['height'] // 2

# Add the goal
number_of_rooms = len(rooms)
last_room = rooms[number_of_rooms - 1];
goal_symbol = Fore.GREEN + '@' + Style.RESET_ALL

goal_x = last_room['x'] + last_room['width'] - 1
goal_y = last_room['y'] + last_room['height'] - 1

print(goal_x, goal_y)


def display_grid():
    """Function to display the grid with the player"""
    
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen when not in jupyter
    
    for y, row in enumerate(grid):
        line = ''
        for x, cell in enumerate(row):
            if x == player_x and y == player_y:
                line += player_symbol
            elif x == goal_x and y == goal_y:
                line += goal_symbol
            else:
                line += cell_symbols.get(cell, ' ')
        print(line)

def can_move(x, y):
    """Function to check if the player can move to the next position"""
    return grid[y][x] in ['.', '#', '+']  # Player can walk on rooms, corridors, and doors

# Main game loop
while True:
    display_grid() # 1. GRAPHICS
    move = input("Move (WASD): ").lower() # 2. INPUT

    new_x, new_y = player_x, player_y # 3. MOVEMENT

    if move == 'w' and can_move(player_x, player_y - 1):
        new_y -= 1
    elif move == 's' and can_move(player_x, player_y + 1):
        new_y += 1
    elif move == 'a' and can_move(player_x - 1, player_y):
        new_x -= 1
    elif move == 'd' and can_move(player_x + 1, player_y):
        new_x += 1

    if can_move(new_x, new_y): # GAME LOGIC
        player_x, player_y = new_x, new_y






