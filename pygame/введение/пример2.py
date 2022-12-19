import pygame


def draw_square(screen):
    color = pygame.Color(50, 150, 50)
    # рисуем "тень"
    pygame.draw.rect(screen, color,
                     (20, 20, 100, 100), 0)
    hsv = color.hsva
    # увеличиваем параметр Value, который влияет на яркость
    color.hsva = (hsv[0], hsv[1], hsv[2] + 30, hsv[3])
    # рисуем сам объект(верхний)
    pygame.draw.rect(screen, color, (10, 10, 100, 100), 0)

if __name__ == '__main__':
    pygame.init()
    size = width, height = 130, 130
    screen = pygame.display.set_mode(size) # холст
    draw_square(screen)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()