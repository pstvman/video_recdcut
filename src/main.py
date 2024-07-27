import pyautogui
import time

# 确定位置
yes_x, yes_y = 1450, 760

# 安全位置
safe_x, safe_y = 2035, 1420

def select_cloumn(dyc_y, time_long):
    # 第5个栏目
    x, y = 2455, dyc_y
    pyautogui.moveTo(x, y, duration=1)  # 移动到 (100, 200) 位置，持续时间为 1 秒
    pyautogui.click()   # 点击鼠标左键

    pyautogui.moveTo(yes_x, yes_y, duration=1)  # 移动到确定位置
    pyautogui.click()   # 点击鼠标左键

    pyautogui.moveTo(safe_x, safe_y, duration=0.5)  # 移动到安全位置
    pyautogui.click()  # 焦点离开当前界面

    # 等待时长
    time.sleep(60 * time_long / 1.5)



# 第6个栏目
x, y = 2455, 235
pyautogui.moveTo(x, y, duration=1)  # 移动到 (100, 200) 位置，持续时间为 1 秒

# # 如果你需要双击
# pyautogui.doubleClick()

# # 如果你需要右键点击
# pyautogui.rightClick()

# # 如果你需要中键点击
# pyautogui.middleClick()


# # 获取屏幕尺寸
# screenWidth, screenHeight = pyautogui.size()
# print(f"Screen width: {screenWidth}, Screen height: {screenHeight}")

# # 获取当前鼠标位置
# currentMouseX, currentMouseY = pyautogui.position()
# print(f"Current mouse position: ({currentMouseX}, {currentMouseY})")



# 第5个栏目
x, y = 2455, 215

# 准备时间
time.sleep(5)

# 第5
select_cloumn(215, 60)

# 第6
select_cloumn(235, 60)

# 第7
select_cloumn(255, 48)

# 第8
select_cloumn(275, 74)

# 第9
select_cloumn(295, 66)

# 第10
select_cloumn(315, 60)