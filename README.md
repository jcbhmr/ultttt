# Ultimate tic-tac-toe

♟️ Ultimate tic-tac-toe game GUI application using Python and PyGame

<p align=center>
  <img src="">
</p>

## Installation

TODO

## Development

This project uses [uv]() as its Python toolchain. Why uv and not Poetry or something else? Because uv unifies everything _including installing the right Python version_. uv is [not a task runner yet](https://github.com/astral-sh/uv/issues/5903) and as such we use [Poe the Poet](https://poethepoet.natn.io/) to define our tasks.

The most ineteresting thing to do is build the `ultttt` executable binary using [PyInstaller](https://pyinstaller.org/):

```sh
uv run poe build-exe
```
