import os
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def main():
    size = 400, 300
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('свой курсор')
    all_strites = pygame.sprite.Group()

    cursor_image = load_image('arrow.png')
    cursor = pygame.sprite.Sprite(all_strites)
    cursor.image = cursor_image
    cursor.rect = cursor.image.get_rect()
    pygame.mouse.set_visible(False)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                cursor.rect.topleft = event.pos
        screen.fill(pygame.Color("black"))
        if pygame.mouse.get_focused():
            all_strites.draw(screen)
            pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()