import math
import sys
import asyncio
from functools import partial

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QProgressBar
from quamash import QEventLoop


class MyWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QGridLayout()

        self.pairs = []
        for i in range(10):
            b = QPushButton('Countdown: &%d' % i, clicked=partial(self.on_click, i))
            p = QProgressBar(visible=False)
            layout.addWidget(b, i, 0)
            layout.addWidget(p, i, 1)
            self.pairs.append((b, p))

        self.setLayout(layout)

    def on_click(self, i):
        b, p = self.pairs[i]
        asyncio.ensure_future(self.do_countdown(b, p, i))

    @staticmethod
    async def do_countdown(b, p, n):
        b.setEnabled(False)
        p.setVisible(True)

        i = n * 100
        p.setMaximum(i)

        while i >= 0:

            await asyncio.sleep(0.01)

            p.setValue(i)
            b.setText('Countdown: %d' % math.ceil(i/100))
            i -= 1

        b.setText('Countdown: &%d' % n)
        b.setEnabled(True)
        p.setVisible(False)


def main():
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)  # NEW must set the event loop
    asyncio.events._set_running_loop(loop)

    w = MyWidget()
    w.show()

    with loop:
        loop.run_forever()

if __name__ == '__main__':
    main()
