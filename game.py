import pygame
import math
import sys
from base_entitiy import BaseEntity
from environment import EnvironmentElement
from projectile import Projectile
from player import Player
from npc import NPC
from fire_projectile import FireProjectile
from background import Background
from map import Map


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
            'light gray': (224, 224, 224)
        }
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("My Game")
        main_skill = FireProjectile("main", (10, 10), self.color["black"], 10, 15)
        sec_skill = FireProjectile("secondary", (100, 200), self.color["yellow"], 50, 1)
        self.player = Player((screen_width//2, screen_height//2),
                             (60, 60),
                             self.color["magenta"],
                             3,
                             [main_skill, sec_skill],
                             0,
                             100)
        self.entities = [
            Background((self.screen_width//2, self.screen_height//2), (screen_width, screen_height), self.color["light gray"], "test"),
            self.player
        ]

    # def create_projectile(self):
    #     pos = self.player.pos()
    #     angle = self.player.angle_to_point(pygame.mouse.get_pos())
    #     pos = (pos[0] + math.cos(angle) * 45, pos[1] + math.sin(angle) * 45)
    #     new_projectile = self.player.use_skill()
    #     self.entities.append(new_projectile)

    def draw(self):
        self.screen.fill((255, 255, 255))
        for entity in self.entities:
            entity.draw(self.screen)
        pygame.display.flip()

    def generate_map(self):
        map = Map((-400, -400), 300)
        map.load_tile(1)
        for ele in map.environment_elements:
            self.entities.append(ele)
        for npc in map.mob:
            self.entities.append(npc)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return True

    def run(self):
        clock = pygame.time.Clock()
        self.generate_map()
        while True:
            self.update()
            self.draw()

            clock.tick(60)

    def update(self):
        mouse_clicked = self.handle_events()
        if mouse_clicked:
            skill = self.player.use_skill()
            if isinstance(skill, Projectile):
                self.entities.append(skill)

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
                elif entity.entity_collision_to_type(self.player.speed, self.entities, Projectile):
                    for proj in self.entities:
                        if isinstance(proj, Projectile) and entity.entity_collision(self.player.speed, proj):
                            entity.is_hit(proj.damage)
                if entity.hp <= 0:
                    self.entities.remove(entity)
                entity.update_agro(self.player)
            # handle events for projectiles
            elif isinstance(entity, Projectile):
                if entity.is_beyond_screen(self.screen_width, self.screen_height):
                    self.entities.remove(entity)
                elif entity.entity_collision_to_type(self.player.speed, self.entities, NPC) or entity.entity_collision_to_type(self.player.speed, self.entities, EnvironmentElement):
                    self.entities.remove(entity)
            # handle generic events
            entity.update_pos(self.player.speed, not player_collision)
            entity.move(not npc_collision)

        keys = pygame.key.get_pressed()
        for i in range(pygame.K_0, pygame.K_9 + 1):
            if keys[i]:
                self.player.select_skill(i - pygame.K_0)
