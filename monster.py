from __future__ import annotations

from entity import Entity
from item import Item, ItemEffect

import pygame as pg

class MonsterList:
    def __init__(self, max: int) -> None:
        self.ents: list[Monster] = []
        self.max = max

    @staticmethod
    def new_with(max: int, ents: list[Monster]) -> MonsterList:
        new = MonsterList(max)
        new.ents = ents[:max]
        return new

    def is_maxed(self) -> bool:
        return len(self.ents) == self.max

class Monster(Entity):
    def __init__(self, name: str, rect: pg.Rect, speed: float, attack: Item) -> None:
        sprite = pg.transform.scale(
            pg.image.load("assets/" + name + ".png"),
            [rect.width, rect.height]
        )
        super().__init__(sprite, rect, speed)
        self._attack = attack

    def attack(self, mpos: list[float]) -> ItemEffect:
        return self._attack.get_effect(mpos)
