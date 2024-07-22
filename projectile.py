import pygame as pg
from _time import Counter

from entity import Entity

class Projectile(Entity):
    def __init__(self, sprite: pg.Surface, rect: pg.Rect, speed: float, direction: list[float], timer: Counter) -> None:
        super().__init__(sprite, rect, speed)
        self.direction = direction
