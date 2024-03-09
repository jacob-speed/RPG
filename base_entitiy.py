import pygame


# BaseEntity Class
class BaseEntity:
    def __init__(self, pos, size, color):
        self.pos = list(pos)
        self.size = size
        self.color = color

    def move(self, keys, speed, move):
        if move:
            if keys[pygame.K_w]:
                self.pos[1] += speed
            if keys[pygame.K_s]:
                self.pos[1] -= speed
            if keys[pygame.K_a]:
                self.pos[0] += speed
            if keys[pygame.K_d]:
                self.pos[0] -= speed

    # Check for collisions with other entities
    def entity_collision(self, keys, speed, entity):
        current_pos = self.pos.copy()
        self.move(keys, speed, True)
        collisions = False
        if entity != self and isinstance(entity, BaseEntity):
            if pygame.Rect(self.pos[0] - self.size[0] // 2, self.pos[1] - self.size[1] // 2,
                           self.size[0], self.size[1]).colliderect(
                pygame.Rect(entity.pos[0] - entity.size[0] // 2, entity.pos[1] - entity.size[1] // 2,
                            entity.size[0], entity.size[1])):
                collisions = True
        self.pos = current_pos
        return collisions

    def update(self):
        pass

    def draw(self, screen):
        pass
