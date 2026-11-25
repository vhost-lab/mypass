# コード保護（Nuitka）ガイド — 任意

[보호가이드.md](../ko/보호가이드.md) · [protection-guide.md](../en/protection-guide.md) · [protection-guide.md](protection-guide.md) · [protection-guide.md](../zh-CN/protection-guide.md)

`build.bat`（PyInstaller）で作ったexeは、Pythonコードが「バイトコード」の状態で入っているため、メモ帳では読めませんが、`uncompyle6` のような専用ツールで**デコンパイルを試みると元のソースに近い形まで復元されてしまいます。**

このガイドは、**Nuitka** というツールを使ってPythonコードをそのまま**C言語に変換し、機械語(machine code)にコンパイル**する方法です。バイトコードではなく本物の実行ファイルになるため、一般的なPythonのデコンパイルツールが通用しません。現在ある保護方法の中で、**無料で使えるものとしては最も強力な部類**に入ります。

> まず訂正です：以前の回答でPyArmorを「最も強力な」方法としてご案内しましたが、PyArmorはCLIツール自体はpipで取得できるものの、**文字列暗号化などの実質的な保護機能や商用利用には有料ライセンスが必要**です（公式ドキュメントに自ら「Free To Use But Restricted」と記載されており、体験版は商用製品に使えないと明記されています — [出典](https://pyarmor.readthedocs.io/en/v8.2/licenses.html)）。調査自体は正しく行いましたが、費用が必要であることを先にはっきりお伝えすべきでした。そのため、既定値を**完全無料・オープンソースのNuitka**に変更します。（NuitkaはApache系ではなくAGPLv3ライセンスですが、「コンパイルして生成された実行ファイル(exe)には適用されない」という例外条項があるため、皆さんが作ったMyPass.exeをソースコードなしでそのまま配布してかまいません — [出典](https://nuitka.net/pages/overview.html)）

## 1. 保護ビルドの実行

`빌드가이드.ja.md` の2段階まで同じように進めて、`mypass_package.zip` 内のファイル（`mypass.py`、`mypass_i18n.py`、`build.bat`、`build_protected.bat`、`requirements.txt`、`requirements-protected.txt`、`fonts` フォルダー、`icon.ico` など）を1つのフォルダー（`C:\mypass_build` など）にまとめたら、今回は `build.bat` の代わりに **`build_protected.bat`** をダブルクリックしてください。

- パッケージのインストール、コンパイル、exe作成まで自動で進みます。
- **初回はCコンパイラを自動でダウンロードするため、かなり時間がかかります（10分以上かかることもあります）。** 「WARNING」が表示されても途中で閉じずに待ってください。
- 完了すると `dist\MyPass.exe` が作られます。（通常ビルドとファイル名・場所は同じです）

## 2. 知っておくべきこと（必ずお読みください）

- **入力・ブラウザー連携部分（uiautomation/comtypes）は私自身でテストできていません。** comtypesは実行中に必要なコードをその都度生成する方式なので、Nuitkaでコンパイルしたexe内でも同じように動作するかは、実際のWindowsで一度確認が必要です。うまく動かない場合は、既に動作確認済みの `build.bat`（PyInstaller）側をお使いください。
- **実行ファイルの容量と初回起動速度**がPyInstallerより大きい・遅いことがあります（コンパイルされたランタイムを含むため）。機能上の問題ではありません。
- 署名されていないexeのため、Windowsのセキュリティ警告（青い画面、「不明な発行元」）が表示されることがあります。これはPyInstallerでビルドしても同じく出る問題で、Nuitka固有のものではありません。配布を広げるなら、コード署名証明書の取得を検討してください。
- アップデート（`빌드가이드.ja.md` の6段階）も、`mypass.py` を変更した後、今回は `build_protected.bat` を再度実行すればOKです。

## 3.（参考）PyArmor — 有料の代替手段

文字列まで暗号化するPyArmorのような方式を追加で使いたい場合の選択肢として残しておきます。ただし：

- **無料体験版は商用配布に使用できません。** 実際に使うにはProまたはGroupライセンス（一回払い、価格はPyArmor側のポリシーにより変動する可能性あり）が必要です — 購入前に[公式ライセンスページ](https://pyarmor.readthedocs.io/en/latest/licenses.html)で最新条件を必ず確認してください。
- Nuitkaのように機械語に変換するのではなく「暗号化されたバイトコード＋復号コード」という方式なので、Nuitkaと併用する意味はありません。どちらか一方を選んでください。
- ライセンスの種類によっては、利用者のPCが初回実行時にインターネットに接続している必要がある場合があり、USBで持ち運ぶ用途とは相性があまり良くありません。

ご希望であればPyArmor用のビルドスクリプトも別途お作りできますが、費用の問題がなければ**Nuitka（無料）を既定としておすすめします。**
