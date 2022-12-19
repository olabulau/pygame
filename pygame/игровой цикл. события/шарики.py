import pygame


size = width, height = 400, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('шарики')
running = True

c_color = pygame.Color('white')
c_radius = 10
circle = []
speed = []
screen2 = pygame.Surface(screen.get_size())
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            circle.append(list(event.pos))
            speed.append([-1, -1])

    screen2.fill(pygame.Color('black'))
    for i in range(len(circle)):
        for ext in (0, 1):
            if circle[i][ext] >= size[ext] - c_radius or circle[i][ext] <= c_radius:
                speed[i][ext] = -speed[i][ext]
            circle[i][ext] += speed[i][ext]
        pygame.draw.circle(screen2, c_color, circle[i], c_radius, 0)
    screen.blit(screen2, (0, 0))
    pygame.display.flip()
    clock.tick(100)
pygame