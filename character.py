class Character:

    def __init__(self, name, level = 1, lineage = 'Warrior', hp = 100, mp = 100, 
                 attack = 5, defense = 5, intelligence = 5, agility = 5):
        self.name = name
        self.level = level
        self.lineage = lineage
        self.xp = 0
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.defense = defense
        self.intelligence = intelligence
        self.agility = agility
        self.skill_points = 0


    def basic_attack():
        pass

    def special_attack():
        pass
