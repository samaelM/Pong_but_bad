# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Wall.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/07/29 16:40:35 by marvin            #+#    #+#              #
#    Updated: 2023/07/29 16:40:35 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pygame
from Constant import *

class Wall():
    def __init__(self, x, y, height, width, speed):
        self.x = x
        self.y = y
        self.h = height
        self.w = width
        self.score = 0
        self.speed = speed

    def update(self, screen):
        self.y = max(0, min(self.y, SCREEN_HEIGHT - self.h))
        self.rect = pygame.draw.rect(screen, WHITE, (self.x, self.y, self.w, self.h))

    def ai_update(self, screen, ball):
        if (self.y + (self.h)//2) > (ball.y + (ball.h)//2):
            self.y -= self.speed
        elif (self.y + (self.h)//2) < (ball.y + (ball.h)//2):
            self.y += self.speed
        print(self.speed, self.x, self.y)
        self.y = max(0, min(self.y, SCREEN_HEIGHT - self.h))
        self.rect = pygame.draw.rect(screen, WHITE, (self.x, self.y, self.w, self.h))
