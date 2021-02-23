#!/usr/bin/env python3
import aiohttp
import aiofiles
import asyncio

from pathlib import Path


URLS_PATH = Path('urls.txt')


async def fetch(session: aiohttp.ClientSession,
                url: str,
                **params) -> str:
    pass
        

async def dump(data: str,
               out_file: str) -> None:
    pass


async def worker(worker_id: int) -> None:
    pass


async def bound_fetch(urls: List[str],
                      out_paths: List[str]) -> None:
    pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()

