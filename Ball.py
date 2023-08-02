# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Ball.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/07/29 17:32:35 by marvin            #+#    #+#              #
#    Updated: 2023/07/29 17:32:35 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pygame
from Constant import *


class Ball:
    def __init__(self, x, y, h, speed):
        self.rect = None
        self.x = x
        self.y = y
        self.s = speed
        self.sy = 0
        self.ox = x
        self.oy = y
        self.os = speed
        self.osy = 0
        self.h = h

    def reset(self):
        self.x = self.ox
        self.y = self.oy
        self.s = self.os
        self.sy = 0

    def update(self, screen, p, a):
        self.s = max(-(1.8 * BALL_HEIGHT), min(self.s, (1.8 * BALL_HEIGHT)))
        self.x += self.s
        if self.y + self.sy < 0 or self.y + self.sy > SCREEN_HEIGHT - self.h:
            self.sy = -self.sy
        self.y += self.sy
        self.rect = pygame.draw.rect(screen, WHITE, (self.x, self.y, self.h, self.h))
        if self.rect.colliderect(p):
            self.s = -self.s * BALL_ACC
            self.sy = -((self.y + self.h // 2) - (p.y + p.h // 2)) * BALL_ANGLE
        elif self.rect.colliderect(a):
            self.s = -self.s * BALL_ACC
            self.sy = -((self.y + self.h // 2) - (a.y + a.h // 2)) * BALL_ANGLE
