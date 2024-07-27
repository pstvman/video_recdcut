import pyautogui
import pyperclip
import time
import logging

class Recoder:
    
    def run_recoder(self):

        # 等待准备就绪
        logging.info("5s后，将启动录制...")
        time.sleep(5)
                
        # 模拟按下 Ctrl + Alt + S
        pyautogui.hotkey('ctrl', 'alt', 's')
        logging.info("启动录制快捷键")

        # 选择要录制的屏幕区域
        start_positon = pyautogui.position(6, 21)
        end_position = pyautogui.position(2335, 1330)
        pyautogui.moveTo(start_positon, duration=0.5)
        pyautogui.dragTo(end_position, duration=0.5)
        logging.info("选择录制的屏幕区域")

        # 选择禁用输入麦克风
        micro_position = pyautogui.position(2212, 1355)
        pyautogui.moveTo(micro_position, duration=0.5)
        pyautogui.click()  # 点击确定按钮
        logging.info("禁用麦克风")

        # 点击录制
        record_position = pyautogui.position(2300, 1357)
        pyautogui.moveTo(record_position, duration=0.5)
        pyautogui.click()  # 点击确定按钮
        logging.info("点击 “开始录制”")

        # 回到安全位置
        record_position = pyautogui.position(2035, 1420)
        pyautogui.moveTo(record_position, duration=0.5)
        pyautogui.click()  # 点击确定按钮
        logging.info("鼠标回到安全位置")
        # pyautogui.hotkey('enter')  # 按下回车键确认录制

        # 抵消倒计时
        time.sleep(3)
        logging.info("延迟3s，抵消录制倒计时")

        # 等待录制完成并保存
        # pyautogui.sleep(10)  # 假设录制时间为10秒


    def ext_recoder(self, epic_name):
        # 退出播放器
        record_position = pyautogui.position(2544, 8)
        pyautogui.moveTo(record_position, duration=0.5)
        time.sleep(1)
        pyautogui.click()  # 点击确定按钮
        logging.info("点击关闭播放器，并延迟5s")
        time.sleep(5)

        # 结束录制
        end_record_position = pyautogui.position(2280, 1360)
        pyautogui.moveTo(end_record_position, duration=0.5)
        pyautogui.click()
        logging.info("点击 “结束录制”")

        # 预览另存为
        save_as_position = pyautogui.position(1672, 987)
        pyautogui.moveTo(save_as_position, duration=0.5)
        pyautogui.click()
        logging.info("录屏界面点击 “另存为”")

        # 修改视频名称
        # pyautogui.write(epic_name)
        pyperclip.copy(epic_name)
        pyautogui.hotkey('ctrl', 'v')
        logging.info("修改文件名为: %s" % (epic_name))
        time.sleep(1)

        # 保存
        save_position = pyautogui.position(1550, 868)
        pyautogui.moveTo(save_position, duration=0.5)
        pyautogui.click()
        logging.info("保存当前录制文件，并延迟10s等待录屏文件界面响应")
        time.sleep(10)

        # 退出预览
        save_ext_position = pyautogui.position(1699, 392)
        pyautogui.moveTo(save_ext_position, duration=0.5)
        pyautogui.click()
        logging.info("点击退出录屏文件预览")
        time.sleep(1)
        # 确定退出
        sure_ext_position = pyautogui.position(1330, 755)
        pyautogui.moveTo(sure_ext_position, duration=0.5)
        pyautogui.click()
        logging.info("确认退出，并延时3s")
        time.sleep(3)


if __name__ == "__main__":
    recoder = Recoder()
    recoder.run_recoder()
    time.sleep(10)
    recoder.ext_recoder("200天第")


