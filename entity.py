from __future__ import annotations
import pygame as pg
from error import Error, ErrorObject, Okay

class Entity:
    def __init__(self, sprite: pg.Surface, rect: pg.Rect) -> None:
        self.sprite = sprite
        self.rect = rect

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

class Player(Entity):
    PLAYER_HEIGHT = 50
    PLAYER_WIDTH = 50
    SPEED = 250.0

    def __init__(self, tlc: list[float]) -> None:
        sprite = pg.transform.scale(
            pg.image.load("assets/player_stationary.png"),
            [Player.PLAYER_WIDTH, Player.PLAYER_HEIGHT]
        )
        rect = sprite.get_rect().move(tlc)
        super().__init__(sprite, rect)
        self.party = EntityList(6)
        self.party_selected = -1 # < 0 indicates no member selected

    def add_party_member(self, name: str, rect: pg.Rect) -> ErrorObject:
        member = Monster(name, rect)
        if self.party.is_maxed():
            return Error("Attempted Adding to Full Party")
        self.party.ents.append(member)
        return Okay()

    def render_to(self, surf: pg.Surface):
        if self.party_selected >= 0:
            self.party.ents[self.party_selected].render_to(surf)
        return super().render_to(surf)

class Monster(Entity):
    def __init__(self, name: str, rect: pg.Rect) -> None:
        sprite = pg.transform.scale(
            pg.image.load("assets/" + name + ".png"),
            [rect.width, rect.height]
        )
        super().__init__(sprite, rect)
