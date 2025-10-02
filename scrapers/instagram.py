"""
Instagramフォロワー数取得モジュール

TODO: Instagram Graph APIを使用して実装
https://developers.facebook.com/docs/instagram-api
"""

import logging

logger = logging.getLogger(__name__)

def get_followers(username):
    """
    Instagramのフォロワー数を取得

    Args:
        username (str): Instagramユーザー名

    Returns:
        int or None: フォロワー数。取得失敗時はNone

    実装例:
        import requests

        # Instagram Graph API
        access_token = 'YOUR_ACCESS_TOKEN'
        user_id = 'YOUR_USER_ID'

        url = f'https://graph.instagram.com/{user_id}'
        params = {
            'fields': 'followers_count',
            'access_token': access_token
        }

        response = requests.get(url, params=params)
        data = response.json()

        if 'followers_count' in data:
            return data['followers_count']
    """

    # TODO: 上記の実装例を参考に実装
    logger.info(f"Instagram @{username} の取得は未実装です")
    return None

# メタデータ（server.pyが自動認識するため）
PLATFORM_NAME = "instagram"
DISPLAY_NAME = "Instagram"
