from flask import Flask, render_template, request
import telebot

app = Flask(__name__)

# Telegram Bot Token
BOT_TOKEN = '7817159589:AAHYCXZ_Dbd5MeZFpEuKLBuI4Mq3GSbaylQ'
bot = telebot.TeleBot(BOT_TOKEN)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['ชื่อ-สกุล']
    phone = request.form['เบอร์โทร']
    detail = request.form['ข้อความเพิ่มเติม']

    message = f"📬 แบบฟอร์มแจ้งเตือน\n👤 ชื่อ: {name}\n📞 เบอร์: {phone}\n📝 รายละเอียด: {detail}"
    bot.send_message(chat_id='YOUR_CHAT_ID', text=message)

    return "✅ ส่งข้อมูลเรียบร้อยแล้ว!"

if __name__ == '__main__':
    app.run()
