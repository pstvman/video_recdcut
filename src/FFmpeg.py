#pip install ffmpeg-python

# 命令行范例：
# ffmpeg -i input.mp4 -ss start_time -t duration -c copy output.mp4
# -i input.mp4 指定输入文件。
# -ss start_time 设置开始时间，例如 -ss 00:01:30 表示从 1 分 30 秒开始。
# -t duration 设置持续时间，例如 -t 00:00:45 表示持续 45 秒。 -to 是表示结束时间。注意区别
# -c copy 指示 FFmpeg 尽量保持原始编解码器设置不变，以提高效率。
# output.mp4 是输出文件名。

import ffmpeg
import logging
from mylogger import setup_logging

class FFmpeg:
    def split_video_ffmpeg(self, input_video, start_time, end_time, output_video):
        try:
            # 使用 FFmpeg 进行视频分割
            ffmpeg.input(input_video, ss=start_time, to=end_time).output(output_video, c='copy').run()
            logging.info(f"视频已成功分割并保存到 {output_video}")
        except ffmpeg.Error as e:
            logging.error(f"分割视频时出错: {str(e)}")
            try:
                logging.error(f"解码出错: {e.stderr.decode()}")
            except AttributeError:
                logging.error(f"无法解码：e.stderr 为 None")
        except AttributeError as e:
            logging.error(f"AttributeError: {str(e)}")
        except Exception as ex:
            logging.error(f"其他错误：{str(ex)}")



    def split_video(self, epic_segments, input_video, output_base_path, video_type):
        
        # 循环处理每个片段
        for index, (start_time, end_time) in enumerate(epic_segments):
            # 构建输出文件名
            output_video = f"{output_base_path}{index + 1}{'集-'}{video_type}"
            
            # 调用函数进行视频分割
            self.split_video_ffmpeg(input_video, start_time, end_time, output_video)
        
        logging.info("视频分割任务全部完成，再次感谢您的使用。\n\n\n")


if __name__ == "__main__":
    setup_logging("../log/test.log")
    logging.info(" == FFmpeg单元测试-->")
    # 定义片段的起始时间和结束时间列表（格式为 hh:mm:ss）
    segments = [
            ("00:00:05.000", "00:41:03.666"),   # 第 1 集
            ("00:41:15.666", "01:11:06.333"),   # 第 2 集
            ("01:11:18.333", "01:48:03.000"),   # 第 3 集
            ("01:48:15.000", "02:25:19.000"),   # 第 4 集
            ("02:25:31.000", "02:59:59.000"),   # 第 5 集
            ("03:00:11.000", "03:29:25.000"),   # 第 6 集
            ("03:29:37.000", "04:07:33.000"),   # 第 7 集
            # 添加更多片段的时间范围
        ]
    # 输入视频文件路径
    input_video = "E:\\7DC2-PUB\\9天第.mp4"
    # 定义输出视频文件的基础路径和扩展名
    output_base_path = "E:\\7DC2-PUB\\9天第"
    output_extension = ".mp4"
    
    ff = FFmpeg()
    ff.split_video(segments, input_video, output_base_path, output_extension)
    # 如果速度太慢可以使用多线程或者进程

