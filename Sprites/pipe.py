import pygame
from random import randint
from settings import HEIGHT, PIPE_GAP, SPEED

class Pipe():
    def __init__(self, x):
        super().__init__()
        self.bottom_pipe = pygame.image.load(f'assets/images/pipe.png').convert_alpha()
        self.top_pipe = pygame.transform.flip(self.bottom_pipe, 0, 1)
        
        top_y = randint(-440, -440 + PIPE_GAP)
        self.bottom_rect = self.bottom_pipe.get_rect(topleft=(x, top_y + 496 + PIPE_GAP))
        self.top_rect = self.top_pipe.get_rect(topleft=(x, top_y))

        self.bottom_pos = pygame.Vector2(self.bottom_rect.topleft)
        self.top_pos = pygame.Vector2(self.top_rect.topleft)
    
    def draw(self, surface):
        surface.blit(self.bottom_pipe, (self.bottom_rect.x, self.bottom_rect.y))
        surface.blit(self.top_pipe, (self.top_rect.x, self.top_rect.y))
    
    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.top_pipe)
        bottom_mask = pygame.mask.from_surface(self.bottom_pipe)

        top_offset = (self.top_rect.x - bird.rect.x, self.top_rect.y - bird.rect.y)
        bottom_offset = (self.bottom_rect.x - bird.rect.x, self.bottom_rect.y - bird.rect.y)
    
        return bird_mask.overlap(top_mask, top_offset) or bird_mask.overlap(bottom_mask, bottom_offset)

    def update(self, dt, pipes):
        self.bottom_pos.x -= SPEED * dt
        self.top_pos.x -= SPEED * dt

        self.bottom_rect.x = round(self.bottom_pos.x)
        self.top_rect.x = round(self.top_pos.x)

        if self.bottom_rect.x <= -self.bottom_rect.width:
            pipes.remove(self)
        