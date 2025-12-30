import pygame
import numpy as np

pygame.init()

screen = pygame.display.set_mode((800, 800))
pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
clock = pygame.time.Clock()

# VARIABLES #

dt = 0
angle = 0
angle_x = 0
angle_y = 0
camera_distance = 2
vel_x = 0
vel_y = 0
friction = 0.9
line_thickness = 7
cir_radius = 3

# --------- #

VERTICES = [
    (-0.5, -0.5, -0.5), 
    ( 0.5, -0.5, -0.5), 
    (-0.5,  0.5, -0.5), 
    (-0.5, -0.5,  0.5), 
    ( 0.5,  0.5, -0.5), 
    ( 0.5, -0.5,  0.5), 
    (-0.5,  0.5,  0.5), 
    ( 0.5,  0.5,  0.5), 
]

EDGES = [
    (0, 1), (1, 4), (4, 2), (2, 0),
    (3, 5), (5, 7), (7, 6), (6, 3),
    (0, 3), (1, 5), (4, 7), (2, 6)
]

def rotate(VERTICES):
    rotated_vertices = []
    for v in VERTICES:
        v_y = np.dot(rotation_y, v)
        v_xy = np.dot(rotation_x, v_y)
        v_xyz = np.dot(rotation_z, v_xy)
        rotated_vertices.append(v_xyz)
    return rotated_vertices

def matrix_x(angle):
    matrix = [
        [1, 0, 0],
        [0, np.cos(angle), -np.sin(angle)],
        [0, np.sin(angle), np.cos(angle)]
    ]
    return matrix

def matrix_y(angle):
    matrix = [
        [np.cos(angle), 0, np.sin(angle)],
        [0, 1, 0],
        [-np.sin(angle), 0, np.cos(angle)]
    ]
    return matrix

def matrix_z(angle):
    matrix = [
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ]
    return matrix


def project(matrix):
    POINTS = []
    for mat in matrix:
        x = (mat[0]) / (mat[2] + camera_distance)
        y = (mat[1]) / (mat[2] + camera_distance)
        POINTS.append(((x * pos.x) + pos.x, (y * pos.y) + pos.y))
    return POINTS

def draw_edges(POINTS, line_thickness):
    FACES = []
    for edge in EDGES:
        start = edge[0]
        end = edge[1]
        
        s_point = POINTS[start]
        e_point = POINTS[end]
        
        FACES.append((s_point, e_point))
    
    for face in FACES:
        pygame.draw.line(screen, (255, 0, 0), face[0], face[1], line_thickness)
        
    return FACES

def draw_points(POINTS, radius):
    for point in POINTS:
        pygame.draw.circle(screen, (255, 0, 0), point, radius)
        
POINTS = project(VERTICES)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                camera_distance += 0.1

            elif event.button == 5:
                camera_distance -= 0.1

    
    screen.fill((0, 0, 0))
    
    
    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:
        rel_x, rel_y = pygame.mouse.get_rel()
        print(rel_x, rel_y)
        
        vel_x = rel_x * 0.005
        vel_y = rel_y * 0.005
    else:
        pygame.mouse.get_rel()
        
        vel_x *= friction
        vel_y *= friction
    
    angle_x += vel_x
    angle_y += vel_y
    
    rotation_y = matrix_y(-angle_x)
    rotation_x = matrix_x(angle_y)
    rotation_z = matrix_z(0)
    
    rotated_vertices = rotate(VERTICES)
    
    POINTS = project(rotated_vertices)
    
    draw_edges(POINTS, line_thickness)
    draw_points(POINTS, cir_radius)
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000
            
pygame.quit()

