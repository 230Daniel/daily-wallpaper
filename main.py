import ctypes
from pathlib import Path

import requests


def get_wallpaper_url():
    response = requests.get("https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US")
    response.raise_for_status()
    return "https://www.bing.com" + response.json()["images"][0]["url"]


def download_wallpaper(image_url):
    filename = f"{Path.home()}\\Pictures\\DailyWallpaper.jpg"
    response = requests.get(image_url)
    with open(filename, "wb") as file:
        file.write(response.content)
    return filename


def set_wallpaper(filename):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filename, 0)


def main():
    wallpaper_url = get_wallpaper_url()
    filename = download_wallpaper(wallpaper_url)
    set_wallpaper(filename)


if __name__ == "__main__":
    main()
