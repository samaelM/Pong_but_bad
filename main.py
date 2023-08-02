# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/07/29 19:25:29 by marvin            #+#    #+#              #
#    Updated: 2023/07/29 19:25:29 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pygame
from Constant import *
from Wall import *
from Ball import *
from Goal import Goal

pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Wall(2 * BALL_HEIGHT, (SCREEN_HEIGHT // 2) - (WALL_HEIGHT // 2), WALL_HEIGHT, BALL_HEIGHT, WALL_SPEED)
ai = Wall(SCREEN_WIDTH - 3 * BALL_HEIGHT, (SCREEN_HEIGHT // 2) - (WALL_HEIGHT // 2), WALL_HEIGHT, BALL_HEIGHT, 5)
gp = Goal(SCREEN_WIDTH - BALL_HEIGHT, SCREEN_HEIGHT, BALL_HEIGHT, player, GREEN)
ga = Goal(0, SCREEN_HEIGHT, BALL_HEIGHT, ai, RED)
ball = Ball(3 * BALL_HEIGHT, player.y + (player.h // 2), BALL_HEIGHT, BALL_SPEED)
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= player.speed
    elif keys[pygame.K_DOWN]:
        player.y += player.speed
    screen.fill(BLACK)
    player.update(screen)
    ai.ai_update(screen, ball)
    ball.update(screen, player, ai)
    gp.update(screen, ball)
    ga.update(screen, ball)
    score_text = font.render("Score: " + str(player.score), True, WHITE)
    screen.blit(score_text, (10, 10))
    score_text = font.render("Score: " + str(ai.score), True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH-120, 10))
    pygame.display.flip()
    pygame.time.Clock().tick(30)
