# import pygame
#
# pygame.init()
#
# WIDTH = 600
# HEIGHT = 600
# wn = pygame.display.set_mode((WIDTH, HEIGHT))
#
#
# class Player:
#     def __init__(self):
#         self.speed = 5
#         self.width = 20
#         self.height = 20
#         self.color = (255, 255, 0)
#         self.rect = pygame.Rect((WIDTH - self.width) / 2, (HEIGHT - self.height) / 2, 20, 20)
#
#     def up(self):
#         self.rect.y = max([self.rect.y - self.speed, 0])
#
#     def down(self):
#         self.rect.y = min([self.rect.y + self.speed, HEIGHT - self.height])
#
#     def left(self):
#         self.rect.x = max([self.rect.x - self.speed, 0])
#
#     def right(self):
#         self.rect.x = min([self.rect.x + self.speed, WIDTH - self.width])
#
#     def draw(self):
#         pygame.draw.rect(wn, self.color, self.rect)
#
#
# char = Player()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_w]:
#         char.up()
#     if keys[pygame.K_s]:
#         char.down()
#     if keys[pygame.K_a]:
#         char.left()
#     if keys[pygame.K_d]:
#         char.right()
#     wn.fill((0, 0, 0))
#     char.draw()
#     pygame.display.update()

# # importing the modules
# import pygame
# import random
#
# # instantiating the class
# pygame.init()
#
# # dimension of the screen
# width = 700
# height = 550
#
# # colours
# white = (255, 255, 255)
# red = (255, 0, 0)
# green = (0, 255, 0)
# blue = (0, 0, 255)
# black = (0, 0, 0)
#
# # creating a Screen
# screen = pygame.display.set_mode((width, height))
#
# # title of the screen
# pygame.display.set_caption("Bouncy Ball")
#
# # declaring variables for the ball
# ball_X = width / 2 - 12
# ball_Y = height / 2 - 12
# ball_XChange = 3 * random.choice((1, -1))
# ball_YChange = 3
# ballPixel = 24
#
# # gaming Loop
# running = True
# while running:
#
#     # background color
#     screen.fill(black)
#
#     # to exit the loop
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # bouncing the ball
#     if ball_X + ballPixel >= width or ball_X <= 0:
#         ball_XChange *= -1
#     if ball_Y + ballPixel >= height or ball_Y <= 0:
#
#     # moving the ball
#     ball_X += ball_XChange
#     ball_Y += ball_YChange
#
#     # drawing the ball
#     ballImg = pygame.draw.circle(screen, (0, 0, 255),
#                                  (int(ball_X), int(ball_Y)),
#                                  15)
#
#     pygame.display.update()



class Tank:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.health = 10
        self.attack = 3

    def fire(self):
        input("Press enter to fire")
        returnDamage = random.randint(self.attack - 2, self.attack + 2)
        return returnDamage

    def getName(self):
        return self.name

    def getColour(self):