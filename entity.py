from __future__ import annotations
from abc import ABC
from error import Error, ErrorObject, Okay

import pygame as pg

from item import Item, ItemEffect

class Entity:
    def __init__(self, sprite: pg.Surface, rect: pg.Rect, speed: float) -> None:
        self.sprite = sprite
        self.rect = rect
        self.speed = speed

    def render_to(self, surf: pg.Surface):
        surf.blit(self.sprite, self.rect)

    def move(self, dx: float, dy: float):
        self.rect.move_ip(dx, dy)

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
