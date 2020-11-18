import time

from src import dice_roller


def test_small_gathering() -> None:
    start = time.perf_counter()
    assert dice_roller.runner() == [1, 2, 3, 4, 5, 6]
    assert 0.2 < time.perf_counter() - start
