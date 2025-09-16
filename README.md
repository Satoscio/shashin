# Shashin
__From Japanese: 写真, picture.__

## Overview
Shashin is a simple Python script that extracts EXIF data from JPG photos and adds a frame containing exposure information, copyright and an optional title.

This is a "fork" from an upublished version of [Exentio](https://github.com/exentio)'s 'Ganta', which itself was inspired by [yurucam](https://github.com/yurucam)'s [exif-frame](https://github.com/yurucam/exif-frame).

## Sample images
### Horizontal
Light theme | Dark theme
:----------:|:---------:
![](https://fumetteria.moe/img/shashin/h-light.jpg) | ![](https://fumetteria.moe/img/shashin/h-dark.jpg)
### Vertical
Light theme | Dark theme
:----------:|:---------:
![](https://fumetteria.moe/img/shashin/v-light.jpg) | ![](https://fumetteria.moe/img/shashin/v-dark.jpg)

## Setup

### Requirements
- Python 3.x (not sure which one tbh)
- Python 3 PIP

### Windows
1. Install [Git](https://git-scm.com/downloads), [Python 3](https://python.org/downloads) and the [Visual C++ 2022 redistributable (direct Microsoft link)](https://aka.ms/vs/17/release/VC_redist.x64.exe)
2. Clone the repository<br>`git clone https://github.com/satoscio/shashin` and `cd` into it
3. Create a virtual environment<br>`python -m venv <name>`
4. Enable the virtual environment<br>`<name>\Scripts\activate.bat`
5. Install the required libraries<br>`pip3 install -r requirements.txt`
6. You're good to go!

### Linux
1. Install `git`, `python3-pip` and `python3-venv` (or `python-pip` and `python-venv`, depends on you distro) via your distro's package manager.
2. Clone the repository<br>`git clone https://github.com/satoscio/shashin` and `cd` into it
3. Create a virtual environment<br>`python3 -m venv <name>`
4. Enable the virtual environment<br>`source <name>\bin\activate` (or `activate.fish` if you use the fish shell)
5. Install the required libraries<br>`python3 -m pip install -r requirements.txt`
6. You're good to go!

### macOS

1. Install [Homebrew](https://brew.sh/)
2. Install `python3`, `git` and `inih` from Homebrew
3. Clone the repository<br>`git clone https://github.com/satoscio/shashin` and `cd` into it
4. Create a virtual environment<br>`python3 -m venv <name>`
5. Enable the virtual environment<br>`source <name>\bin\activate`
6. Install the required libraries<br>`python3 -m pip install -r requirements.txt`
7. You're good to go!

Figure it out yourself, rich kid

## Usage
`python3 main.py <path/to/picture.jpg> [-c/--theme {dark, light}] [-t/--title "insert your title here"]`

Example:<br>
`python3 main.py /home/satoscio/pictures/japan-2024/JPN01843.jpg --theme light --title "出口を探している"`

- This script has been written to work with my gear (Sony and Canon cameras), not everything might work well, open an issue to help me out :)
- This script will ONLY work with pictures that have been edited in Adobe Lightroom (other software MIGHT work)
- Fonts included with this repository are publicly available on Google Fonts

## TO-DO

- Italic Japanese text support
- Support (mostly formatting lol) for other camera and lens make and models
- Honestly, a lot, if you have suggestions you can open an issue