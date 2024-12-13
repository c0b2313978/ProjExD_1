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

        x, y = 0, 0

        if key_lst[pg.K_UP]:
            y += -1
        if key_lst[pg.K_DOWN]:
            y += 1
        if key_lst[pg.K_LEFT]:
            x += -1
        if key_lst[pg.K_RIGHT]:
            x += 1
        else:   # 何もキーを押していない場合は背景画像と同じ速度で左に流れる。
            x -= 1

        kk_rct.move_ip((x, y))


        screen.blit(bg_img, [-(tmr%3200), 0])
        screen.blit(bg_img_inverted, [-(tmr%3200) + 1600, 0])        
        screen.blit(bg_img, [-(tmr%3200) + 3200, 0])
        screen.blit(bg_img_inverted, [-(tmr%3200) + 4800, 0])
        screen.blit(kokaton, kk_rct)

        pg.display.update()
        tmr += 1
        clock.tick(500)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()