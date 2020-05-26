import time
import asyncio
import aiohttp
import aiofiles
from concurrent.futures import ThreadPoolExecutor
import multiprocessing


def write_file(data):
    name = f'Downloaded_imgs/photo_{int(time.time() * 1000)}.jpg'
    with open(name, 'wb') as f:
        f.write(data)


# 1
async def fetch(url, session):
    async with session.get(url, allow_redirects=True) as resp:
        data = await resp.read()
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, write_file, data)


# # 2
# async def fetch(url, session):
#     async with session.get(url, allow_redirects=True) as resp:
#         data = await resp.read()
#         pool = ThreadPoolExecutor(max_workers=multiprocessing.cpu_count())
#         loop = asyncio.get_event_loop()
#         await loop.run_in_executor(pool, write_file, data)
#
#
# # 3
# async def write_file(data):
#     name = f'Downloaded_imgs/photo_{int(time.time() * 1000)}.jpg'
#     async with aiofiles.open(name, mode='wb') as f:
#         await f.write(data)
#         await f.close()
#
#
# async def fetch(url, session):
#     async with session.get(url, allow_redirects=True) as resp:
#         data = await resp.read()
#         await write_file(data)


async def main():
    url = 'https://loremflickr.com/320/240'
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            tasks.append(asyncio.create_task(fetch(url, session)))

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()

    print('TT', t2 - t1)
