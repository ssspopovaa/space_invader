import pygame

pygame.init()

icon = pygame.image.load('spaceship.png')

pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((800, 600))

# playerImg = pygame.image.load('battleship.png')
playerImg = pygame.image.load('spaceship1.png')

playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
    screen.blit(playerImg,(x, y))

running = True

while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -0.3
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.3
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0
        if event.key == pygame.K_q:
            running = False

    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()
