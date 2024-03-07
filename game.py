import pygame
import math
import sys
from character import Character
from environment import Environment
from projectile import Projectile

class Game:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("My Game")

        self.character = Character(screen_width, screen_height)
        self.environment = Environment()
        self.projectiles = []

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Left mouse button (shoot)
                start_pos = self.character.get_projectile_start_pos()
                projectile = Projectile(start_pos, self.character.angle, 3)
                self.projectiles.append(projectile)

    def update(self):
        keys = pygame.key.get_pressed()

        # Move character
        self.character.move(keys)

        # Rotate character towards the mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.character.rotate(mouse_x, mouse_y)

        # Move environment
        self.environment.move(keys, 5)

        # Move and remove projectiles
        for projectile in self.projectiles:
            projectile.move()
            if not (0 <= projectile.pos[0] <= self.screen_width and 0 <= projectile.pos[1] <= self.screen_height):
                self.projectiles.remove(projectile)

    def draw(self):
        # Draw the background
        self.screen.fill((255, 255, 255))

        # Draw environment
        for rect in self.environment.rects:
            pygame.draw.rect(self.screen, (0, 0, 0), rect)

        # Draw character
        rotated_points = [(x * math.cos(self.character.angle) - y * math.sin(self.character.angle) + self.character.pos[0],
                           x * math.sin(self.character.angle) + y * math.cos(self.character.angle) + self.character.pos[1])
                          for x, y in [(0, -self.character.size // 2), (-self.character.size // 2, self.character.size // 2),
                                       (self.character.size // 2, self.character.size // 2)]]
        pygame.draw.polygon(self.screen, (0, 0, 0), rotated_points)

        # Draw projectiles
        for projectile in self.projectiles:
            projectile.draw(self.screen)

        # Update the display
        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()

        while True:
            self.handle_events()
            self.update()
            self.draw()

            # Cap the frame rate
            clock.tick(60)
