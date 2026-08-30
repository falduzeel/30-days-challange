class Character:
    def __init__(self, name, role, health=100):
        self.name = name
        self.role = role
        self.health = health
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        print(f"Added '{item}' to {self.name}'s inventory.")

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} has taken {amount} damage and is knocked out!")
        else:
            print(f"{self.name} took {amount} damage. Remaining Health: {self.health}")

    def display_status(self):
        print("\n--- Character Details ---")
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Health: {self.health}")
        print(f"Items: {', '.join(self.inventory) if self.inventory else 'Empty'}")
        print("------------------------\n")


if __name__ == "__main__":
    hero = Character(name="Aria", role="Mage", health=120)
    villain = Character(name="Goblin", role="Warrior", health=50)

    hero.display_status()

    hero.add_item("Health Potion")
    hero.add_item("Magic Wand")
    
    hero.take_damage(30)
    
    hero.display_status()