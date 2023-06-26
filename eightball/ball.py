import pygame

class Ball:
    WHITE =     (255, 255, 255)
    BLUE =      (  0,   0, 255)
    GREEN =     (  0, 255,   0)
    RED =       (255,   0,   0)

    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.v_x = 100
        self.v_y = 100

    def move(self,dt):
        self.x += round(dt * self.v_x)
        self.y += round(dt * self.v_y)

    def draw(self):
        pygame.draw.circle(self.screen, self.RED, (self.x,self.y), 50)