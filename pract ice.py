import pygame

pygame.init()

WIDTH = 600
HEIGHT = 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))


class Player:
    def __init__(self):
        self.speed = 1
        self.width = 20
        self.height = 20
        self.color = (255, 255, 0)
        self.rect = pygame.Rect((WIDTH - self.width) / 2, (HEIGHT - self.height) / 2, 20, 20)

    def up(self):
        self.rect.y = max([self.rect.y - self.speed, 0])

    def down(self):
        self.rect.y = min([self.rect.y + self.speed, HEIGHT - self.height])

    def left(self):
        self.rect.x = max([self.rect.x - self.speed, 0])

    def right(self):
        self.rect.x = min([self.rect.x + self.speed, WIDTH - self.width])

    def draw(self):
        pygame.draw.rect(wn, self.color, self.rect)


char = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        char.up()
    if keys[pygame.K_s]:
        char.down()
    if keys[pygame.K_a]:
        char.left()
    if keys[pygame.K_d]:
        char.right()
    wn.fill((0, 0, 0))
    char.draw()
    pygame.display.update()