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

4. ChromeDriverのインストール：
   - [ChromeDriverのダウンロードページ](https://sites.google.com/a/chromium.org/chromedriver/downloads)から、使用しているChromeブラウザのバージョンに合ったChromeDriverをダウンロードします。
   - ダウンロードしたChromeDriverをシステムのPATHが通っているディレクトリに配置するか、コードで明示的にパスを指定します。

## SeleniumとChromeDriverのバージョン不一致問題の対処

SeleniumとChromeDriverのバージョンの不一致は、よく遭遇する問題です。このプロジェクトでは、以下の方法でこの問題に対処しています：

1. Chromeオプションの設定：
   ```python
   chrome_options = Options()
   chrome_options.add_argument('--no-sandbox')
   chrome_options.add_argument('--ignore-certificate-errors')
   chrome_options.add_argument('--disable-dev-shm-usage')
   chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
   chrome_options.add_argument('--disable-gpu')
   chrome_options.add_argument('--ignore-ssl-errors')
   chrome_options.add_argument("--disable-extensions")
   ```
   
   これらのオプションにより、一般的な互換性の問題を回避し、安定した動作を実現しています。

2. Service objectの使用：
   ```python
   service = Service()
   driver = webdriver.Chrome(service=service, options=chrome_options)
   ```
   
   Serviceオブジェクトを使用することで、ChromeDriverの設定をより柔軟に行えます。

3. 定期的な更新：
   ChromeブラウザとChromeDriverを定期的に更新し、最新のバージョンを使用することをお勧めします。

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
- 結果の読み込みを待機（time.sleepを使用）
- 検索結果のタイトルの特定と抽出
- 結果の数と最初の5つの結果タイトルの表示

## 注意点

- このスクリプトは現在ヘッドレスモードを使用していません。ブラウザの動作を確認できます。
- エラーハンドリングが実装されており、実行中に発生した例外をキャッチして表示します。
- スクリプトの終了時、エラーが発生した場合でもブラウザは自動的に閉じられます。

## トラブルシューティング

SeleniumやChromeDriverに関する問題が発生した場合は、以下を試してください：

1. Seleniumを最新バージョンに更新する
2. Chromeブラウザを最新バージョンに更新する
3. ChromeDriverをChromeブラウザのバージョンに合わせて更新する
4. 仮想環境を再作成し、依存関係を再インストールする

## ライセンス

[ここにライセンスを指定してください。例：MIT License]