import os
import random
import pygame
import PIL
from PIL import ImageFilter

size = width, height = 600, 95
screen = pygame.display.set_mode(size)

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    # if colorkey is not None:
    if colorkey == -1:
            colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
    image = image.convert_alpha()
    return image


class Bomb(pygame.sprite.Sprite):
    image = load_image("car.png")
    '''image_boom = load_image("boom.png")'''

    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = 5
        self.rect.y = 5

    def update(self, *args):
        self.rect = self.rect.move(5,
                                   random.randrange(1))
        if self.rect.x == width:
            car = self.image.filter(ImageFilter.ROTATE180)
            image = load_image(car)
        '''if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom'''


clock = pygame.time.Clock()

# группа, содержащая все спрайты
all_sprites = pygame.sprite.Group()

for i in range(1):
    # нам уже не нужно даже имя объекта!
    Bomb(all_sprites)

running = True
while running:
    all_sprites.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.update(event)
    screen.fill(pygame.Color("white"))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(20)
pygame.quit()