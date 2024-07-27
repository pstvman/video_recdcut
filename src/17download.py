import pyautogui
import time
from datetime import datetime, timedelta

# 确定位置
yes_x, yes_y = 1450, 760

# 安全位置
safe_x, safe_y = 2035, 1420

def select_cloumn(dyc_y, time_long):
    # 第n个栏目
    x, y = 2455, dyc_y
    pyautogui.moveTo(x, y, duration=1)  # 移动到 (100, 200) 位置，持续时间为 1 秒
    pyautogui.click()   # 点击鼠标左键

    pyautogui.moveTo(yes_x, yes_y, duration=1)  # 移动到确定位置
    pyautogui.click()   # 点击鼠标左键

    pyautogui.moveTo(safe_x, safe_y, duration=0.5)  # 移动到安全位置
    pyautogui.click()  # 焦点离开当前界面

    # 等待时长
    time.sleep(60 * time_long / 1.5 + 60)
    # time.sleep(5) # 测试


# # 第5个栏目
# x, y = 2455, 215

# 第17天视频时长
counter_long = [49, 60, 48, 61, 49, 44, 83]    # 每集实际长度
counter = len(counter_long)                     # 集数控制器
o_time = 0
for i in counter_long:
    o_time += i
s_time = o_time / 1.5

now = datetime.now()
ending_time = now + timedelta(minutes=s_time)
print("本次录制范围：全 {} 集。".format(counter), f"原时长 {o_time} 分钟，加速后预计用时 {round(s_time, 2)} 分钟！", "请 %s 后领取大礼包！！" % ending_time.strftime("%H:%M:%S"))

position = [135 + i * 20 for i in range(counter)]
# position1 = list(range(135, 135 + 20 * counter, 20))
# print("或者，本次录制范围：全 {counter} 集", position1

for index, pos_column in enumerate(position):    # i 集数
    print("第%d集位置：%d" % (index+1, pos_column))


# 开始录制
time.sleep(5)   # 程序启动时间
print("\n开始录制:")
for d_y, t_long in zip(position, counter_long):
    print("%s --- 当前位置y：%d, 原视频时长：%d mins" % (now.strftime("%H:%M:%S"), d_y, t_long))
    select_cloumn(d_y, t_long)


