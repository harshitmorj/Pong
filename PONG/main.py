import pygame

pygame.init()  # initialising pygame

screen = pygame.display.set_mode((800, 600))
score = 0
# Title and Icon
pygame.display.set_caption("Pong")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
# Game Over Screen
font1 = pygame.font.Font('freesansbold.ttf', 64)
font2 = pygame.font.Font('freesansbold.ttf', 30)

def Gameover(x):
    over = font1.render('Game Over', True, (255, 255, 255))
    screen.blit(over, (200, 250))
    score = font2.render('Score :' + str(x), True, (0, 0, 0))
    screen.blit(score, (260, 314))

# Time
clock = pygame.time.Clock()

# Ball
ballImg = pygame.image.load('ball.png')
ballX = 390
ballY = 574
speedX = 3
speedY = -2


def ball(x, y):
    screen.blit(ballImg, (x, y))


# Bar
barImg = pygame.image.load('bar.png')
barX = 360
barY = 572
barspeedX = 0


def bar(x, y):
    screen.blit(barImg, (x, y))


# EnemyBar
ebarX = 360
ebarY = -36


def ebar(x, y):
    screen.blit(barImg, (x, y))


# Game loop
running = True
while running:
    screen.fill((200, 200, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            barspeedX = -2 - score * 0.5
        if event.key == pygame.K_RIGHT:
            barspeedX = +2 + score * 0.5
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            barspeedX = 0

    bar(barX, barY)  # BAR MOVING
    if barX < 0:
        barX = 0
    elif barX > 736:
        barX = 736
    barX += barspeedX

    ebar(ballX - 32, ebarY)  # EBAR MOVING

    # Ball moving
    if ballY == 580 and ballX - barX <= 64 and ballX - barX >= -10:
        speedY = -(speedY + 0.25 * score ** 1.25)
        score += 1
    elif ballX > 788 or ballX < 8:
        speedX = -speedX
    elif ballY < 4:
        speedY = -speedY
    elif ballY > 600:
        Gameover(score)
    ballX += speedX
    ballY += speedY
    ball(ballX, ballY)

    clock.tick(60)
    pygame.display.update()
print("YOU LOSE")
print('Score = ', score)
