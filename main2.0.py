import pygame
import random
import math
#start pygame
import os, sys

def resource_path(relative_path):
    """ Get absolute path to resource (for PyInstaller) """
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))

    return os.path.join(base_path, relative_path)

pygame.mixer.init()
pygame.init()
laser_sound = pygame.mixer.Sound(resource_path("laser.wav"))
collision_sound = pygame.mixer.Sound(resource_path("explosion.wav"))
pygame.mixer.music.load(resource_path("background.mp3")) 
pygame.mixer.music.play(-1)

#creating the screen and captopn and logo
screen=pygame.display.set_mode((800,600))
#background
background=pygame.image.load(resource_path("background.png"))
score=0
pygame.display.set_caption("  Space Invaders")
icon = pygame.image.load(resource_path("ufo.png"))
pygame.display.set_icon(icon)
clock  = pygame.time.Clock()
FPS = 60

#Loading font
#Player
class Spaceship(pygame.sprite.Sprite):
    def __init__(self,char_type,player_x,player_y,speed):
        self.char_type=char_type
        self.playerimg = pygame.image.load(resource_path(f"{char_type}.png"))
        self.player_x=player_x
        self.player_y=player_y
        self.speed=speed
        self.direction=1
        self.bullet_active = False
        self.rect = self.playerimg.get_rect(topleft=(self.player_x, self.player_y))

    #Drawing the player    
    def draw(self):
        screen.blit(self.playerimg,(self.player_x, self.player_y))
        self.rect.topleft = (self.player_x, self.player_y)  

    def move(self,moving_left,moving_right):
            
        #reset movement
            dx=0
            dy=0

            #changing dx
            if moving_left:
                dx=-self.speed  

            if moving_right:
                dx=self.speed

            # changing the co-ordinates
            self.player_x += dx

            #Adding Boundary conditions
            if self.player_x < 0:
                self.player_x = 0
            if self.player_x > 800 - self.playerimg.get_width():
                self.player_x = 800 - self.playerimg.get_width()
            
            self.player_y+=dy    

    def enemove(self):
        dx=self.speed
        # changing the co-ordinates od enemy
        self.player_x += (dx*self.direction)
        if self.player_x < 0:
                self.player_x = 0
                self.direction=1
                self.player_y += 60
        if self.player_x > 800 - self.playerimg.get_width():
            self.player_x = 800 - self.playerimg.get_width()
            self.direction=-1
            self.player_y += 60
    # bullet moving when fired        
    def bulmove(self):
        self.player_y-=7       


#Creating objects   
no_of_enemies=4   
no_buttlets=3
enemy_speed=3     
player=Spaceship('player',370,480,5)
enimies = []
# Function to create enemies
def create_enemies(no_of_enemies):
    global enimies
    enimies = []
    for i in range(no_of_enemies):
        enemy_x = random.randint(0, 800 - 64)
        enemy_y = random.randint(50, 150)
        enemy = Spaceship('enemy', enemy_x, enemy_y, enemy_speed)
        enimies.append(enemy)

def reset_game():
    global score, player, enemies, bullets, no_of_enemies, enemy_speed,no_buttlets
    score = 0
    no_buttlets = 3
    no_of_enemies = 4
    enemy_speed = 3
    player = Spaceship('player', 370, 480, 5)
    bullets = []
    create_enemies(no_of_enemies)

def show_game_over():
    font = pygame.font.Font(None, 74)
    over_text = font.render("GAME OVER", True, (255, 0, 0))
    restart_text = pygame.font.Font(None, 36).render("Press SPACE to restart or ESC to quit", True, (255, 255, 255))
    screen.blit(over_text, (250, 250))
    screen.blit(restart_text, (200, 320))

create_enemies(no_of_enemies)
#game loop variables
moving_left=False
moving_right=False
bullet_active = False
bullet = None  
run=True
game_over=False
bullets=[]  #To store different bullets objects to stop overwritting
#game loop
def iscollision(bullet,enemy):
    return bullet.rect.colliderect(enemy.rect)


def show_score(score):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))


while run:
    clock.tick(FPS)
    #bgcolor
    screen.fill((0,0,0))
    #Loading background
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_LEFT:
                    moving_left=True
                if event.key == pygame.K_RIGHT:
                    moving_right=True 
                if event.key==pygame.K_SPACE:
                    if len(bullets)<no_buttlets: 
                        #player music
                        laser_sound.play()
                        # Create a new bullet object
                        new_bullet = Spaceship('bullet', player.player_x + player.playerimg.get_width() // 2 - 8, player.player_y, 7) #to create a new object for evry spacebar pressed
                        bullets.append(new_bullet)   

            elif game_over:
                if event.key == pygame.K_SPACE:
                    # Reset game state
                    reset_game()
                    game_over = False
                    moving_left = False
                    moving_right = False
                    run = True
                if event.key == pygame.K_ESCAPE:
                    run = False


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left=False
            if event.key == pygame.K_RIGHT:
                moving_right=False          
            
    
    if not game_over:
        #move player
        player.move(moving_left,moving_right)
        #enemy moving
        for enemy in enimies:
            enemy.enemove()
            if enemy.player_y > 440:
                game_over = True
                break

        #moving bullets 
        for bullet in bullets[:]:  
            bullet.bulmove()
            bullet.draw()
            if bullet.player_y < 0:
                bullets.remove(bullet)
        #collision detection
        for bullet in bullets[:]:
            for enemy in enimies:
                collision = iscollision(bullet, enemy)
                if collision:
                    collision_sound.play()
                    bullets.remove(bullet)
                    score += 1
                    enimies.remove(enemy)
                    # Check if all enemies are defeated
                    if len(enimies)==0:
                        # If all enemies are defeated, respawn them
                        no_of_enemies += 1
                        enemy_speed += 0.5 # Increase speed of enemies
                        create_enemies(no_of_enemies)
                    break  

        player.draw()
        for enemy in enimies:
            enemy.draw()
        #display the score
        show_score(score)

    elif game_over:
        show_game_over()  
    #Important to updtate screen over every iteration
    pygame.display.update()


