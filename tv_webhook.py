from flask import Flask, request
import requests

app = Flask(__name__)

# 你自己的 Telegram bot token 和 chat id
BOT_TOKEN = '7929780148:AAEKw3t9XUQdc-LkxK2J9tCWwbxqMtahjoU'
CHAT_ID = '-1002558731125'

# 首頁測試，打開網址會看到這個文字
@app.route("/", methods=["GET"])
def home():
    return "✅ Webhook server is live!", 200

# webhook 接收 TradingView 訊號的地方
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("📩 Received alert:", data)

    # 提取 message，如果沒有就用預設文字
    message = data.get("message", "🚨 收到 TradingView 訊號！")

    # 傳送到 Telegram
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)

    return "✅ Alert received!", 200

# Render 執行主程序
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
