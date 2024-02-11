import pygame

# pygame setup
pygame.init()

pygame.display.set_caption("JELLO")
width = 1200
height = 720
image_height = 40
image_width = 40

screen = pygame.display.set_mode((width, height))

x = 600
y = 360

clock = pygame.time.Clock()

running = True

dt = 0

player_pos = pygame.Vector2(screen.get_width() / 10, screen.get_height() / 10)

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill("black")

    heart_sprite = pygame.image.load("Undertaleheart.png")
    IMAGE_SIZE = (image_width,image_height)
    heart_sprite = pygame.transform.scale(heart_sprite, IMAGE_SIZE)
    screen.blit(heart_sprite, (x, y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= 300 * dt
    if keys[pygame.K_s]:
        y += 300 * dt
    if keys[pygame.K_a]:
        x -= 300 * dt
    if keys[pygame.K_d]:
        x += 300 * dt

    #screen.fill((0,0,0))
  #  pygame.draw.rect(screen, (255,0,0), (x,y, image_width , image_height))
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()

