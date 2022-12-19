import os
import sys
import random
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print(f"Cannot load image:", name)
        sys.exit()

    if colorkey == -1:
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    image = image.convert_alpha()
    return image


size = width, height = 400, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# создадим группу, содержащую все спрайты
all_sprites = pygame.sprite.Group()

bomb_image = load_image('bomb.png')

for i in range(50):
    # можно сразу создавать спрайты с указанием группы
    bomb = pygame.sprite.Sprite(all_sprites)
    bomb.image = bomb_image
    bomb.rect = bomb.image.get_rect()

    # задаём случайное местоположение бомбочке
    bomb.rect.x = random.randrange(width)
    bomb.rect.y = random.randrange(height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color("white"))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
