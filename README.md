# yt-dlp_kirinukiとは

yt-dlpを使用して、切り抜き動画制作に特化したダウンローダー

基本あなたが望んでいるダウンロード形式の全てできます、ほんとになんでもできます。

ちなみにデフォルトだと

- ライブ配信中に追いかけ録画
- 動画・音声だけDL
- 特定の範囲だけDL


デフォルトだと最高画質最高画質でDLします。ファイル形式は動画ならmp4,音声ならwav

自分で好きなようにファイル形式、保存先変えれます。

# インストール方法

矢印のをダウンロードして、展開 ※画像はこのページの上部です

![image](https://github.com/keimaruO/kirinuki_dl/assets/91080250/df0e07ee-db73-4154-be3a-e5328d2927f3)


次に

下記のリンクを開いてyt-dlp.exeをクリックでダウンロード

https://github.com/yt-dlp/yt-dlp/releases/

![image](https://github.com/keimaruO/kirinuki_dl/assets/91080250/fca104af-6d5e-4cfb-86d7-671e51e5886f)

次に

下記のリンクを開いてffmpeg-n6.0-latest-win64-gpl-6.0.zipをクリックでダウンロード

https://github.com/yt-dlp/FFmpeg-Builds/releases/tag/latest

![image](https://github.com/keimaruO/kirinuki_dl/assets/91080250/004ffaa4-780c-45f4-a423-378238340c98)

そしてダウンロードしてきたのを解凍し、下の画像のように配置すればOK

![image](https://github.com/keimaruO/kirinuki_dl/assets/91080250/0b1172b5-80c6-42f3-864f-eac56cd35197)


# 使い方

ショートカットをデスクトップとか、わかりやすいところに置いておいて下さい。ファイル名も自分がわかりやすいのに変えてもおｋ

- !Audio.bat - ショートカット.lnk

wavで音声だけDL

- !Live-wait.bat - ショートカット.lnk

ライブ追いかけmp4でDL。枠がたっていてまだ配信が開始してなくても、配信開始されると自動で録画してくれる

- !Section.bat - ショートカット.lnk

指定した範囲をDL。dlurl.txtの1行目にURL、2行目に時間の範囲指定をすればその箇所だけDL、dlurl.txtに複数記入しても

- !Video.bat - ショートカット.lnk

mp4で動画だけDL
