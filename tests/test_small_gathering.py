import time

from src import small_gathering


def test_small_gathering(capsys) -> None:
    start = time.perf_counter()
    small_gathering.runner(7)
    assert 0.95 < time.perf_counter() - start < 1.05
    assert capsys.readouterr().out.splitlines() == (['first!'] * 7) + (['last!'] * 7)
