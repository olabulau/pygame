import pygame
import sys


def main():
    pygame.init()
    pygame.display.set_caption('шахматная клетка')
    try:
        wight, number = [int(i) for i in input().split()]
        if wight % number != 0:
            print('количестао клеток не кратно размеру окна')
            return
    except ValueError:
        print('неправильный формат ввода')
        return -1

    size = wight, wight
    screen = pygame.display.set_mode(size)
    draw(screen, number)

    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()


def draw(screen, number):
    cell_color = number % 2
    width = screen.get_width()
    square_width = width // number
    for i in range(0, width, square_width):
        for j in range(0, width, square_width):
            square_point = [(i, j), (square_width, square_width)]
            cell_color = (cell_color + 1) % 2
            if not cell_color:
                square_color = pygame.Color('black')
            else:
                square_color = pygame.Color('white')
            pygame.draw.rect(screen, square_color, square_point, 0)
        if number % 2 == 0:
            cell_color += 1


if __name__ == '__main__':
    sys.exit(main())