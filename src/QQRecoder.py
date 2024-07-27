import pyautogui
import pyperclip
import time

class QQRecoder:
    
    def run_recoder(self):
        # 模拟按下 Ctrl + Alt + S
        pyautogui.hotkey('ctrl', 'alt', 's')

        # 选择要录制的屏幕区域
        start_positon = pyautogui.position(6, 21)
        end_position = pyautogui.position(2335, 1330)
        pyautogui.moveTo(start_positon, duration=0.5)
        pyautogui.dragTo(end_position, duration=0.5)

        # 选择禁用输入麦克风
        micro_position = pyautogui.position(2212, 1355)
        pyautogui.moveTo(micro_position, duration=0.5)
        pyautogui.click()  # 点击确定按钮

        # 点击录制
        record_position = pyautogui.position(2300, 1357)
        pyautogui.moveTo(record_position, duration=0.5)
        pyautogui.click()  # 点击确定按钮

        # 回到安全位置
        record_position = pyautogui.position(2035, 1420)
        pyautogui.moveTo(record_position, duration=0.5)
        pyautogui.click()  # 点击确定按钮
        # pyautogui.hotkey('enter')  # 按下回车键确认录制

        # 抵消倒计时
        time.sleep(3)

        # 等待录制完成并保存
        # pyautogui.sleep(10)  # 假设录制时间为10秒


    def ext_recoder(self, epic_name):
        # 退出播放器
        record_position = pyautogui.position(2544, 8)
        pyautogui.moveTo(record_position, duration=0.5)
        time.sleep(1)
        pyautogui.click()  # 点击确定按钮

        time.sleep(5)
        # 结束录制
        end_record_position = pyautogui.position(2280, 1360)
        pyautogui.moveTo(end_record_position, duration=0.5)
        pyautogui.click()

        # 预览另存为
        save_as_position = pyautogui.position(1672, 987)
        pyautogui.moveTo(save_as_position, duration=0.5)
        pyautogui.click()

        # 修改视频名称
        # pyautogui.write(epic_name)
        pyperclip.copy(epic_name)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        # 保存
        save_position = pyautogui.position(1550, 868)
        pyautogui.moveTo(save_position, duration=0.5)
        pyautogui.click()
        time.sleep(10)

        # 退出预览
        save_ext_position = pyautogui.position(1699, 392)
        pyautogui.moveTo(save_ext_position, duration=0.5)
        pyautogui.click()
        # 确定退出
        sure_ext_position = pyautogui.position(1330, 755)
        pyautogui.moveTo(sure_ext_position, duration=0.5)
        pyautogui.click()


if __name__ == "__main__":
    recoder = QQRecoder()
    recoder.run_recoder()
    time.sleep(10)
    recoder.ext_recoder("200天第")


