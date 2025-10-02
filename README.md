# 📊 SNSフォロワーレポート

TikTok、YouTube、Instagramのフォロワー数をリアルタイムで表示するWebアプリケーションです。
ラズパイで動作し、ローカルネットワーク内からブラウザでアクセスできます。

## ✨ 機能

- 📱 **TikTokフォロワー数取得** - スクレイピングで自動取得
- 📺 **YouTube登録者数** - 準備中（YouTube Data API v3）
- 📷 **Instagramフォロワー数** - 準備中（Instagram Graph API）
- 🔄 **リアルタイム更新** - 30秒ごとに自動更新
- 🎨 **レスポンシブデザイン** - PC/スマホ対応

## 🚀 ラズパイでの起動方法

### 1. リポジトリをクローン

```bash
git clone https://github.com/ryo-mgawa/FollowerReport.git
cd FollowerReport
```

### 2. サーバーを起動

```bash
./start.sh
```

起動スクリプトが自動で以下を実行します：
- Python仮想環境の作成
- 必要なパッケージのインストール
- Flaskサーバーの起動

### 3. ブラウザでアクセス

- **ローカル**: http://localhost:5000
- **ネットワーク**: http://<ラズパイのIPアドレス>:5000

## 📦 必要な環境

- Python 3.7以上
- pip
- インターネット接続

## 🛠️ 手動インストール

```bash
# 仮想環境の作成
python3 -m venv venv
source venv/bin/activate

# パッケージのインストール
pip install -r requirements.txt

# サーバー起動
python3 server.py
```

## 📁 ファイル構成

```
FollowerReport/
├── server.py          # Flaskバックエンドサーバー
├── index.html         # メインページ
├── styles.css         # スタイルシート
├── app.js             # フロントエンドロジック
├── requirements.txt   # Pythonパッケージ
├── start.sh           # 起動スクリプト
└── README.md          # このファイル
```

## 🔧 カスタマイズ

### TikTokユーザー名の変更

`server.py`の以下の行を編集：

```python
TIKTOK_USERNAME = "nyan.tsubu"  # ここを変更
```

### YouTube/Instagram対応

`server.py`の以下の変数にAPIキーとIDを設定：

```python
YOUTUBE_CHANNEL_ID = ""     # YouTube チャンネルID
INSTAGRAM_USERNAME = ""     # Instagram ユーザー名
```

## 🐛 トラブルシューティング

### Python3がない場合

```bash
sudo apt update
sudo apt install python3 python3-pip
```

### ポート5000が使用中の場合

`server.py`の最終行を編集：

```python
app.run(host='0.0.0.0', port=8080, debug=True)  # ポート番号を変更
```

### TikTokデータが取得できない

- インターネット接続を確認
- TikTokのHTML構造が変更された可能性
- ログを確認：サーバー起動時のコンソール出力をチェック

## 📝 今後の実装予定

- [ ] YouTube Data API v3連携
- [ ] Instagram Graph API連携
- [ ] フォロワー数の履歴グラフ表示
- [ ] アラート通知機能（目標達成時）
- [ ] データベース保存機能

## 📄 ライセンス

MIT License

## 🤝 貢献

バグ報告や機能追加のプルリクエストを歓迎します！