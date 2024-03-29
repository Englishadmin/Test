# @Auther : chengx
# @Time   : 2019/7/24 11:07
from wall import Wall
from displayer import Dispalyer
from snake import Snake
from bug import Bug
import time
import threading
import msvcrt


displayer = Dispalyer()  # 创建显示管理对象
wall = Wall()  # 创建墙的对象
snake = Snake()  # 创建蛇的对象
bug = Bug(snake.points)  # 创建虫子

running = True  # 声明在类外的变量，称为全局变量，在整个文件中都能被使用


class InputThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        global running, snake
        while running:
            c = str(msvcrt.getch())  # 输入读取，无需回车
            if c == "b'q'":
                running = False
            elif c == "b'w'":
                snake.set_toward('up')
            elif c == "b's'":
                snake.set_toward('down')
            elif c == "b'a'":
                snake.set_toward('left')
            elif c == "b'd'":
                snake.set_toward('right')


input_thread = InputThread()
input_thread.start()  # 启动子线程，负责输入读取

while running:
    # 蛇动
    death = snake.action(bug,wall.points)
    if death:
        print("小蛇死了！！\n按q键退出\n")
        break

    # 将墙的坐标导入到displayer
    displayer.extend_points(wall.points)
    displayer.extend_points(snake.points)
    displayer.extend_points(bug.point)

    # 绘制图像
    displayer.draw_graphics(snake.score)
    # 清空这一帧数据
    displayer.clear()
    time.sleep(snake.sleep_time)


