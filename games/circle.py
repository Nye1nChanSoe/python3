import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 600))
bg_color = (30, 30, 30)
self_color = (0, 200, 0)
pygame.display.set_caption("Flying circle")
fps = 30

clock = pygame.time.Clock()
running = True

while running:
    # 1. Poll Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill(bg_color)
    pygame.draw.circle(screen, self_color, center=(100, 100), radius=10)
    pygame.display.flip()
    clock.tick(fps)

# Clean up
pygame.quit()
sys.exit()