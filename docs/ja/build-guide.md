# exe 作成ガイド（最初から最後まで順番に）

[빌드가이드.md](../ko/빌드가이드.md) · [build-guide.md](../en/build-guide.md) · [build-guide.md](build-guide.md) · [build-guide.md](../zh-CN/build-guide.md)

> このガイドは **MyPass.exe を作る人** 向けです。（1台のPCで1回だけ行えばOKです）
> 作られたexeを使う人はPythonは不要です。→ `설치가이드.ja.md` を参照
> 以下の手順を **上から順番にそのまま** 進めてください。`このような字体`はそのまま入力するコマンドです。

所要時間：初回は約10〜15分（ほとんどがインストールとダウンロードの時間）
必要なもの：Windows 10/11 PC、インターネット接続

---

## 1段階. Python をインストールする

1. インターネットブラウザーで **https://www.python.org/downloads/** を開きます。
2. 黄色いボタン **`Download Python 3.x.x`** を押してインストールファイルを取得します。（3.10以上ならどのバージョンでもOKです）
3. 受け取ったファイル（`python-3.x.x-amd64.exe`）をダブルクリックして実行します。
4. 最初の画面の **一番下** にある **`Add python.exe to PATH`** のチェック欄を **必ずチェック** します。← 最も重要
5. **`Install Now`** を押します。（権限確認画面が出たら「はい」）
6. `Setup was successful` と表示されたら **`Close`** を押します。

### インストール確認
1. キーボードで **`Windows キー + R`** を押し、入力欄に `cmd` と入力して Enter → 黒い画面（コマンドプロンプト）が開きます。
2. 以下を入力して Enter：

   `python --version`

3. `Python 3.12.x` のようにバージョンが表示されれば成功です。黒い画面は閉じてOKです。（`exit` と入力後 Enter）

> `Python was not found` と表示されたり、Microsoft Storeが開く場合 → 一番下の **[トラブルシューティング1番]** を参照してください。

---

## 2段階. 作業フォルダーを作ってファイルを入れる

1. エクスプローラーで **Cドライブ** に `mypass_build` フォルダーを新規作成します。→ `C:\mypass_build`
   （日本語・空白のない短いパスを使うとエラーが少なくなります。**別のフォルダーに展開してもかまいません**。その場合、以下の `C:\mypass_build` は「自分がファイルを入れたフォルダー」と読み替えてください。成果物はそのフォルダー内の `dist\MyPass.exe` です。）
2. 受け取った `mypass_package.zip` を展開します。（zipを右クリック → `展開` または `すべて展開`）
3. 展開すると `mypass` フォルダーが出てきます。その **中のファイル** を `C:\mypass_build` の中に移動します。
4. `C:\mypass_build` を開いたときに **以下の項目がすぐ見える** 状態である必要があります。（フォルダーの中のフォルダーではなく、このフォルダーの直下に）

   - `mypass.py`
   - `mypass_i18n.py`（翻訳ファイル）
   - `build.bat`
   - `requirements.txt`（インストールするパッケージの一覧 — build.bat が自動で読み込んで一括インストールします）
   - `fonts` フォルダー（アプリで使うフォント — ビルド時に自動的に成果物の横にコピーされます）
   - `icon.ico`

---

## 3段階. exe を作る

### 方法A. 最も簡単な方法（推奨）

1. `C:\mypass_build` フォルダーで **`build.bat` をダブルクリック** します。
2. 黒い画面が開き、文字がどんどん流れます。**閉じずに待ちます。**（初回は3〜10分、インターネット速度により異なります）
   - `[0/4]` Python確認 → `[1/4]` 仮想環境 → `[2/4]` パッケージインストール → `[3/4]` exe作成中 → `[4/4] 完了`
   - 途中で `WARNING` が出ても正常です。`ERROR` で止まったら **[トラブルシューティング]** を参照してください。
3. 最後の行にexeの場所（`...\dist\MyPass.exe` のようなパス）と「続行するには何かキーを押してください」という内容の行（これはWindows側の `pause` コマンドの標準メッセージなので、お使いのWindowsの表示言語で出ます）が表示されれば成功です。何かキーを押して画面を閉じます。
4. `C:\mypass_build\dist\MyPass.exe` が作られたか確認します。→ **5段階** に進んでください。

> Windowsが「PCを保護しました」という画面を出したら `詳細情報` → `実行` を押してください。

### 方法B. 直接入力する方法（方法Aがうまくいかないとき）

**B-1. コマンドプロンプトを作業フォルダーで開く**
1. エクスプローラーで `C:\mypass_build` フォルダーを開きます。
2. 画面上部の **アドレスバー**（`C:\mypass_build` と書かれている場所）を一度クリックします。
3. 表示されている文字を消して `cmd` と入力し Enter。→ 黒い画面が開き、一番前に `C:\mypass_build>` と表示されるはずです。

**どの黒い画面を使っても（cmd / PowerShell / Git Bash）** — 以下のコマンドの先頭にある `.venv\Scripts\python.exe` の部分だけ、使用する画面の種類に合わせて書き換えて入力してください。（それ以外は同じです）

