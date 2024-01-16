# yt-dlp_kirinukiとは

yt-dlpを使用して、切り抜き動画制作に特化したダウンローダー

[yt-dlpとは? wiki](https://wiki.archlinux.jp/index.php/Yt-dlp#:~:text=yt%2Ddlp%E3%81%AF%E3%80%811000%E4%BB%A5%E4%B8%8A,%E3%81%A7%E3%81%8D%E3%82%8B%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E3%83%A9%E3%82%A4%E3%83%B3%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0%E3%81%A7%E3%81%99%E3%80%82)
<br>
<br>
<br>
少しコマンドを加えるとあなたが望んでいるダウンロード形式に自由自在にカスタムできます。基本的に思いつくことはなんでも出来ます。それぐらい機能が豊富です。
<br>
<br>
ちなみに下記の手順を進めていくと、最終的に下記の事ができます。

- [x] ライブ配信中に追いかけ録画
- [x] 動画・音声だけダウンロード(DL)
- [x] 特定の範囲だけDL
- [x] チャンネルすべての動画をダウンロード


デフォルトで最高画質/音質でダウンロードします。出力されるファイル形式は動画ならmp4　音声ならwav

後から自分で好きなようにファイル拡張子や保存先なども変えれます。

<br>
<br>
<br>


# インストール方法

## １　まず前提としてPythonをいれる必要があります。所要時間は8分ぐらい？

<br>
<br>
<br>
-  [Pythonインストール方法](https://prog-8.com/docs/python-env-win)
<br>
<br>
<br>

<br>
<br>

## ２　次に、このプロジェクトを当ページ上部からダウンロードする

![image](https://github.com/keimaruO/kirinuki_dl/assets/91080250/9f4d7d1e-f629-4af1-bf0a-692569d5f8b1)

<br>
<br>
<br>

## ３　次に、下記リンクを開いて`yt-dlp.exe`をクリックし、ダウンロード

https://github.com/yt-dlp/yt-dlp/releases/

<br>

![image](https://github.com/keimaruO/kirinuki_dl/assets/91080250/ae976dc8-d68e-4b9d-89c4-5cf838cf5eda)

<br>
<br>

## ４　次に、下記リンクを開いて`ffmpeg-n6.0-latest-win64-gpl-6.0.zip`をダウンロード

https://github.com/yt-dlp/FFmpeg-Builds/releases/tag/latest

<br>

![image](https://github.com/keimaruO/kirinuki_dl/assets/91080250/5c309489-25c6-45f7-93f1-f0d8c36489dc)

<br>
<br>

## ５　次に、ダウンロードしてきた３つのファイルを解凍する。画像のように配置すればOK

<br>

![image](https://github.com/keimaruO/kirinuki_dl/assets/91080250/0dc46007-870b-4394-a069-a5e2a13df082)

※上部に5つあるショートカットと書いてあるファイルは無視してください。

<br>
<br>
<br>
<br>

# 基本的な使い方

<br>

 _Audio.bat　とか _Video.batをダブルクリックしてコマンドラインを開き、URLを貼り付けてEnterを押せばOK
 
<br>

_Section.batは先にdlurl.txtをメモ帳などで開き、URLと時間範囲を指定する必要があります。

<br>
<br>
<br>
<br>
<br>

> 例　：　動画をダウンロードしたい時。

１ －　_Section.batを起動する

２ －　ダウンロードしたいURLを貼り付けてEnter❣

３ －　ダウンロードが完了したら閉じて大丈夫です。ファイルは同じ場所に出力されます。

<br>
<br>

出力先はひとつ前の画像、そのばしょにあります。ダウンロードが終わった後は別の場所にバックアップするのが汚くならないのでおすすめです。
　
<br>
<br>
<br>
<br>
<br>
<br>



# 詳しい使い方

## _Audio.bat

- 音声のみダウンロード（出力はWAV）

## _Video.bat

- 動画のみダウンロード（出力はMP4）

## _Live-wait.bat

- ライブ配信中の動画を追いかけてダウンロード（出力はMP4）

枠さえたっていれば配信が開始してなくても、配信開始されると自動でダウンロード開始する

## _Section.bat　※使い方少し違う

- 指定した時間範囲のみをダウンロード

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

# 全チャンネルの動画をダウンロードする方法

![4](https://github.com/keimaruO/kirinuki_dl/assets/91080250/bb1d492c-faf7-4e1e-83e8-cdc8c17a6a44)

エクスプローラー上部にあるURLみたいなところを押して、cmdと入力してEnterを押すと。そのフォルダパスでコマンドプロンプトが開きます。

そして　yt-dlp [チャンネルURL]　を入力すると全ての動画がダウンロードされます。※メン限は含まない

## 例 ：　動画をダウンロードしたい場合

```
yt-dlp https://www.youtube.com/@MomosuzuNene
```

基本的にはないですが、もしダウンロード中に中断されてしまったり、エラーが出た場合は[チャンネルURL]ところを再生リストのURLにすると再生リストの順でダウンロードされます。

初めから再生リストでやると失敗した際に再開しやすいのかも？です。

[YouTube™ の複数選択 Chrome拡張機能](https://chromewebstore.google.com/detail/youtube-%E3%81%AE%E8%A4%87%E6%95%B0%E9%81%B8%E6%8A%9E/gpgbiinpmelaihndlegbgfkmnpofgfei?hl=ja)

1つ1つ再生リストにぶちこむのめんどいので、この拡張機能を活用してみてください。

## メンバー限定の動画をダウンロードしたい場合

メンバーに加入しているブラウザを指定するだけでいけます。※メンバーに加入してない場合はもちろんできません。

例：Chromeの場合
```
yt-dlp --cookies-from-browser firefox https://www.youtube.com/playlist?list=UUMOAWSyEs_Io8MtpY3m-zqILA
```

例：Firefoxの場合
```
yt-dlp --cookies-from-browser firefox https://www.youtube.com/playlist?list=UUMOAWSyEs_Io8MtpY3m-zqILA
```

※ワイのPC環境だとChromeのコマンドがうまく機能しませんでした、うまくいかない場合はFirefoxでお試しください。





# その他、自分好みにカスタムする方法

ファイル形式をmp3とかopusとかにしたい場合は.pyそのコードを変更すればいいだけです。これまじで簡単です。

拡張子が.pyとなってるのがPythonのファイル形式で、メモ帳やテキストエディターでソースコードを開いてwavのところを変更すればおｋ

保存先変更したい場合や解像度など細かく変更したい場合

基本的にchatGPT君に〇〇のようにしたいんだけどって、ソースコードと一緒に要件をお願いすると書いてくれます

chatGPTのリンク貼っときます。https://chat.openai.com/

ではまた。

質問などはissueでもOKです。https://linktr.ee/keimaruのマシュマロでもTwitterでもいいのでなにかあれば気軽にどぞ！
