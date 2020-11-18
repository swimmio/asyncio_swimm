# `asyncio` Public Swimm Playlists

## Playlists Overview

The Playlists in this repo are supposed to present bite-sized exercises (or as we in Swimm call them, _Units_) that give you the building blocks necessary to create more complicated scripts and projects later on.
As a bonus and to ease your progress as you slowly "learn to swim", the Playlists will follow the whimsical tale of a developer (you!) applying to their dream job at a record store, so you won't feel alone as you start to dive deeper into material.

### Unit Structure

Before you take your first few steps it's important to set our expectations:

* Each Unit you will be asked to make some tests pass (use `swimm test` as a shortcut for that) and will be presented with the files necessary for you to edit after you `swimm play`.
* The **technical specifications** of what you need to achieve will be written as docstrings inside the **code itself**.
* The Units descripions themselves will not focus on teaching new `SQLAlchemy` concepts, but instead will offer some _"Recommended References"_ that will help you solve this specific challenge. We encourage you to search online and dive deeper on your own!

## Prerequisites

* Basic Python knowledge.

## Setup

There are several things you need in order to run the relevant tests for the unit in this repo:

* Have the `python` command in your path, which will point to version `X` of Python where `X>=3.8`.
* Have `aiofiles` installed in your Python environment.
* Have `pytest` installed in your Python environment.

We recommend using [`Pipenv`](https://github.com/pypa/pipenv) in order to setup a virtual environment that satisfies all of the requirements above (although a classic [`requirements.txt`](./requirements.txt) is also provided).
