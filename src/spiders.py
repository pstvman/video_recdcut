import sys
import pyautogui
import time
from datetime import datetime, timedelta
import logging
import settings
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

        time1 = time.time()
        logging.info("第 %d 个专辑录制--->>>" % eposide)

        # 计算专辑总时长
        ori_time = 0
        for index, cur_time in enumerate(counter_long):
            if index not in record_list:
                continue
            ori_time += cur_time
        sum_time = ori_time / video_speed

        # 计算发送通知的具体时间
        post_time = datetime.now() + timedelta(seconds = sum_time + interal_time * counter)
        logging.info("本次录制范围：全 {} 集。原时长 {:.2f} 分钟，加速后预计用时 {:.2f} 分钟！请于 {} 后领取大礼包！！".format(
            len(record_list), ori_time/60, round(sum_time/60, 2), post_time.strftime("%H:%M:%S")))

        # 视频列表
        position = [135 + i * 20 for i in range(counter)]

        for index, pos_column in enumerate(position):    # i 集数
            logging.info("第 %d 集位置：%d" % (index+1, pos_column))

        init_time = 0           # 首次录制延迟时间
        real_time = 0           # 下一集起始时间
        move_time = 0
        # time.sleep(init_time)  # 延迟5s启动
        logging.info("启动中，请等待...\n")
        init_time = time.time() - time1
        logging.info("init_time: %.2f s" % (init_time))

        # 开始录制（视频时长从这里开始计算）
        for index, (d_y, t_long) in enumerate(zip(position, counter_long)):
            if index not in record_list:
                continue
            
            move_start_time = time.time()
            # 开启录制
            self.select_cloumn(d_y)
            move_end_time = time.time()     # 录制开始时间
            move_time = move_end_time - move_start_time
            logging.info("move_time: %.2f s" % (move_time))

            # 计算每集的开始录制时间和结束录制时间，用于后期剪辑
            # 每集start_time必须通过实时计算得来
            cut_start_time = init_time + real_time + move_time      # 当前集剪辑开始时间，延迟便于测试+2s移动时间
            cut_end_time = cut_start_time + t_long / video_speed    # 当前集剪辑结束时间，1.5倍加速
            init_time = 0                                           # 非首集不再延迟，连续录制
            # real_time = cut_end_time + interal_time                 # 记录实时位置时间，上次结束时间+间隔时间

            # 转换为H:m:s格式
            cut_start = self.change_cut_time_format(cut_start_time)
            cut_end = self.change_cut_time_format(cut_end_time)
            logging.info("当前位置y：%d, 原视频时长：%d mins, 加速后时长：%d mins, 建议剪辑区间：(\"%s\", \"%s\"),   # 第 %d 集" 
                         % (d_y, t_long / 60, t_long / 60 / 1.5, cut_start, cut_end, index+1))
            # 添加当前分区
            video_segments.append((cut_start, cut_end))
            logging.info("分区列表：\n%s" % (video_segments))

            logging.info("第 %d 集，开始录制..." % (index+1))
            # 等待本集录制完成
            if flag == "test":
                time.sleep(3)       # 测试
            elif flag == "prod":
                time.sleep(t_long / video_speed)  # 加速后时长(s)
            
            time.sleep(interal_time)
            time2 = time.time()
            real_time += time2 - move_start_time
            logging.info("第 %d 集，录制完成..." % (index+1))

        logging.info("所有内容已录制结束，感谢您的使用。\n")

        # 返回所有分区
        return video_segments


if __name__ == "__main__":
    player = Player()
    if len(sys.argv)  < 3:
        print("eg: python spiders.py [test|prod] [epic_num], 参数错误")
        sys.exit(0)
    else:
        run_method, epic = sys.argv[1:3]
        if run_method not in ("test", "prod") or not epic.isdigit():
            print("eg: python spiders.py [test|prod] [epic_num], 参数错误，请检查！")
            sys.exit()

        if run_method == "test":
            setup_logging("../log/test.log")
        elif run_method == "prod":
            setup_logging("../log/app.log")
        logging.info("当前模式选择为：%s" % (run_method))
    
    save_path = settings.save_path
    save_filename = str(epic) + settings.save_filename
    save_type = settings.save_type

    # 输入视频文件路径
    input_video = save_path + save_filename + save_type
    # 输出视频文件的基础路径
    output_base_path = save_path + save_filename


    # 1. 录制前准备
    qq = Recoder()
    qq.run_recoder()
    
    # 2. 开始录制
    segments = player.main_record(int(epic), settings.counter_long, run_method, settings.record_list)

    # 3. 退出录制界面并保存文件
    qq.ext_recoder(save_filename)

    # 4. 剪辑
    cut = FFmpeg()
    cut.split_video(segments, input_video, output_base_path, save_type)



