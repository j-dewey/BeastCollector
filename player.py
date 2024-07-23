import pygame as pg

from entity import Entity
from error import *
from item import Item, ItemEffect
from items import PartySpawner
from monster import MonsterList, Monster

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
        super().__init__(sprite, rect, Player.SPEED)
        self.party = MonsterList(6)
        self.party_selected = 0
        self.active_party_member = -1 # < 0 indicates no member selected
        self.controlling_party = False
        self.inventory: list[Item] = [PartySpawner()]
        self.selected_item = 0

    def add_party_member(self, name: str, rect: pg.Rect, speed: float, attack: Item) -> ErrorObject:
        member = Monster(name, rect, speed, attack)
        if self.party.is_maxed():
            return Error("Attempted Adding to Full Party")
        self.party.ents.append(member)
        return Okay()

    def render_to(self, surf: pg.Surface):
        if self.active_party_member >= 0:
            self.party.ents[self.party_selected].render_to(surf)
        return super().render_to(surf)

    def activate_item(self, mpos: list[float]) -> ItemEffect:
        if self.controlling_party:
            effect = self.party.ents[self.party_selected].attack(mpos)
        else:
            effect = self.inventory[self.selected_item].get_effect(mpos)
        return effect

    def handle_movement(self, x_dir: float, y_dir: float, dt: float) -> None:
        if self.controlling_party:
            speed = self.party.ents[self.party_selected].speed
            dx = x_dir * speed * dt
            dy = y_dir * speed * dt
            self.party.ents[self.party_selected].move(dx, dy)
            return
        dx = x_dir * self.speed * dt
        dy = y_dir * self.speed * dt
        self.move(dx, dy)
