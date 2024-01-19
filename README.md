# yt-dlp_kirinukiとは

yt-dlpを使用して、切り抜き動画制作に特化したダウンローダー

<br>

[yt-dlpとは? wiki](https://wiki.archlinux.jp/index.php/Yt-dlp#:~:text=yt%2Ddlp%E3%81%AF%E3%80%811000%E4%BB%A5%E4%B8%8A,%E3%81%A7%E3%81%8D%E3%82%8B%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E3%83%A9%E3%82%A4%E3%83%B3%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0%E3%81%A7%E3%81%99%E3%80%82)

<br>

少しソースコード編集すれば自由自在にカスタムすることもできます。
<br>
<br>
ちなみに下記の手順を進めていくと、最終的に下記の事ができます。

<br>

- [x] **ライブ配信中に追いかけ録画**
- [x] **動画・音声だけダウンロード(DL)**
- [x] **特定の範囲だけDL**
- [x] **チャンネルすべての動画をダウンロード メン限も可**

<br>

デフォルトで最高画質/音質でダウンロードします。出力されるファイル形式は動画ならmp4　音声ならwav

後から自分で好きなようにファイル拡張子や保存先なども変えれます。

<br>
<br>
<br>

**追記：ダウンロードをする前に、保存先を指定できるverも作りました。**

毎回、ダウンロード先を決めてからDLしたい場合こちらをお使いください。

https://github.com/keimaruO/kirinuki_dl_v1.0.1-beta

<br>
<br>
<br>

※保存先を指定できるverとこのプロジェクト(保存先を指定しないver)を別々のに分けた理由は、効率厨のワイ個人的にはこちらの方が同ディレクトリで完結してるから、ファイル間の移動がなく、効率良くて便利だと思ったからです、、！ｗ

<br>
<br>

# インストール方法

## １　まず前提としてPythonを導入してください。所要時間は6分ほど？

<br>
<br>
<br>

[Pythonのインストール方法](https://prog-8.com/docs/python-env-win)

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
<br>
<br>




**例 ： 動画をダウンロードしたい時。**

```bash
> １ －　_Video.batを起動する

> ２ －　URLを貼り付けてEnter

> ３ －　ダウンロードが完了したら閉じる。
```

<br>
<br>

**例 ： 指定した時間範囲をダウンロードしたい時。**

```bash
> １ －　dlurl.txtをメモ帳などで開き、1行目にURL、2行目に時間の範囲指定を書く。

> ２ －　_Section.batを起動する
 
> ３ －　ダウンロードが完了したら閉じる。保存先はoutputフォルダ内に保存されてます。


```

<br>
<br>

ちなみに、dlurl.txtに複数記入してもおｋ
```bash
1行目　URL
2行目　xx:xx-xx:xx
3行目　URL
4行目　xx:xx-xx:xx
...
```

<br>
<br>

**_Live-wait.bat**

```bash
枠さえたっていれば配信が開始してなくても、配信開始されると自動でダウンロード開始する
```
<br>
<br>
<br>

ファイル名 | 何をする | 出力形式
-----------| ------------| ------------
_Audio.bat | 音声のみDL | WAV
_Video.bat | 動画のみDL | MP4
_Live-wait.bat | ライブ配信中の動画を追いかけてDL | MP4
_Section.bat | 指定した時間範囲のみをDL | MP4

<br>
<br>
<br>

# チャンネルの全動画をダウンロードする方法

![4](https://github.com/keimaruO/kirinuki_dl/assets/91080250/bb1d492c-faf7-4e1e-83e8-cdc8c17a6a44)

※エクスプローラー上部にあるURLみたいなところを押して、cmdと入力してEnterを押すと。そのフォルダパスでコマンドプロンプトが開きます。

<br>
<br>

## コマンド

<br>
<br>

`yt-dlp [チャンネルURL]`　を入力すると全ての動画がダウンロードされます。　　※メン限は含まない

<br>

**例 ：　チャンネル全部の動画をダウンロード**　※メン限は含まない

```bash
yt-dlp https://www.youtube.com/@MomosuzuNene/videos
```

<br>
<br>
<br>
<br>


**例 ：　チャンネル全部のライブをダウンロード**　※メン限は含まない

```bash
yt-dlp https://www.youtube.com/@MomosuzuNene/streams
```

<br>
<br>
<br>
<br>

**例 ：　再生リストをダウンロードしたい場合**　※メン限は含まない

```bash
yt-dlp https://www.youtube.com/playlist?list=UUMOAWSyEs_Io8MtpY3m-zqILA
```

<br>
<br>
<br>
<br>
<br>

**例 ：　メンバー限定の動画をダウンロードしたい場合**

Chromeの場合
```
yt-dlp --cookies-from-browser chrome https://www.youtube.com/playlist?list=UUMOAWSyEs_Io8MtpY3m-zqILA
```

<br>

Firefoxの場合
```
yt-dlp --cookies-from-browser firefox https://www.youtube.com/playlist?list=UUMOAWSyEs_Io8MtpY3m-zqILA
```

<br>

※ワイのPC環境だとChromeのコマンドはうまく機能しませんでした、うまくいかない場合はFirefoxでお試しください。

<br>
<br>
<br>
<br>


基本的に`yt-dlp --cookies-from-browser firefox`の後ろにチャンネルの動画URLか、liveのURL、再生リストのURLを貼ればメン限動画もDLされると思います。

![image](https://github.com/keimaruO/kirinuki_dl/assets/91080250/217a0cbe-febc-45e2-b88e-0374bd7c67e4)

ダウンロードしたいやつを選択してURLをコピーすればshortsでも同様にいけます。　URLがshortsとかstreamsが変わるだけだけど。手で変更しても全然良いw

<br>
<br>

> [!NOTE]  
> もしダウンロード中に中断されてしまったりエラーが出た場合は`[チャンネルURL]`ところを`[再生リストのURL]`にすると再生リストの順番でダウンロードされます。
> 初めから再生リストでやると失敗する前提だったら再開しやすいのかも？です。
> 
> 一つ一つ再生リストにぶちこむのめんどいので、この拡張機能を活用してみてください。超効率よく再生リストが作れます。
> 
> [YouTube™ の複数選択 Chrome拡張機能](https://chromewebstore.google.com/detail/youtube-%E3%81%AE%E8%A4%87%E6%95%B0%E9%81%B8%E6%8A%9E/gpgbiinpmelaihndlegbgfkmnpofgfei?hl=ja)
> 
> <br>
> そしてもう一つおすすめの拡張機能を紹介します。
>
> チャンネルページで拡張機能をクリックするとチャンネル全てのメン限動画を全てまとめた再生リストを表示できます。
> 
> [メン限動画プレイリストView](https://chromewebstore.google.com/detail/%E3%83%A1%E3%83%B3%E9%99%90%E5%8B%95%E7%94%BB%E3%83%97%E3%83%AC%E3%82%A4%E3%83%AA%E3%82%B9%E3%83%88view/alipjbeolhembeklphfcehbkgncdlnom)


<br>
<br>
<br>
<br>
<br>
<br>



# その他、自分好みにカスタムする方法

基本的にchatGPT君に〇〇のようにしたいんだけどって、ソースコードと一緒に要件をお願いすると書いてくれます。

chatGPTのリンク貼っときます。https://chat.openai.com/

<br>

ファイル形式をmp3とかopusとか出力ファイルを特定の拡張子にしたい場合は.pyそのコードを変更すればいいだけです。

拡張子が.pyとなってるのがソースコードで、メモ帳やテキストエディターを開いてwavのところを変更すればおｋ

ソースコードをバッチファイルで簡単に実行できるようにしてるので自由自在にソースコード変えれば色々できます。


質問などはissueでもOKです。https://linktr.ee/keimaruのマシュマロでもTwitterでもいいのでなにかあれば気軽にどぞ！
