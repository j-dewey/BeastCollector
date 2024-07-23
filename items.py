'''
    Here are the actual items. Items also include spell effects for obvious reasons
'''

from _time import FrameCounter
from item import Item, ItemEffect, ItemEffectType
from projectile import Projectile

import pygame as pg

class FireSpawner(Item):
    '''Spawns fire'''
    def __init__(self, scale: list[float]) -> None:
        super().__init__()
        sprite = pg.transform.scale(
            pg.image.load("assets/fire.png"),
            scale
        )
        hitbox = pg.Rect(0, 0, scale[0], scale[1])
        # lives for 0 so it ends when mouse click ends
        # TODO: make this not suck
        self.fire = Projectile(sprite, hitbox, 0.0, [0.0, 0.0], FrameCounter(0))

    def get_effect(self, mpos: list[float]) -> ItemEffect:
        return ItemEffect(ItemEffectType.SPAWN_PROJECTILE, (self.fire))

class PartySpawner(Item):
    '''Spawns a party member when activated'''
    def __init__(self) -> None:
        super().__init__()

    def get_effect(self, mpos: list[float]) -> ItemEffect:
        return ItemEffect(ItemEffectType.SPAWN_PARTY_MEMBER, (mpos))
