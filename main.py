from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
CHAT_ID = 'YOUR_CHAT_ID'

@app.route('/')
def home():
    return '✅ Telegram Bot Form is running on Render!'

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.to_dict()
    message = '\n'.join([f'{key}: {value}' for key, value in data.items()])
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': message}
    response = requests.post(url, data=payload)
    return '✅ ส่งข้อความเรียบร้อยแล้ว' if response.status_code == 200 else f'❌ ล้มเหลว: {response.text}', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
