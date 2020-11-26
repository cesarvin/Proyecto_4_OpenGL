import pygame
from pygame.locals import *

from gl import Renderer, Model
import shaders

deltaTime = 0.0

# Inicializacion de pygame
pygame.init()
clock = pygame.time.Clock()
screenSize = (960, 540)
screen = pygame.display.set_mode(screenSize, DOUBLEBUF | OPENGL)

# Inicializacion de nuestro Renderer en OpenGL
r = Renderer(screen)
r.camPosition.z = 1
# r.camPosition.y = 0
r.pointLight.x = 200
r.pointLight.z = 200

r.setShaders(shaders.vertex_shader, shaders.fragment_shader)

r.modelList.append(Model('modelos/Hamster.obj', 'modelos/Hamster.bmp'))



isPlaying = True
while isPlaying:

    # Para revisar si una tecla esta presionada
    keys = pygame.key.get_pressed()

    # Move cam
    if keys[pygame.K_a]:
        r.camPosition.x += 0.2 * deltaTime
    if keys[pygame.K_d]:
        r.camPosition.x -= 0.2 * deltaTime
    if keys[pygame.K_w]:
        r.camPosition.y += 0.2 * deltaTime
    if keys[pygame.K_s]:
        r.camPosition.y -= 0.2 * deltaTime
    if keys[pygame.K_z]:
        r.camPosition.z -= 0.2 * deltaTime        
    if keys[pygame.K_x]:
        r.camPosition.z += 0.2 * deltaTime        
    if keys[pygame.K_UP]:
        r.rx += 25 * deltaTime 
    if keys[pygame.K_DOWN]:
        r.rx -= 25 * deltaTime  
    if keys[pygame.K_LEFT]:
        r.ry += 25 * deltaTime 
    if keys[pygame.K_RIGHT]:
        r.ry -= 25 * deltaTime 
    if keys[pygame.K_y]:
        r.rz += 25 * deltaTime 
    if keys[pygame.K_u]:
        r.rz -= 25 * deltaTime 

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isPlaying = False
        elif ev.type == pygame.KEYDOWN:
            # para revisar en el momento que se presiona una tecla
            if ev.key == pygame.K_1:
                r.filledMode()
            elif ev.key == pygame.K_2:
                r.wireframeMode()
            elif ev.key == pygame.K_ESCAPE:
                isPlaying = False

    # Main Renderer Loop
    r.render()

    pygame.display.flip()
    clock.tick(60)
    deltaTime = clock.get_time() / 1000


pygame.quit()
