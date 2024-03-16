from skill import Skill
from projectile import Projectile


# FireProjectile Class
class FireProjectile(Skill):
    def __init__(self, name, size, color, damage, speed):
        super().__init__(name)
        self.size = size
        self.color = color
        self.damage = damage
        self.speed = speed

    def use(self, pos, angle):
        new_projectile = Projectile(pos, self.size, self.color, angle, self.speed)
        return new_projectile
