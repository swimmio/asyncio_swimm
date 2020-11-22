# `asyncio` Public Swimm Playlists

## `asyncio`?

From the [official Python docs](https://docs.python.org/3/library/asyncio.html):
> `asyncio` is a library to write concurrent code using the `async/await` syntax.

`asyncio` is our way as Python developers to interface with the asynchronous capabilities of the language, giving us the power to boost our performance and make our code utilize it's processing resources to their fullest.
As it name might suggest, `asyncio` shines brightest when our code is I/O bound and not CPU bound, given how we can concurrently await on multiple I/O operations such as network requests or filesystem usage (in contrast to a CPU heavy program that is already using it's time to run our code without waiting).

If all of this sounds confusing to you, you came to the right place! This is the perfect opportunity for you to realize the potential of `asyncio` and asynchronous programming!

## Playlists Overview

The Playlists in this repo are supposed to present bite-sized exercises (or as we in Swimm call them, _Units_) that give you the building blocks necessary to create more complicated scripts and projects later on.

### Unit Structure

Before you take your first few steps it's important to set our expectations:

* In each Unit, you will be asked to make some tests pass (use `swimm test` as a shortcut for that) and will be presented with the files necessary for you to edit after you `swimm play`.
* The **technical specifications** of what you need to achieve will be written as docstrings inside the **code itself**.
* The Units' descripions themselves will not focus on teaching `asyncio` concepts, but instead will offer some _"Recommended References"_ that will help you solve each specific challenge. We encourage you to search online and dive deeper on your own!

## Prerequisites

* Basic Python knowledge.

## Setup

There are several things you need in order to run the relevant tests for the unit in this repo:

* Have the `python` command in your path, which will point to version `X` of Python where `X>=3.8`.
* Have `aiofiles` installed in your Python environment.
* Have `pytest` installed in your Python environment.

We recommend using [`Pipenv`](https://github.com/pypa/pipenv) in order to setup a virtual environment that satisfies all of the requirements above (although a classic [`requirements.txt`](./requirements.txt) is also provided).
