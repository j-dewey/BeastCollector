import pygame as pg

from abc import ABC, abstractmethod
from enum import Enum
from typing_extensions import Any

from projectile import Projectile

'''
    ItemEffect and ItemEffectType determine the behaviour of an item
    when it gets used. The data that is expected from ItemEffect.data
    is dependant on the on the value of ItemEffect.type. Since Python
    has neither real enums nor unions, this has to be ensured by the
    programmer and assumed true at run-time
'''


# Having an item contain a defined type which is read in the main loop
# rather than creating subclasses of Item was chosen since item effects
# spill out to other objects rather than being contained to that item
# instance
class ItemEffectType(Enum): # definition of Item.data
    SPAWN_PARTY_MEMBER = 0  # (mouse pos)
    SPAWN_PROJECTILE = 1    # (spawn pos, direction)

class ItemEffect:
    def __init__(self, type: ItemEffectType, data: Any) -> None:
        self.type = type
        self.data = data

class Item(ABC):
    @abstractmethod
    def get_effect(self, mpos: list[float]) -> ItemEffect: pass
