import pygame as pg
import sys


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    #爆弾を作る
    bb_img = pg.Surface((20,20)) #黒い正方形を作る
    pg.draw.circle(bb_img,(255,0,0),(10,10),10)#中心に赤い円を描画
    bb_img.set_colorkey((0,0,0))#黒を透過させる
    tmr = 0



    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])#こうかとん画像を900,440の位置にblit(貼り付ける)
        screen.blit(bb_img, [600, 200])
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()