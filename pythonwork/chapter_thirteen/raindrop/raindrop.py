import sys

import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """表示单个雨滴的图像"""

    def __init__(self, ai_game):
        """初始化雨滴并设置其起始位置"""
        super().__init__()
        self.screen = ai_game.screen

        # 加载雨滴图像并设置其rect属性
        self.image = pygame.image.load('images/raindrop.png')
        self.rect = self.image.get_rect()

        # 每个雨滴最初都在屏幕的左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 储存雨滴的精确水平位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """让雨滴向下落"""
        self.y += 1    # 这就要用 settings 了
        self.rect.y = self.y

class RainPhoto:
    """创建一片雨幕"""        

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        pygame.key.stop_text_input()

        pygame.display.set_caption("raindrop Photo")

        self.raindrops = pygame.sprite.Group()
        self._create_rain()    

    def run_game(self):
        """开始画面的主循环"""
        while True:
            self._check_enevts()
            self.raindrops.update() 
            self._update_raindrops()
            self._update_screen()
            # 每次循环都会时都重绘屏幕
            self.clock.tick(60)

    def _check_enevts(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
    def _create_rain(self):
        """按队列铺满雨滴"""
        raindrop_width, raindrop_height = Raindrop(self).rect.size
        current_y = raindrop_height
        while current_y < (self.screen_height - 3 * raindrop_height):
            current_x = raindrop_width
            while current_x < (self.screen_width - 3 * raindrop_width):
                new_raindrops = Raindrop(self)
                new_raindrops.x = current_x
                new_raindrops.y = current_y
                new_raindrops.rect.x = int(new_raindrops.x)
                new_raindrops.rect.y = int(new_raindrops.y)
                self.raindrops.add(new_raindrops)

                current_x += 3 * raindrop_width

            current_y += 3 * raindrop_height
    def _update_raindrops(self):
        """更新子弹的位置并删除已消失的子弹"""
        # 更新子弹的位置
        self.raindrops.update()

        # 删除已经消失的子弹
        for raindrop in self.raindrops.copy():
            if raindrop.rect.bottom <= 0:
                self.raindrops.remove(raindrop)

    def _update_screen(self):
        """重绘屏幕"""
        self.screen.fill((30, 0, 40))
        self.raindrops.draw(self.screen)
        #让最近绘制的屏幕可见
        pygame.display.flip()



if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = RainPhoto()
    ai.run_game()