'''
    Here are the actual items. Items also include spell effects for obvious reasons
'''

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
        self.fire = Projectile(sprite, hitbox, 0.0, [0.0, 0.0])

    def get_effect(self, mpos: list[float]) -> ItemEffect:
        pass

class PartySpawner(Item):
    '''Spawns a party member when activated'''
    def __init__(self, selected_member: int) -> None:
        super().__init__()
        self.selected = selected_member

    def get_effect(self, mpos: list[float]) -> ItemEffect:
        return ItemEffect(ItemEffectType.SPAWN_PARTY_MEMBER, self.selected)
