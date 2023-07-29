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

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, height, width):
        super().__init__()
        self.x = x
        self.y = y
        self.h = height
        self.w = width
    def update(self):
        pass
