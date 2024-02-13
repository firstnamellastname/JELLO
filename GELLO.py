import pygame as pg

# pygame setup
pg.init()

pg.display.set_caption("JELLO")
width = 1200
height = 720
image_height = 40
image_width = 40
screen_colour = (0, 0, 0)
screen = pg.display.set_mode((width, height))

x = width/2
y = height/2

clock = pg.time.Clock()

running = True

dt = 0

player_pos = pg.Vector2(screen.get_width() / 10, screen.get_height() / 10)

while running:
    # poll for events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    screen.fill(screen_colour)

    heart_sprite = pg.image.load("Undertaleheart.png")
    IMAGE_SIZE = (image_width,image_height)
    heart_sprite = pg.transform.scale(heart_sprite, IMAGE_SIZE)
    screen.blit(heart_sprite, (x, y))

    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        y -= 300 * dt
    if keys[pg.K_s]:
        y += 300 * dt
    if keys[pg.K_a]:
        x -= 300 * dt
    if keys[pg.K_d]:
        x += 300 * dt

    pg.draw.rect(screen ,"white" , pg.Rect(435,200,350,350 ), 4)
    pg.display.flip()
    dt = clock.tick(60) / 1000

pg.quit()

