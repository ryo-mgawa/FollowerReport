#!/usr/bin/env python3
"""
SNSフォロワーレポート - Flaskサーバー

scrapers/ディレクトリ内のモジュールを自動的に読み込み、
各SNSのフォロワー数を取得するAPIを提供します。
"""

import importlib
import os
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime
import logging

import config

app = Flask(__name__, static_folder='.')
CORS(app)

# ログ設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# スクレイパーの動的読み込み
SCRAPERS = {}

def load_scrapers():
    """scrapers/ディレクトリから自動的にスクレイパーモジュールを読み込む"""
    scrapers_dir = 'scrapers'

    if not os.path.exists(scrapers_dir):
        logger.warning(f"{scrapers_dir}ディレクトリが見つかりません")
        return

    for filename in os.listdir(scrapers_dir):
        if filename.endswith('.py') and not filename.startswith('_'):
            module_name = filename[:-3]  # .pyを除去

            try:
                # モジュールをインポート
                module = importlib.import_module(f'scrapers.{module_name}')

                # get_followers関数が存在するか確認
                if hasattr(module, 'get_followers'):
                    platform_name = getattr(module, 'PLATFORM_NAME', module_name)
                    SCRAPERS[platform_name] = module
                    logger.info(f"✓ {platform_name} スクレイパーを読み込みました")
                else:
                    logger.warning(f"✗ {module_name}.pyにget_followers関数がありません")

            except Exception as e:
                logger.error(f"✗ {module_name}の読み込みエラー: {e}")

# スクレイパーの初期化
load_scrapers()

def get_platform_data(platform_name, identifier):
    """
    指定されたプラットフォームのデータを取得

    Args:
        platform_name (str): プラットフォーム名 (tiktok, youtube, instagram)
        identifier (str): ユーザー名またはチャンネルID

    Returns:
        dict: フォロワー数データ
    """
    if platform_name not in SCRAPERS:
        return {
            'count': 0,
            'username': identifier or 'アカウント未設定',
            'available': False
        }

    if not identifier:
        return {
            'count': 0,
            'username': 'アカウント未設定',
            'available': False
        }

    scraper = SCRAPERS[platform_name]
    follower_count = scraper.get_followers(identifier)

    return {
        'count': follower_count or 0,
        'username': identifier if platform_name != 'tiktok' else f'@{identifier}',
        'available': follower_count is not None and follower_count > 0
    }

@app.route('/')
def index():
    """メインページ"""
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    """静的ファイル配信"""
    return send_from_directory('.', path)

@app.route('/api/followers')
def get_all_followers():
    """全SNSのフォロワー数を取得"""

    # 各プラットフォームのデータを取得
    tiktok_data = get_platform_data('tiktok', config.TIKTOK_USERNAME)
    youtube_data = get_platform_data('youtube', config.YOUTUBE_CHANNEL_ID)
    instagram_data = get_platform_data('instagram', config.INSTAGRAM_USERNAME)

    data = {
        'tiktok': tiktok_data,
        'youtube': youtube_data,
        'instagram': instagram_data,
        'timestamp': datetime.now().isoformat()
    }

    return jsonify(data)

@app.route('/api/tiktok')
def get_tiktok_data():
    """TikTokのみのデータ取得"""
    data = get_platform_data('tiktok', config.TIKTOK_USERNAME)
    data['timestamp'] = datetime.now().isoformat()
    return jsonify(data)

@app.route('/api/youtube')
def get_youtube_data():
    """YouTubeのみのデータ取得"""
    data = get_platform_data('youtube', config.YOUTUBE_CHANNEL_ID)
    data['timestamp'] = datetime.now().isoformat()
    return jsonify(data)

@app.route('/api/instagram')
def get_instagram_data():
    """Instagramのみのデータ取得"""
    data = get_platform_data('instagram', config.INSTAGRAM_USERNAME)
    data['timestamp'] = datetime.now().isoformat()
    return jsonify(data)

@app.route('/api/health')
def health_check():
    """ヘルスチェック"""
    return jsonify({
        'status': 'ok',
        'scrapers_loaded': list(SCRAPERS.keys()),
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    logger.info("=" * 50)
    logger.info("  SNSフォロワーレポート サーバー起動")
    logger.info("=" * 50)
    logger.info(f"読み込まれたスクレイパー: {', '.join(SCRAPERS.keys())}")
    logger.info(f"アクセスURL: http://localhost:{config.SERVER_PORT}")
    logger.info(f"または: http://<ラズパイのIPアドレス>:{config.SERVER_PORT}")
    logger.info("=" * 50)

    app.run(
        host=config.SERVER_HOST,
        port=config.SERVER_PORT,
        debug=config.DEBUG_MODE
    )
