import random, sys, time, pygame
from pygame.locals import *
from random import *

def hcf(a, b):
    while b:
        a, b = b, a % b
    return a


Tile_Multipler = 1
pygame.init()
window_resolution = 800, 600
window = pygame.display.set_mode((window_resolution[0], window_resolution[1]))
pygame.display.set_caption('GELLO')
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
goal_pos = goal_pos_x, goal_pos_y
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
    if not set_borders(player_pos, direct):
        for pos in no_walls_tiles:
            if (direct == "right" or "left") and ((player_pos[1] == pos[0][1]) or (player_pos[1] == pos[1][1])):
                if direct == "right":
                    if ((player_pos[0] == pos[0][0]) or (player_pos[0] == pos[1][0])) and (((player_pos[0] + 1) == pos[1][0]) or ((player_pos[0] + 1) == pos[0][0])):
                        return False
                elif direct == 'left':
                    if ((player_pos[0] == pos[0][0]) or (player_pos[0] == pos[1][0])) and (((player_pos[0] - 1) == pos[1][0]) or ((player_pos[0] - 1) == pos[0][0])):
                        return False
                if (direct == 'up' or 'down') and ((player_pos[0] == pos[1][0]) or (player_pos[0] == pos[0][0])):
                    if direct == 'up':
                        if ((player_pos[1] == pos[0][1]) or (player_pos[1] == pos[1][1])) and (((player_pos[1] - 1) == pos[1][1]) or ((player_pos[1] - 1) == pos[0][1])):
                            return False
                    elif direct == 'down':
                        if ((player_pos[1] == pos[0][1]) or (player_pos[1] == pos[1][1])) and (((player_pos[1] + 1) == pos[1][1]) or ((player_pos[1] + 1) == pos[0][1])):
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
    global no_walls_tiles
    no_walls_tiles = []
    generation_pos = [randint(0, border[0]), randint(0, border [1])]
    generation_last_pos = []
    first_run = True
    while not wall_generated:
        if tuple(generation_pos) in generation_visit:
            is_visted = True
        else:
            is_visted = False

        if not is_visted:
            generation_visit.append(tuple(generation_pos))
            if not first_run:
                no_walls_tiles.append((tuple(generation_last_pos), tuple(generation_pos)))
        direction = random_direction()
        generation_last_pos = generation_pos.copy()
        if not set_borders(tuple(generation_pos), direction):
            if direction == "right":
                generation_last_pos = generation_pos.copy()
                generation_pos[0] += 1
            elif direction == "left":
                generation_last_pos = generation_pos.copy()
                generation_pos[0] -= 1
            elif direction == "up":
                generation_last_pos = generation_pos.copy()
                generation_pos[1] -= 1
            elif direction == 'down':
                generation_last_pos = generation_pos.copy()
                generation_pos[1] += 1

            first_run = False
            if len(generation_visit) == tile_amount:
                print(no_walls_tiles)
                wall_generated = True


# def is_touched(x):
#     return x in touched


def draw_walls():
    opposite_cord = 0
    line_color = 255, 255, 255
    for z in range(window_resolution[0] // tile_width_height):
        global line_width
        should_draw = False
        cord_x = window_resolution[0] // 10
        cord_y = window_resolution[1] // 10
        posx = 0
        for x in range(cord_x // 10 * 4 * Tile_Multipler):
            for i in range(1, 4):
                if i == 1:
                    for coord in no_walls_tiles:
                        if (x, z) in coord and (x, z+1) in coord:
                            should_draw = False
                            break
                        should_draw = True
                    if should_draw:
                        pygame.draw.line(window,line_color, (posx, opposite_cord + tile_width_height),
                                         (tile_width_height + posx, opposite_cord + tile_width_height), line_width)
                elif i == 2:
                    for coord in no_walls_tiles:
                        if (x, z) in coord and (x+1, z) in coord:
                            should_draw = False
                            break
                        should_draw = True
                    if should_draw:
                        pygame.draw.line(window, line_color, (posx + tile_width_height, opposite_cord),
                                         (posx + tile_width_height, opposite_cord + tile_width_height), line_width)
            posx += tile_width_height
            line_width = stag_line_width
        for y in range(cord_y // 10 * 4 * Tile_Multipler):
            posx += tile_width_height
            line_width = stag_line_width
        opposite_cord += tile_width_height


def vic_royal():
    if player_pos == goal_pos:
        return True
    return False

def draw_tiles():
    opposite_cord = 0
    for z in range(window_resolution[0] // tile_width_height):
        global line_width
        rect_color = 0, 0, 0
        rect_color_perma = rect_color
        cordx = window_resolution[0] // 10
        cordy = window_resolution[1] // 10
        posx = 0
        for x in range(cordx // 10 * 4 * Tile_Multipler):
            if goal_pos_x == x and goal_pos_y == z:
                line_width = 0
                rect_color = (0, 255, 0)
            elif player_pos_x == x and player_pos_y == z:
                rect_color = (255, 0, 0)
                line_width = 0
            pygame.draw.rect(window, rect_color, (posx, opposite_cord, tile_width_height, tile_width_height), line_width)
            rect_color = rect_color_perma
            posx += tile_width_height
            line_width = stag_line_width
        for y in range(cordy // 10 * 4 * Tile_Multipler):
            if player_pos_y == z and player_pos_y == y:
                line_width = 1
            pygame.draw.rect(window,rect_color, (opposite_cord, posx, tile_width_height, tile_width_height), line_width)
            posx += tile_width_height
            line_width = stag_line_width
        opposite_cord += tile_width_height


generate_maze()
draw_walls()
draw_tiles()
pygame.display.update()

while True:
    player_pos = player_pos_x, player_pos_y
    if vic_royal():
        player_pos_x = 0
        player_pos_y = 0
        goal_pos_x = randint(0, border[0])
        goal_pos_y = randint(0, border[1])
        goal_pos = goal_pos_x, goal_pos_y
        touched = []
        generate_maze()
        window.fill((0, 0, 0))
        draw_tiles()
        draw_walls()
        pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_a and set_walls('left') == False:
                if player_pos not in touched:
                    touched.append(player_pos)
                player_pos_x -= 1
                window.fill((0, 0, 0))
                draw_tiles()
                draw_walls()
                pygame.display.update()
            elif event.key == K_d and set_walls('right') == False:
                if player_pos not in touched:
                    touched.append(player_pos)
                player_pos_x += 1
                window.fill((0, 0, 0))
                draw_tiles()
                draw_walls()
                pygame.display.update()
            elif event.key == K_s and set_walls('down') == False:
                if player_pos not in touched:
                    touched.append(player_pos)
                player_pos_y += 1
                window.fill((0, 0, 0))
                draw_tiles()
                draw_walls()
                pygame.display.update()
            elif event.key == K_w and set_walls('up') == False:
                if player_pos not in touched:
                    touched.append(player_pos)
                player_pos_y -= 1
                window.fill((0, 0, 0))
                draw_tiles()
                draw_walls()
                pygame.display.update()
