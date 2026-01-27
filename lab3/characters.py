class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def attack_description(self):
        return f"attacks with {self.name} for {self.damage} damage"



class Character:
    def __init__(self, name, special_power):
        self.name = name
        self.special_power = special_power
        self.weapon = None

    def __str__(self):
        return f"I am {self.name}, a {self.__class__.__name__}"


    def equip_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            return f"{self.name} {self.weapon.attack_description()}!"
        return f"{self.name} attacks with bare hands for 5 damage!"


    def get_status(self):
        weapon_info = self.weapon.name if self.weapon else "unarmed"
        return f"{self.name} the {self.__class__.__name__} - Weapon: {weapon_info}"


    def summon_power(self):
        raise NotImplementedError("Subclasses must implement summon_power()")



class Warrior(Character):

    def __init__(self, name):

        super().__init__(name, "Berserker Rage")


    def summon_power(self):

        return f"{self.name} unleashes {self.special_power}! Attack power doubled!"



class Mage(Character):

    def __init__(self, name):

        super().__init__(name, "Arcane Blast")


    def summon_power(self):

        return f"{self.name} channels {self.special_power}! Enemies are stunned!"

class Archer (Character) :
    def __init__ (self, name) :
        super().__init__(name, "Multishot")

    def summon_power(self) :
        return f"{self.name} channels {self.special_power}! Multishot activated!"
    
sword = Weapon("Sword", 20)
staff = Weapon("Staff", 15)
bow = Weapon("Bow", 17)

army = [
    Warrior("Thorin"),
    Mage("Gandalf"),
    Archer("Legolas")
]

army[0].equip_weapon(sword)
army[1].equip_weapon(staff)
army[2].equip_weapon(bow)

for character in army:
    print(character)
    print(character.get_status()) # weapon info
    print(character.summon_power()) # special ability
    print(character.attack()) # normal attack
    print("-" * 40)

print("Weapon Swap")
print(army[2].attack())

army[2].equip_weapon(staff)
print(army[2].attack())

# Equipment is modeled as composition so the weapon can be changed at any time.
# Using inheritence instead would mean we would have to make a subclass for every weapon.