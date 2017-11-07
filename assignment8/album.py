import re
import os

FILENAME_RE = re.compile(
    r"^.*?(?P<track>\d+)\.?\W(?P<artist>.+?)?\W?-\W(?P<title>.+)\..{3}",
    re.MULTILINE | re.UNICODE
)


def tracklisting(path):
    # Extract meta information for all files in the given directory
    album = [
        FILENAME_RE.search(filename).groupdict()
        for filename in os.listdir(path)
    ]

    # Sort by track number
    formated_songs = []
    for song_meta in sorted(album, key=lambda song: song['track']):
        song_meta['track'] = int(song_meta['track'])
        formated_songs.append("{track:2d} {title}".format(**song_meta))

    return "\n".join(formated_songs)
