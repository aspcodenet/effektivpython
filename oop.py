# 1 leta substantiv

import random

# ==========================================
# OOP & Arv (Inheritance)
# ==========================================

class GameCharacter:
    """Basklass för alla spelkaraktärer."""
    
    def __init__(self, name: str):
        self.name = name
        print("GameCharacter created!")

    def act(self):
        print(f"{self.name} does something.")

    def might_level_up(self):
        # Grundklassen gör ingenting vid level up
        pass


class Human(GameCharacter):
    """Ärver från GameCharacter (Human IS-A GameCharacter)."""
    
    def __init__(self, name: str, age: int):
        super().__init__(name)  # Anropar bas-konstruktorn
        self.age = age
        self.level = 1
        self.burp_count = 0  # Räknar rapar i rad
        print("Human created!")

    def might_level_up(self):
        if self.burp_count >= 3:
            self.level += 1
            self.burp_count = 0  # Återställ räknaren
            print(f"{self.name} leveled up to level {self.level}!")

    def act(self):
        actions = ["eats", "drinks", "burps"]
        action = random.choice(actions)

        if action == "burps":
            self.burp_count += 1
        else:
            self.burp_count = 0  # Återställ om handlingen inte var en rap

        print(f"{self.name} {action}")


class Fly(GameCharacter):
    """Ärver från GameCharacter (Fly IS-A GameCharacter)."""
    
    def __init__(self, name: str):
        super().__init__(name)
        print("Fly created!")

    def act(self):
        actions = ["flies", "lands in the food", "buzzes"]
        action = random.choice(actions)
        print(f"Fly {self.name} {action}")

    def might_level_up(self):
        # Flugor går inte upp i level
        pass




# ==========================================
# Main / Gameloop
# ==========================================

def main():
    # Minneshantering som heap/stack, new/delete, shared_ptr och raw pointers 
    # sköts helt automatiskt av Pythons skräpsamlare (Garbage Collector).

    stefan = Human("Stefan", 30)
    kerstin = Human("Kerstin", 28)
    oliver = Human("Oliver", 5)
    fly = Fly("Buzz")

    # Pythons-listor hanterar dynamisk storlek automatiskt (som std::vector)
    characters: list[GameCharacter] = [stefan, kerstin, oliver, fly]

    while True:  # Gameloop
        # Polymorfism: Varje objekt kör sin egen version av act()
        for character in characters:
            character.act()

        for character in characters:
            character.might_level_up()

        input("Press key for next turn (Enter)... ")


if __name__ == "__main__":
    main()