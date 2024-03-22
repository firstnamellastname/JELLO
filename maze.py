import random, sys, time, pygame
from pygame.locals import *
from random import *

def hcf(a, b):
    while b:
        a, b = b, a%b
    return a

Tile_Multipler = 1
pygame.init()
window_resolution = 800, 600
window = pygame.display.set_mode((window_resolution[0], window_resolution[1]))
score = 0
stag_line_width = 5
line_width = stag_line_width
tile_width_height = hcf(window_resolution[0], window_resolution[1]) // 4 // Tile_Multipler
touched = []
wall_drawn = False
player_pos_x = 0
player_pos_y = 0
border = window_resolution[0]//100 *2 * Tile_Multipler -1, window_resolution[1]//100 *2 * Tile_Multipler -1
goal_pos_x = randint(0, border[0])
goal_pos_y = randint(0, border[1])
player_pos = player_pos_x, player_pos_y
keys = pygame.key.get_pressed()
tile_amount = window_resolution[0] // tile_width_height * (window_resolution[1] // tile_width_height)

def set_borders(cords, direction):
    if direction == "right":
        if cords[0] >= border[0]:
            return True
        else:
            return False

    elif direction == "left":
        if cords[0] <= 0:
            return True
        else:
            return False

    elif direction == "up":
        if cords[1] <= 0:
            return True
        else:
            return False

    elif direction == "down":
        if cords[1] >= border[1]:
            return True
        else:
            return False
    else:
        return False


def set_walls(direct):
    if set_borders(player_pos, direct) == False:
        for pos in no_wall_tiles:
            if (direct == "right" or "left") and ((player_pos[1] == pos[0][1]) or (player_pos[1] == pos[1][1])):
                if direct == "right"
                    if ((player_pos[0] == pos[0][0]) or (player_pos[0] == pos[1][0])) and (
                            ((player_pos[0] + 1) == pos[1][0]) or ((player_pos[0] + 1) == pos[0][0])):
                        return False
                elif direct == 'left':
                    if ((player_pos[0] == pos[0][0]) or (player_pos[0] == pos[1][0])) and (
                            ((player_pos[0] - 1) == pos[1][0]) or ((player_pos[0] - 1) == pos[0][0])):
                        return False
                if (direct == 'up' or 'down') and ((player_pos[0] == pos[1][0]) or (player_pos[0] == pos[0][0])):
                    if direct == 'up':
                        if ((player_pos[1] == pos[0][1]) or (player_pos[1] == pos[1][1])) and (
                                ((player_pos[1] - 1) == pos[1][1]) or ((player_pos[1] - 1) == pos[0][1])):
                            return False
                    elif direct == 'down':
                        if ((player_pos[1] == pos[0][1]) or (player_pos[1] == pos[1][1])) and (
                                ((player_pos[1] + 1) == pos[1][1]) or ((player_pos[1] + 1) == pos[0][1])):
                            return False
        return True
    else:
        return True

def random_direction():
    digit = randint(1,4)
    if digit == 1:
        return "right"
    if digit == 2:
        return "left"
    if digit == 3:
        return "up"
    if digit == 4:
        return "down"

def generate_maze():
    wall_generated = False
    generation_visit = []
    global  no_walls_tiles
    no_walls_tiles = []
    generation_pos = [randint(0, border[0]), randint(0, border [1])]
    generation_last_pos = []
    first_run = True
    while wall_generated == False:
        if tuple(generation_pos) in generation_visit:
            is_visted = True
        else:
            is_visted = False

        if is_visted == False:
            generation_visit.append(tuple(generation_pos))
            if first_run == False:
                no_walls_tiles.append((tuple(generation_last_pos), tuple(generation_pos)))
        direction =  random_direction()
        generation_last_pos = generation_pos.copy()
        if is_border(tuple(generation_pos), direction) == False:
            if d




