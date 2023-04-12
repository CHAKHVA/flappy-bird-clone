import pygame
from Sprites.background import Background
from Sprites.bird import Bird
from Sprites.ground import Ground
from Sprites.pipe import Pipe
from settings import BLACK, FPS, GAP, HEIGHT, WHITE, WIDTH

class Game:
    def __init__(self):
        # Setup
        pygame.init()
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Flappy Bird')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('assets/fonts/FB.woff', 50)

        # Sprites
        self.background = pygame.sprite.GroupSingle(Background())
        self.ground = pygame.sprite.GroupSingle(Ground())
        self.bird = pygame.sprite.GroupSingle(Bird())
        self.pipes = []
        self.scored_pipes = []

        self.pipes.append(Pipe(2 * WIDTH))

        # Helpers
        self.state = 'menu'
        self.started = False
        self.score = 0

    def draw_score(self):
        score = str(self.score)
        score_surface = self.font.render(score, False, WHITE, BLACK)
        self.surface.blit(score_surface, ((WIDTH - score_surface.get_width()) // 2, 20))

    def run(self):
        running = True
        while running:
            dt = self.clock.tick_busy_loop(FPS) / 1000

            self.background.draw(self.surface)


            if self.state == 'playing':
                for pipe in self.pipes:
                    for bird in self.bird.sprites():
                        if pipe.collide(bird):
                            self.__init__()
                        elif bird.rect.right >= pipe.bottom_rect.x + 20 and pipe not in self.scored_pipes:
                            if bird.rect.top > 0:
                                self.score += 1
                                self.scored_pipes.append(pipe)
                            else:
                                self.__init__()
                    pipe.update(dt, self.pipes)
                    pipe.draw(self.surface)
                
                for pipe in self.pipes:
                    if pipe.bottom_rect.x >= GAP - 2 and pipe.bottom_rect.x <= GAP:
                        self.pipes.append(Pipe(WIDTH))
                        break

            events = pygame.event.get()
            for event in events:
                if ((event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0])) and not self.started:
                    self.started = True
                    self.state = 'playing'
                if event.type == pygame.QUIT:
                    running = False

            self.draw_score()

            self.ground.update(dt)
            self.bird.update(dt, self.state)
            
            self.ground.draw(self.surface)
            self.bird.draw(self.surface)

            if pygame.sprite.groupcollide(self.bird, self.ground, False, False):
                self.__init__()

            pygame.display.update()
        
        pygame.quit()

def main():
    game = Game()
    game.run()

if __name__=='__main__':
    main()