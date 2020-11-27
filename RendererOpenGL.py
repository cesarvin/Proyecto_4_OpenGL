import pygame
from pygame.locals import *

from gl import Renderer, Model
import shaders
import numpy as np

deltaTime = 0.0

# Inicializacion de pygame
pygame.init()
clock = pygame.time.Clock()
screenSize = (960, 540)
screen = pygame.display.set_mode(screenSize, DOUBLEBUF | OPENGL)

# Inicializacion de nuestro Renderer en OpenGL
r = Renderer(screen)
r.camPosition.z = 1
r.camPosition.y = 0.5
r.pointLight.x = 200
r.pointLight.z = 200
angx = 0
angy = 0
angz = 0



r.setShaders(shaders.vertex_shader, shaders.fragment_shader)

r.modelList.append(Model('modelos/Pikachu.obj', 'modelos/Pikachu.bmp'))

def pikachu():
    pygame.mixer.music.load('sonidos/pikachu.mp3')
    pygame.mixer.music.play(0)

def hamster():
    pygame.mixer.music.load('sonidos/hamster.mp3')
    pygame.mixer.music.play(0) 

def microphone():
    pygame.mixer.music.load('sonidos/microphone.mp3')
    pygame.mixer.music.play(0)

def giraffe_car():
    pygame.mixer.music.load('sonidos/giraffe_car.mp3')
    pygame.mixer.music.play(0)

isPlaying = True
pikachu()
while isPlaying:

    # Para revisar si una tecla esta presionada
    keys = pygame.key.get_pressed()

    # Move cam
    if keys[pygame.K_a]:
        r.camPosition.x += 0.2 * deltaTime
    if keys[pygame.K_d]:
        r.camPosition.x -= 0.2 * deltaTime
    if keys[pygame.K_s]:
        r.camPosition.y += 0.2 * deltaTime
    if keys[pygame.K_w]:
        r.camPosition.y -= 0.2 * deltaTime
    if keys[pygame.K_i]:
        r.camPosition.z -= 0.2 * deltaTime        
    if keys[pygame.K_o]:
        r.camPosition.z += 0.2 * deltaTime        
    if keys[pygame.K_UP]:
        r.rx += 25 * deltaTime 
    if keys[pygame.K_DOWN]:
        r.rx -= 25 * deltaTime  
    if keys[pygame.K_LEFT]:
        r.ry -= 25 * deltaTime 
    if keys[pygame.K_RIGHT]:
        r.ry += 25 * deltaTime 
    if keys[pygame.K_q]:
        r.rz += 25 * deltaTime 
    if keys[pygame.K_e]:
        r.rz -= 25 * deltaTime 

    if keys[pygame.K_c]:
        r.modelList.clear()
        pikachu()
        r.camPosition.z = 1
        r.camPosition.y = 0.5
        r.modelList.append(Model('modelos/Pikachu.obj', 'modelos/Pikachu.bmp'))
    if keys[pygame.K_v]:
        r.modelList.clear()
        hamster()
        r.camPosition.z = 1
        r.camPosition.y = 0
        r.modelList.append(Model('modelos/Hamster.obj', 'modelos/Hamster.bmp'))
    if keys[pygame.K_b]:
        r.modelList.clear()
        microphone()
        r.camPosition.z = 0.3
        r.camPosition.y = -0.1
        r.modelList.append(Model('modelos/Microphone.obj', 'modelos/Microphone.bmp'))
    if keys[pygame.K_n]:
        r.modelList.clear()
        giraffe_car()
        r.camPosition.z = 15
        r.camPosition.y = 2
        r.modelList.append(Model('modelos/Giraffe_Car.obj', 'modelos/Giraffe_Car.bmp'))
    if keys[pygame.K_m]:
        r.modelList.clear()
        r.camPosition.z = 3
        r.camPosition.y = 0
        r.modelList.append(Model('modelos/Model.obj', 'modelos/Model.bmp'))
    
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
        elif ev.type == pygame.MOUSEBUTTONUP:
            r.pointLight.x = -r.pointLight.x
            r.pointLight.y = -r.pointLight.y

    # Main Renderer Loop
    r.render()

    pygame.display.flip()
    clock.tick(60)
    deltaTime = clock.get_time() / 1000


pygame.quit()
