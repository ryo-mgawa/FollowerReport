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
            # 最も下の桁が0でない値を取得（丸められていない正確な値）
            counts = [int(count) for count in follower_matches]
            # 末尾が0でない（丸められていない）値を優先
            non_rounded = [c for c in counts if c % 10 != 0]
            follower_count = non_rounded[0] if non_rounded else counts[0]
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
