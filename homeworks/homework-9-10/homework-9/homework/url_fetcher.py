import time
import asyncio
import aiohttp
import requests
from bs4 import BeautifulSoup
import re
import argparse


parser = argparse.ArgumentParser(description="URL Fetcher")

parser.add_argument("-c", "--count",type=int, help="Count one-time requests")
parser.add_argument("filename", type=str)
args = parser.parse_args()


def get_web_page_data(url):
    web_page_soup = BeautifulSoup(url, features='html.parser')
    web_page_text = " ".join(filter(lambda word: len(word) > 0, [word for word in re.split(r"\W", web_page_soup.get_text())]))
    data = web_page_text
    return data


def write_file(data):
    name = f'Downloaded_urls/url_{int(time.time() * 1000)}.txt'
    with open(name, 'w') as f:
        f.write(data)


async def fetch(url, session):
    async with session.get(url) as resp:
        data = await resp.read()
        url_data = get_web_page_data(data)
        write_file(url_data)


async def main(count_conn, file_urls):
    tasks = []
    conn = aiohttp.TCPConnector(limit=count_conn)

    async with aiohttp.ClientSession(connector=conn) as session:
        with open(file_urls, "r") as f:
            for line in f:
                tasks.append(asyncio.create_task(fetch(line.rstrip(), session)))

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    t1 = time.time()
    count_conn = args.count
    file_urls = args.filename
    asyncio.run(main(count_conn, file_urls))
    t2 = time.time()

    print('TT', t2 - t1)