| 画面の種類 | 先頭部分をこう書く |
|---|---|
| コマンドプロンプト(cmd) | `.venv\Scripts\python.exe`（下記のそのまま） |
| PowerShell | `.\.venv\Scripts\python.exe`（先頭に `.\` を付ける） |
| Git Bash (bash) | `./.venv/Scripts/python.exe`（スラッシュ `/` を使用） |

最初の `python -m venv .venv` は3つの画面すべて同じように入力します。
（どの画面を使うか分からない場合は、方法Aの `build.bat` ダブルクリックが一番簡単です。）

**B-2. 以下のコマンドを1行ずつ、1つ入力してEnter、終わったら次の行**（コピーして貼り付けてもOKです。黒い画面では右クリックが貼り付けです）

① 仮想環境を作る（1〜2分、終わると `C:\mypass_build>` が再び表示される）

`python -m venv .venv`

② pip（インストールツール）を最新に

`.venv\Scripts\python.exe -m pip install --upgrade pip`

③ 必要なパッケージを一括インストール（`requirements.txt` に書かれた一覧どおりにインストールされます。1〜3分、最後に `Successfully installed ...` が出る必要あり）

`.venv\Scripts\python.exe -m pip install -r requirements.txt`

④ exe を作る（1〜3分、最後に `Building EXE ... completed successfully.` が出る必要あり）

`.venv\Scripts\python.exe -m PyInstaller --noconfirm --clean --onefile --windowed --name MyPass --icon icon.ico --collect-all uiautomation --collect-all comtypes mypass.py`

⑤ 終わったら `exit` と入力して Enter で画面を閉じます。`C:\mypass_build\dist\MyPass.exe` ができているか確認します。

---

## 4段階.（参考）各コマンドが行うこと
| コマンド | 行うこと |
|---|---|
| `python -m venv .venv` | このフォルダー内だけで使う独立したPython環境（仮想環境）を作ります。PC上の他のPythonと混ざりません。 |
| `pip install ... cryptography` | 暗号化機能 |
| `pip install ... uiautomation` | ブラウザーのアドレス読み取り、入力（Fill）機能（Windows専用） |
| `pip install ... pyinstaller` | Pythonプログラムをexeにまとめるツール |
| `PyInstaller ...` | Pythonとパッケージを1つのファイル（MyPass.exe）にまとめます。 |

---

## 5段階. 実行してみる
1. `C:\mypass_build\dist\MyPass.exe` を **ダブルクリック** します。（初回は数秒かかることがあります）
2. ログイン画面が表示されれば成功です。`新規ユーザー` でユーザーを作って試してみてください。
3. 実行するとexeと **同じフォルダー** に `data` フォルダーが作られ、情報はそこに保存されます。
4. 配布するには **`MyPass.exe` ファイルだけ** を好きな場所（USBなど）にコピーすればOKです。`build`、`.venv` フォルダーなどは不要です。
5. テストで作ったユーザー情報は `dist\data` フォルダーを削除すると消えます。（配布する際はこのフォルダーをコピーしないでください）

---

## 6段階. 後で新しいバージョンを作る
1. `mypass.py` と `mypass_i18n.py` を新しいものに入れ替えます。（同じフォルダー、上書き）
2. `build.bat` を再度ダブルクリックします。（`.venv` が既にあるのでずっと速いです）
3. 新しい `dist\MyPass.exe` が作られます。

---

## トラブルシューティング

**1. `python` 入力時に `Python was not found` と出る、またはMicrosoft Storeが開く**
- 原因：Pythonインストール時に `Add python.exe to PATH` をチェックしなかった、またはWindowsのストア連携によるものです。
- 解決①：Pythonインストールファイルを再実行 → `Modify` または `Uninstall` の後、最初からインストールし直し **PATHをチェック**。
- 解決②：`Windows キー` → `アプリ実行エイリアスの管理` を検索 → `python.exe`、`python3.exe`（アプリインストーラー）の2項目を **オフ**。
- インストール後は開いている黒い画面をすべて閉じて **新しく開き直す** 必要があります。
- （参考：`build.bat` は `python` が無い場合 `py` コマンドも自動で試します。）

**2. `pip install` 中に `Could not find a version` / `Connection` / `timed out` エラー**
- インターネット接続を確認してコマンドを再実行します。会社・学校のネットワークではセキュリティソフトがブロックすることがあります。

**3. `'.venv\Scripts\python.exe' is not recognized as an internal or external command...`（内部または外部コマンドとして認識されない）エラー（文言はお使いのWindowsの表示言語により異なります）**
- ①の仮想環境作成が失敗しています。`.venv` フォルダーを削除し `python -m venv .venv` からやり直します。
- コマンドプロンプトが `C:\mypass_build>` で開かれているか確認してください。

**4. `can't open file ... mypass.py` / `No such file`**
- `mypass.py` が `C:\mypass_build` の直下にありません。2段階の4番をもう一度確認してください。

**5. `build.bat` を開いたら文字化けして見える**
- 画面の表示は動作に影響しません。方法Bで進めてもかまいません。

**6. ウイルス対策ソフトがexeを削除する、または「脅威」と表示する**
- 自作の署名なしexeでよく出る誤検知です。`dist` フォルダーと `MyPass.exe` をウイルス対策ソフトの除外リストに追加してから作り直してください。

**7. exe実行後、何も画面が出ない**
- 10〜20秒待ってみます。それでも出ない場合はウイルス対策ソフト（6番）を確認し、タスクマネージャーに `MyPass.exe` が残っていたら終了してから再実行します。
- それでも解決しない場合は `python mypass.py` で直接実行してエラーメッセージを確認できます：
  `.venv\Scripts\python.exe mypass.py`（この場合は `pyinstaller` なしでも実行できます）

**8. `ModuleNotFoundError: No module named ...`**
- 3段階③（パッケージインストール）が最後まで完了していません。③をもう一度実行してください。
