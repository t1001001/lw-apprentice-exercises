def battle(c1, c2):
    turn = 0
    while not c1.is_defeated() and not c2.is_defeated():
        print("\n--- Turn", turn + 1, "---")
        if turn % 2 == 0:
            c1.attack(c2)
        else:
            c2.attack(c1)
        turn += 1

    print("\n--- Game Over ---")
    if c1.is_defeated():
        print(f"{c1.name} has been defeated. {c2.name} wins!")
    else:
        print(f"{c2.name} has been defeated. {c1.name} wins!")