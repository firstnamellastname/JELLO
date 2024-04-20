import pygame
#
pygame.init()

WIDTH = 600
HEIGHT = 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))


class Player:
    def __init__(self):
        self.speed = 5
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

# importing the modules
import pygame
import random

# instantiating the class
pygame.init()

# dimension of the screen
width = 700
height = 550

# colours
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# creating a Screen
screen = pygame.display.set_mode((width, height))

# title of the screen
pygame.display.set_caption("Bouncy Ball")

# declaring variables for the ball
ball_X = width / 2 - 12
ball_Y = height / 2 - 12
ball_XChange = 3 * random.choice((1, -1))
ball_YChange = 3
ballPixel = 24

# gaming Loop
running = True
while running:

    # background color
    screen.fill(black)

    # to exit the loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # bouncing the ball
    if ball_X + ballPixel >= width or ball_X <= 0:
        ball_XChange *= -1
    if ball_Y + ballPixel >= height or ball_Y <= 0:

        # moving the ball
        ball_X += ball_XChange
        ball_Y += ball_YChange

        # drawing the ball
        ballImg = pygame.draw.circle(screen, (0, 0, 255),
                                     (int(ball_X), int(ball_Y)),
                                     15)

        pygame.display.update()

    # create the display surface object
    # of specific dimension..e(500, 500).
    win = pygame.display.set_mode((500, 500))

    # set the pygame window name
    pygame.display.set_caption("Moving rectangle")

    # object current co-ordinates
    x = 200
    y = 200

    # dimensions of the object
    width = 20
    height = 20

    # velocity / speed of movement
    vel = 10

    # Indicates pygame is running
    run = True

    # infinite loop
    while run:
        # creates time delay of 10ms
        pygame.time.delay(10)

        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():

            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if event.type == pygame.QUIT:
                # it will make exit the while loop
                run = False
        # stores keys pressed
        keys = pygame.key.get_pressed()

        # if left arrow key is pressed
        if keys[pygame.K_LEFT] and x > 0:
            # decrement in x co-ordinate
            x -= vel

            # if left arrow key is pressed
        if keys[pygame.K_RIGHT] and x < 500 - width:
            # increment in x co-ordinate
            x += vel

            # if left arrow key is pressed
        if keys[pygame.K_UP] and y > 0:
            # decrement in y co-ordinate
            y -= vel

            # if left arrow key is pressed
        if keys[pygame.K_DOWN] and y < 500 - height:
            # increment in y co-ordinate
            y += vel

            # completely fill the surface object
        # with black colour
        win.fill((0, 0, 0))

        # drawing object on screen which is rectangle here
        pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))

        # it refreshes the window
        pygame.display.update()

# closes the pygame window
pygame.quit()



