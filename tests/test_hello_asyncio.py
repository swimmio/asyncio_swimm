import time

from src import hello_asyncio


def test_hello_asyncio(capsys) -> None:
    assert hasattr(hello_asyncio, 'asyncio')
    start = time.perf_counter()
    hello_asyncio.runner()
    assert 0.95 < time.perf_counter() - start < 1.05
    assert capsys.readouterr().out.splitlines() == ['This is going to be legen...', '...dary!']
