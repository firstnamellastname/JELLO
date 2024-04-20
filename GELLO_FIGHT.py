import pygame as pg
import random
pg.init()
print(random.randint(1,22))
pg.display.set_caption("FIGHT FIGHT FIGHT")
screen_width = 1200
screen_height = 720
image_height = 40
image_width = 40
screen_colour = (0, 0, 0)
screen = pg.display.set_mode((screen_width, screen_height))
undertale_green = "#00c000"
pos_x = screen_width/2
pos_y = screen_height/2
clock = pg.time.Clock()
dt = 0
player_pos = pg.Vector2(screen.get_width() / 10, screen.get_height() / 10)


def generate_fight(x, y):

    global dt
    running = True

    while running:
        # check for events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill(screen_colour)
        heart_sprite = pg.image.load("Undertaleheart.png")
        image_size = (image_width, image_height)
        heart_sprite = pg.transform.scale(heart_sprite, image_size)
        heart_border = pg.draw.rect(screen, (0, 0, 0), (x, y, image_width, image_height))
        fight_menu = pg.draw.rect(screen, (255, 255, 255),(0, screen_height - 150, 1200, 150))
        screen.blit(heart_sprite, (x, y))
        player_health = 100

        keys = pg.key.get_pressed()
        if keys[pg.K_w] and y > dt:
            y -= 300 * dt

        if keys[pg.K_s] and y < (screen_height - image_height - dt):
            y += 300 * dt

        if keys[pg.K_a] and x > dt:
            x -= 300 * dt

        if keys[pg.K_d] and x < (screen_width - image_width - dt):
            x += 300 * dt

        pg.display.flip()
        dt = clock.tick(60) / 1000


generate_fight(pos_x, pos_y)
pg.quit()



### scrap the box, instead of having an border right makke the whole screen the arena
## then just border around the whole screen, replace the heart with a rectangle, add pathtracking projectiles that you
# fuck coding bruh this is ass
# rewrite all of this just with functions, make everything much easier,
def collision_dect():
    return

