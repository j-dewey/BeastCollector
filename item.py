import pygame as pg

from abc import ABC, abstractmethod
from enum import Enum
from typing_extensions import Any

'''
    ItemEffect and ItemEffectType determine the behaviour of an item
    when it gets used. The data that is expected from ItemEffect.data
    is dependant on the on the value of ItemEffect.type. Since Python
    has neither real enums nor unions, this has to be ensured by the
    programmer and assumed true at run-time
'''

class ItemEffectType(Enum):
    SPAWN_PARTY_MEMBER = 0
    SPAWN_PROJECTILE = 1

class ItemEffect:
    def __init__(self, type: ItemEffectType, data: Any) -> None:
        self.type = type
        self.data = data

class Item(ABC):
    @abstractmethod
    def get_effect(self, mpos: list[float]) -> ItemEffect: pass

'''
    Here are the actual items. Items also include spell effects for obvious reasons
'''

class FireSpawner(Item):
    '''Spawns fire'''
    def __init__(self, scale: list[float]) -> None:
        super().__init__()
        sprite = pg.transform.scale(
            pg.image.load("assets/fire.png"),
            scale
        )

    def get_effect(self, mpos: list[float]) -> ItemEffect:
        pass

class PartySpawner(Item):
    '''Spawns a party member when activated'''
    def __init__(self, selected_member: int) -> None:
        super().__init__()
        self.selected = selected_member

    def get_effect(self, mpos: list[float]) -> ItemEffect:
        return ItemEffect(ItemEffectType.SPAWN_PARTY_MEMBER, self.selected)
