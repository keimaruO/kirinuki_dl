import os
import subprocess
import sys

def main(url):
    cmd = " ".join([
        "yt-dlp",
        "-f", "\"bestaudio/best\"",
        "--extract-audio",
        "--audio-format", "wav",
        "-o", "%(title)s.%(ext)s",
        url
    ])

    print("Executing command:", cmd)
    subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    main(sys.argv[1])
