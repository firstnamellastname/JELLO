import pygame as pg
import random
# pygame setup
pg.init()
print(random.randint(1,22))
pg.display.set_caption("FIGHT FIGHT FIGHT")
screen_width = 1200
screen_height = 720

image_height = 40
image_width = 40
screen_colour = (0, 0, 0)
screen = pg.display.set_mode((screen_width, screen_height))
hbox = 350
vbox = 350
x = screen_width/2
y = screen_height/2

clock = pg.time.Clock()

running = True

dt = 0

player_pos = pg.Vector2(screen.get_width() / 10, screen.get_height() / 10)

while running:
    # check for events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    screen.fill(screen_colour)

    heart_sprite = pg.image.load("Undertaleheart.png")
    IMAGE_SIZE = (image_width,image_height)
    heart_sprite = pg.transform.scale(heart_sprite, IMAGE_SIZE)
    heart_border = pg.draw.rect(screen, (0, 0, 0), (x, y, image_width, image_height))
    fight_menu = pg.draw.rect(screen, (255, 255, 255),(0, 600, 1200, 200))
    screen.blit(heart_sprite, (x, y))

    keys = pg.key.get_pressed()
    if keys[pg.K_w] and y > dt:
        y -= 300 * dt

    if keys[pg.K_s] and y < (600 - image_height - dt):
        y += 300 * dt

    if keys[pg.K_a] and x > dt:
        x -= 300 * dt

    if keys[pg.K_d] and x < (screen_width - image_width - dt):
        x += 300 * dt

    pg.display.flip()
    dt = clock.tick(60) / 1000
pg.quit()



### scrap the box, instead of having an border right makke the whole screen the arena
## then just border around the whole screen, replace the heart with a rectangle, add pathtracking projectiles that you
# fuck coding bruh this is ass
