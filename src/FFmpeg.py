#pip install ffmpeg-python

# 命令行范例：
# ffmpeg -i input.mp4 -ss start_time -t duration -c copy output.mp4
# -i input.mp4 指定输入文件。
# -ss start_time 设置开始时间，例如 -ss 00:01:30 表示从 1 分 30 秒开始。
# -t duration 设置持续时间，例如 -t 00:00:45 表示持续 45 秒。 -to 是表示结束时间。注意区别
# -c copy 指示 FFmpeg 尽量保持原始编解码器设置不变，以提高效率。
# output.mp4 是输出文件名。


import ffmpeg

def split_video_ffmpeg(input_video, start_time, end_time, output_video):
    try:
        # 使用 FFmpeg 进行视频分割
        ffmpeg.input(input_video, ss=start_time, to=end_time).output(output_video, c='copy').run()
        print(f"视频已成功分割并保存到 {output_video}")
    except ffmpeg.Error as e:
        print(f"分割视频时出错: {e.stderr.decode()}")


if __name__ == "__main__":
    # 输入视频文件路径
    # input_video = "E:\\test\\test-cut\\16天第.mp4"
    input_video = "E:\\7DC2-PUB\\15天第.mp4"

    # 定义片段的起始时间和结束时间列表（格式为 hh:mm:ss）
    segments = [
        ("00:00:03.000", "00:34:23.666"),   # 第 1 集
        ("00:35:26.666", "01:13:20.666"),   # 第 2 集
        ("01:14:23.666", "01:41:22.333"),   # 第 3 集
        ("01:42:25.333", "02:19:37.333"),   # 第 4 集
        ("02:20:40.333", "02:47:55.666"),   # 第 5 集
        ("02:48:58.666", "03:23:51.333"),   # 第 6 集
        ("03:24:54.333", "03:53:44.333"),   # 第 7 集
        # 添加更多片段的时间范围
    ]
    
    # 定义输出视频文件的基础路径和扩展名
    # output_base_path = "E:\\test\\test-cut\\16天第"
    output_base_path = "E:\\7DC2-PUB\\15天第"
    output_extension = ".mp4"
    
    # 循环处理每个片段
    for index, (start_time, end_time) in enumerate(segments):
        # 构建输出文件名
        output_video = f"{output_base_path}{index + 1}{'集-'}{output_extension}"
        
        # 调用函数进行视频分割
        split_video_ffmpeg(input_video, start_time, end_time, output_video)


# 如果速度太慢可以使用多线程或者进程

