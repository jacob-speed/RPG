import pygame
import math
import sys
from environment import EnvironmentElement, Projectile
from character import Player, NPC

# Game Class
class Game:
    def __init__(self, screen_width, screen_height):
        pygame.init()

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("My Game")

        self.entities = [
            EnvironmentElement((100, 100), (50, 50), "rectangle", math.radians(45)),
            EnvironmentElement((200, 200), (30, 30), "circle"),
            EnvironmentElement((300, 300), (40, 40), "triangle", math.radians(30)),
            NPC((400, 400), (60, 60), 0, 100, "enemy"),
            Player((500, 500), (60, 60), 0, 100, "player"),
            Projectile((600, 600), (10, 10), math.radians(45), 5),
        ]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        keys = pygame.key.get_pressed()

        for entity in self.entities:
            entity.move(keys)
            entity.update()

    def draw(self):
        self.screen.fill((255, 255, 255))

        for entity in self.entities:
            entity.draw(self.screen)

        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()

        while True:
            self.handle_events()
            self.update()
            self.draw()

            clock.tick(60)