import pygame, sys, time
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        pause = False
        fps = 60

        previous_time = time.time()
        while running:
            dt = time.time() - previous_time
            previous_time = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()
                    sys.exit(0)
                self.clock.tick(fps)