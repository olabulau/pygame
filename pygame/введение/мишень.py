import pygame
import sys

COLORS = (pygame.Color('blue'), pygame.Color('red'), pygame.Color('green'))


def main():
    pygame.init()
    pygame.display.set_caption('Мишень')
    try:
        circle_wigth, number = [int(i) for i in input().split()]
    except ValueError:
        print('Неправильный формат ввода')
        return -1
    size = (2 * circle_wigth * number, 2 * circle_wigth * number)
    screen = pygame.display.set_mode(size)
    draw(screen, circle_wigth, number)
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()

def draw(screen, circle_wigth, number):
    circle_radius = circle_wigth * number
    circle_pos = (circle_radius, circle_radius)
    while number > 0:
        pygame.draw.circle(screen, COLORS[number % 3], circle_pos, circle_radius, 0)
        circle_radius -= circle_wigth
        number -= 1


if __name__ == '__main__':
    sys.exit(main())