import pygame
from settings import HEIGHT, SPEED


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        ground_image = pygame.image.load('assets/images/ground.png').convert()
        width = ground_image.get_width()
        height = ground_image.get_height()
        self.image = pygame.Surface((2 * width, height))
        self.image.blit(ground_image, (0, 0))
        self.image.blit(ground_image, (width, 0))
        self.rect = self.image.get_rect(bottomleft=(0, HEIGHT))
        self.pos = pygame.Vector2(self.rect.topleft)
    
    def update(self, dt):
        self.pos.x -= SPEED * dt
        if self.rect.centerx <= 0:
            self.pos.x = 0
        self.rect.x = round(self.pos.x)


        