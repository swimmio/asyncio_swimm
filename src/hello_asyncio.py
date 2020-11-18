import asyncio


async def hello_asyncio() -> None:
    """
    Print some infamous quote with a respectable 1 second sleep for a dramatic effect.
    """
    print('This is going to be legen...')
    await asyncio.sleep(1)
    print('...dary!')


def runner() -> None:
    """
    Run the function `hello_asyncio`.
    """
    asyncio.run(hello_asyncio())
