from fighter import Fighter
import random

class Samus(Fighter):
    def __init__(self):
        print("samus constructor here")
        super().__init__("Samus", "Metroid", "Human", "Arm cannon", 5,8,8,4)
        self.charged = False
    def special(self,opponent):
        if(self.charged):
            damage = 35
            print(f"{self.name} fired her arm cannon at {opponent.name} and dealt {damage}%!!! WOW!")
            opponent.percentage += damage
            self.charged = False
        else:
            self.charged = True
            print("Samus is charging up her arm cannon!")

class Meta_Knight(Fighter):
    def __init__(self):
        print("meta knight constructor here")
        super().__init__("Meta Knight","Kirby","Ball","Sword",2,6,1,9)
    def special(self, opponent):
        damage = 5
        times = random.randint(5, 10)

        print(f"{self.name} is slashing in a tornado fashion!! Look out he's doing it ")
        for i in range(times):
            print(f"{i+1} times!")
            opponent.percentage += damage
        print(f"{self.name} hit the opponent {times} times! That dealt {damage * times}!! Wowee zowee!")


samus = Samus()
samus.status()

mk = Meta_Knight()

samus.attack(mk)
mk.special(samus)
samus.special(mk)
mk.attack(samus)
samus.special(mk)

samus.status()
mk.status()