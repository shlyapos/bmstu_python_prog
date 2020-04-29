# Анимация на pygame

from math import *
from random import *

import pygame
pygame.init()

nice = 1

# Формирование формы облаков
def clouds(coord):
    x = coord[0]
    y = coord[1]
    pygame.draw.circle(screen, white, [x, y], 10, 0)
    
    pygame.draw.circle(screen, white, [x + 85, y], 20, 0)
    pygame.draw.circle(screen, white, [x - 10, y], 10, 0)
    
    pygame.draw.circle(screen, white, [x - 5, y - 5], 10, 0)
    
    pygame.draw.circle(screen, white, [x + 75, y + 1], 20, 0)
    pygame.draw.circle(screen, white, [x + 15, y - 5], 15, 0)
    
    pygame.draw.circle(screen, white, [x + 30, y - 10], 20, 0)
    pygame.draw.circle(screen, white, [x + 60, y - 15], 30, 0)
    pygame.draw.circle(screen, white, [x + 80, y - 10], 10, 0)
    pygame.draw.circle(screen, white, [x + 100, y - 5], 20, 0)
    pygame.draw.circle(screen, white, [x + 85, y - 23], 15, 0)
    
    pygame.draw.circle(screen, white, [x + 115, y - 10], 20, 0)

# Отрисовка предметов в небе
def sky_anim():
    pygame.draw.circle(screen, sun_col, [size[0], 0], 100, 0)
    for i in range(number_of_cloud):
        clouds(positions[i])
        positions[i][0] -= positions[i][2]  # уменьшение x позиции облаков
        if positions[i][0] <= size[0] - (size[0] + 150):
            positions[i][0] = size[0] + 100
            positions[i][1] = randint(0, size[1] // 4)
            positions[i][2] = randint(1, 2)

# Отрисовка предметов на земле и анимация машины
def floor_anim():
    pygame.draw.rect(screen, grass_col,
                     [0, size[1] - 100,
                      size[0], size[1]])
    pygame.draw.rect(screen, road_col,
                     [0, size[1] - 100,
                      size[0], 50])
    pygame.draw.rect(screen, porebrik_col,
                     [0, size[1] - 70,
                      size[0], 20])
    
    for i in range(1):
        car_anim(car_position, car_color[car_position[3]])
        car_wheel_anim(car_position)
        car_position[0] -= car_speed
        car_position[2] += car_speed + 2
        if car_position[0] <= -300:
            car_position[0] = size[0] + 300
            car_position[3] = randint(0, len(car_color) - 1)
    tree_anim()
    
# Анимация колёс у машины
def car_wheel_anim(car_position):
    wheel_size = 31
    half_size = wheel_size // 2
    
    pos_x_surf_wheel = car_position[0] - 200
    pos_y_surf_wheel = car_position[1] - 110

    pos_x2_surf_wheel = car_position[0] - 65
    pos_y2_surf_wheel = car_position[1] - 110
    
    # first wheel
    surf_wheel = pygame.Surface((wheel_size, wheel_size))
    surf_wheel.fill(porebrik_col)
    
    pygame.draw.line(surf_wheel, black,
                     [0, 0],
                     [wheel_size , wheel_size], 5)
    pygame.draw.line(surf_wheel, black,
                     [half_size, 0],
                     [half_size , wheel_size], 3)
    pygame.draw.line(surf_wheel, black,
                     [wheel_size, 0],
                     [0 , wheel_size], 5)
    pygame.draw.line(surf_wheel, black,
                     [0, half_size],
                     [wheel_size , half_size], 3)
    pygame.draw.circle(surf_wheel, porebrik_col, [half_size, half_size], 6)
    pygame.draw.circle(surf_wheel, black, [half_size, half_size], 4)
    
    rot = pygame.transform.rotate(surf_wheel, car_position[2])
    rot_rect = surf_wheel.get_rect(
        center = (pos_x_surf_wheel + (wheel_size - rot.get_size()[0]) / 2,
                  pos_y_surf_wheel + (wheel_size - rot.get_size()[0]) / 2))
    screen.blit(rot, rot_rect)

    pygame.draw.circle(screen, black,
                      [pos_x_surf_wheel,
                       pos_y_surf_wheel], 30, 11)
    
    pygame.draw.circle(screen, porebrik_col,
                      [pos_x_surf_wheel,
                       pos_y_surf_wheel], 23, 7)
    
    # second wheel
    surf_wheel = pygame.Surface((wheel_size, wheel_size))
    surf_wheel.fill(porebrik_col)
    
    pygame.draw.line(surf_wheel, black,
                     [0, 0],
                     [wheel_size , wheel_size], 5)
    pygame.draw.line(surf_wheel, black,
                     [half_size, 0],
                     [half_size , wheel_size], 3)
    pygame.draw.line(surf_wheel, black,
                     [wheel_size, 0],
                     [0 , wheel_size], 5)
    pygame.draw.line(surf_wheel, black,
                     [0, half_size],
                     [wheel_size , half_size], 3)
    pygame.draw.circle(surf_wheel, porebrik_col, [half_size, half_size], 6)
    pygame.draw.circle(surf_wheel, black, [half_size, half_size], 4)
    
    rot = pygame.transform.rotate(surf_wheel, car_position[2])
    rot_rect = surf_wheel.get_rect(
        center = (pos_x2_surf_wheel + (wheel_size - rot.get_size()[0]) / 2,
                  pos_y2_surf_wheel + (wheel_size - rot.get_size()[0]) / 2))
    screen.blit(rot, rot_rect)

    pygame.draw.circle(screen, black,
                      [pos_x2_surf_wheel,
                       pos_y2_surf_wheel], 30, 11)
    
    pygame.draw.circle(screen, porebrik_col,
                      [pos_x2_surf_wheel,
                       pos_y2_surf_wheel], 23, 7)

# Отрисовка кузова машины
def car_anim(car_position, color):
    pygame.draw.rect(screen, color,
                     [car_position[0] - 260, car_position[1] - 155, 240, 48])
    
    x11 = car_position[0] - 230
    y11 = car_position[1] - 155
    
    x12 = car_position[0] - 170
    y12 = car_position[1] - 205
    
    x13 = car_position[0] - 40
    y13 = y12
    
    x14 = car_position[0] - 21
    y14 = y11
    
    pygame.draw.polygon(screen, color,
                        [[x11, y11], [x12, y12],
                        [x13, y13], [x14, y14]])
    pygame.draw.polygon(screen, wind_car_col,
                        [[x11 + 9, y11], [x12 + 4, y12 + 4],
                         [x13 - 4, y13 + 4], [x14 - 5, y14]])
    x_line = x11 + 90
    y_line_start = y12 + 4
    y_line_end = y14
    pygame.draw.line(screen, black, [x_line, y_line_start],
                     [x_line, y_line_end], 3)
    pygame.draw.line(screen, black, [x_line + 94, y_line_start],
                     [x_line + 94, y_line_end], 3)

    pygame.draw.circle(screen, white,
                       [car_position[0] - 252, car_position[1] - 147], 10)
    pygame.draw.circle(screen, red,
                       [car_position[0] - 30, car_position[1] - 147], 10)
    pygame.draw.rect(screen, color,
                     [car_position[0] - 260, car_position[1] - 155, 240, 48], 6)

# Анимация опадания листьев с дерева
def drop_leaves(coord):
    x = coord[0]
    y = coord[1]
    pygame.draw.ellipse(screen, grass_col,
                        [x, y, 14, 11])

# Отрисовка дерева
def tree_anim():
    flag = True
    x_center = size[0] // 4
    pygame.draw.polygon(screen, tree_col,
                        [[x_center - 50, size[1]],
                         [x_center - 30, size[0] - (size[0] + 200)],
                         [x_center + 20, size[0] - (size[0] + 200)],
                         [x_center + 50, size[1]]], 0)
    
    for i in range(number_of_leaves):
        drop_leaves(leaves_positions[i])
        leaves_positions[i][1] += leaves_positions[i][2]
        if flag:
            leaves_positions[i][0] -= 0.4
            flag = False
        else:
            leaves_positions[i][0] += 0.2
            flag= True
            
        if leaves_positions[i][1] >= 500:
            left = randint(0, 1)
            if left:
                leaves_positions[i][0] = randint(0, x_center)
            else:
                leaves_positions[i][0] = randint(x_center, x_center + 193)
            leaves_positions[i][1] = randint(size[1] - 470, size[1] - 460)
            leaves_positions[i][2] = randint(1, 3)
            
    pygame.draw.circle(screen, grass_col,
                       [x_center, size[1] - 330], 100)
    pygame.draw.circle(screen, grass_col,
                       [x_center, size[1] - 470], 195)
    pygame.draw.circle(screen, grass_col,
                       [x_center, size[1] + 230], 300)

size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption('Деревня Хацапедовка')

clock = pygame.time.Clock()

# Случайная генерация облаков на небе
def generate_clouds_pos(number_of_cloud):
    left = number_of_cloud // 2
    positions = list()
    for i in range(left):
        x = randint(0, size[0] // 2)
        y = randint(0, size[1] // 4)
        speed = randint(1, 2)
        positions.append([x, y, speed])

    for i in range(left, number_of_cloud):
        x = randint(size[0] // 2, size[0])
        y = randint(0, size[1] // 4)
        speed = randint(1, 2)
        positions.append([x, y, speed])
        
    return positions

# Случайная генерация листьев
def generate_leaves_pos(number_of_leaves):
    left = number_of_leaves // 2
    center = size[0] // 4
    positions = list()
    for i in range(left):
        x = randint(0, center)
        y = randint((size[1] - 470), (size[1] - 460))
        speed = randint(1, 3)
        positions.append([x, y, speed])

    for i in range(left, number_of_leaves):
        x = randint(center, center + 193)
        y = randint(size[1] - 470, size[1] - 460)
        speed = randint(1, 3)
        positions.append([x, y, speed])

    return positions

# Данные для облаков
number_of_cloud = 9
positions = generate_clouds_pos(number_of_cloud)

# Данные для машины
angle = 0
car_speed = 3
if nice == 1:
    car_x_spawn = size[0] + 2380
else:
    car_x_spawn = size[0] + 300

car_y_spawn = size[1]
car_color = [( 31, 133, 222),
             ( 25, 211,  66),
             (208, 211,  25),
             ( 31, 223, 183),
             ( 39, 173, 204),
             (109,  27, 227),
             (151,  76, 177),
             (255,   0, 255),
             (153, 135,  45)]
j = randint(0, len(car_color) - 1)
car_position = [car_x_spawn, car_y_spawn, angle, j]

# Данные для дерева и падающих листьев
number_of_leaves = 14
leaves_positions = generate_leaves_pos(number_of_leaves)

'''Colors'''
red          = (235,  52,  29)
white        = (255, 255, 255)
black        = (  0,   0,   0)
sky_col      = ( 83, 158, 224)
sun_col      = (239, 231,  70)
car_col      = (228, 228,   2)
road_col     = ( 84,  84,  84)
tree_col     = (152, 111,  54)
grass_col    = ( 42, 158,  57)
porebrik_col = (126, 126, 126)
wind_car_col = (120, 191, 182)

if car_x_spawn != size[0] + 300:
    file_music = 'music.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(file_music)
    pygame.mixer.music.play(-1)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(sky_col)

    sky_anim()
    floor_anim()
            
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
