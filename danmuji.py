"""
    Danmuji main event logics
"""
import asyncio
import functools
from traceback import format_exc

import qasync
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator, QIcon
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from PyQt5.QtCore import QCoreApplication, Qt
from qasync import QEventLoop
import numpy as np

from core import Danmuku
from ui import Ui_MainWindow


QtWidgets.QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)   # enable highdpi scaling
QtWidgets.QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)      # use highdpi icons


VERSION = "v0.0.3"
ICON_PATH = 'asset/icon.ico'
WINDOW_MIN_WIDTH = 420
WINDOW_MIN_HEIGHT = 650

LOTTERY_INTERVAL_MIN = 10
LOTTERY_INTERVAL_MAX = 300
LOTTERY_INTERVAL_INC = 5


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        # Input validator
        self.onlyInt = QIntValidator()
        # Danmuku
        self.danmuku = Danmuku()

    def setup_ui(self, ui_main_window):
        self.ui = ui_main_window
        # More adjustments on UI
        # Icon
        self.setWindowIcon(QIcon(ICON_PATH))
        # Window title
        self.setWindowTitle(QCoreApplication.translate("MainWindow", "Bilibili 弹幕抽奖姬 " + VERSION))
        # Minimal window size
        self.setMinimumSize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)
        # Setup widget signal and slots
        # Enable/disable danmu filter lineEdit widget when the corresponding checkbox state changes
        self.ui.checkBox_paizi.toggled.connect(
            lambda: self.ui.lineEdit_paizi.setEnabled(self.ui.checkBox_paizi.isChecked()))
        self.ui.checkBox_keyword.toggled.connect(
            lambda: self.ui.lineEdit_keyword.setEnabled(self.ui.checkBox_keyword.isChecked()))
        # Setup lottery button signal
        self.ui.pushButton_lottery.clicked.connect(self.lottery_button_on_click)
        # Setup input lineEdit validators
        # room_id lineEdit only allow integer input
        self.ui.lineEdit_room_id.setValidator(self.onlyInt)

    # === UI Event Logic ===

    # Main lottery button events
    def lottery_button_on_click(self):
        # Change button state/text and call corresponding function
        if self.ui.pushButton_lottery.text() == "开始统计":
            asyncio.create_task(self.start_monitor())
        else:
            asyncio.create_task(self.start_lottery())

    # Update monitor displays when new danmu arrives
    def update_monitor(self, num_danmu, viewer_list):
        self.ui.lcdNumber_num_danmu.display(num_danmu)
        self.ui.lcdNumber_num_viewer.display(len(viewer_list))
        self.ui.textBrowser_viewers.setText('\n'.join(viewer_list))

    # Reset monitor displays to 0
    def reset_monitor(self):
        self.ui.lcdNumber_num_danmu.display(0)
        self.ui.lcdNumber_num_viewer.display(0)
        self.ui.textBrowser_viewers.setText('')

    async def start_monitor(self):
        """
        Start the live danmu monitoring
        """
        # Rest previous output
        self.reset_monitor()  # Clear LCD
        self.ui.textBrowser_lottery_result.setText('')  # Clear text display
        # Get input
        # Make sure room_id contains something
        room_id = self.ui.lineEdit_room_id.text()
        if not room_id:
            QMessageBox.critical(self, "输入错误", "请填写Bilibili直播间房间号！")
            return
        room_id = int(room_id)
        paizi = self.ui.lineEdit_paizi.text().strip()
        keyword = self.ui.lineEdit_keyword.text().strip()

        try:
            await self.danmuku.start_monitor(
                self.update_monitor,
                room_id,
                paizi if self.ui.checkBox_paizi.isChecked() else None,
                keyword if self.ui.checkBox_keyword.isChecked() else None
            )
        except Exception:
            QMessageBox.critical(self.main_window, "连接Bilibili直播服务时出现错误", format_exc())

        # Change button caption at the end
        self.ui.pushButton_lottery.setText("结束统计并抽奖")

    async def start_lottery(self):
        """
        Stop monitoring and start lottery
        """
        self.ui.pushButton_lottery.setEnabled(False)
        candidates = await self.danmuku.stop_monitor()

        # The lottery process visualization
        if len(candidates) > 0:
            for interval_ms in range(LOTTERY_INTERVAL_MIN, LOTTERY_INTERVAL_MAX, LOTTERY_INTERVAL_INC):
                self.ui.textBrowser_lottery_result.setText(np.random.choice(candidates))
                await asyncio.sleep(interval_ms / 1000)

        # Make the winner red
        self.ui.textBrowser_lottery_result.setText(
            '<p style="color: red">' + np.random.choice(candidates) + '</p>'
        )

        # Change button name at the end
        self.ui.pushButton_lottery.setEnabled(True)
        self.ui.pushButton_lottery.setText("开始统计")


async def main():
    def close_future(future, loop):
        loop.call_later(10, future.cancel)
        future.cancel()

    loop = asyncio.get_event_loop()
    future = asyncio.Future()

    app = QtWidgets.QApplication(sys.argv)
    if hasattr(app, "aboutToQuit"):
        getattr(app, "aboutToQuit").connect(
            functools.partial(close_future, future, loop)
        )

    # Set style
    app.setStyle('Fusion')

    # Setup main window and UI
    main_window = MainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.setup_ui(ui)
    main_window.show()

    await future
    return True


if __name__ == "__main__":
    import sys

    try:
        qasync.run(main())
    except asyncio.exceptions.CancelledError:
        sys.exit(0)
