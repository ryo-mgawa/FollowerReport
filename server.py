#!/usr/bin/env python3
import requests
import re
import json
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime
import logging

app = Flask(__name__, static_folder='.')
CORS(app)

# ログ設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 設定
TIKTOK_USERNAME = "nyan.tsubu"
YOUTUBE_CHANNEL_ID = ""  # 今後設定
INSTAGRAM_USERNAME = ""  # 今後設定

def get_tiktok_followers(username):
    """TikTokのフォロワー数を取得"""
    try:
        url = f"https://www.tiktok.com/@{username}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

        response = requests.get(url, headers=headers, timeout=10)

        # followerCountを探す
        follower_matches = re.findall(r'"followerCount["\s:]*:?\s*(\d+)', response.text)
        if follower_matches:
            # 最大値を取得（通常は正確な値）
            follower_count = max([int(count) for count in follower_matches])
            logger.info(f"TikTok フォロワー数取得成功: {follower_count:,}")
            return follower_count

        logger.warning("TikTok フォロワー数が見つかりませんでした")
        return None

    except Exception as e:
        logger.error(f"TikTok取得エラー: {e}")
        return None

def get_youtube_subscribers(channel_id):
    """YouTube登録者数を取得（未実装）"""
    # TODO: YouTube Data API v3を使用
    return None

def get_instagram_followers(username):
    """Instagramフォロワー数を取得（未実装）"""
    # TODO: Instagram Graph APIを使用
    return None

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
    tiktok_count = get_tiktok_followers(TIKTOK_USERNAME)
    youtube_count = get_youtube_subscribers(YOUTUBE_CHANNEL_ID) if YOUTUBE_CHANNEL_ID else None
    instagram_count = get_instagram_followers(INSTAGRAM_USERNAME) if INSTAGRAM_USERNAME else None

    # モックデータで補完（実データが取得できない場合）
    if tiktok_count is None:
        tiktok_count = 0

    data = {
        'tiktok': {
            'count': tiktok_count,
            'username': f'@{TIKTOK_USERNAME}',
            'available': tiktok_count is not None and tiktok_count > 0
        },
        'youtube': {
            'count': youtube_count or 0,
            'username': 'チャンネル未設定',
            'available': False
        },
        'instagram': {
            'count': instagram_count or 0,
            'username': 'アカウント未設定',
            'available': False
        },
        'timestamp': datetime.now().isoformat()
    }

    return jsonify(data)

@app.route('/api/tiktok')
def get_tiktok_data():
    """TikTokのみのデータ取得"""
    count = get_tiktok_followers(TIKTOK_USERNAME)

    return jsonify({
        'count': count or 0,
        'username': f'@{TIKTOK_USERNAME}',
        'available': count is not None and count > 0,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/health')
def health_check():
    """ヘルスチェック"""
    return jsonify({
        'status': 'ok',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    logger.info("サーバーを起動しています...")
    logger.info("アクセスURL: http://localhost:5000")
    logger.info("または: http://<ラズパイのIPアドレス>:5000")

    # ラズパイで外部からアクセスできるように0.0.0.0でバインド
    app.run(host='0.0.0.0', port=5000, debug=True)
