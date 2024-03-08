import pygame
import math
import sys
from environment import EnvironmentElement
from projectile import Projectile
from character import Player, NPC

# Game Class
class Game:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.color = {
            'black': (0, 0, 0),
            'white': (255, 255, 255),
            'red': (255, 0, 0),
            'green': (0, 255, 0),
            'blue': (0, 0, 255),
            'yellow': (255, 255, 0),
            'cyan': (0, 255, 255),
            'magenta': (255, 0, 255),
            'gray': (128, 128, 128),
        }
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("My Game")

        self.entities = [
            EnvironmentElement((100, 100), (50, 50), self.color["black"],"rectangle", math.radians(45)),
            EnvironmentElement((200, 200), (30, 30), self.color["cyan"],"circle"),
            EnvironmentElement((300, 300), (40, 40), self.color["red"],"triangle", math.radians(30)),
            # NPC((400, 400), (60, 60), 0, 100, "enemy"),
            Player((screen_width//2, screen_height//2), (60, 60), self.color["magenta"],1, 0, 100),
        ]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        keys = pygame.key.get_pressed()

        for entity in self.entities:
            entity.move(keys, 1)
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