from __future__ import annotations
from abc import ABC
from error import Error, ErrorObject, Okay

import pygame as pg

from item import Item

class Entity:
    def __init__(self, sprite: pg.Surface, rect: pg.Rect, speed: float) -> None:
        self.sprite = sprite
        self.rect = rect
        self.speed = speed

    def render_to(self, surf: pg.Surface):
        surf.blit(self.sprite, self.rect)

    def move(self, dx: float, dy: float):
        self.rect.move_ip(dx, dy)

class EntityList:
    def __init__(self, max: int) -> None:
        self.ents: list[Entity] = []
        self.max = max

    @staticmethod
    def new_with(max: int, ents: list[Entity]) -> EntityList:
        new = EntityList(max)
        new.ents = ents[:max]
        return new

    def is_maxed(self) -> bool:
        return len(self.ents) == self.max

class Monster(Entity):
    def __init__(self, name: str, rect: pg.Rect, speed: float) -> None:
        sprite = pg.transform.scale(
            pg.image.load("assets/" + name + ".png"),
            [rect.width, rect.height]
        )
        super().__init__(sprite, rect, speed)

    def attack(self, mpos: list[float]) -> None:
        pass
