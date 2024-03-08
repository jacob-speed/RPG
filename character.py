from base_entitiy import BaseEntity


# Character Class (Derived from BaseEntity)
class Character(BaseEntity):
    def __init__(self, pos, size, angle=0, hp=100):
        super().__init__(pos, size)
        self.angle = angle
        self.hp = hp

    def update(self):
        pass  # Implement specific logic for characters

    def draw(self, screen):
        pass  # Implement drawing logic for characters

# NPC Class (Derived from Character)
class NPC(Character):
    def __init__(self, pos, size, angle, hp, npc_type):
        super().__init__(pos, size, angle, hp)
        self.npc_type = npc_type

    def update(self):
        pass  # Implement specific logic for NPCs

# Player Class (Derived from Character)
class Player(Character):
    def __init__(self, pos, size, angle, hp, player_type):
        super().__init__(pos, size, angle, hp)
        self.player_type = player_type

    def update(self):
        pass  # Implement specific logic for players
