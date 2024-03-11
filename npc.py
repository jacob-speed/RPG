import math
import random
import pygame
from character import Character


# NPC Class (Derived from Character)
class NPC(Character):
    def __init__(self, pos, size, color, speed, angle, hp, sight, npc_type):
        super().__init__(pos, size, color, speed, angle, hp)
        self.moving = False
        self.agro = False
        self.npc_type = npc_type
        self.anchor_pos = list(pos)
        self.sight = sight
        self.player_pos = (0, 0)

    def move(self):
        if self.agro:
            self.moving = True
            self.angle = self.angle_to_point(self.player_pos)
        if random.random() > 0.98:
            self.moving = not self.moving
            anchor_distance = self.distance_to_point(self.anchor_pos)
            anchor_angle = self.angle_to_point(self.anchor_pos)
            if anchor_distance > 1000:
                self.angle = anchor_angle
            else:
                sd = math.cos((anchor_distance * math.pi) / 1000) * math.pi
                self.angle = (random.gauss(anchor_angle, sd))
        if self.moving:
            self.pos[0] += self.speed * math.sin(self.angle)
            self.pos[1] -= self.speed * math.cos(self.angle)

    def update_position(self, keys, speed, move):
        if move:
            if keys[pygame.K_w]:
                self.pos[1] += speed
                self.anchor_pos[1] += speed
            if keys[pygame.K_s]:
                self.pos[1] -= speed
                self.anchor_pos[1] -= speed
            if keys[pygame.K_a]:
                self.pos[0] += speed
                self.anchor_pos[0] += speed
            if keys[pygame.K_d]:
                self.pos[0] -= speed
                self.anchor_pos[0] -= speed

    def update_agro(self, player):
        self.player_pos = player.pos
        player_distance = self.distance_to_point(self.player_pos)
        if player_distance < self.sight:
            self.agro = True
        elif player_distance > self.sight * 2:
            self.agro = False