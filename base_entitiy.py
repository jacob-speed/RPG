import pygame


# BaseEntity Class
class BaseEntity:
    def __init__(self, pos, size, speed=0, color=(0, 0, 0)):
        self.pos = list(pos)
        self.size = size
        self.speed = speed
        self.color = color

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
        pass

    def draw(self, screen):
        pass
