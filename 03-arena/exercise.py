from characters.knight import Knight
from characters.archer import Archer
from characters.wizard import Wizard
from logic.battle import battle

if __name__ == "__main__":
    k = Knight("Arthur", health = 100, damage = 20)
    w = Wizard("Merlin", health = 80, damage = 50)
    battle(k, w)