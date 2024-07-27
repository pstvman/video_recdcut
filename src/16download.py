import pyautogui
import time
from datetime import datetime, timedelta
import logging
from mylogger import setup_logging

from Recoder import Recoder
from FFmpeg import FFmpeg


class Player:

    def change_cut_time_format(self, total_seconds):
        # 计算小时、分钟和剩余的秒数
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        milliseconds = int((total_seconds - int(total_seconds)) * 1000)

        # 格式化输出为“时:分:秒.毫秒”的形式
        formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"
        # print(formatted_time)

        return formatted_time
    

    def select_cloumn(self, dyc_y):
        # 确定位置
        yes_x, yes_y = 1450, 760

        # 安全位置
        safe_x, safe_y = 2035, 1420

        # 第n个栏目
        x, y = 2455, dyc_y
        pyautogui.moveTo(x, y, duration=1)              # 移动到 (100, 200) 位置，持续时间为 1 秒
        pyautogui.click()                               # 点击鼠标左键

        pyautogui.moveTo(yes_x, yes_y, duration=0.5)    # 移动到确定位置
        pyautogui.click()                               # 点击鼠标左键

        pyautogui.moveTo(safe_x, safe_y, duration=0.5)  # 移动到安全位置
        pyautogui.click()                               # 焦点离开当前界面


    def main_record(self, eposide, counter_long, flag, record_list):
        video_segments = []         # 返回各集时长分区 
        counter = len(counter_long) # 集数控制器
        interal_time = 10           # 每集间隔时间
        video_speed = 1.5           # 视频加速
        logging.info("第 %d 个专辑录制--->>>" % eposide)

        # 计算专辑总时长
        ori_time = 0
        for i in counter_long:
            ori_time += i
        sum_time = ori_time / video_speed

        # 计算发送通知的具体时间
        post_time = datetime.now() + timedelta(seconds = sum_time + interal_time * counter)
        logging.info("本次录制范围：全 {} 集。原时长 {:.2f} 分钟，加速后预计用时 {:.2f} 分钟！请于 {} 后领取大礼包！！".format(
            counter, ori_time/60, round(sum_time/60, 2), post_time.strftime("%H:%M:%S")))

        # 视频列表
        position = [135 + i * 20 for i in range(counter)]

        for index, pos_column in enumerate(position):    # i 集数
            logging.info("第 %d 集位置：%d" % (index+1, pos_column))

        delay_time = 5          # 首次录制延迟时间
        real_time = 0           # 下一集位移时间
        time.sleep(delay_time)  # 延迟5s启动
        logging.info("启动中，请等待...\n")

        # 开始录制（视频时长从这里开始计算）
        for index, (d_y, t_long) in enumerate(zip(position, counter_long)):
            if index not in record_list:
                continue
            # 计算每集的开始录制时间和结束录制时间，用于后期剪辑
            cut_start_time = delay_time + real_time                 # 当前集剪辑开始时间，延迟便于测试
            cut_end_time = cut_start_time + t_long / video_speed    # 当前集剪辑结束时间，1.5倍加速
            delay_time = 0                                          # 非首集不再延迟，连续录制
            real_time = cut_end_time + 2 + interal_time             # 记录实时位置时间，上次结束时间+移动时间+间隔时间

            # 转换为H:m:s格式
            cut_start = self.change_cut_time_format(cut_start_time)
            cut_end = self.change_cut_time_format(cut_end_time)
            logging.info("当前位置y：%d, 原视频时长：%d mins, 加速后时长：%d mins, 建议剪辑区间：(\"%s\", \"%s\"),   # 第 %d 集" 
                         % (d_y, t_long / 60, t_long / 60 / 1.5, cut_start, cut_end, index+1))
            # 添加当前分区
            video_segments.append((cut_start, cut_end))

            # 开启录制 耗时2s
            self.select_cloumn(d_y)
            logging.info("第 %d 集，开始录制..." % (index+1))
            # 等待本集录制完成
            if flag == "test":
                time.sleep(3)       # 测试
            elif flag == "prod":
                time.sleep(t_long / video_speed)  # 加速后时长(s)
            logging.info("第 %d 集，录制完成..." % (index+1))
            time.sleep(interal_time)

        logging.info("所有内容已录制结束，感谢您的使用。\n")

        # 返回所有分区
        return video_segments


if __name__ == "__main__":
    player = Player()
    setup_logging("../log/app.log")

    # 运行模式 test | prod
    run_method = "prod"
    # 专辑名(day)
    epic = 11
    # 视频时长(s)
    counter_long = [
        60 * 48 + 46,   # 第1集 
        60 * 63 + 17,   # 第2集 
        60 * 47 + 52,   # 第3集 
        60 * 56 + 14,   # 第4集 
        60 * 43 +  9,   # 第5集 
        60 * 35 + 38,   # 第6集       
        60 * 34 +  6,   # 第7集       
        60 * 38 + 49,   # 第8集       
        # 60 * 35 + 44,   # 第9集       
        # 60 * 57 +  1,   # 第10集
        ]
    # 指定需要录制的集数
    record_list = [
        # 0, 
        # 1, 
        # 2, 
        # 3, 
        # 4, 
        5, 
        6,
        7,
        ]
    
    logging.info("当前模式选择为：%s" % (run_method))
    save_path = "E:\\7DC2-PUB\\"    # 保存位置
    save_filename = str(epic) + "天第后3集"
    save_type = ".mp4"

    # 输入视频文件路径
    input_video = save_path + save_filename + save_path
    # 输出视频文件的基础路径
    output_base_path = save_path + save_filename

    if run_method not in ("test", "prod"):
        logging.error("未支持的运行模式，请检查！")
        exit -1

    # 录制前准备
    qq = Recoder()
    qq.run_recoder()
    
    # 开始录制
    segments = player.main_record(epic, counter_long, run_method)

    # 退出录制界面并保存文件
    qq.ext_recoder(save_filename)

    # 剪辑
    cut = FFmpeg()
    # segments = [
    #     ("00:00:03.000", "00:34:23.666"),   # 第 1 集
    #     ("00:35:26.666", "01:13:20.666"),   # 第 2 集
    #     ("01:14:23.666", "01:41:22.333"),   # 第 3 集
    #     ("01:42:25.333", "02:19:37.333"),   # 第 4 集
    #     ("02:20:40.333", "02:47:55.666"),   # 第 5 集
    #     ("02:48:58.666", "03:23:51.333"),   # 第 6 集
    #     ("03:24:54.333", "03:53:44.333"),   # 第 7 集
    #     # 添加更多片段的时间范围
    # ]

    # input_video = "E:\\7DC2-PUB\\15天第.mp4"
    cut.split_video(segments, input_video, output_base_path, save_type)






