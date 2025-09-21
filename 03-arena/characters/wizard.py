from characters.character import Character

class Wizard(Character):
    def attack(self, other):
        damage = self.damage
        from characters.archer import Archer
        if isinstance(other, Archer):
            damage *= 2
        other.receive_damage(damage, self)

    def receive_damage(self, amount, attacker):
        super().receive_damage(amount, attacker)