# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Goal.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/07/29 19:24:51 by marvin            #+#    #+#              #
#    Updated: 2023/07/29 19:24:51 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pygame
from Constant import *

class Goal():
    def __init__(self, x, y, h, w, wall, color):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.wall = wall
        self.c = color
    def update(self, screen, ball):
        self.rect = pygame.draw.rect(screen, self.c, (self.x, self.y, self.w, self.h))
        if self.rect.colliderect(ball.rect):
            self.wall.score += 1
            ball.reset()