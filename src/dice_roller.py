import asyncio
import random
import typing

SLEEP_TIME = 0.2


async def dice_roller(target: int) -> int:
    """
    Roll a six sided die over and over again until you get the target number.
    Sleep the appropriate SLEEP_TIME between each roll.
    When the target is rolled, return it.

    :param target: The target that this function should roll.
    :type target: int
    :return: The target number.
    :rtype: int
    """
    while roll := random.randint(1, 6):
        print(f'{target} is rolling the dice')
        await asyncio.sleep(SLEEP_TIME)
        print(f'{target} rolled a {roll}')
        if roll == target:
            print(f'{target} is out!')
            return roll


async def gatherer() -> typing.Container[int]:
    """
    Gather and return a list containing the results of all the required coroutine calls.
    There will be six (6) `dice_roll` calls, each with a different target (so `dice_roll(1)` to `dice_roll(6)`).

    :return: List of every coroutine result.
    :rtype: typing.Container[int]
    """
    return await asyncio.gather(*[dice_roller(i) for i in range(1, 7)])


def runner() -> typing.Container[int]:
    return asyncio.run(gatherer())
