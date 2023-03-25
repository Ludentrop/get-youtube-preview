from get_youtube_preview import *


WHITE = "\033[00m"
GREEN = "\033[0;92m"
RED = "\033[1;31m"

with open('urls.txt') as file:
    for line in file:
        if download(get_video_id(line.rstrip())) == 200:
            print(f'{GREEN}[+]{WHITE} Successfully downloaded')
        else:
            print(f'{RED}[+]{WHITE} Download failed: invalid link: {line.rstrip()}')
