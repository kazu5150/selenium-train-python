# Selenium Google検索自動化

このプロジェクトは、PythonとSeleniumを使用してGoogle検索を自動化し、検索結果を取得する方法を示しています。

## 前提条件

- Python 3.x
- 仮想環境 (venv)
- Chromeブラウザ
- ChromeDriver

## セットアップ

1. このリポジトリをクローンします：
   ```
   git clone https://github.com/あなたのユーザー名/リポジトリ名.git
   cd リポジトリ名
   ```

2. 仮想環境を作成し、有効化します：
   ```
   python -m venv selenium_env
   source selenium_env/bin/activate  # Windowsの場合は `selenium_env\Scripts\activate`
   ```

3. 必要なパッケージをインストールします：
   ```
   pip install selenium
   ```

4. ChromeDriverがインストールされ、システムのPATHに追加されていることを確認してください。

## 使用方法

スクリプトを実行するには、以下のコマンドを使用します：

```
python main.py
```

スクリプトは以下の動作を行います：
1. ChromeブラウザでGoogleを開く
2. "python selenium"を検索
3. 結果が読み込まれるまで待機
4. 見つかった結果の数を表示
5. 最初の5つの検索結果のタイトルを表示

## コードの説明

このスクリプトは、Selenium WebDriverを使用して以下の操作を自動化します：
- 最適なパフォーマンスと互換性のためのChromeオプションの設定
- Googleのホームページを開く
- 検索ボックスを見つけて"python selenium"と入力
- 検索クエリの送信
- 結果の読み込みを待機
- 検索結果のタイトルの特定と抽出
- 結果の数と最初の5つの結果タイトルの表示

## 注意点

- このスクリプトはヘッドレスブラウザ設定を使用しています。ブラウザの動作を確認したい場合は、`chrome_options`から`--headless`オプションを削除してください。
- エラーハンドリングが実装されており、実行中に発生した例外をキャッチして表示します。
- スクリプトの終了時、エラーが発生した場合でもブラウザは自動的に閉じられます。

## ライセンス

[ここにライセンスを指定してください。例：MIT License]
