"""
This script allows to download a youtube video preview by its link
"""
import requests as r
import re


def main() -> None:
    url = input('URL: ')
    download(get_video_id(url))


def get_video_id(url: str) -> str:
    """
    The function extract a youtube video identifier

    Args:
        url (str): This is a video link

    Returns:
        (str): A video identifier
    """

    if 'index' in url:
        return re.findall(r".+=(.{11})&", url)[0]

    return url[-11:]
    # return re.findall(r".+[shorts | be]/(.{11})", url)[0]


def download(video_id: str) -> None:
    """
    The function download a youtube video preview by its identifier

    Args:
        video_id (str): This is a video identifier

    Returns:
        None
    """

    data = r.get(f'https://img.youtube.com/vi/{video_id}/maxresdefault.jpg')

    if data.status_code == 200:
        with open(f'image-{video_id}.jpg', 'wb') as file:
            file.write(data.content)

    return data.status_code



if __name__ == '__main__':
    main()
