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

### Installation
1. Clone the repository<br>`git clone https://github.com/satoscio/shashin`
2. Create a virtual environment<br>`python3 -m venv <name>`
3. Install pip3<br>`python -m pip3 install --upgrade pip`
4. Install the required libraries<br>`pip3 install -r requirements.txt`
5. You're good to go!

### Usage
`python3 main.py <path/to/picture.jpg> [-c/--theme {dark, light}] [-t/--title "insert your title here"]`

Example:<br>
`python3 main.py /home/satoscio/pictures/japan-2024/JPN01843.jpg --theme light --title "出口を探している"`

## Notes

- This script has been written to work with my gear (Sony and Canon cameras), not everything might work well, open an issue to help me out :)
- This script will ONLY work with pictures that have been edited in Adobe Lightroom (other software MIGHT work)
- Fonts included with this repository are publicly available on Google Fonts

## TO-DO

- Italic Japanese text support
- Support (mostly formatting lol) for other camera and lens make and models
- Honestly, a lot, if you have suggestions you can open an issue