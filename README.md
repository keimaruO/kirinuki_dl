# yt-dlp_kirinukiとは

yt-dlpを使用して、切り抜き動画制作に特化したダウンローダー

あなたが望んでいるダウンロード形式の全てカスタムできます、ほんとになんでもできるかとおもいま

ちなみにデフォルトだと

- ライブ配信中に追いかけ録画
- 動画・音声だけDL
- 特定の範囲だけDL


デフォルトだと最高画質,画質でDLします。ファイル形式は動画ならmp4,音声ならwav

自分で好きなようにファイル形式、保存先変えれます。

※1時間で作ったのでおてやわらかに、でもくっそ便利なはず

# インストール方法

まず前提としてPythonをいれる必要があります。簡単です

> [Python](https://prog-8.com/docs/python-env-win)　※インストール方法が書いてあるサイト

## このプロジェクトをダウンロードする ※画像はこのページの上部です

![image](https://github.com/keimaruO/kirinuki_dl/assets/91080250/9f4d7d1e-f629-4af1-bf0a-692569d5f8b1)


次に

下記のリンクを開いてyt-dlp.exeをクリックでダウンロード

https://github.com/yt-dlp/yt-dlp/releases/

![image](https://github.com/keimaruO/kirinuki_dl/assets/91080250/ae976dc8-d68e-4b9d-89c4-5cf838cf5eda)


次に

下記のリンクを開いてffmpeg-n6.0-latest-win64-gpl-6.0.zipをクリックでダウンロード

https://github.com/yt-dlp/FFmpeg-Builds/releases/tag/latest

![image](https://github.com/keimaruO/kirinuki_dl/assets/91080250/5c309489-25c6-45f7-93f1-f0d8c36489dc)


そして上のやつでダウンロードしてきたの者たちを解凍し、下の画像のように配置すればOK

![image](https://github.com/keimaruO/kirinuki_dl/assets/91080250/0dc46007-870b-4394-a069-a5e2a13df082)



ショートカットをデスクトップとか、わかりやすいところに置いておいて下さい。ファイル名も自分がわかりやすいのに変えてもおｋ

# 使い方

!Audio.bat - ショートカット.lnk　とかのやつらをダブルクリックするとコマンドラインが開くのでそこにURLを貼り付けるだけ。ちな説明すると、.batを起動するためのショートカットです

※!Section.batの使い方だけちょい違う


## !Audio.bat

音声だけDL

## !Video.bat

動画だけDL

## !Live-wait.bat

ライブ配信追いかけDL

枠がたっていてまだ配信が開始してなくても、配信開始されると自動で録画してくれる

## !Section.bat　※ちょい使い方違う

指定した範囲だけをDL

dlurl.txtの1行目にURL、2行目に時間の範囲指定を書く。

で、

で、!Section.batを起動する

ちな、dlurl.txtに複数記入してもおｋ

- 1行目　URL
- 2行目　xx:xx-xx:xx
- 3行目　URL
- 4行目　xx:xx-xx:xx
- ...

って感じ

# カスタムのやり方

ファイル形式をmp3とかopusとかにしたい場合はそのコードを変更すればいいだけです。これまじで簡単です。

拡張子が.pyとなってるのがPythonのファイル形式で、メモ帳やテキストエディターでソースコードを開いてwavのところを変更すればおｋ

それ以外は、基本的にchatGPT君に〇〇のようにしたいんだけどって、ソースコードと一緒に要件をお願いすると書いてくれます

chatGPTのリンク貼っときます。https://chat.openai.com/

ではまた。

issueでもいいし、https://linktr.ee/keimaruのマシュマロでもTwitterでもいいのでなにかあれば気軽にどぞ
