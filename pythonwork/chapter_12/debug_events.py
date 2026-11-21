"""诊断脚本: 看看 pygame 到底收到了什么事件、输出有没有到终端。

用法:
    1. 运行它
    2. 在弹出的窗口里点几下、按几个键(比如 q、方向键)
    3. 关闭窗口
结果会实时显示在终端, 同时写入同目录下的 debug_log.txt。
"""

import sys

import pygame

log_file = open("debug_log.txt", "w", encoding="utf-8", buffering=1)


def p(msg):
    """同时输出到终端和日志文件"""
    print(msg, flush=True)
    log_file.write(msg + "\n")


p("1. 脚本开始")
ok, fail = pygame.init()
p(f"2. pygame.init() 完成: 成功 {ok} 个模块, 失败 {fail} 个")

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("事件诊断")
p(f"3. 窗口创建完成: 尺寸 {screen.get_size()}, 视频驱动 {pygame.display.get_driver()}")

clock = pygame.time.Clock()
frames = 0
motion_count = 0

while True:
    frames += 1

    for event in pygame.event.get():
        # 鼠标移动事件太多, 只计数不逐条打印
        if event.type == pygame.MOUSEMOTION:
            motion_count += 1
            continue

        p(f"   事件: {event}")

        if event.type == pygame.QUIT:
            p("   收到 QUIT, 程序结束")
            log_file.close()
            sys.exit()

    # 每 60 帧(约 1 秒)打一次心跳, 证明主循环还活着
    if frames % 60 == 0:
        p(f"心跳: 已运行 {frames // 60} 秒, 累计收到的鼠标移动事件 {motion_count} 个")

    screen.fill((135, 206, 235))
    pygame.display.flip()
    clock.tick(60)
