// APIからデータを取得
async function fetchFollowerData() {
    try {
        const response = await fetch('/api/followers');
        if (!response.ok) {
            throw new Error('API取得失敗');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('データ取得エラー:', error);
        // エラー時はモックデータを返す
        return {
            tiktok: {
                count: 0,
                username: '@nyan.tsubu',
                available: false
            },
            youtube: {
                count: 0,
                username: 'チャンネル未設定',
                available: false
            },
            instagram: {
                count: 0,
                username: 'アカウント未設定',
                available: false
            }
        };
    }
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
async function initialize() {
    const initialData = await fetchFollowerData();
    updateFollowerData(initialData);
}

// リアルタイム更新（30秒ごと）
function startRealtimeUpdates() {
    setInterval(async () => {
        const newData = await fetchFollowerData();
        updateFollowerData(newData);
    }, 30000); // 30秒
}

// ページ読み込み時に実行
document.addEventListener('DOMContentLoaded', () => {
    initialize();
    startRealtimeUpdates();
});

// TikTok個別取得（デバッグ用）
async function fetchTikTokFollowers() {
    try {
        const response = await fetch('/api/tiktok');
        const data = await response.json();
        return data.count;
    } catch (error) {
        console.error('TikTok取得エラー:', error);
        return 0;
    }
}
