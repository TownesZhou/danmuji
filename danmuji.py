"""
    Danmuji main event logics
"""
import asyncio
from traceback import format_exc
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from PyQt5.QtCore import QCoreApplication
from qasync import QEventLoop
import numpy as np

from core import Danmuku
from ui import Ui_MainWindow


VERSION = "v0.0.1"

LOTTERY_INTERVAL_MIN = 10
LOTTERY_INTERVAL_MAX = 500
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
        self.setWindowTitle(QCoreApplication.translate("MainWindow", "Bilibili 弹幕抽奖姬 " + VERSION))
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

    # Function for updating the live danmu stats LCDNumber widgets
    def update_lcd(self, num_danmu, num_viewers):
        self.ui.lcdNumber_num_danmu.display(num_danmu)
        self.ui.lcdNumber_num_viewer.display(num_viewers)

    async def start_monitor(self):
        """
        Start the live danmu monitoring
        """
        # Rest previous output
        self.update_lcd(0, 0)  # Clear LCD
        self.ui.textBrowser_lottery_result.setText('')  # Clear text display
        # Get input
        # Make sure room_id contains something
        room_id = self.ui.lineEdit_room_id.text()
        if not room_id:
            QMessageBox.critical(self.main_window, "输入错误", "请填写Bilibili直播间房间号！")
            return
        room_id = int(room_id)
        paizi = self.ui.lineEdit_paizi.text().strip()
        keyword = self.ui.lineEdit_keyword.text().strip()

        try:
            await self.danmuku.start_monitor(self.update_lcd, room_id, paizi, keyword)
        except Exception as e:
            QMessageBox.critical(self.main_window, "连接Bilibili直播服务时出现错误", format_exc())

        # Change button caption at the end
        self.ui.pushButton_lottery.setText("结束统计并抽奖")

    async def start_lottery(self):
        """
        Stop monitoring and start lottery
        """
        self.ui.pushButton_lottery.setEnabled(False)
        candidates = list(await self.danmuku.stop_monitor())

        # The lottery process visualization
        if len(candidates) > 0:
            for interval_ms in range(LOTTERY_INTERVAL_MIN, LOTTERY_INTERVAL_MAX, LOTTERY_INTERVAL_INC):
                self.ui.textBrowser_lottery_result.setText(np.random.choice(candidates))
                await asyncio.sleep(interval_ms / 1000)

        # Change button name at the end
        self.ui.pushButton_lottery.setEnabled(True)
        self.ui.pushButton_lottery.setText("开始统计")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Setup application async event loop
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    asyncio.events._set_running_loop(loop)

    # Setup main window and UI
    main_window = MainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.setup_ui(ui)
    main_window.show()

    with loop:
        loop.run_forever()

    sys.exit(app.exec_())
