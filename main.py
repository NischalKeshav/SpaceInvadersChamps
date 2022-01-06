import pygame
import random
# initialize pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

# # Screeetup
pygame.display.set_caption('Space Invaders')
icn = pygame.image.load('alien-pixelated-shape-of-a-digital-game-3.png')
pygame.display.set_icon(icn)
running = True
# player
PlayerImage = pygame.image.load('ship copy.png')
playerXpos = 370
playerYpos = 480
playerXmove = 0
playerYmove = 0

# alien Atacker
AlienImage = pygame.image.load('monster.png')
alienXpos = random.randint(0,736)
alienYpos = random.randint(0,200)
alienXmove =3
alienYmove = .5
bulletReady= True

#Bullet
BulletImage = pygame.image.load('bullet.png')
bulletXpos = random.randint(0,736)
bulletYpos = playerYpos
bulletXmove = 0
bulletYmove = 10

def alien(x, y):
    screen.blit(AlienImage, (x, y))

def bullet(x,y):
    global bulletReady
    bulletReady = False
    screen.blit(BulletImage,(x+15,y+10))

def player(x, y):
    screen.blit(PlayerImage, (x, y))


while running:  # game loop
    screen.fill((60, 10, 70))  # RGB screenfill
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXmove = -3
            if event.key == pygame.K_SPACE:
                bullet(playerXpos, playerYpos)
            elif event.key == pygame.K_RIGHT:
                playerXmove = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXmove = 0


    playerXpos += playerXmove
    if playerXpos <= 0:
        playerXpos = 0
    elif playerXpos >= 736:
        playerXpos = 736
    alienXpos += alienXmove
    alienYpos += alienYmove
    if alienXpos <= 0:
        alienXpos = 0
        alienXmove = -1*alienXmove
    elif alienXpos >= 736:
        alienXpos = 736
        alienXmove = -1 * alienXmove
    if alienYpos >= 600 :
        alienXpos = random.randint(0, 736)
        alienYpos = random.randint(0, 200)
    player(playerXpos, playerYpos)
    alien(alienXpos,alienYpos)
    pygame.display.update()
