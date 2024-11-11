import asyncio
import time
from datetime import datetime

import click


async def sleep_and_print(seconds):
    print(f"starting {seconds} sleep 😴")
    await asyncio.sleep(seconds)
    print(f"finished {seconds} sleep ⏰")
    return seconds

async def main():
    #result = await asyncio.gather(sleep_and_print(3), sleep_and_print(6))

    #building list 
    coroutines_list = []
    for k in range(1, 11):
        coroutines_list.append(sleep_and_print(k))
    results = await asyncio.gather(*coroutines_list)
    print(results)

start = datetime.now()
asyncio.run(main())
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")
