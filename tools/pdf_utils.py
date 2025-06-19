# utils/async_queue.py
import asyncio

class TaskQueue:
    def __init__(self):
        self.queue = asyncio.Queue()
        
    async def add_task(self, task):
        await self.queue.put(task)
        
    async def process_tasks(self):
        while not self.queue.empty():
            task = await self.queue.get()
            await task.execute()
