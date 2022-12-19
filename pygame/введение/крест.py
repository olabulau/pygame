import pygame
import sys


def draw(screen):
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255), (0, 0), size, 5)
    pygame.draw.line(screen, (255, 255, 255), (0, width), (height, 0), 5)


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
    pygame.quit()