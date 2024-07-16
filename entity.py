import pygame as pg

class Entity:
    def __init__(self, sprite: pg.Surface, rect: pg.Rect) -> None:
        self.sprite = sprite
        self.rect = rect

    def render_to(self, surf: pg.Surface):
        surf.blit(self.sprite, self.rect)

class Player(Entity):
    PLAYER_HEIGHT = 50
    PLAYER_WIDTH = 50
    def __init__(self, tlc: list[float]) -> None:
        sprite = pg.image.load("assets/player_stationary.png")
        rect = sprite.get_rect().move(tlc)
        super().__init__(sprite, rect)
