#   Pong
#   Author: Garrison White
#   Date: 11/22/2025
#   Description: 2-player Pong game made with PyGame.

import pygame
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
BALL_SIZE = 13
BALL_SPEED = 8
BG_COLOR = (30, 30, 30)
PADDLE_COLOR = (200,200,200)
BALL_COLOR = (255,180,0)

paddle = pygame.Rect(30, (HEIGHT - PADDLE_HEIGHT)//2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - 30 - PADDLE_WIDTH, (HEIGHT - PADDLE_HEIGHT)//2, PADDLE_WIDTH, PADDLE_HEIGHT)

ball = pygame.Rect(
    WIDTH//2 - BALL_SIZE//2,
    HEIGHT//2 - BALL_SIZE//2,
    BALL_SIZE,
    BALL_SIZE)

#Randomly decides which side ball starts on.
ball.x = WIDTH // 2
dx = random.choice([-6, 6])

#The ball goes to the opposite side of the player who just scored.
def reset_game_p1():
    paddle.y = HEIGHT//2 - PADDLE_HEIGHT//2
    paddle2.y = HEIGHT//2 - PADDLE_HEIGHT//2

    ball.x = WIDTH // 2
    ball.y = HEIGHT//2 - BALL_SIZE//2

    return 6, random.choice([-0.6, 0.6])

def reset_game_p2():
    paddle.y = HEIGHT//2 - PADDLE_HEIGHT//2
    paddle2.y = HEIGHT//2 - PADDLE_HEIGHT//2

    ball.x = WIDTH // 2
    ball.y = HEIGHT//2 - BALL_SIZE//2

    return -6, random.choice([-0.6, 0.6])


one_player = False
game_speed = "normal"
#Start screen loop. Player clicks screen to start game.
start_screen = True
while start_screen:   

    win.fill(BG_COLOR)

    #Game title
    font = pygame.font.Font(None, 60)
    text = font.render("PONG", True, (255,255,255))
    win.blit(text, (WIDTH//2 - text.get_width()//2, 200))
    font = pygame.font.Font(None, 30)

    #Buttons for 1 or 2 players
    btn1 = pygame.Rect(WIDTH//2 - 150, HEIGHT//2, 300, 60)
    btn2 = pygame.Rect(WIDTH//2 - 150, HEIGHT//2 + 80, 300, 60)

    pygame.draw.rect(win, (70,70,70), btn1)
    pygame.draw.rect(win,(70,70,70), btn2)

    text = font.render("1 Player", True, (255,255,255))
    win.blit(text, (btn1.centerx - text.get_width()//2,
                    btn1.centery - text.get_height()//2))
    
    text = font.render("2 Players", True, (255,255,255))
    win.blit(text, (btn2.centerx - text.get_width()//2,
                    btn2.centery - text.get_height()//2))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos

            if btn1.collidepoint(mx, my):
                one_player = True
                start_screen = False
            if btn2.collidepoint(mx,my):
                one_player = False
                start_screen = False
    

    pygame.display.flip()


#Menu to select game speed:
speed_screen = True
while speed_screen:
    win.fill(BG_COLOR)

    font = pygame.font.Font(None, 40)
    title = font.render("Select Game Speed:", True, (255,255,255))
    win.blit(title, (WIDTH//2 - title.get_width()//2, 75))

    font = pygame.font.Font(None, 30)

    btn_slow   = pygame.Rect(WIDTH//2 - 150, 150, 300, 60)
    btn_medium = pygame.Rect(WIDTH//2 - 150, 250, 300, 60)
    btn_fast   = pygame.Rect(WIDTH//2 - 150, 350, 300, 60)

    pygame.draw.rect(win, (70,70,70), btn_slow)
    pygame.draw.rect(win, (70,70,70), btn_medium)
    pygame.draw.rect(win, (70,70,70), btn_fast)

    # labels
    text = font.render("Normal", True, (255,255,255))
    win.blit(text, (btn_slow.centerx - text.get_width()//2,
                    btn_slow.centery - text.get_height()//2))

    text = font.render("Fast", True, (255,255,255))
    win.blit(text, (btn_medium.centerx - text.get_width()//2,
                    btn_medium.centery - text.get_height()//2))

    text = font.render("Crazy Fast", True, (255,255,255))
    win.blit(text, (btn_fast.centerx - text.get_width()//2,
                    btn_fast.centery - text.get_height()//2))
    

    text1 = font.render("Left paddle: W + S", True, (255,255,255))
    text2 = font.render("Right paddle: ARROW KEYS", True, (255,255,255))
    text3 = font.render("Move paddle: ARROW KEYS", True, (255,255,255))
    text4 = font.render("Pause: ESC", True, (255,255,255))

    if one_player == False:
        win.blit(text1, (WIDTH//2 - text1.get_width()//2, 450))
        win.blit(text2, (WIDTH//2 - text2.get_width()//2, 480))
        win.blit(text4, (WIDTH//2 - text4.get_width()//2, 510))
    else:
        win.blit(text3, (WIDTH//2 - text3.get_width()//2, 450))
        win.blit(text4, (WIDTH//2 - text4.get_width()//2, 480))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos

            if btn_slow.collidepoint(mx, my):
                game_speed = "slow"
                speed_screen = False
            if btn_medium.collidepoint(mx, my):
                game_speed = "normal"
                speed_screen = False
            if btn_fast.collidepoint(mx, my):
                game_speed = "fast"
                speed_screen = False

    pygame.display.flip()


if game_speed == "slow":
    BALL_SPEED = 10
    PADDLE_SPEED = 12
elif game_speed == "normal":
    BALL_SPEED = 15
    PADDLE_SPEED = 17
elif game_speed == "fast":
    BALL_SPEED = 20
    PADDLE_SPEED = 22

#Direction of ball on x and y axis
dx = 6
dy = random.choice([-0.6, 0.6])

pad_speed = PADDLE_SPEED

p1_score = 0
p2_score = 0
font = pygame.font.Font(None, 60)
ai_error = 0
error_timer = 0

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
        pygame.time.wait(80)  
        continue

    #Get key inputs
    keys = pygame.key.get_pressed()
    
    if one_player:

        if pygame.time.get_ticks() > error_timer:
            error = random.randint(-50,50)
            error_timer = pygame.time.get_ticks() + random.randint(500,1500)

        target_y = ball.centery + error

        if target_y > paddle2.centery:
            if game_speed == "slow":
                paddle2.y += 7
            if game_speed == "normal":
                paddle2.y += 12
            if game_speed == "fast":
                paddle2.y += 19
        if target_y < paddle2.centery:
            if game_speed == "slow":
                paddle2.y -= 7
            if game_speed == "normal":
                paddle2.y -= 12
            if game_speed == "fast":
                paddle2.y -= 19

        if keys[pygame.K_UP]:
            paddle.y -= pad_speed
        if keys[pygame.K_DOWN]:
            paddle.y += pad_speed
    else:    
        if keys[pygame.K_w]:
            paddle.y -= pad_speed
        
        if keys[pygame.K_s]:
            paddle.y += pad_speed
            
        if keys[pygame.K_UP]:
            paddle2.y -= pad_speed

        if keys[pygame.K_DOWN]:
            paddle2.y += pad_speed

    paddle.y = max(0, min(paddle.y, HEIGHT - PADDLE_HEIGHT))
    paddle2.y = max(0, min(paddle2.y, HEIGHT - PADDLE_HEIGHT))
    
    #Move ball in proper direction.
    ball.x += dx
    ball.y += dy

    #If ball hits the top or bottom of the screen, reverse y direction.
    if ball.top <= 0:
        ball.top = 0
        dy = -dy
        wall_sound.play()
    if ball.bottom >= HEIGHT:
        ball.bottom = HEIGHT
        dy = -dy
        wall_sound.play()

    #If ball hits Player 1 paddle.
    if ball.colliderect(paddle):
        dx = BALL_SPEED

        hit_pos = (ball.centery - paddle.centery)
        if game_speed == "fast":
            dy = hit_pos * 0.4
        elif game_speed == "normal":
            dy = hit_pos * 0.3
        else:
            dy = hit_pos * 0.2
       
        paddle_sound.play()


    #If ball hits Player 2 paddle.
    if ball.colliderect(paddle2):
        dx = BALL_SPEED
        dx = -dx

        hit_pos = (ball.centery - paddle2.centery)
        if game_speed == "fast":
            dy = hit_pos * 0.4
        elif game_speed == "normal":
            dy = hit_pos * 0.3
        else:
            dy = hit_pos * 0.2

        paddle_sound.play()

    #If ball goes off screen to either side, add point to appropriate player and reset game.
    if ball.left <= 0:
        p2_score += 1
        score_sound.play()
        dx, dy = reset_game_p1()

    if ball.right >= WIDTH:
        p1_score += 1
        score_sound.play()
        dx, dy = reset_game_p2()


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