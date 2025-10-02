"""
TikTokフォロワー数取得モジュール
"""

import requests
import re
import logging

logger = logging.getLogger(__name__)

def get_followers(username):
    """
    TikTokのフォロワー数を取得

    Args:
        username (str): TikTokユーザー名（@なし）

    Returns:
        int or None: フォロワー数。取得失敗時はNone
    """
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
            logger.info(f"TikTok @{username} フォロワー数: {follower_count:,}")
            return follower_count

        logger.warning(f"TikTok @{username} フォロワー数が見つかりませんでした")
        return None

    except Exception as e:
        logger.error(f"TikTok取得エラー: {e}")
        return None

# メタデータ（server.pyが自動認識するため）
PLATFORM_NAME = "tiktok"
DISPLAY_NAME = "TikTok"
