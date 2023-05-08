from random import random, randrange, randint
import time
from colorama import init


init()
from colorama import Fore, Back, Style
"""
Description 3
"""

class Plant:
    def __init__(self, grow=0, life=100, size=0, name=None):
        self.life = life
        self.size = size
        self.name = name
        self.grow = grow

    def give_damage(self):
        if self.life > 50:
            return (randint(0, 40))
        elif self.life < 50:
            return (randint(0, 30))

    def get_damage(self, damage):
        self.life -= damage
        return self.life


class Insects:
    def __init__(self, life=10, name=None):
        self.life = life
        self.name = name

    def give_damage(self):
        if self.life > 50:
            return (randint(0, 40))
        elif self.life < 50:
            return (randint(0, 30))

    def get_damage(self, damage):
        self.life -= int(damage)


if __name__ == '__main__':
    chamomile = Plant(size=0, name='цветок', life=100)
    caterpillar = Insects(life=100, name='гусеница')

    while chamomile.size != 100:
        if chamomile.size < 100:
            chamomile.size = chamomile.size + 1
            time.sleep(0.005)
            print(f"растение выросло на {chamomile.size}%")
        else:
            print("2")

    while chamomile.life > 0 or caterpillar.life > 0:
        if caterpillar.life <= 0:
            print(Fore.LIGHTGREEN_EX + f"{chamomile.name} победил")
            time.sleep(2)
        else:
            time.sleep(2)
            caterpillar.get_damage(chamomile.give_damage())
            print(Fore.GREEN + f"жизни растения: {chamomile.life}")
            
        if chamomile.life <= 0:
            print(Fore.LIGHTRED_EX + f"{caterpillar.name} победила")
            time.sleep(2)
        else:
            time.sleep(2)
            chamomile.get_damage(caterpillar.give_damage())
            print(Fore.RED + f"жизни насекомого: {caterpillar.life}")
