"""
設定ファイル

各SNSのユーザー名やAPIキーをここで一元管理します。
"""

# TikTok設定
TIKTOK_USERNAME = "nyan.tsubu"

# YouTube設定（YouTube Data API v3が必要）
YOUTUBE_CHANNEL_ID = ""  # チャンネルIDを設定
YOUTUBE_API_KEY = ""     # APIキーを設定

# Instagram設定（Instagram Graph APIが必要）
INSTAGRAM_USERNAME = ""     # ユーザー名を設定
INSTAGRAM_USER_ID = ""      # ユーザーIDを設定
INSTAGRAM_ACCESS_TOKEN = "" # アクセストークンを設定

# サーバー設定
SERVER_HOST = "0.0.0.0"  # すべてのネットワークインターフェースでリッスン
SERVER_PORT = 5000        # ポート番号
DEBUG_MODE = True         # デバッグモード

# 更新間隔（秒）
UPDATE_INTERVAL = 30  # フロントエンドの自動更新間隔
