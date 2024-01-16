# yt-dlp_kirinukiとは

yt-dlpを使用して、切り抜き動画制作に特化したダウンローダー

[yt-dlpとは? wiki](https://wiki.archlinux.jp/index.php/Yt-dlp#:~:text=yt%2Ddlp%E3%81%AF%E3%80%811000%E4%BB%A5%E4%B8%8A,%E3%81%A7%E3%81%8D%E3%82%8B%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E3%83%A9%E3%82%A4%E3%83%B3%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0%E3%81%A7%E3%81%99%E3%80%82)

少しコマンドを加えるとあなたが望んでいるダウンロード形式に自由自在にカスタムできます。基本的に思いつくことはなんでも出来ます。それぐらい機能が豊富です。

ちなみに下記の手順を進めていくと、最終的に下記の事ができます。

- ライブ配信中に追いかけ録画
- 動画・音声だけダウンロード(DL)
- 特定の範囲だけDL


デフォルトだと最高画質/音質でDLします。出力されるファイル形式は動画ならmp4,音声ならwav

自分で好きなようにファイル形式、保存先変えれます。


# インストール方法

まず前提としてPythonをいれる必要があります。簡単です

> [Pythonインストール方法](https://prog-8.com/docs/python-env-win)

## このプロジェクトをダウンロードする ※画像はこのページの上部です

![image](https://github.com/keimaruO/kirinuki_dl/assets/91080250/9f4d7d1e-f629-4af1-bf0a-692569d5f8b1)


次に下記のリンクを開いてyt-dlp.exeをクリックでダウンロード

https://github.com/yt-dlp/yt-dlp/releases/

![image](https://github.com/keimaruO/kirinuki_dl/assets/91080250/ae976dc8-d68e-4b9d-89c4-5cf838cf5eda)


次に下記のリンクを開いてffmpeg-n6.0-latest-win64-gpl-6.0.zipをクリックでダウンロード

https://github.com/yt-dlp/FFmpeg-Builds/releases/tag/latest

![image](https://github.com/keimaruO/kirinuki_dl/assets/91080250/5c309489-25c6-45f7-93f1-f0d8c36489dc)


そして上のやつでダウンロードしてきたの者たちを解凍し、下の画像のように配置すればOK

![image](https://github.com/keimaruO/kirinuki_dl/assets/91080250/0dc46007-870b-4394-a069-a5e2a13df082)



ショートカットをデスクトップとか、わかりやすいところに置いておいて下さい。

# 基本的な使い方

_Audio.bat　とか　_Video.batのやつらをダブルクリックするとコマンドラインが開くのでそこにURLを貼り付けてEnter押すだけ。

動画をダウンロードしたい時は。

１ －　_Section.batを起動する

２ －　ダウンロードしたいURLを貼り付けてEnter❣

３ －　ダウンロードが完了したら閉じて大丈夫です。ファイルは同じ場所に出力されます。


出力先はひとつ前の画像、そのばしょにあります。ダウンロードが終わった後は別の場所にバックアップするのが汚くならないのでおすすめです。
　



## _Audio.bat

- 何をするか：音声だけダウンロードします。出力はWAV

## _Video.bat

- 何をするか：動画だけダウンロードします。出力はMP4

## _Live-wait.bat

- 何をするか：ライブ配信中に追いかけダウンロード。出力はMP4

枠さえたっていれば配信が開始してなくても、配信開始されると自動でダウンロード開始する

## _Section.bat　※使い方少し違う

- 何をするか：指定した時間範囲だけをダウンロード。

#### 使い方

１ －　dlurl.txtをメモ帳などで開き、1行目にURL、2行目に時間の範囲指定を書く。

２ －　書いたら　_Section.batを起動する

３ －　保存先は同じディレクトリのoutputフォルダ内に保存されてます。

以上。

ちなみに、dlurl.txtに複数記入してもおｋ

- 1行目　URL
- 2行目　xx:xx-xx:xx
- 3行目　URL
- 4行目　xx:xx-xx:xx
- ...

# カスタムのやり方

ファイル形式をmp3とかopusとかにしたい場合はそのコードを変更すればいいだけです。これまじで簡単です。

拡張子が.pyとなってるのがPythonのファイル形式で、メモ帳やテキストエディターでソースコードを開いてwavのところを変更すればおｋ

保存先変更したい場合や解像度など細かく変更したい場合

基本的にchatGPT君に〇〇のようにしたいんだけどって、ソースコードと一緒に要件をお願いすると書いてくれます

chatGPTのリンク貼っときます。https://chat.openai.com/

ではまた。

issueでもいいし、https://linktr.ee/keimaruのマシュマロでもTwitterでもいいのでなにかあれば気軽にどぞ！
