import os
import subprocess
import tkinter as tk
from tkinter import filedialog
import sys

def main(url):
    # ダウンロード先のディレクトリを選択
    root = tk.Tk()
    root.withdraw()  # メインウィンドウを表示しない
    download_dir = filedialog.askdirectory(title="ダウンロード先を選択してください")

    # ダウンロード先のディレクトリが選択されなかった場合は終了
    if not download_dir:
        print("ダウンロード先が選択されていません。プログラムを終了します。")
        sys.exit(1)

    cmd = [
        "yt-dlp",
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
        "--live-from-start",
        "--wait-for-video", "10",
        "-o", os.path.join(download_dir, "%(title)s.%(ext)s"),  # パスを指定
        "-S", "vcodec:h264",
        url
    ]

    print("Executing command:", " ".join(cmd))
    subprocess.run(cmd)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("URLが指定されていません。プログラムを終了します。")
        sys.exit(1)

    main(sys.argv[1])
