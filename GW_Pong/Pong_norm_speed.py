#   Pong
#   Author: Garrison White
#   Date: 11/22/2025
#   Description: 2-player Pong game made with PyGame.

import pygame
import sys
import random
import os, sys

def resource_path(relative_path):
    try:
        # PyInstaller stores files in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # When running normally (not exe)
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)
pygame.init()

paddle_sound = pygame.mixer.Sound(resource_path("sounds/paddle_impact.ogg"))
wall_sound = pygame.mixer.Sound(resource_path("sounds/wall_impact.ogg"))
score_sound = pygame.mixer.Sound(resource_path("sounds/blip.wav"))

run = False

#Set dimensions of window and all game objects/variables.
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Pong")

FPS = 60 
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 10
BALL_SIZE = 14
BALL_SPEED = 8
BG_COLOR = (30, 30, 30,)
PADDLE_COLOR = (200,200,200)
BALL_COLOR = (255,180,0)

paddle = pygame.Rect(30, (HEIGHT - PADDLE_HEIGHT)//2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - 30 - PADDLE_WIDTH, (HEIGHT - PADDLE_HEIGHT)//2, PADDLE_WIDTH, PADDLE_HEIGHT)

ball = pygame.Rect(
    WIDTH//2 - BALL_SIZE//2,
    HEIGHT//2 - BALL_SIZE//2,
    BALL_SIZE,
    BALL_SIZE)


#Direction of ball on x and y axis
dx = BALL_SPEED
dy = random.choice([-0.1*BALL_SPEED, 0.1*BALL_SPEED])

pad_speed = PADDLE_SPEED

#Randomly decides which side ball starts on.
x = random.randint(0,1)
if x == 1:
    ball.x = WIDTH // 2
    dx = 4
else:
   ball.x = WIDTH // 2
   dx = -4

#The ball goes to the opposite side of the player who just scored.
def reset_game_p1():
    paddle.y = HEIGHT//2 - PADDLE_HEIGHT//2
    paddle2.y = HEIGHT//2 - PADDLE_HEIGHT//2

    ball.x = WIDTH // 2
    ball.y = HEIGHT//2 - BALL_SIZE//2

    return 4, random.choice([-0.1*BALL_SPEED, 0.1*BALL_SPEED])

def reset_game_p2():
    paddle.y = HEIGHT//2 - PADDLE_HEIGHT//2
    paddle2.y = HEIGHT//2 - PADDLE_HEIGHT//2

    ball.x = WIDTH // 2
    ball.y = HEIGHT//2 - BALL_SIZE//2

    return -4, random.choice([-0.1*BALL_SPEED, 0.1*BALL_SPEED])

#Start screen loop. Player clicks screen to start game.
start_screen = True
while start_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_screen = False

    win.fill(BG_COLOR)

    font = pygame.font.Font(None, 60)
    text = font.render("PONG", True, (255,255,255))
    win.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
    font = pygame.font.Font(None, 30)
    text = font.render("Click to start", True, (255,255,255))
    win.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 + text.get_height() * 2))

    pygame.display.flip()

p1_score = 0
p2_score = 0
font = pygame.font.Font(None, 60)


#GAME LOOP
paused = False
run = True
while run:
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused
    
    if paused:
        win.fill((20, 20, 20))
        font = pygame.font.Font(None, 80)
        text = font.render("PAUSED", True, (255,255,255))
        win.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
        pygame.display.flip()
        clock.tick(FPS)
        continue

    #Get key inputs
    keys = pygame.key.get_pressed()

    if keys [pygame.K_w]:
        paddle.y -= pad_speed
    
    if keys[pygame.K_s]:
        paddle.y += pad_speed
    paddle.y = max(0, min(paddle.y, HEIGHT - PADDLE_HEIGHT))

    if keys[pygame.K_UP]:
        paddle2.y -= pad_speed

    if keys[pygame.K_DOWN]:
        paddle2.y += pad_speed

    paddle2.y = max(0, min(paddle2.y, HEIGHT - PADDLE_HEIGHT))
    
    #Move ball in proper direction.
    ball.x += dx
    ball.y += dy

    #If ball hits the top or bottom of the screen, reverse y direction.
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        dy = -dy
        wall_sound.play()

    #If ball hits Player 1 paddle.
    if ball.colliderect(paddle):
        dx = BALL_SPEED

        hit_pos = (ball.centery - paddle.centery)
        dy = hit_pos * 0.15
       
        paddle_sound.play()

    #If ball hits Player 2 paddle.
    if ball.colliderect(paddle2):
        dx = BALL_SPEED
        dx = -dx

        hit_pos = (ball.centery - paddle2.centery)
        dy = hit_pos * 0.15

        paddle_sound.play()

    #If ball goes off screen to either side, add point to appropriate player and reset game.
    if ball.left <= 0:
        p2_score += 1
        score_sound.play()
        dx, dy = reset_game_p1()

    if ball.right >= WIDTH:
        p1_score += 1
        score_sound.play()
        dx, dy, = reset_game_p2()


    #Fill in window and draw all objects.
    win.fill(BG_COLOR)
    dot_width = 4
    dot_height = 20
    gap = 20   # space between dots

    for y in range(0, HEIGHT, dot_height + gap):
        pygame.draw.rect(win, (255,255,255), 
                        (WIDTH//2 - dot_width//2, y, dot_width, dot_height))
    score_text = font.render(f"{p1_score}                  {p2_score}", True, (255,255,255))
    win.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 20))
    pygame.draw.rect(win, PADDLE_COLOR, paddle)
    pygame.draw.rect(win, PADDLE_COLOR, paddle2)
    pygame.draw.ellipse(win, BALL_COLOR, ball)

    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()
sys.exit()