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
        self.player = Player((screen_width//2, screen_height//2), (60, 60), self.color["magenta"],3, 0, 100)
        self.entities = [
            self.player,
            EnvironmentElement((100, 100), (50, 50), self.color["black"],"rectangle", math.radians(45)),
            EnvironmentElement((200, 200), (30, 30), self.color["cyan"],"circle"),
            EnvironmentElement((300, 300), (40, 40), self.color["red"],"triangle", math.radians(30)),
            # NPC((400, 400), (60, 60), 0, 100, "enemy"),
        ]


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.create_projectile()

    def create_projectile(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        start_pos = (self.screen_width // 2, self.screen_height // 2)
        angle = math.atan2(mouse_y - start_pos[1], mouse_x - start_pos[0])
        new_projectile = Projectile(start_pos, size=(5, 5), color=(0, 0, 0), angle=angle, speed=10)
        self.entities.append(new_projectile)

    def update(self):
        keys = pygame.key.get_pressed()

        move = True
        for entity in self.entities:
            if entity.player_collision(keys, self.player.speed, self.player):
                move = False

        for entity in self.entities:
            entity.move(keys, self.player.speed, move)
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