import pygame
import random
import math

pygame.init()

icon = pygame.image.load('spaceship.png')

pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((800, 600))
backgroundImg = pygame.image.load('background.png')

#Score
score_value = 0

# font = pygame.font.Font('freesansbold.ttf', 32)
font = pygame.font.Font('digital.ttf', 32)
textX = 10
textY = 10

# playerImg = pygame.image.load('battleship.png')
playerImg = pygame.image.load('spaceship1.png')
playerX = 370
playerY = 480
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for enemy in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy_1.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(0, 50))
    enemyX_change.append(0.3)
    enemyY_change.append(20)

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = 0
def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score,(x, y))
    
def player(x, y):
    screen.blit(playerImg,(x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i],(x, y))
    
def fire_bullet(x, y):
    # global bullet_state
    # bullet_state = "fire"
    screen.blit(bulletImg,(x, y))
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow((enemyX - bulletX), 2) + math.pow((enemyY - bulletY), 2))
    if distance < 27:
        return True
    return False
    
running = True

while running:
    # screen.fill((0,0,0))
    screen.blit(backgroundImg, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_SPACE:
                if not bullet_state:
                    bullet_state = 1
                    bulletX = playerX
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        
    playerX += playerX_change
    
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]
            
        if enemyY[i] >= 600 - 64:
            enemyY[i] = 0
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = 480
            bullet_state = 0
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = 0
        enemy(enemyX[i], enemyY[i], i)
            
    if bulletY < 0:
       bullet_state = 0
       bulletY = 480
        
    if bullet_state:
        fire_bullet(bulletX +16, bulletY)
        bulletY -= bulletY_change
            
    player(playerX, playerY)
    show_score(textX, textY)

    pygame.display.update()
