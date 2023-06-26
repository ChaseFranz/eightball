import pygame, sys, time
from ball import Ball
from subject_handler import SubjectHandler

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.clock = pygame.time.Clock()

        self.ball = Ball(self.screen,100,100)
        self.ball2 = Ball(self.screen,400,300)

        self.subjectHandler = SubjectHandler()
        self.subjectHandler.AddSubject(self.ball)
        self.subjectHandler.AddSubject(self.ball2)

    def update_screen(self):
        self.screen.fill('black')
        self.subjectHandler.draw_subjects()
        pygame.display.update()

    def move_subjects(self,dt):
        self.subjectHandler.move_subjects(dt)

    def run(self):
        running = True
        pause = False
        fps = 60

        # draw screen before starting game loop
        self.update_screen()

        previous_time = time.time()
        while running:
            dt = time.time() - previous_time
            previous_time = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()
                    sys.exit(0)

            self.move_subjects(dt)
            self.update_screen()
            self.clock.tick(fps)