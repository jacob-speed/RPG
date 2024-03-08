import pygame

class Environment:
    def __init__(self):
        self.rects = [
            pygame.Rect(100, 100, 50, 50),
            pygame.Rect(200, 200, 50, 50),
            pygame.Rect(300, 300, 50, 50),
        ]

    def move(self, keys, speed):
        for rect in self.rects:
            if keys[pygame.K_w]:
                rect.y += speed
            if keys[pygame.K_s]:
                rect.y -= speed
            if keys[pygame.K_a]:
                rect.x += speed
            if keys[pygame.K_d]:
                rect.x -= speed

    def draw(self, screen):
        # Draw environment rectangles
        for rect in self.rects:
            pygame.draw.rect(screen, (0, 0, 0), rect)
