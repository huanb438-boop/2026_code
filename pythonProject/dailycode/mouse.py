import pyautogui
import pyscreeze
pyautogui.FAILSAFE =False #自动防故障功能
pyautogui.PAUSE = 1    #停顿功能

#获取屏幕分辨率
# print(pyautogui.size())   # 返回所用显示器的分辨率； 输出：Size(width=1920, height=1080)
# width,height = pyautogui.size()
# print(width,height)  # 1920 1080

#移动鼠标
#移动到指定位置
#pyautogui.moveTo(1000,300,duration=1)
#按方向移动
#pyautogui.moveRel(100,500,duration = 4) #第一个参数是左右移动像素值 第二个是上下
#点击鼠标
#pyautogui.click(100,100)  #鼠标点击指定位置 默认左键
#pyautogui.click(100,100,button='right')  #鼠标点击指定位置 设置右键
#pyautogui.click(100,100,button='middle')  #鼠标点击指定位置 设置中间键

# pyautogui.doubleClick(100,100)  # 指定位置，双击左键
# pyautogui.rightClick(100,100)   # 指定位置，双击右键
# pyautogui.middleClick(100,100)  # 指定位置，双击中键

# print(pyautogui.position())  #Point(x=4081, y=116)为搜索栏位置

#图像功能
# pyautogui.alert()  >>> alert(text='', title='', button='OK')
#pyautogui.confirm() >>> confirm(text='', title='', buttons=['OK', 'Cancel'])
#pyautogui.prompt(text = 'please input u name' ,title = 'name' ,default = 'No')
#pyautogui.password()  >>> password(text='', title='', default='', mask='*')

#截图功能

# im1 = pyautogui.screenshot()
# im2 = pyautogui.screenshot('my_screenshot.png')  # 捕获并保存到本地
# im3 = pyautogui.screenshot(region=(0,0, 300, 400))  # 捕获指定范围

# import time
#
# while True:
#     # 本页存在指定图标
#     if pyautogui.locateOnScreen('my_screenshot.png'):
#         time.sleep(0.5)  # 等待 0.5 秒
#         position = pyautogui.center(pyautogui.locateOnScreen('my_screenshot.png'))  # 寻找图标的中心
#         pyautogui.click(position)  # 点击
#     # 本页不存在指定图标
#     else:
#         pyautogui.scroll(-500)  # 滚动鼠标，进入下一页

# 案例获取鼠标的位置，方便复制我们定位的鼠标坐标点到代码中
# import pyautogui
# import time
#
#
# # 获取鼠标位置
# def get_mouse_positon():
#     time.sleep(5)  # 准备时间
#     print('开始获取鼠标位置')
#     try:
#         for i in range(10):
#             # Get and print the mouse coordinates.
#             x, y = pyautogui.position()
#             positionStr = '鼠标坐标点（X,Y）为：{},{}'.format(str(x).rjust(4), str(y).rjust(4))
#             pix = pyautogui.screenshot().getpixel((x, y))  # 获取鼠标所在屏幕点的RGB颜色
#             positionStr += ' RGB:(' + str(pix[0]).rjust(3) + ',' + str(pix[1]).rjust(3) + ',' + str(pix[2]).rjust(
#                 3) + ')'
#             print(positionStr)
#             time.sleep(0.5)  # 停顿时间
#     except:
#         print('获取鼠标位置失败')
#
#
# if __name__ == "__main__":
#     get_mouse_positon()

#pyautogui.dragTo(100,300,duration = 1) 控制鼠标拖动￥
# 键盘输入函数
# pyautogui.keyDown('shift')    # 按下shift
# pyautogui.press('4')    # 按下 4
# pyautogui.keyUp('shift')   # 释放 shift

#模拟快捷键
# pyautogui.keyDown('ctrl')
# pyautogui.keyDown('c')
# pyautogui.keyUp('c')
# pyautogui.keyUp('ctrl')

# pyautogui.hotkey('ctrl','c')
# for i in range(2):  # 画正方形
#     pyautogui.moveTo(200, 200, duration=1)
#     pyautogui.moveTo(200, 400, duration=1)
#     pyautogui.moveTo(400, 400, duration=0.5)
#     pyautogui.moveTo(400, 200, duration=2)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Zhang Kai time:

# import pyautogui
# import time
#
# try:
#     while True:
#         x,y = pyautogui.position()
#         posi = 'x:' + str(x).rjust(4) + ' y:' + str(y).rjust(4)
#         print('\r',posi,end='')
#         time.sleep(0.5)
#
# except KeyboardInterrupt:
#     print('\n已退出！')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Zhang Kai

# import pyautogui
# import time
#
#
# def zan():
#     time.sleep(0.5)    # 等待 0.5 秒
#     left, top, width, height = pyautogui.locateOnScreen('20220117023149.png')   # 寻找 点赞图片；
#     center = pyautogui.center((left, top, width, height))    # 寻找 图片的中心
#     pyautogui.click(center)    # 点击
#     print('点赞成功！')
#
#
# while True:
#     if pyautogui.locateOnScreen('20220117023149.png'):
#         zan()   # 调用点赞函数
#     else:
#         pyautogui.scroll(-500)    # 本页没有图片后，滚动鼠标；
#         print('没有找到目标，屏幕下滚~')
# import time
# import pyautogui
# import keyboard
#
# a = int(input("点击次数："))
# b = float(input("点击间隔/s："))
# c = float(input("请输入您将鼠标移动至指定位置所需的时间:"))
#
# while c >= 0:
#     print(c, "s内将鼠标移动至指定位置")
#     time.sleep(1)
#     c -= 1
#
# z = pyautogui.position()
#
# print("开始运行")
# print("点击esc可以退出")
#
# while a > 0:
#     pyautogui.click(z[0], z[1])
#     a -= 1
#    # time.sleep(0.1)
#     if keyboard.is_pressed('esc'):
#         break
# 改进版
import pyautogui as pag
from time import sleep, time

pag.PAUSE = 0


def mouse():
    b = input('请问您需要点击多少下？')
    b = int(b)
    c = input('点击时需要左键还是右键？\n左键请输入0，右键输入1：')
    c = int(c)
    print('请注意：您需要在8秒内将鼠标移动到您需要连点的地方，然后不要动，等待开始快速连点。')
    sleep(8)
    print('开始点击！')
    x, y = pag.position()
    d = 'left'
    if c:
        d = 'right'
    e = time()
    for i in range(0, b):
        pag.click(x, y, button=d)
    f = time() - e
    input('完成。用时%f秒。' % f)


def key():
    print('请在以下支持的按键中挑选您需要的键。')
    for i in pag.KEYBOARD_KEYS:
        print(r'%s' % i, end=' ')
    b = input('\n请输入您需要快速输入的字符：')
    if b in pag.KEYBOARD_KEYS:
        c = input('请输入您需要多少次输入：')
        c = int(c)
        print('请注意，您需要在8秒内切换到需要输入的窗口。')
        sleep(8)
        print('开始工作！')
        e = time()
        for i in range(0, c):
            pag.press(b)
        f = time() - e
        input('完成。用时%f秒。' % f)
    else:
        input('您输入的字符不属于支持字符，请修改。')


try:
    a = input('输入您需要的服务（数字）：\n1:快速连点\n2:快速输入\n>>> ')
    a = int(a)
    if a == 1:
        mouse()
    elif a == 2:
        key()
    else:
        input('不好意思，没有找到您需要的服务。\n')
except Exception as e:
    print('错误；\n', e)
