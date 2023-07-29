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
player = Wall(20, 100, 300, 10, 5)
gp = Goal(SCREEN_WIDTH-10, 0, SCREEN_HEIGHT, 10, player, GREEN)
ai = Wall(770, 100, 300, 10, 5)
ga = Goal(0, 0, SCREEN_HEIGHT, 10, ai, RED)
ball = Ball(100, 100, 10, 6)
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
