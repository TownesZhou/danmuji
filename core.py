"""
    Test getting live danmu from bilibili live room.
"""
import asyncio
from bilibili_api import live, sync


class Danmuku():
    """
        The core danmu class providing service to the application's main window.

        A subclass of QObject so that it runs in Qt's worker thread.
    """

    def __init__(self):
        # Internal states
        self.room = None
        self.num_danmu = 0
        self.viewer_list = []
        self.start_monitor_task, self.stop_monitor_task = None, None
        self.loop = None

    async def get_room_info(self, room_id):
        """
        Returns room title, anchor name, live status
        """
        room_info = await live.LiveRoom(room_id).get_room_info()
        return room_info['room_info']['title'], \
               room_info['anchor_info']['base_info']['uname'], \
               room_info['room_info']['live_status']

    async def start_monitor(self, new_danmu_callback, room_id, paizi=None, keyword=None):
        print("Start monitoring!")
        assert callable(new_danmu_callback)
        self.room = live.LiveDanmaku(room_id, debug=False)

        # Async function to record new danmu and report to callback
        @self.room.on('DANMU_MSG')
        async def on_new_danmu(event):
            # Get message content
            data = event['data']['info']
            msg, viewer, tag = data[1: 4]
            viewer_name = viewer[1]
            tag_name = '' if len(tag) < 2 else tag[1]
            # Decide to record or not
            if (not paizi or paizi == tag_name) and (not keyword or keyword in msg):
                self.num_danmu += 1
                if viewer_name not in self.viewer_list:
                    self.viewer_list.append(viewer_name)
                print(f"Reporting danmu -- msg: {msg}, viewer_name: {viewer_name}")
                new_danmu_callback(self.num_danmu, self.viewer_list)

        # Create a new event loop in this thread and Create the coroutine task to run concurrently
        self.start_monitor_task = asyncio.create_task(self.room.connect())

    async def stop_monitor(self):
        print("Stop monitoring!")
        # Create another task to run disconnect() in the existing event loop
        self.stop_monitor_task = asyncio.create_task(self.room.disconnect())
        # Wait for disconnection
        await self.stop_monitor_task
        # get result and Clear stats
        result = self.viewer_list
        self.num_danmu = 0
        self.viewer_list = []
        return result


# === DEBUG ONLY ===
if __name__ == "__main__":
    room_id = 23676151
    live_room = live.LiveRoom(room_id)

    # def stats_report_func(num_danmu, num_viewers):
    #     print(f"Num danmu: {num_danmu}, num_viewers: {num_viewers}")
    #     print(f"Total view list: {list(danmuku.viewer_list)}")
    #
    # danmuku.start_monitor(stats_report_func, room_id)

    # print(sync(live_room.get_room_info()))

    result = sync(live_room.get_room_info())
    print(result['room_info']['title'])
    print(result['anchor_info']['base_info']['uname'])
