import pygame
import random
from Grid import Grid

# pygame setup
pygame.init()
screen_size = (1280,720)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
running = True

random.seed()
grid = Grid(screen_size, 10)

def playTurn():
    pass

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#13191F")

    # RENDER YOUR GAME HERE
    for row in grid.grid:  # Iterate over rows
        for gridnode in row:  # Iterate over gridnode objects in each row
            gridnode.rect = pygame.Rect(gridnode.xpos, gridnode.ypos, grid.cell_size, grid.cell_size)
            pygame.draw.rect(screen, gridnode.color, gridnode.rect, 0)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()