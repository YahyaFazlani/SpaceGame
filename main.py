import pygame
import sys
from pygame.locals import QUIT
import time
import random

pygame.init()

WIDTH = 400
HEIGHT = 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Warriors")

rocket = pygame.image.load("rocket.png")
bullet = pygame.image.load("bullet.png")
asteroid = pygame.image.load("asteroid.png")

rocket = pygame.transform.scale(rocket, [50, 50])
bullet = pygame.transform.scale(bullet, [20, 20])
asteroid = pygame.transform.scale(asteroid, [50, 50])

bullets = []
asteroids = []

rocket_x = WIDTH / 2
rocket_y = HEIGHT / 2

rocket_speed_x = 1.5
rocket_speed_y = 1.5

bullet_speed_y = 5
asteroid_speed_y = 2

for i in range(5):
    asteroids.append([random.randrange(1,400), random.randrange(-150, -50)])

running = True

while running:
    SCREEN.fill([50, 50, 50])
    pygame.event.pump()

    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        rocket_y -= rocket_speed_y
    if key[pygame.K_DOWN]:
        rocket_y += rocket_speed_y
    if key[pygame.K_RIGHT]:
        rocket_x += rocket_speed_x
    if key[pygame.K_LEFT]:
        rocket_x -= rocket_speed_x

    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([rocket_x + rocket.get_width()/4, rocket_y])

    #* Bullets
    # Display and animate bullet
    for b in bullets:
        b[1] -= bullet_speed_y
        SCREEN.blit(bullet, b)

    # Remove if bullet goes out of screen 
    for b in bullets:
        if b[1] < 0:
            bullets.remove(b)

    #* Asteroids
    # Display and animate asteroid
    for a in asteroids:
        a[1] += asteroid_speed_y
        SCREEN.blit(asteroid, a)
    
    # Remove if asteroid goes out of screen
    for a in asteroids:
        if a[1] > 400:
            asteroids.remove(a)
            asteroids.append([random.randrange(1,400), random.randrange(-150, -50)])

    # Remove if bullet hits asteroid
    for b in bullets:
        for a in asteroids:
            if (b[0] >= a[0] and b[0] <= a[0] + asteroid.get_width()) and (b[1] >= a[1] and b[1] <= a[1] + asteroid.get_height()):
                asteroids.remove(a)
                bullets.remove(b)
                asteroids.append([random.randrange(1,400), random.randrange(-150, -50)])

    # Stop game if asteroid collides with player
    for a in asteroids:
        if (rocket_x >= a[0] and rocket_x <= a[0] + asteroid.get_width()) and (rocket_y >= a[1] and rocket_y <= a[1] + asteroid.get_height()):
            print("game over")
            running = False

    SCREEN.blit(rocket, [rocket_x, rocket_y])

    time.sleep(0.01)
    pygame.display.update()
