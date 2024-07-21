from __future__ import annotations
from abc import ABC
from error import Error, ErrorObject, Okay

import pygame as pg

class Entity:
    def __init__(self, sprite: pg.Surface, rect: pg.Rect, speed: float) -> None:
        self.sprite = sprite
        self.rect = rect
        self.speed = speed

    def render_to(self, surf: pg.Surface):
        surf.blit(self.sprite, self.rect)

    def move(self, dx: float, dy: float):
        self.rect.move_ip(dx, dy)
