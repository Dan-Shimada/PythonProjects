import random

class Enemy:
    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh
        
    def getAtk(self):
        print("Attack dmg ", self.atkl)

    def getHp(self):
        print("Hp is", self.hp)

enemy1 = Enemy(40,49)
enemy1.getAtk()

enemy2 = Enemy(75, 90)
enemy2.getAtk()

'''
playerhp = 260
enemyatkl= 60
enemyatkh = 80


while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30
    
    print("Enemy strikes for ", dmg, "point of dmg. Current hp is, ", playerhp)

    if playerhp > 30:
        continue
    

    print("Your health is low, teleporting to the base")
    break  
'''
