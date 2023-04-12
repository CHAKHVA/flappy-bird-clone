import pygame
from settings import HEIGHT


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.load_images()
        self.frame = 0
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(midleft=(115, HEIGHT // 2))
        self.pos = pygame.Vector2(self.rect.topleft)
        self.velocity = pygame.Vector2(0, 100)
        self.gravity = 1800

        self.pressed = False
    
    def load_images(self):
        self.images = []
        for i in range(1, 4):
            self.images.append(pygame.image.load(f'assets/images/Bird/bird{i}.png').convert_alpha())

    def get_mask(self):
        return pygame.mask.from_surface(self.image)

    def animate(self, dt):
        self.frame += 10 * dt
        if self.frame >= len(self.images):
            self.frame = 0
        self.image = self.images[int(self.frame)]
    
    def wave(self, dt):
        self.velocity.y += self.gravity * dt
        self.pos.y += self.velocity.y * dt
        self.rect.y = round(self.pos.y)
        if self.rect.y >= HEIGHT // 2 + 30:
            self.velocity.y = -300
    
    def apply_gravity(self, dt):
        self.velocity.y += self.gravity * dt
        self.pos.y += self.velocity.y * dt
        self.rect.y = round(self.pos.y)

    def jump(self, dt):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_SPACE] or pygame.mouse.get_pressed()[0]) and not self.pressed:
            self.velocity.y = -500
            self.pressed = True
        elif not keys[pygame.K_SPACE] and not pygame.mouse.get_pressed()[0]:
            self.pressed = False
    
    def tilt(self, dt):
        angle = -1 * self.velocity.y / 10
        if angle < -90:
            angle = -90
        if angle > 20:
            angle = 20
        self.image = pygame.transform.rotate(self.image, angle)

    def update(self, dt, state):
        if state == 'menu':
            self.wave(dt)
        elif state == 'playing':
            self.animate(dt)
            self.tilt(dt)
            self.apply_gravity(dt)
            self.jump(dt)