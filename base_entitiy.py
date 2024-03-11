import pygame
import math


# BaseEntity Class
class BaseEntity:
    def __init__(self, pos, size, color):
        self.pos = list(pos)
        self.size = size
        self.color = color

    def angle_to_point(self, point_pos):
        angle = math.atan2(point_pos[1] - self.pos[1], point_pos[0] - self.pos[0]) + math.pi / 2
        return angle

    def distance_to_point(self, point_pos):
        distance = math.sqrt((self.pos[0] - point_pos[0]) ** 2 + (self.pos[1] - point_pos[1]) ** 2)
        return distance

    def draw(self, screen):
        pass

    def entity_collision(self, player_speed, entity):
        current_pos = self.pos.copy()
        entity_pos = entity.pos.copy()
        self.update_pos(player_speed, True)
        entity.update_pos(player_speed, True)
        self.move(True)
        entity.move(True)
        collisions = False
        if entity != self and isinstance(entity, BaseEntity):
            if pygame.Rect(self.pos[0] - self.size[0] // 2, self.pos[1] - self.size[1] // 2,
                           self.size[0], self.size[1]).colliderect(
                pygame.Rect(entity.pos[0] - entity.size[0] // 2, entity.pos[1] - entity.size[1] // 2,
                            entity.size[0], entity.size[1])):
                collisions = True
        self.pos = current_pos
        entity.pos = entity_pos
        return collisions

    def entity_collision_to_type(self, player_speed, entity_list, entity_type):
        collision = False
        for entity in entity_list:
            if isinstance(entity, entity_type) and self.entity_collision(player_speed, entity):
                collision = True
        return collision

    def move(self, move):
        pass

    def update_pos(self, player_speed, move):
        keys = pygame.key.get_pressed()
        if move:
            if keys[pygame.K_w]:
                self.pos[1] += player_speed
            if keys[pygame.K_s]:
                self.pos[1] -= player_speed
            if keys[pygame.K_a]:
                self.pos[0] += player_speed
            if keys[pygame.K_d]:
                self.pos[0] -= player_speed
