import pygame
import math
import sys
from base_entitiy import BaseEntity
from environment import EnvironmentElement
from projectile import Projectile
from player import Player
from npc import NPC


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
        self.player = Player((screen_width//2, screen_height//2), (60, 60), self.color["magenta"], 3, 0, 100)
        self.entities = [
            self.player,
            NPC((400, 400), (60, 60), self.color["red"], 1, 0, 10, 200, "enemy"),
            NPC((500, 400), (60, 60), self.color["red"], 2, 0, 10, 200, "enemy"),
            NPC((400, 500), (60, 60), self.color["red"], 3, 0, 10, 200, "enemy"),
            NPC((500, 500), (60, 60), self.color["red"], 2, 0, 10, 200, "enemy")
        ]

    def create_projectile(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        start_pos = (self.screen_width // 2, self.screen_height // 2)
        angle = math.atan2(mouse_y - self.screen_height // 2, mouse_x - self.screen_width // 2)
        start_pos = (start_pos[0] + math.cos(angle) * 45, start_pos[1] + math.sin(angle) * 45)
        new_projectile = Projectile(start_pos, size=(5, 5), color=(0, 0, 0), angle=angle, speed=15)
        self.entities.append(new_projectile)

    def draw(self):
        self.screen.fill((255, 255, 255))
        for entity in self.entities:
            entity.draw(self.screen)
        pygame.display.flip()

    def generate_map(self):
        self.entities.append(EnvironmentElement((self.screen_width//2 - 1500, self.screen_height//2), (300, 3300), self.color["black"], "rectangle"))
        self.entities.append(EnvironmentElement((self.screen_width//2 + 1500, self.screen_height//2), (300, 3300), self.color["black"], "rectangle"))
        self.entities.append(EnvironmentElement((self.screen_width//2, self.screen_height//2 - 1500), (3300, 300), self.color["black"], "rectangle"))
        self.entities.append(EnvironmentElement((self.screen_width//2, self.screen_height//2 + 1500), (3300, 300), self.color["black"], "rectangle"))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.create_projectile()

    def run(self):
        clock = pygame.time.Clock()
        self.generate_map()
        while True:
            self.handle_events()
            self.update()
            self.draw()

            clock.tick(60)

    def update(self):
        # check if player is colliding with environment
        player_collision = self.player.entity_collision_to_type(self.player.speed, self.entities, EnvironmentElement)
        for entity in self.entities:
            npc_collision = False
            # handle events for NPCs
            if isinstance(entity, NPC):
                if entity.entity_collision_to_type(self.player.speed, self.entities, EnvironmentElement):
                    npc_collision = True
                elif entity.entity_collision_to_type(self.player.speed, self.entities, Player):
                    npc_collision = True
                entity.update_agro(self.player)
            # handle events for projectiles
            if isinstance(entity, Projectile):
                if entity.is_beyond_screen(self.screen_width, self.screen_height):
                    self.entities.remove(entity)
                elif entity.entity_collision_to_type(self.player.speed, self.entities, BaseEntity):
                    self.entities.remove(entity)
            # handle generic events
            entity.update_pos(self.player.speed, not player_collision)
            entity.move(not npc_collision)
