import pygame
import math
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()
logger.info("Program started")

def f(x):
    return math.sin(x)

pygame.init()

w = 600
h = 600

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Draw graph")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill((0, 0, 0))

    for x_pixel in range(w):
        x = (x_pixel - w // 2) / 50  # Scale and center x
        y = f(x)
        y_pixel = h // 2 - int(y * 50)  # Scale and center y
        if 0 <= y_pixel < h:
            screen.set_at((x_pixel, y_pixel), (255, 255, 255))

    pygame.display.flip()

pygame.quit()
