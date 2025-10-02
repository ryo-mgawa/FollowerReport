#!/bin/bash

echo "========================================="
echo "  SNSフォロワーレポート サーバー起動"
echo "========================================="
echo ""

# Python3のチェック
if ! command -v python3 &> /dev/null; then
    echo "❌ エラー: python3がインストールされていません"
    echo "   以下のコマンドでインストールしてください:"
    echo "   sudo apt install python3 python3-pip"
    exit 1
fi

# 仮想環境の作成・起動
if [ ! -d "venv" ]; then
    echo "📦 仮想環境を作成しています..."
    python3 -m venv venv
fi

echo "🔧 仮想環境を起動しています..."
source venv/bin/activate

# 依存パッケージのインストール
echo "📥 依存パッケージをインストールしています..."
pip install -r requirements.txt

echo ""
echo "========================================="
echo "  サーバーを起動します"
echo "========================================="
echo ""
echo "アクセスURL:"
echo "  ローカル: http://localhost:5000"
echo "  ネットワーク: http://$(hostname -I | awk '{print $1}'):5000"
echo ""
echo "停止するには Ctrl+C を押してください"
echo ""

# サーバー起動
python3 server.py
