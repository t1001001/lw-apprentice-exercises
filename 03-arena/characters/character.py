class Character:
    def __init__(self, name: str, health: int, damage: int):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, other):
        other.receive_damage(self.damage, self.name) 

    def is_defeated(self):
        return self.health <= 0

    def receive_damage(self, amount, attacker):
        self.health -= amount
        print(f"{attacker.name} attacks {self.name} for {amount} damage. {self.name} now has {self.health} health.")