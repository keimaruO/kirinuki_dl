import os
import subprocess
import sys

def main(url):
    cmd = " ".join([
        "yt-dlp",
        "-f", "\"bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]\"",
        "-N", "1",
        "-S", "vcodec:h264",
        "-o", "%(title)s.%(ext)s",
        url
    ])

    print("Executing command:", cmd)
    subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    main(sys.argv[1])
