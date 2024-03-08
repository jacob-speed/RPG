import pygame


# BaseEntity Class
class BaseEntity:
    def __init__(self, pos, size, speed=0):
        self.pos = list(pos)  # Change to list
        self.size = size
        self.speed = speed

    def move(self, keys):
        if keys[pygame.K_w]:
            self.pos[1] -= self.speed
        if keys[pygame.K_s]:
            self.pos[1] += self.speed
        if keys[pygame.K_a]:
            self.pos[0] -= self.speed
        if keys[pygame.K_d]:
            self.pos[0] += self.speed

    def update(self):
        pass  # To be implemented in derived classes

    def draw(self, screen):
        pass  # To be implemented in derived classes
