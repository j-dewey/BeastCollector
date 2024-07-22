import pygame as pg
pg.init()

import entity
import error
# to avoid circular imports, specific objects are seperated
# from abstract class declerations
import item
import items
import monster
import projectile
from player import Player
import time

# player movement commands
UP_BUTTON = pg.K_w
DOWN_BUTTON = pg.K_s
LEFT_BUTTON = pg.K_a
RIGHT_BUTTON = pg.K_d
# switch btwn controlling party and player
SWITCH_ACTIVE = pg.K_SPACE
# take active party member out of battle
RECALL_BUTTON = pg.K_r

WIN_WIDTH = 800
WIN_HEIGHT = 600
MAX_FPS = 60

if __name__ == '__main__':
    win = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pg.time.Clock()

    player = Player([400, 300])
    player.add_party_member("fire_dog", pg.Rect([100, 200, 100, 100]), Player.SPEED, items.FireSpawner([100.0, 100.0]))

    while True:
        dt = clock.tick(MAX_FPS) / 1000.0
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                quit()
            # this activates items
            elif ev.type == pg.MOUSEBUTTONDOWN:
                effect = player.activate_item(ev.pos)
                match effect.type:
                    case item.ItemEffectType.SPAWN_PARTY_MEMBER:
                        player.controlling_party = True
                        player.active_party_member = player.party_selected
                    case item.ItemEffectType.SPAWN_PROJECTILE:
                        print('spawning projectile')
            # this is any key press
            elif ev.type == pg.KEYDOWN:
                if ev.key == SWITCH_ACTIVE and player.party_selected > -1:
                    # ^need to ensure that a member is active before switch
                    player.controlling_party = not player.controlling_party
                elif ev.key == RECALL_BUTTON:
                    player.controlling_party = False
                    player.active_party_member = -1

        keys = pg.key.get_pressed()
        player.handle_movement(
            float(keys[RIGHT_BUTTON]) - float(keys[LEFT_BUTTON]),
            float(keys[DOWN_BUTTON]) - float(keys[UP_BUTTON]),
            dt
        )

        win.fill((0, 122, 0))
        player.render_to(win)
        pg.display.flip()
