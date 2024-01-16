# yt-dlp_kirinukiとは

yt-dlpを使用して、切り抜き動画制作に特化したダウンローダー

[yt-dlpとは? wiki](https://wiki.archlinux.jp/index.php/Yt-dlp#:~:text=yt%2Ddlp%E3%81%AF%E3%80%811000%E4%BB%A5%E4%B8%8A,%E3%81%A7%E3%81%8D%E3%82%8B%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E3%83%A9%E3%82%A4%E3%83%B3%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0%E3%81%A7%E3%81%99%E3%80%82)

あなたが望んでいるダウンロード形式の全てカスタムできます、基本的に思いつくことはなんでもあると思います、それぐらい機能が豊富です。

ちなみに下記の手順を進めていくと、最終的に下記の事ができます。

- ライブ配信中に追いかけ録画
- 動画・音声だけダウンロード(DL)
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

# 基本的な使い方

_Audio.bat　とか　_Video.batのやつらをダブルクリックするとコマンドラインが開くのでそこにURLを貼り付けてEnter押すだけ。

出力先はひとつ前の画像、そのばしょにあります。ダウンロードが終わった後は別の場所にバックアップするのが汚くならないのでおすすめです。

TwitterのスペースとかTwitchなどたしか1000以上のサイトに対応しいます。詳しくは　　yt-dlp  [あなたが知りたいこと]　　で検索　



## _Audio.bat

音声だけダウンロードします。出力はWAV

## _Video.bat

動画だけダウンロードします。出力はMP4

## _Live-wait.bat

ライブ配信中に追いかけダウンロード。出力はMP4

枠さえたっていれば配信が開始してなくても、配信開始されると自動でダウンロード開始する

## _Section.bat　※ちょい使い方違う

指定した時間範囲だけをダウンロード。

dlurl.txtの1行目にURL、2行目に時間の範囲指定を書く。

で、

で、_Section.batを起動する

ちな、dlurl.txtに複数記入してもおｋ

- 1行目　URL
- 2行目　xx:xx-xx:xx
- 3行目　URL
- 4行目　xx:xx-xx:xx
- ...

って感じ、この保存先は同じディレクトリのoutputフォルダ内に保存されます。

# カスタムのやり方

ファイル形式をmp3とかopusとかにしたい場合はそのコードを変更すればいいだけです。これまじで簡単です。

拡張子が.pyとなってるのがPythonのファイル形式で、メモ帳やテキストエディターでソースコードを開いてwavのところを変更すればおｋ

保存先変更したい場合や解像度など細かく変更したい場合

基本的にchatGPT君に〇〇のようにしたいんだけどって、ソースコードと一緒に要件をお願いすると書いてくれます

chatGPTのリンク貼っときます。https://chat.openai.com/

ではまた。

issueでもいいし、https://linktr.ee/keimaruのマシュマロでもTwitterでもいいのでなにかあれば気軽にどぞ！
