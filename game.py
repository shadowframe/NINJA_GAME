import sys
import pygame

pygame.init()

<<<<<<< HEAD
pygame.display.set_caption('ninja game')
=======
>>>>>>> d4df46a801ce42b97997beafa445d1b237588673
screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)
