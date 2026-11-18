import sys

import pygame

class Sky:
    """管理天空的类"""
    def __init__(self):
        """初始化天空并创建天空资源"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Blue Sky")

        # 天空蓝
        self.bg_color = (135, 206, 235)

    def run_game(self):
        """开始主循环"""
        while True:
            # 监听事件
            for enevt in pygame.event.get():
                if enevt.type == pygame.QUIT:
                    sys.exit()

            #每次循环都重绘屏幕
            self.screen.fill(self.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    sky = Sky()
    sky.run_game()