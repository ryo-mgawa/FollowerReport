# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

SNSフォロワー数をリアルタイムで表示するWebアプリケーション。Raspberry Pi上で動作し、TikTok/YouTube/Instagramのフォロワー数を取得・表示する。

## 開発環境セットアップ

```bash
# 仮想環境作成とパッケージインストール
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# サーバー起動
python3 server.py
```

または起動スクリプトを使用：
```bash
./start.sh
```

## アーキテクチャ

### プラグイン型スクレイパーシステム

`server.py`は起動時に`scrapers/`ディレクトリを自動スキャンし、各SNSのスクレイパーモジュールを動的に読み込む。

**重要な仕組み：**
- `scrapers/`内の`.py`ファイルは自動認識される
- 各モジュールは`get_followers(identifier)`関数を実装する必要がある
- `PLATFORM_NAME`と`DISPLAY_NAME`メタデータで識別
- `server.py`を変更せずに新しいSNS対応を追加可能

### スクレイパーモジュールの実装規則

新しいSNSスクレイパーを追加する場合：

```python
# scrapers/platform_name.py
import logging

logger = logging.getLogger(__name__)

def get_followers(identifier):
    """
    フォロワー数を取得

    Args:
        identifier: ユーザー名、チャンネルID等

    Returns:
        int or None: フォロワー数、取得失敗時はNone
    """
    # 実装
    return follower_count

# 必須メタデータ
PLATFORM_NAME = "platform_name"  # API/設定で使用するキー
DISPLAY_NAME = "Platform Name"   # 表示名
```

### TikTokスクレイパーの注意点

`scrapers/tiktok.py`は複数の`followerCount`値が見つかった場合、**末尾が0でない値**を優先して正確な数値を返す。これは丸められた値（91,000）と正確な値（90,993）が混在するため。

### 設定管理

すべての設定は`config.py`で一元管理：
- SNSのユーザー名/ID
- APIキー（YouTube, Instagram用）
- サーバー設定（ホスト、ポート、デバッグモード）

## API エンドポイント

- `GET /api/followers` - 全SNSのフォロワー数を返す
- `GET /api/tiktok` - TikTokのみ
- `GET /api/youtube` - YouTubeのみ
- `GET /api/instagram` - Instagramのみ
- `GET /api/health` - ヘルスチェック、読み込まれたスクレイパー一覧を返す

## デプロイ

Raspberry Pi向けに最適化されている。GitHub Actionsによる自動デプロイ設定が`.github/workflows/`にあるが、現在はローカル実行が想定されている。

## テスト方法

```bash
# スクレイパー単体テスト
python3 -c "
from scrapers import tiktok
print(tiktok.get_followers('nyan.tsubu'))
"

# APIテスト（サーバー起動後）
curl http://localhost:5000/api/followers
```
