import math
import pygame
import random
from pygame import mixer
pygame.init()

screen = pygame.display.set_mode((800, 600))
mixer.music.load('background.wav')
mixer.music.play(-1)
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
pic = pygame.image.load('monster.png')
AlienImage = []
alienXpos = []
alienYpos =[]
alienXmove =[]
alienYmove =[]
bulletReady= True
num_of_enemy =4
for i in range (num_of_enemy):
    AlienImage.append(pic)
    alienXpos.append(random.randint(0,800))
    alienYpos.append(random.randint(0,400))
    if i < 2:
        alienXmove.append(-2)
    else:
        alienXmove.append(4)
    alienYmove.append(.5)


#Bullet
BulletImage = pygame.image.load('bullet.png')
bulletXpos = random.randint(0,736)
bulletYpos = playerYpos
bulletYmove = 10

def alien(x, y):
    screen.blit(pic, (x, y))

def bullet(x,y):
    global bulletReady
    bulletReady = False
    screen.blit(BulletImage,(x+15,y+10))

def player(x, y):
    screen.blit(PlayerImage, (x, y))

def collide(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2) + math.pow(enemyY-bulletY,2))
    if distance <=36:
        return True
    else:
        return False
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
font_end = pygame.font.Font('freesansbold.ttf', 72)
def score_shower(x,y):
        score = font.render("Score:" + str(score_value),True,(250,255,255))
        screen.blit(score,(x,y))
def GAMEOVER():
    text = font_end.render("GAME OVER", True, (255, 0, 0))
    screen.blit(text,(200,70))
background = pygame.image.load('background.png')
while running:  # game loop
    screen.blit(background,(0,0))  # RGB screenfill
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXmove = -3
            elif event.key == pygame.K_RIGHT:
                playerXmove = 3
            elif event.key == pygame.K_SPACE:
                if bulletReady:
                    bulletSound =mixer.Sound('laser.wav')
                    bulletSound.play()
                    bulletXpos = playerXpos
                    bullet(bulletXpos, playerYpos)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                if event.key == pygame.K_LEFT and playerXmove > 0:
                    playerXmove += 0
                elif event.key == pygame.K_RIGHT and playerXmove < 0:
                        playerXmove += 0
                else:
                    playerXmove = 0


    playerXpos += playerXmove
    if playerXpos <= 0:
        playerXpos = 0
    elif playerXpos >= 736:
        playerXpos = 736
    if bulletReady == False:
        bullet(bulletXpos, bulletYpos)
        bulletYpos -= bulletYmove
        if bulletYpos <= -32:
            bulletYpos = 480
            bulletReady = True
    for i in range(num_of_enemy):
        alienXpos[i] += alienXmove[i]
        alienYpos[i] += alienYmove[i]
        if alienXpos[i] <= 0:
            alienXpos[i] = 0
            alienXmove[i] = -1*alienXmove[i]
        elif alienXpos[i] in range (736,800):
            alienXpos[i] = 736
            alienXmove[i] = -1 * alienXmove[i]


        if alienYpos[i] in range (602,700) :
            alienXpos[i] = random.randint(0, 736)
            alienYpos[i] = random.randint(0, 200)
        if collide(alienXpos[i],alienYpos[i],bulletXpos,bulletYpos):
            if bulletReady == False:
                alienXpos[i] = random.randint(0, 736)
                alienYpos[i] = random.randint(0, 200)
                killSound = mixer.Sound('explosion.wav')
                killSound.play()
                bulletReady = True
                score_value += 1

        if collide(alienXpos[i],alienYpos[i],playerXpos,playerYpos):
            for j in range(num_of_enemy):
                alienXpos[j] = 20000
                alienYmove[j]= 0
                for z in range(num_of_enemy):
                    alienXpos[z] = 20000
                    pygame.display.update()
                GAMEOVER()
            running = False
        alien(alienXpos[i], alienYpos[i])
    player(playerXpos, playerYpos)
    score_shower(10,10)
    pygame.display.update()
playerXpos = [10000,1000000,1000000,1000000,10000,1000000]
for i in range (num_of_enemy):
    alien(100000000000,1000000)
    pygame.display.update()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


