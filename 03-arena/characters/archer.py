from characters.character import Character

class Archer(Character):
    def attack(self, other):
        damage = self.damage
        from characters.knight import Knight
        if isinstance(other, Knight):
            damage *= 2
        other.receive_damage(damage, self)

    def receive_damage(self, amount, attacker):
        super().receive_damage(amount, attacker)