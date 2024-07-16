import pygame as pg
pg.init()
import entity

if __name__ == '__main__':
    WIN_WIDTH = 800
    WIN_HEIGHT = 600

    win = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    player = entity.Player([400, 300])

    while True:
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                quit()

        win.fill((0, 122, 0))
        player.render_to(win)
        pg.display.flip()
