import asyncio
import pytest
from pathlib import Path
from src import file_cabinet

TEST_TEXT = '''
abcd
efgh
ijkl
mnop
qrst
uvwx
yz
'''.strip()


def test_read_write(tmp_path: Path) -> None:
    filename = tmp_path / 'tmp'
    asyncio.run(file_cabinet.write_file(filename, TEST_TEXT))
    assert [line.rstrip() for line in asyncio.run(file_cabinet.read_file(filename))] == TEST_TEXT.splitlines()


@pytest.mark.parametrize(
    'from_file, to_file',
    [(Path('a_from'), Path('a_to')), (Path('b_from'), Path('b_to')), (Path('c_from'), Path('c_to'))],
)
def test_file_cabinet(tmp_path: Path, from_file: Path, to_file: Path) -> None:
    from_path = tmp_path / from_file
    to_path = tmp_path / to_file
    from_path.write_text(TEST_TEXT)
    asyncio.run(file_cabinet.copy_every_odd_line(from_path, to_path))
    assert to_path.read_text().splitlines() == TEST_TEXT.splitlines()[::2]
