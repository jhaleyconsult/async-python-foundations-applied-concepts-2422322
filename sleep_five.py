import asyncio
import time
from datetime import datetime
import click

async def sleep_five(seconds):
    print(f"starting {seconds} sleep 😴")
    await asyncio.sleep(seconds)
    print(f"finished {seconds} sleep ⏰")
    return seconds

async def sleep_3_then_five(sec1, sec2):
    x = [sec1,sec2]
    for k in x:
        print(f"starting {k} sleep 😴")
        await asyncio.sleep(k)
        print(f"finished {k} sleep ⏰")
        return k

async def main():
    result = await asyncio.gather(
        sleep_five(5),
        sleep_3_then_five(3,5))
    print(result)
    click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")

start = datetime.now()
asyncio.run(main())
