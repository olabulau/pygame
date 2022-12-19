import pygame


size = width, height = 300, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('перетаскивание')
running = True
r_width = 0
r_x = 0
r_y = 0
s_width = 100
r_color = pygame.Color('green')
r_r = ((r_x, r_y), (s_width, s_width))
x1 = x2 = y1 = y2 = 0
while running:
    screen.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = event.pos
            if (x1 < r_x) or (x1 > r_x + s_width) or (y1 <  r_y) or (y1 > r_y + s_width):
                x1 = y1 = 0
        if event.type == pygame.MOUSEBUTTONUP:
            r_x += x2
            r_y += y2
            x1 = x2 = y1 = y2 = 0
        if event.type == pygame.MOUSEMOTION and x1 > 0:
            x2 = event.pos[0] - x1
            y2 = event.pos[1] - y1
    r_r = ((r_x + x2, r_y + y2), (s_width, s_width))
    pygame.draw.rect(screen, r_color, r_r, r_width)
    pygame.display.flip()
    clock.tick(10)
pygame.quit()