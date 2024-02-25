import pygame
import random

pygame.init()

HEIGHT = 400
WIDTH = 800

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
running = True


BLACK = (0,0,0)
WHITE = (255,255,255)

paddle_width = 10
paddle_height = 60
paddle_speed = 5

player_paddle = pygame.Rect(50,70,paddle_width,paddle_height)
opponent_paddle = pygame.Rect(750, 70, paddle_width,paddle_height)


ball_radius = 10
ball_x = WIDTH//2
ball_y = HEIGHT//2
ball_dx = random.choice([-2,2])
ball_dy = random.choice([-2,2])

player_score = 0
opponent_score = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_paddle.y -= paddle_speed
    if keys[pygame.K_s]:
        player_paddle.y += paddle_speed

    if keys[pygame.K_UP]:
        opponent_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN]:
        opponent_paddle.y += paddle_speed


    ball_x += ball_dx
    ball_y += ball_dy


    if ball_x < 0:
        opponent_score += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
    elif ball_x > WIDTH:
        player_score += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2

    
    if ball_y <= 0 or ball_y >= HEIGHT - ball_radius:
        ball_dy *= -1

    if player_paddle.collidepoint(ball_x,ball_y) or opponent_paddle.collidepoint(ball_x,ball_y):
        ball_dx *= -1


    screen.fill(BLACK)

    pygame.draw.rect(screen,WHITE,player_paddle)
    pygame.draw.rect(screen,WHITE,opponent_paddle)
    pygame.draw.circle(screen,WHITE,(ball_x,ball_y), ball_radius)


    font = pygame.font.Font(None, 36)
    player_text = font.render(str(player_score), True, WHITE)
    opponent_text = font.render(str(opponent_score), True, WHITE)
    screen.blit(player_text, (WIDTH//2 - 50, 10))
    screen.blit(opponent_text, (WIDTH//2 + 30, 10))



    pygame.display.flip()
    clock.tick(60)