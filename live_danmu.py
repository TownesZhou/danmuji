"""
    Test getting live danmu from bilibili live room.
"""
import asyncio
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from bilibili_api import live, sync


class Danmuku(QObject):
    """
        The core danmu class providing service to the application's main window.

        A subclass of QObject so that it runs in Qt's worker thread.
    """
    # Set up thread signals as class attributes
    new_danmu = pyqtSignal(int, int)   # Report new danmu stats when monitoring
    viewer_report = pyqtSignal(set)
    finished = pyqtSignal()

    def __init__(self, room_id, paizi=None, keyword=None):
        """
        Set up the danmuku worker to monitor the bilibili live room specified by `room_id`. Optionally, provide `paizi`
        and `keyword` to filter danmu that was sent with the specified paizi or contains the specified danmu.

        """
        super(Danmuku, self).__init__()
        self.room_id = room_id
        self.paizi = paizi
        self.keyword = keyword

        # Internal states
        self.room = None
        self.num_danmu = 0
        self.viewer_set = set()
        self.task = None
        self.loop = None

    def start_monitor(self):
        """
        Start monitoring live danmu.

        When there's a new danmu that meets the condition, will emit the `new_danmu` Qt signal with signature:
            new_danmu.emit(num_total_danmu, num_total_viewer)
        """
        print("Start monitoring!")
        self.room = live.LiveDanmaku(self.room_id)

        # Async function to record new danmu and report to callback
        @self.room.on('DANMU_MSG')
        async def on_new_danmu(event):
            # Get message content
            data = event['data']['info']
            msg, viewer, tag = data[1: 4]
            viewer_name = viewer[1]
            tag_name = '' if len(tag) < 2 else tag[1]
            # Decide to record or not
            if (not self.paizi or self.paizi == tag_name) and (not self.keyword or self.keyword in msg):
                self.num_danmu += 1
                self.viewer_set.add(viewer_name)
                print(f"Reporting danmu -- msg: {msg}, viewer_name: {viewer_name}")
                # stats_report_func(self.num_danmu, len(self.viewer_set))
                self.new_danmu.emit(self.num_danmu, len(self.viewer_set))

        # Create a new event loop in this thread and Create the coroutine task to run concurrently
        self.loop = asyncio.new_event_loop()
        print(f"Event loop: {self.loop}")
        asyncio.set_event_loop(self.loop)
        # asyncio.set_event_loop(asyncio.new_event_loop())

        # self.task = asyncio.create_task(self.room.connect())
        # self.task = loop.create_task(self.room.connect())

        asyncio.run(self.room.connect())

    def stop_monitor(self):
        """
        Stop the live danmu monitoring, and returns the viewer set by emitting the Qt signal `viewer_report` with the
        following signature:
            viewer_report.emit(set)
        where the set of viewer names are passed.

        It then emits the `finished` signal to announce that job is done.
        """
        print("Stop monitoring!")
        # Run disconnect() until it gets results
        asyncio.run(self.room.disconnect())
        # self.loop.run_until_complete(self.room.disconnect())
        # Report the set of viewers
        self.viewer_report.emit(self.viewer_set)
        # Emit finished signal to notice job done
        self.finished.emit()


# === DEBUG ONLY ===
if __name__ == "__main__":
    room_id = 21603945
    danmuku = Danmuku()

    def stats_report_func(num_danmu, num_viewers):
        print(f"Num danmu: {num_danmu}, num_viewers: {num_viewers}")
        print(f"Total view list: {list(danmuku.viewer_set)}")

    danmuku.start_monitor(stats_report_func, room_id)
