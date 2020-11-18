import typing
from pathlib import Path

import aiofiles


async def write_file(path: Path, content: str) -> None:
    """
    Create a new file in `path` with the content `content`.

    :param path: Valid path on the filesystem to write a file to.
    :type path: Path
    :param content: Content to write to the file.
    :type content: str
    """
    async with aiofiles.open(path, 'w') as f:
        await f.write(content)


async def read_file(path: Path) -> typing.List[str]:
    """
    Read and return the contents of the file in `path`.

    :param path: Valid path on the filesystem to read from.
    :type path: Path
    :return: Contents of the file in `path`.
    :rtype: typing.List[str]
    """
    async with aiofiles.open(path) as f:
        return await f.readlines()


async def copy_every_odd_line(read_path: Path, write_path: Path) -> None:
    """
    Read a file's contents and write only the odd lines to a new path.
    Notice that (sadly) we start to count line numbers from 1.

    :param read_path: Valid path on the filesystem to read from.
    :type read_path: Path
    :param write_path: Valid path on the filesystem to write to.
    :type write_path: Path
    """
    read_lines = await read_file(read_path)
    write_buffer = ''.join(read_lines[::2])
    await write_file(write_path, write_buffer)
