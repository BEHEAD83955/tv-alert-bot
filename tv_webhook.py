from flask import Flask, request
import requests
import os

app = Flask(__name__)

# ✅ 設定 Telegram Bot Token 與 Chat ID（可以用環境變數管理）
BOT_TOKEN = os.environ.get("BOT_TOKEN", "你的實際BotToken")
CHAT_ID = os.environ.get("CHAT_ID", "你的ChatID")

# 🔹 根目錄 GET 用來測試 Render 是否有正常運作
@app.route("/", methods=["GET"])
def home():
    return "✅ Webhook server is live!", 200

# 🔹 webhook 接收 POST 請求
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("📩 Received alert:", data)

    # 從傳來的資料抓 message 欄位，或設預設訊息
    message = data.get('message', '📈 TradingView 訊號來了！')

    # 發送到 Telegram
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }

    try:
        r = requests.post(url, data=payload)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"❌ Telegram 發送失敗：{e}")
        return "Telegram 發送失敗", 500

    return "✅ Alert received and forwarded to Telegram!", 200

# 🔹 啟動 Flask 應用
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
