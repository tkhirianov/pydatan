#!/usr/bin/env python3
import asyncio
import logging
import time
from pathlib import Path
from typing import List, Tuple

import aiofiles
import aiohttp
import requests


URLS_PATH = Path('urls.txt')
URLS_TO_PATHS = List[Tuple[str, str]]

logging.basicConfig(
    format="[{asctime},{msecs:3.0f}] [{levelname}:{process}:{thread}] "
           "[{module}:{funcName}] {message}",
    level=logging.INFO,
    style='{'
)

logging.getLogger('requests').setLevel(logging.ERROR)
logging.getLogger('urllib3').setLevel(logging.ERROR)


async def fetch_async(session: aiohttp.ClientSession,
                      url: str,
                      **params) -> str:
    async with session.get(url, params=params) as response:
        if response.status == 200:
            return await response.text(encoding='utf-8')

        logging.error(f"{response.reason}, because of {response.status}")
        

async def dump_async(data: str,
                     out_file: str) -> None:
    async with aiofiles.open(out_file, 'w', encoding='utf-8') as f:
        await f.write(data)


async def worker(args_queue: asyncio.Queue,
                 worker_id: int) -> None:
    while True:
        session, url, out_file = args_queue.get_nowait()

        logging.debug(f"[{worker_id=}] requested to {url=}")
        data = await fetch_async(session, url)
        
        if data:
            logging.debug(f"[{worker_id=}] successfully received from {url=}")

            await dump_async(data, out_file)
            logging.debug(f"[{worker_id=}] {url=} successfully dumped")

        args_queue.task_done()


async def bound_fetch(urls_to_paths: URLS_TO_PATHS) -> None:
    args_queue = asyncio.Queue(maxsize=-1)
    timeout = aiohttp.ClientTimeout(30)

    async with aiohttp.ClientSession(timeout=timeout) as session:
        for url, out_path in urls_to_paths:
            await args_queue.put((session, url, out_path))

        tasks = []
        for worker_id in range(5):
            task = asyncio.create_task(worker(args_queue, worker_id + 1))
            tasks += [task]

        await args_queue.join()

        for task in tasks:
            task.cancel()


def main_async(urls_to_paths: URLS_TO_PATHS) -> float:
    start = time.perf_counter()
    asyncio.run(bound_fetch(urls_to_paths))
    executing_time = round(time.perf_counter() - start, 2)

    logging.info(f"{len(urls_to_paths)} sites processed, {executing_time = }s")

    return executing_time


def fetch_sync(url: str, **params) -> str:
    try:
        html = requests.get(url, params=params).text
    except Exception:
        logging.exception(f"Error requesting to {url=}")
    else:
        return html


def dump_sync(data: str,
              out_file: str) -> None:
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(data)


def main_sync(urls_to_paths: URLS_TO_PATHS) -> float:
    start = time.perf_counter()

    for url, out_path in urls_to_paths:
        data = fetch_sync(url)
        if data:
            logging.debug(f"Successfully received from {url=}")

            dump_sync(data, out_path)
            logging.debug(f"{url=} successfully dumped")

    executing_time = round(time.perf_counter() - start, 2)
    logging.info(f"{len(urls_to_paths)} sites processed, {executing_time = }s")

    return executing_time


def get_urls() -> URLS_TO_PATHS:
    urls_to_paths = []
    with URLS_PATH.open(encoding='utf-8') as f:
        for line in f:
            urls_to_paths += [line.split(), ]

    return urls_to_paths


def main() -> None:
    urls_to_paths = get_urls()

    async_time = main_async(urls_to_paths)
    sync_time = main_sync(urls_to_paths)

    result = "faster" if async_time < sync_time else "slower"
    times = round(sync_time / async_time, 2)

    logging.info(f"Async is {times} times {result} than sync")
    logging.warning("Do not forget to remove all html files ;)")


if __name__ == "__main__":
    main()
