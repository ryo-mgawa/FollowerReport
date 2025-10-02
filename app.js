// モックデータ生成関数
function generateMockFollowerData() {
    return {
        tiktok: {
            count: Math.floor(Math.random() * 10000) + 50000, // 50,000 ~ 60,000
            username: '@nyan.tsubu',
            available: true
        },
        youtube: {
            count: Math.floor(Math.random() * 5000) + 20000, // 20,000 ~ 25,000
            username: 'チャンネル未設定',
            available: false
        },
        instagram: {
            count: Math.floor(Math.random() * 8000) + 30000, // 30,000 ~ 38,000
            username: 'アカウント未設定',
            available: false
        }
    };
}

// フォロワー数をフォーマット
function formatNumber(num) {
    if (num >= 1000000) {
        return (num / 1000000).toFixed(1) + 'M';
    } else if (num >= 1000) {
        return (num / 1000).toFixed(1) + 'K';
    }
    return num.toLocaleString('ja-JP');
}

// 日時をフォーマット
function formatDateTime() {
    const now = new Date();
    return now.toLocaleString('ja-JP', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
    });
}

// データを更新
function updateFollowerData(data) {
    // TikTok
    const tiktokCount = document.getElementById('tiktok-count');
    const tiktokStatus = document.getElementById('tiktok-status');
    const tiktokUpdate = document.getElementById('tiktok-update');

    tiktokCount.textContent = formatNumber(data.tiktok.count);
    tiktokCount.classList.add('count-update');
    setTimeout(() => tiktokCount.classList.remove('count-update'), 500);

    if (data.tiktok.available) {
        tiktokStatus.textContent = '✓ アクティブ';
        tiktokStatus.classList.add('active');
    }
    tiktokUpdate.textContent = formatDateTime();

    // YouTube
    const youtubeCount = document.getElementById('youtube-count');
    const youtubeStatus = document.getElementById('youtube-status');
    const youtubeUpdate = document.getElementById('youtube-update');

    youtubeCount.textContent = formatNumber(data.youtube.count);
    youtubeCount.classList.add('count-update');
    setTimeout(() => youtubeCount.classList.remove('count-update'), 500);

    if (data.youtube.available) {
        youtubeStatus.textContent = '✓ アクティブ';
        youtubeStatus.classList.add('active');
    }
    youtubeUpdate.textContent = formatDateTime();

    // Instagram
    const instagramCount = document.getElementById('instagram-count');
    const instagramStatus = document.getElementById('instagram-status');
    const instagramUpdate = document.getElementById('instagram-update');

    instagramCount.textContent = formatNumber(data.instagram.count);
    instagramCount.classList.add('count-update');
    setTimeout(() => instagramCount.classList.remove('count-update'), 500);

    if (data.instagram.available) {
        instagramStatus.textContent = '✓ アクティブ';
        instagramStatus.classList.add('active');
    }
    instagramUpdate.textContent = formatDateTime();

    // 合計
    const total = data.tiktok.count + data.youtube.count + data.instagram.count;
    const totalCount = document.getElementById('total-count');
    totalCount.textContent = formatNumber(total);
    totalCount.classList.add('count-update');
    setTimeout(() => totalCount.classList.remove('count-update'), 500);

    // グローバル更新時刻
    document.getElementById('global-update').textContent = formatDateTime();
}

// 初期データ読み込み
function initialize() {
    const initialData = generateMockFollowerData();
    updateFollowerData(initialData);
}

// リアルタイム更新（30秒ごと）
function startRealtimeUpdates() {
    setInterval(() => {
        const newData = generateMockFollowerData();
        updateFollowerData(newData);
    }, 30000); // 30秒
}

// ページ読み込み時に実行
document.addEventListener('DOMContentLoaded', () => {
    initialize();
    startRealtimeUpdates();
});

// 実際のAPI連携用の関数（将来の実装用）
async function fetchTikTokFollowers(username) {
    // TODO: Pythonスクリプトをバックエンドに移行してAPI化
    // const response = await fetch(`/api/tiktok/${username}`);
    // const data = await response.json();
    // return data.followerCount;

    // 現在はモックデータを返す
    return Math.floor(Math.random() * 10000) + 50000;
}

async function fetchYouTubeSubscribers(channelId) {
    // TODO: YouTube Data API v3を使用
    // const response = await fetch(`/api/youtube/${channelId}`);
    // const data = await response.json();
    // return data.subscriberCount;

    return Math.floor(Math.random() * 5000) + 20000;
}

async function fetchInstagramFollowers(username) {
    // TODO: Instagram Graph APIを使用
    // const response = await fetch(`/api/instagram/${username}`);
    // const data = await response.json();
    // return data.followerCount;

    return Math.floor(Math.random() * 8000) + 30000;
}
