from gameunit import *


class Hero(Attacker):

    def __init__(self, name):
        self._health = 100
        self._attack = 25
        self._name = name
        self._xp = 0

    def exp(self, _xp):
        self._xp += _xp

    def attack(self, target):
        target._health -= self._attack