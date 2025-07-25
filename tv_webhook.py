from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '7929780148:AAEKw3t9XUQdc-LkxK2J9tCWwbxqMtahjoU'
CHAT_ID = '7407074098'

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    message = data.get('message', 'TradingView 訊號來了！')
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': message}
    
    requests.post(url, data=payload)
    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

@app.route('/', methods=['GET'])
def index():
    return 'TV Webhook is running!'
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "🚀 Webhook server is live!", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("📩 Received alert:", data)
    return "✅ Alert received!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
