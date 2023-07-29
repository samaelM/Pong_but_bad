# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/07/29 16:29:03 by marvin            #+#    #+#              #
#    Updated: 2023/07/29 16:29:03 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pygame
from Constant import *
from Wall import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Wall(100, 100, 100, 100)
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pass
    