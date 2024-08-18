# spreadsheet url: https://docs.google.com/spreadsheets/d/1PGug0gq780SLrf3mFqHMep1rpr2i6OUqBeXOsPBYH28/edit?gid=0#gid=0

# ヤマト運輸追跡自動化

このプロジェクトは、ヤマト運輸の荷物追跡番号を使用して配送状況を自動的に確認するプロセスを自動化します。Google スプレッドシートから追跡番号を取得し、Selenium を使用して配送状況を確認し、結果をスプレッドシートに更新します。

## 機能

- 指定された Google スプレッドシートから追跡番号を取得
- Selenium WebDriver を使用して追跡プロセスを自動化
- 追跡結果とタイムスタンプでスプレッドシートを更新
- 一度の実行で複数の追跡番号を処理

## 前提条件

このプロジェクトを使用する前に、以下の要件を満たしていることを確認してください：

- Python 3.6 以上
- Sheets API が有効化された Google Cloud Platform アカウント
- Chrome WebDriver がインストールされ、システムの PATH に設定されていること

## インストール

1. このリポジトリをクローンします：
   ```
   git clone https://github.com/your-username/yamato-tracking-automation.git
   cd yamato-tracking-automation
   ```

2. 必要な Python パッケージをインストールします：
   ```
   pip install -r requirements.txt
   ```

3. Google Cloud の認証情報を設定します：
   - サービスアカウントを作成し、JSON キーファイルをダウンロードします
   - キーファイルの名前を `selenium-spreadhseet-yamato-f83687fbeb1a.json` に変更し、プロジェクトのルートディレクトリに配置します

## 設定

1. `yamato_spread.py` を開き、必要に応じて Google スプレッドシートの設定を更新します。

2. Google スプレッドシートに「発送管理」という名前のワークシートがあり、追跡番号と結果のための列があることを確認します。

## 使用方法

メインスクリプトを実行します：

```
python yamato_spread.py
```

スクリプトは以下の処理を行います：
1. 指定された Google スプレッドシートから追跡番号を取得します
2. Selenium を使用して各荷物の状態を確認します
3. 結果とタイムスタンプでスプレッドシートを更新します

## ファイルの説明

- `yamato_spread.py`: メインスクリプト。Google スプレッドシートとの連携、Selenium を使用した追跡処理、結果の更新を行います。
- `kuroneko_yamato.py`: Selenium を使用してヤマト運輸の配送状況を確認する関数を含むモジュール。

## 貢献

このプロジェクトへの貢献を歓迎します。リポジトリをフォークし、変更を加えたプルリクエストを提出してください。

## ライセンス

[ここにライセンスを指定してください。例：MIT ライセンス]

## 免責事項

このプロジェクトはヤマト運輸株式会社と提携しておらず、同社の承認を受けていません。ヤマト運輸の利用規約に従って責任を持って使用してください。