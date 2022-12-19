import pygame


size = width, height = 400, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('желтый круг')
running = True
screen.fill(pygame.Color('blue'))
c_width = 0
c_radius = 0
c_exists = False
c_color = pygame.Color('yellow')
plus_r = pygame.USEREVENT + 25
pygame.time.set_timer(plus_r, 1000)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            c_exists = True
            screen.fill(pygame.Color('blue'))
            c_radius = 0
            c_pos = event.pos
            pygame.draw.circle(screen, c_color, c_pos, c_radius, c_width)
        if event.type == plus_r and c_exists:
            c_radius += 1
            pygame.draw.circle(screen, c_color, c_pos, c_radius, c_width)
    pygame.display.flip()

pygame.quit()