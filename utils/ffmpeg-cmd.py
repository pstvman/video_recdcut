import subprocess
import os


def split_video(input_video, *segments):
    """
    Splits a video into several segments.
    """

    for i in range(len(segments)):
        segment = segments[i]
        part = input_video.replace('.ts', f'-part_{i}.ts')
        # subprocess.run(['ffmpeg', '-i', input_video, '-ss', segment[0], '-to', segment[1], '-c:v', 'libx264', '-c:a', 'aac', part], check=True)
        subprocess.run(['ffmpeg', '-i', input_video, '-ss', segment[0], '-to', segment[1], '-c', 'copy', part], check=True)


def concat_video(output_video, *input_videos):
    """
    Concatenates several videos into one.
    """

    # 创建一个文件列表 filelist.txt，用于合并视频片段
    with open('filelist.txt', 'w') as f:
        for input_i in input_videos:
            f.write(f"file '{input_i}'\n")

    # 合并两个片段成一个新的视频
    # subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'filelist.txt', '-c', 'copy', output_video])
    subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'filelist.txt', '-c:v', 'libx264', '-c:a', 'aac', output_video])
    os.remove('filelist.txt')


def split_and_concat_video(input_video, output_video, *segments):
    """
    Splits a video into several segments and then concatenates them back together.
    """

    # # 提取第一个片段（从开始到2分钟）
    # subprocess.run(['ffmpeg', '-i', input_video, '-ss', '00:00:00', '-to', '00:01:22', '-c', 'copy', part1])
    # # 提取第二个片段（从5分钟到结束）
    # subprocess.run(['ffmpeg', '-i', input_video, '-ss', '00:01:26', '-to', '00:02:18', '-c', 'copy', part2])

    ## 提取片段并重新编码解决拼接处没有关键帧而导致卡顿的问题
    # subprocess.run(['ffmpeg', '-i', input_video, '-ss', segment1[0], '-to', segment1[1], '-c:v', 'libx264', '-c:a', 'aac', part1], check=True)
    # subprocess.run(['ffmpeg', '-i', input_video, '-ss', segment2[0], '-to', segment2[1], '-c:v', 'libx264', '-c:a', 'aac', part2], check=True)
    with open('filelist.txt', 'w') as f:
        for index, segment in enumerate(segments):
            part = 'part' + str(index) + '.mp4'
            subprocess.run(['ffmpeg', '-i', input_video, '-ss', segment[0], '-to', segment[1], '-c:v', 'libx264', '-c:a', 'aac', part], check=True)
            f.write(f"file '{part}'\n")

    # 重新编码整个视频
    # subprocess.run(['ffmpeg', '-i', input_video, '-c:v', 'libx264', '-c:a', 'aac', '-strict', 'experimental', '-b:a', '128k', '-ar', '44100', '-ac', '2', '-vf', 'scale=1280:720', part1])
    # subprocess.run(['ffmpeg', '-i', input_video, '-c:v', 'libx264', '-c:a', 'aac', '-strict', 'experimental', '-b:a', '128k', '-ar', '44100', '-ac', '2', '-vf', 'scale=1280:720', part2])

    # 合并两个片段成一个新的视频
    subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'filelist.txt', '-c', 'copy', output_video])

    # 清理临时文件
    for i in range(len(segments)):
        os.remove('part' + str(i) + '.mp4')
    os.remove('filelist.txt')


def recode(input_video, output_video):
    """
    Recodes a video using ffmpeg.
    """
    subprocess.run(['ffmpeg', '-i', input_video, '-c:v', 'libx264', '-c:a', 'aac', output_video], check=True)


file_path = "C:\\Users\\jaby0\\Videos\\"
file_path = "C:\\C_BHC\\potPlayer_Recoding\\bps1016\\"


# ## 分割并拼接视频片段
# input_video = file_path + 'vlc-record-2024-07-29-13h28m08s-吐泡泡🫧的抖音直播间 - 抖音直播-.mp4'
# output_video = file_path + 'vlc-record-2024-07-29-13h28m08s-吐泡泡的抖音直播间 - 抖音直播--拼接.mp4'

# segment1 = ('00:04:13', '00:07:36')
# segment2 = ('00:01:26', '00:02:18')

# split_and_concat_video(input_video, output_video, segment1, segment2)


# ## 拼接视频
# input_video1 = file_path + 'bps1016_20240724_141308.ts'
# input_video2 = file_path + 'bps1016_20240724_142044.ts'
# # input_video3 = file_path + 'vlc-record-2024-07-29-13h26m18s.mp4'
# # input_video4 = file_path + 'vlc-record-2024-07-29-13h28m08s.mp4'
# # input_video5 = file_path + 'vlc-record-2024-07-29-13h42m38s.mp4'
# # input_video6 = file_path + 'vlc-record-2024-07-29-14h24m35s.mp4'
# output_video = file_path + 'bps1016_20240724.mp4'

# concat_video(output_video, input_video1, input_video2)


## 视频分割
input_video1 = file_path + '정서이_bps1016_20240724_154927.ts'
segment1 = ('00:00:00', '00:26:16.481')
segment2 = ('00:26:17.181', '01:00:00')
split_video(input_video1, segment1, segment2)


# # 对视频重新编码
# input_video1 = file_path + 'vlc-record-2024-07-29-part1.mp4'
# output_video = file_path + 'vlc-record-2024-07-29-part1-recode.mp4'
# recode(input_video1, output_video)