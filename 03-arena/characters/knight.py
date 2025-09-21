from characters.character import Character

class Knight(Character):
    def attack(self, other):
        damage = self.damage
        from characters.wizard import Wizard
        if isinstance(other, Wizard):
            damage *= 2
        other.receive_damage(damage, self)

    def receive_damage(self, amount, attacker):
        super().receive_damage(amount, attacker)