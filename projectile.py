import pygame as pg

from entity import Entity

class Projectile(Entity):
    def __init__(self, sprite: pg.Surface, rect: pg.Rect, speed: float) -> None:
        super().__init__(sprite, rect, speed)
