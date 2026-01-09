import pygame as pg
import numpy as np
import itertools
import random

SOFT_COLORS = [
    (176, 224, 230), (255, 182, 193), (230, 230, 250), (158, 188, 159), (255, 218, 185),
    (251, 206, 177), (245, 255, 250), (204, 204, 255), (247, 231, 206), (255, 228, 225),
    (157, 172, 139), (194, 115, 127), (106, 140, 171), (214, 189, 151), (204, 115, 87),
    (138, 154, 91), (169, 178, 183), (245, 222, 179), (155, 196, 203), (179, 139, 109),
    (70, 130, 180), (205, 92, 92), (143, 188, 143), (237, 135, 45), (216, 191, 216),
    (135, 206, 235), (218, 165, 32), (0, 191, 255), (221, 160, 221), (255, 127, 80),
    (137, 207, 240), (178, 255, 255), (255, 188, 217), (237, 201, 175), (238, 220, 130),
    (208, 144, 111), (200, 162, 200), (232, 190, 172), (188, 212, 230), (230, 190, 138),
    (147, 197, 114), (159, 226, 191), (250, 214, 165), (243, 229, 171), (247, 202, 201),
    (145, 168, 208), (255, 246, 143), (240, 255, 240), (224, 176, 255), (224, 232, 224)
]

pg.init()

screen = pg.display.set_mode((800, 800))
center = ((screen.get_width() / 2), (screen.get_height() / 2))
clock = pg.time.Clock()
dt = 0
gravity = (9.8 ** 2) * dt

class Circle:
    def __init__(self, x, y, color, speed, degrees, rad):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.rad = rad

        radians = np.radians(degrees)
        
        self.vx = np.cos(radians) * self.speed
        self.vy = np.sin(radians) * self.speed
        
        
    def move(self):
        self.x += self.vx
        self.y += self.vy

def handle_wall_collisions(circle):
    if circle.x + circle.rad >= screen.get_width():
        circle.vx *= -1
        circle.x = screen.get_width() - circle.rad
    elif circle.x - circle.rad <= 0:
        circle.vx *= -1
        circle.x = 0 + circle.rad
        
    if circle.y - circle.rad <= 0:
        circle.vy *= -1
        circle.y = 0 + circle.rad
    elif circle.y + circle.rad >= screen.get_height():
        circle.vy *= -1
        circle.y = screen.get_height() - circle.rad
        
def handle_object_collisions(c1, c2):
    p1 = np.array([c1.x, c1.y])
    p2 = np.array([c2.x, c2.y])
    
    collision_vector = p1 - p2
    distance = np.linalg.norm(collision_vector)
    
    if distance == 0:
        c1.x += 1
        c2.y += 1
        return
    
    if distance < (c1.rad + c2.rad):
        normal = collision_vector / distance

        v1 = np.array([c1.vx, c1.vy])
        v2 = np.array([c2.vx, c2.vy])
        
        rel_v = v1 - v2
        v_along_normal = np.dot(rel_v, normal)
        
        if v_along_normal > 0:
            return
        
        b_impulse = v_along_normal * normal
        
        c1.vx -= b_impulse[0]
        c1.vy -= b_impulse[1]
        c2.vx += b_impulse[0]
        c2.vy += b_impulse[1]
        
        overlap = (c1.rad + c2.rad) - distance
        c1.x += normal[0] * overlap / 2
        c1.y += normal[1] * overlap / 2 
        c2.x -= normal[0] * overlap / 2
        c2.y -= normal[1] * overlap / 2    

circles = []

for _ in range(60):
    circles.append(Circle(*center, random.choice(SOFT_COLORS), 10, random.randint(0, 360), 60))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    for i, c1 in enumerate(circles):
        c2 = circles[(i + 1) % len(circles)]
        c1.move()
        # c1.vy += gravity
        handle_wall_collisions(c1)
        # handle_object_collisions(c1, c2)
    
    for c1, c2 in itertools.combinations(circles, 2):
        handle_object_collisions(c1, c2)
        
    
    screen.fill((0, 0, 0))
    
    for c in circles:
        pg.draw.circle(screen, c.color, (c.x, c.y), c.rad)
        
    pg.display.set_caption(str(clock.get_fps()))
    pg.display.flip()
    dt = clock.tick(60) / 1000