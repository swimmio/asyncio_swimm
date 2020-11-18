import asyncio


async def announce() -> None:
    """
    Announce the first line, wait and then announce the last line.
    """
    print('first!')
    await asyncio.sleep(1)
    print('last!')


async def gatherer(announcements: int) -> None:
    """
    Initialize several `announce` coroutines and wait for all of them to finish.

    :param announcements: The number of `announce` coroutines to instantiate.
    :type announcements: int
    """
    await asyncio.gather(*[announce() for _ in range(announcements)])


def runner(announcements: int) -> None:
    asyncio.run(gatherer(announcements))
