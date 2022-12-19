import pygame
import sys


def draw(screen):
    screen.fill('black')

    pygame.draw.rect(screen, 'red',
                     (1, 1, height - 2, width - 2), 0)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("крест")
    try:
        size = width, height = [int(c) for c in input().split()]
        screen = pygame.display.set_mode(size)
    except Exception:
        print('Неправильный формат ввода')
        sys.exit()

    draw(screen)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
