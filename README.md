# Ultimate tic-tac-toe

♟️ Ultimate tic-tac-toe game GUI application using Python and PyGame

<p align=center>
  <img src="https://github.com/user-attachments/assets/c6fd92b5-f10a-4507-8627-4acdddd829ba">
</p>

<p align=center>
  <a href="https://github.com/jcbhmr/ultttt/blob/main/py%20project%20prop.pdf">Project proposal</a>
  | <a href="https://github.com/jcbhmr/ultttt/blob/main/py%20proj%20pres.pdf">Presentation PDF</a>
  | <a href="https://www.youtube.com/watch?v=NhmhWXjxfqU">Presentation video</a>
</p>

🎨 Has a GUI! \
🤖 Uses GitHub Actions to produce PyInstaller binaries \
🏫 Made for UW-Whitewater Introduction to Python Programming final project \
🧠 Learned about [uv](https://docs.astral.sh/uv/)

## Installation

![GitHub](https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=181717&logo=GitHub&logoColor=FFFFFF&label=)
![PyPI](https://img.shields.io/static/v1?style=for-the-badge&message=PyPI&color=3775A9&logo=PyPI&logoColor=FFFFFF&label=)

The best way to install this application is to download the platform-specific precompiled binary from [the latest release](https://github.com/jcbhmr/ultttt/releases/latest).

<dl>
<dt>Windows x86-64
<dd>https://github.com/jcbhmr/ultttt/releases/download/v1.0.0/ultttt-win_amd64-1.0.0.zip
<dt>macOS x86-64
<dd>https://github.com/jcbhmr/ultttt/releases/download/v1.0.0/ultttt-macosx_10_9_x86_64-1.0.0.tar.gz
<dt>macOS AArch64
<dd>https://github.com/jcbhmr/ultttt/releases/download/v1.0.0/ultttt-macosx_11_0_arm64-1.0.0.tar.gz
<dt>Linux x86-64
<dd>https://github.com/jcbhmr/ultttt/releases/download/v1.0.0/ultttt-linux_x86_64-1.0.0.tar.gz
</dl>

This package is also published to PyPI if you prefer to install it from there:

```sh
uv tool install ultttt
```

## Presentation

We were tasked with making a presentation describing the code to submit in addition to just the code.

[![image](https://github.com/user-attachments/assets/fc0f6925-eb26-4ebb-8906-4cea344e486b)](https://www.youtube.com/watch?v=NhmhWXjxfqU)
[ultttt presentation & demo | YouTube](https://www.youtube.com/watch?v=NhmhWXjxfqU)

## Development

![Python](https://img.shields.io/static/v1?style=for-the-badge&message=Python&color=3776AB&logo=Python&logoColor=FFFFFF&label=)
![uv](https://img.shields.io/static/v1?style=for-the-badge&message=uv&color=DE5FE9&logo=uv&logoColor=FFFFFF&label=)

This project uses [uv](https://docs.astral.sh/uv/) as its Python toolchain. Why uv and not Poetry or something else? Because uv unifies everything _including installing the right Python version_. uv is [not a task runner yet](https://github.com/astral-sh/uv/issues/5903) and as such we use [Poe the Poet](https://poethepoet.natn.io/) to define our tasks.

The most interesting thing to do is build the `ultttt` executable binary using [PyInstaller](https://pyinstaller.org/):

```sh
uv run poe build-exe
```

Release process:

1. Change the version in `pyproject.toml`
2. Change the URLs in the readme to match the new version that you are about to release
3. Run the release workflow manually
4. Make sure it looks good
5. Publish the release to trigger the PyPI release workflow
6. Make sure that works and you're done! 🎉
