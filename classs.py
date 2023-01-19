class Hero:
    def __init__(self, name, abyliti):
        self.name = name
        self.abyliti = abyliti


class Hero_super(Hero):
    def __str__(self):
        return f'name is the {self.name}'

    def name_hero(self):
        return f'it is super hero'

