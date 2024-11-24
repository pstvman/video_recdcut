#pip install ffmpeg-python

# 命令行范例：
# ffmpeg -i input.mp4 -ss start_time -t duration -c copy output.mp4
# -i input.mp4 指定输入文件。
# -ss start_time 设置开始时间，例如 -ss 00:01:30 表示从 1 分 30 秒开始。
# -t duration 设置持续时间，例如 -t 00:00:45 表示持续 45 秒。 -to 是表示结束时间。注意区别
# -c copy 指示 FFmpeg 尽量保持原始编解码器设置不变，以提高效率。
# output.mp4 是输出文件名。


import ffmpeg
from moviepy.editor import VideoFileClip


class FFmpeg:

    # 视频分割
    def video_split(self, input_video, start_time, end_time, output_video):
        try:
            # 使用 FFmpeg 进行视频分割
            ffmpeg.input(input_video, ss=start_time, to=end_time).output(output_video, c='copy').run()
            print(f"视频已成功分割并保存到 {output_video}")
        except ffmpeg.Error as e:
            print(f"分割视频时出错: {e.stderr.decode()}")


    # 竖屏视频裁剪 由于是竖屏，需要计算裁剪的高度以适应横屏电脑
    def video_crop_1080_1920(self, input_file, output_video_file):
        # 竖屏参数
        width = 1080
        height = 1920

        # 调整视频宽高比以适应2560*1440的电脑屏幕
        # width不变，计算新的hegiht
        new_height = int(width * 1440 / 2560)
        print("按16:9裁剪为横屏的宽高比 %d:%d" % (width, new_height))   # (1080, 608)

        # 设置起始裁剪点位置以保存被裁剪的内容包含在新的比例中
        start_y = int((height - new_height) / 2)                # 当视频画面位于正中间，裁剪起始点（0，472）
        start_y = int((height - new_height) / 2 - 266)          # 当视频画面位于正中间上方，裁剪起始点（0，472-266）
        print("裁剪起始位置 (%d, %d) " % (0, start_y))
        
        # 读取视频流
        input_stream = ffmpeg.input(input_file)

        # 应用裁剪滤镜
        # cropped_stream = input_stream.filter_('crop', width, new_height, 0, start_y)
        cropped_stream = input_stream.crop(0, start_y, width, new_height)   # 裁剪起始点x、y,裁剪画面宽、高

        # 获取音频流
        audio_stream = input_stream.audio

        # 设置输出视频参数
        output_stream = ffmpeg.output(cropped_stream, audio_stream, output_video_file)

        # 运行 FFmpeg 命令
        ffmpeg.run(output_stream)
    

    def crop_video_way2(self, input_file, temp_audiofile, output_file, x_start, y_start, width, height):
        
        # 加载视频文件
        clip = VideoFileClip(input_file)

        # 裁剪视频画面
        cropped_clip = clip.crop(x1=x_start, y1=y_start, x2=x_start+width, y2=y_start+height)

        # 保存裁剪后的视频
        cropped_clip.write_videofile(output_file, codec="libx264", audio_codec="aac", temp_audiofile=temp_audiofile)
        # cropped_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

        # 关闭资源
        clip.close()
        cropped_clip.close()


    # 视频缩放
    def video_scale(self, input_file, output_file, start_x, start_y, end_x, end_y):

        width = end_x - start_x
        height = end_y - start_y

        ffmpeg.input(input_file).crop(start_x, start_y, width, height).output(output_file).run()


def user_video_split(given_file):
    ffm = FFmpeg()

    file_path = "E:\\E_RCD\\fideo_Recoding\\"
    # 输入视频文件路径
    input_video = file_path + "EnglishSp-2024.07.27-03.01.48.mp4"
    input_video = file_path + "EnglishSp-2024.07.27-Mini-output.mp4"
    input_video = given_file
    # 定义输出视频文件的基础路径和扩展名
    output_base_path = file_path + "EnglishSp-2024.07.27-第"
    output_extension = ".mp4"

    # 定义片段的起始时间和结束时间列表（格式为 hh:mm:ss）
    segments = [
        # ("00:07:00.000", "00:08:00.742"),   # 第  集
        ("00:04:31.060", "00:21:45.742"),   # 第 1 集
        ("00:21:45.742", "00:38:51.111"),   # 第 2 集
        ("00:38:51.111", "00:55:45.828"),   # 第 3 集
        ("00:55:45.828", "01:14:00.814"),   # 第 4 集
        # ("00:00:02", "00:00:12"),   # 第 5 集
        # ("00:00:20", "00:00:35"),   # 第 6 集
        # ("00:00:36", "00:00:58"),   # 第 7 集
        # 添加更多片段的时间范围
    ]
    
    # 循环处理每个片段
    for index, (start_time, end_time) in enumerate(segments):
        # 构建输出文件名
        output_video = f"{output_base_path}{index + 1}{'集-'}{output_extension}"
        
        # 调用函数进行视频分割
        ffm.video_split(input_video, start_time, end_time, output_video)


def user_video_crop_1080_1920():
    ffm = FFmpeg()

    file_path = "E:\\E_RCD\\fideo_Recoding\\"
    # 方式一
    input_video_file = file_path + "EnglishSp-2024.07.27-03.01.48.mp4"
    output_video_file = file_path + "EnglishSp-2024.07.27-03.01.48-OUTPUT.mp4"
    output_audio_file = file_path + "EnglishSp-2024.07.27-03.01.48-OUTPUT.aac"
    # merge_output_file = file_path + "EnglishSp-2024.07.27-测试-裁剪type1.mp4"
    
    ffm.video_crop_1080_1920(input_video_file, output_video_file)

    return output_video_file


def user_video_crop_1080_1920_MiniTest():
    ffm = FFmpeg()

    file_path = "E:\\E_RCD\\fideo_Recoding\\"
    # 方式一
    input_video_file = file_path + "EnglishSp-2024.07.27-Mini.mp4"
    output_video_file = file_path + "EnglishSp-2024.07.27-Mini-output.mp4"
    output_audio_file = file_path + "EnglishSp-2024.07.27-Mini-output.aac"
    # merge_output_file = file_path + "EnglishSp-2024.07.27-测试-裁剪type1.mp4"
    
    ffm.video_crop_1080_1920(input_video_file, output_video_file)


    # # 方式二
    # # 定义输入输出文件名和裁剪参数
    # input_file = file_path + "EnglishSp-2024.07.27-测试.mp4"
    # temp_audiofile = file_path + "EnglishSp-2024.07.27-测试-裁剪type2-tmp.aac"  # 临时音频文件
    # output_file = file_path + "EnglishSp-2024.07.27-测试-裁剪type2.mp4"
    # x_start, y_start = 0, 656  # 开始裁剪的位置
    # width, height = 1080, 607  # 裁剪的宽度和高度
    
    # ffm.crop_video_way2(input_file, temp_audiofile, output_file, x_start, y_start, width, height)


def user_video_scale(ffm):
    input_file = ""
    output_file = ""
    start_x = 875
    start_y = 287
    end_x = 1684
    end_y = 748

    ffm.huamian(input_file, output_file, start_x, start_y, end_x, end_y)


if __name__ == "__main__":

    ## 测试实际速度，选择先分割后剪裁缩放 Or 先剪裁缩放后分割
    # 第一步 1080*1920竖屏视频裁剪以适应16:9横屏比例
    rt_file = user_video_crop_1080_1920()

    # 第二步 缩放至2560:1440

    # 第三步 对大视频进行分割
    user_video_split(rt_file)

    

