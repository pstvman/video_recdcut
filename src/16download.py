import pyautogui
import time
from datetime import datetime, timedelta
import logging


def setup_logging():
    # 配置日志记录
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("../log/test.log", encoding='utf-8'),  # 日志记录到文件
            logging.StreamHandler()  # 日志记录到控制台
        ]
    )


def select_cloumn(dyc_y, time_long):
    # 确定位置
    yes_x, yes_y = 1450, 760

    # 安全位置
    safe_x, safe_y = 2035, 1420

    # 第n个栏目
    x, y = 2455, dyc_y
    pyautogui.moveTo(x, y, duration=1)  # 移动到 (100, 200) 位置，持续时间为 1 秒
    pyautogui.click()   # 点击鼠标左键

    pyautogui.moveTo(yes_x, yes_y, duration=1)  # 移动到确定位置
    pyautogui.click()   # 点击鼠标左键

    pyautogui.moveTo(safe_x, safe_y, duration=0.5)  # 移动到安全位置
    pyautogui.click()  # 焦点离开当前界面

    # 等待时长
    time.sleep(time_long / 1.5 + 60)
    # time.sleep(5) # 测试


def change_cut_time_format(total_seconds):
    # 计算小时、分钟和剩余的秒数
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    milliseconds = int((total_seconds - int(total_seconds)) * 1000)

    # 格式化输出为“时:分:秒.毫秒”的形式
    formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"
    # print(formatted_time)

    return formatted_time


# # 第5个栏目
# x, y = 2455, 215

def main():
    setup_logging()

    # 修改1：专辑名（天）
    eposide = 15    
    # 修改2：视频时长, 传递秒数
    counter_long = [
        60*51+31,   # 第1集 
        60*56+51,   # 第2集 
        60*40+28,   # 第3集 
        60*55+48,   # 第4集 
        60*40+53,   # 第5集 
        60*52+19,   # 第6集       
        60*43+15,   # 第7集       
        # 60*35+44,   # 第8集       
        # 60*35+44,   # 第9集       
        # 60*57+ 1    # 第10集
        ]   
    logging.info("第 %d 个专辑录制--->>>" % eposide)
    counter = len(counter_long)  # 集数控制器

    o_time = 0
    for i in counter_long:
        o_time += i
    s_time = o_time / 1.5

    now = datetime.now()
    ending_time = now + timedelta(seconds=s_time+60*7)
    logging.info("本次录制范围：全 {} 集。原时长 {:.2f} 分钟，加速后预计用时 {:.2f} 分钟！请 {} 后领取大礼包！！".format(counter, o_time/60, round(s_time/60, 2), ending_time.strftime("%H:%M:%S")))

    position = [135 + i * 20 for i in range(counter)]

    for index, pos_column in enumerate(position):    # i 集数
        logging.info("第 %d 集位置：%d" % (index+1, pos_column))

    # 启动延时
    delay_time = 0
    real_time = 0
    time.sleep(delay_time)
    logging.info("启动中，请等待...\n")

    # 开始录制
    logging.info("开始录制:")
    for index, (d_y, t_long) in enumerate(zip(position, counter_long)):
        
        cut_start_time = delay_time + 3 + real_time     # 当前集剪辑开始时间,3s鼠标移动时间
        cut_end_time = cut_start_time + t_long/1.5      # 当前集剪辑结束时间
        real_time = cut_end_time + 60                   # 记录实时位置时间，视频间等待60s
        cut_start = change_cut_time_format(cut_start_time)
        cut_end = change_cut_time_format(cut_end_time)
        # ("00:00:03", "00:32:02"),
        logging.info("%s --- 当前位置y：%d, 原视频时长：%d mins, 加速后时长：%d mins, 建议剪辑区间：(\"%s\", \"%s\"),   # 第 %d 集" % (now.strftime("%H:%M:%S"), d_y, t_long / 60, t_long / 60 / 1.5, cut_start, cut_end, index+1))
        # select_cloumn(d_y, t_long)
    logging.info("录制结束，感谢您的使用。\n\n\n")

if __name__ == "__main__":
    main()



