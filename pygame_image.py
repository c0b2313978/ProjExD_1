import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_inverted = pg.transform.flip(bg_img, True, False)
    tmr = 0

    kokaton = pg.image.load("fig/3.png")
    kokaton = pg.transform.flip(kokaton, True, False)

    # 練習8
    kk_rct = kokaton.get_rect()
    kk_rct.center = [300, 200]


    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            kk_rct.move_ip((0, -1))
        if key_lst[pg.K_DOWN]:
            kk_rct.move_ip((0, 1))
        if key_lst[pg.K_LEFT]:
            kk_rct.move_ip((-1, 0))
        if key_lst[pg.K_RIGHT]:
            kk_rct.move_ip((1, 0))

        screen.blit(bg_img, [-(tmr%3200), 0])
        screen.blit(bg_img_inverted, [-(tmr%3200) + 1600, 0])        
        screen.blit(bg_img, [-(tmr%3200) + 3200, 0])
        screen.blit(bg_img_inverted, [-(tmr%3200) + 4800, 0])
        screen.blit(kokaton, kk_rct)
        pg.display.update()
        tmr += 1
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()