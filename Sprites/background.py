import pygame
from settings import HEIGHT


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/images/background.png').convert()
        self.rect = self.image.get_rect()