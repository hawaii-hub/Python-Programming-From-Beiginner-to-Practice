import sys


import pygame


class Photo:
    """在蓝色背景上显示一张照片"""

    def __init__(self):
        """初始化窗口, 并添加照片"""
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

#        self.screen = pygame.display.set_mode((1200, 800))

        pygame.key.stop_text_input()          # ← 加这一行
        pygame.display.set_caption("Wangxinru Photo")

        # 天空蓝
        self.bg_color = (135, 206, 235)

        #加载照片,并放到屏幕最中央
        self.image = pygame.image.load('wangxinru.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen.get_rect().center

    

    def run_game(self):
        """开始主循环"""
        while True:
            # 监听事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()


            #每次循环:先绘屏幕, 再画照片, 最后刷新
            self.screen.fill(self.bg_color)
            self.screen.blit(self.image, self.rect)
            pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    photo = Photo()
    photo.run_game()