import sys

import pygame
from pygame.sprite import Sprite

import random


class Star(Sprite):
    """一颗星星"""
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen

        #加载图片
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

        # 精确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


class StarSky:
    """铺满星星的夜空"""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        
        #self.screen = pygame.display.set_mode(
        #    (self.settings.screen_width,self.settings.screen_height)
        #)
        pygame.display.set_caption("Star Sky")
        pygame.key.stop_text_input()

        self.stars = pygame.sprite.Group()
        self._create_star()


    def run_game(self):
        """开始游戏的主循环"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self._update_screen()
            # 每次循环都会时都重绘屏幕
            self.clock.tick(60)
                
    def _create_star(self):
        """按队列铺满星星"""
        star_width, star_height = Star(self).rect.size
        for _ in range(30):
            new_star = Star(self)
            new_star.x = random.randint(0, self.screen_width - star_width)
            new_star.y = random.randint(0, self.screen_height - star_height)
            new_star.rect.x = int(new_star.x)
            new_star.rect.y = int(new_star.y)
            self.stars.add(new_star)


    def _update_screen(self):
        """重绘屏幕"""
        self.screen.fill((0, 0, 40))
        self.stars.draw(self.screen)
        #让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    st = StarSky()
    st.run_game()