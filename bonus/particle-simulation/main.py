import pygame as pg
import pygame_gui as pgui
import math
import numpy
import random

dt = 0

particles = []

pg.init()

screen_size = (800, 800)
screen = pg.display.set_mode(screen_size)

manager = pgui.UIManager((800, 800))

particle_slider = pgui.elements.UIHorizontalSlider(relative_rect=pg.Rect((10, screen_size[1] - 40), (200, 30)),
                                                   start_value=100,
                                                   value_range=(0, 2000),
                                                   manager=manager
                                                   )

center = (screen_size[0] / 2, screen_size[1] / 2)
clock = pg.time.Clock()
font = pg.font.SysFont("Arial", 20)

def create_particle(x, y, color, size, speed, angle, mode):
    return {
        "x": float(x),
        "y": float(y),
        "rect": pg.Rect(x, y, *size),
        "sx": speed[0],
        "sy": speed[1],
        "angle": math.radians(angle),
        "color": color,
        "mode": mode,
    }

def rectangles_collide(a, b):
    if not (a.right > b.left and
            a.left < b.right and
            a.top < b.bottom and
            a.bottom > b.top):
        return None
    
    overlap_left = a.right - b.left
    overlap_right = b.right - a.left
    overlap_top = a.bottom - b.top
    overlap_bottom = b.bottom - a.top
    
    min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)
    

    if min_overlap == overlap_left:
        return "LEFT"
    if min_overlap == overlap_right:
        return "RIGHT"
    if min_overlap == overlap_top:
        return "TOP"
    if min_overlap == overlap_bottom:
        return "BOTTOM"
    
def update_particles(particle_list, dt):
    screen.fill((0,0,0))
    for p in particle_list:
        vx = p["sx"] * math.cos(p["angle"])
        vy = p["sy"] * math.sin(p["angle"])
        
        p["x"] += vx * dt * 60
        p["y"] += vy * dt * 60
        
        p["rect"].x = p["x"]
        p["rect"].y = p["y"]
        
        if p["rect"].right > screen_size[0]:
            p["sx"] *= -1
            p["rect"].right = screen_size[0]
        elif p["rect"].left < 0:
            p["sx"] *= -1
            p["rect"].left = 0
            
        if p["rect"].top < 0:
            p["sy"] *= -1
            p["rect"].top = 0
        elif p["rect"].bottom > screen_size[1]:
            p["sy"] *= -1
            p["rect"].bottom = screen_size[1]
            
        p["x"], p["y"] = p["rect"].x, p["rect"].y
                
    for i in range(len(particle_list)):
        for j in range(i + 1, len(particle_list)):
            p = particle_list[i]
            obj = particle_list[j]
            
            status = rectangles_collide(p["rect"], obj["rect"])
            
            if status:
                if status == "LEFT":
                    p["rect"].right = obj["rect"].left
                    p["sx"] = abs(p["sx"])
                    obj["sx"] = -abs(obj["sx"])
                elif status == "RIGHT":
                    p["rect"].left = obj["rect"].right
                    p["sx"] = -abs(p["sx"])
                    obj["sx"] = abs(obj["sx"])
                elif status == "TOP":
                    p["rect"].bottom = obj["rect"].top
                    p["sy"] = -abs(p["sy"])
                    obj["sy"] = abs(obj["sy"])
                elif status == "BOTTOM":
                    p["rect"].top = obj["rect"].bottom
                    p["sy"] = abs(p["sy"])
                    obj["sy"] = -abs(obj["sy"])
                
                p["angle"] += 5
                obj["angle"] -= 5
                
                p["x"], p["y"] = p["rect"].x, p["rect"].y
                obj["x"], obj["y"] = obj["rect"].x, obj["rect"].y


    for p in particle_list:
        if p["mode"] == "debug":
            pg.draw.rect(screen, (255, 0, 0), p["rect"])
            pg.draw.circle(screen, (255, 255, 255), p["rect"].center, size)
        elif p["mode"] == "fireflies":
            pg.draw.circle(screen, (190, 150, 100), p["rect"].center, size)
            pg.draw.circle(screen, (255, 255, 255), p["rect"].center, size / 2)
        elif p["mode"] == "glow":
            pg.draw.circle(screen, p["color"], p["rect"].center, size)
            pg.draw.circle(screen, (255, 255, 255), p["rect"].center, size / 2)
        else:
            pg.draw.circle(screen, p["color"], p["rect"].center, size)

    

def spawn_particles(count, size, mode):
    for _ in range(count):
        particles.append(create_particle(*center, color=(random.randrange(0, 255, 40), random.randrange(0, 255, 40), random.randrange(0, 255, 40)), size=(size * 2, size * 2), speed=(random.randint(1, 10), random.randint(1, 10)), angle=random.randrange(0, 360, 15), mode=mode))
    return size

size = spawn_particles(0, 10, mode="fireflies")

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        manager.process_events(event)
        
        if event.type == pgui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_element == particle_slider:
                new_count = int(event.value)
                particles = []
                size = spawn_particles(new_count, 5, mode="debug")
                print(new_count)
        
    screen.fill((0,0,0))
    fps = clock.get_fps()
    fps_text = font.render(f"FPS: {fps:.2f}", True, (255, 255, 255))
    update_particles(particles, dt)
    screen.blit(fps_text, (10, 10))
    
    manager.update(dt)
    manager.draw_ui(screen)
    
    pg.display.flip()
    dt = clock.tick(60) / 1000  
    
pg.quit()
