📘 Vocabulary Learning Bot (vocabBot)

A simple Telegram bot that helps users learn 3000 English vocabulary words, sending 5 new words every day.
The bot is built with Python + python-telegram-bot and stores vocabulary progress locally or in a database.

🚀 Features

📩 Daily delivery: Sends 5 random vocabulary words every day at a fixed time.

📝 Meanings included: Each word comes with definition + example sentence.

📚 3000-word dataset included.

📊 Progress tracking: Remembers which words you’ve learned.

🔔 Reminders: Notifies you automatically without user interaction.

⚡ Lightweight, easy to deploy on any server/VPS.

# 🔥 Learn10WordsBot – Telegram Bot Gửi Từ Vựng Mỗi Ngày

Bot Telegram tự động gửi **X từ vựng mỗi ngày** theo giờ Việt Nam.  
Toàn bộ cấu hình (giờ gửi, tiêu đề, số từ/ngày) đều nằm trong `config.json`.

---

# ⭐ 1. Giới Thiệu

Bot được thiết kế để giúp bạn học từ vựng tiếng Anh mỗi ngày hoàn toàn tự động.  
Chỉ cần:

- Cung cấp từ vựng trong `vobeng.json`
- Set giờ gửi trong `config.json`
- Deploy bot lên Railway

Bot sẽ gửi tin nhắn Telegram mỗi ngày đúng giờ bạn chọn.

---

# ⭐ 2. Tạo Telegram Bot & Lấy Token

### 👉 Bước 1: Mở Telegram → tìm **@BotFather**

Gõ:

/newbot

perl
Copy code

### 👉 Bước 2: Đặt tên bot  
Ví dụ: `Learn 10 Words Bot`

### 👉 Bước 3: Đặt username bot  
Ví dụ: `Learn10WordsBot`

### 👉 Bước 4: Nhận TOKEN

BotFather trả về:

Use this token to access the HTTP API:
1234567890:AAxxxxxx

yaml
Copy code

→ Đây là **BOT_TOKEN**

⚠️ Không chia sẻ token cho ai.

---

# ⭐ 3. Lấy CHAT_ID để bot gửi tin nhắn cho bạn

1. Mở bot của bạn trên Telegram → nhấn **Start**  
2. Gửi tin nhắn: `hi`
3. Mở trình duyệt:

https://api.telegram.org/bot<BOT_TOKEN>/getUpdates

css
Copy code

4. Kết quả:

```json
"chat": {
  "id": 123456789,
  "type": "private"
}
→ 123456789 chính là CHAT_ID của bạn.

⭐ 4. Cấu Trúc Repository
Repo của bạn cần có các file sau:

pgsql
Copy code
.
├── bot.py
├── config.json
├── vobeng.json
└── requirements.txt
bot.py → Code chính điều khiển bot

config.json → File cấu hình chỉnh giờ gửi, số từ/ngày

vobeng.json → Danh sách từ vựng

requirements.txt → Các thư viện cần cài

⭐ 5. File config.json – chỉnh giờ gửi & số từ/ngày
Ví dụ:

json
Copy code
{
  "hour": 22,
  "minute": 40,
  "words_per_day": 10,
  "title": "📚 *Từ vựng hôm nay:*"
}
Key	Ý nghĩa
hour	Giờ gửi theo giờ Việt Nam (0–23)
minute	Phút gửi (0–59)
words_per_day	Số từ gửi mỗi ngày
title	Tiêu đề tin nhắn Telegram

Ví dụ muốn gửi 15 từ lúc 9h sáng:

json
Copy code
{
  "hour": 9,
  "minute": 0,
  "words_per_day": 15,
  "title": "🌟 Từ vựng hôm nay:"
}
⭐ 6. File vobeng.json – danh sách từ vựng
Ví dụ format:

json
Copy code
[
  {
    "stt": 1,
    "w": "to",
    "m": "đến, để",
    "ipa": "/tuː, tə/",
    "sample": "I go to work."
  },
  {
    "stt": 2,
    "w": "of",
    "m": "của, về",
    "ipa": "/əv, ɒv/",
    "sample": "A cup of coffee."
  }
]
Bot sẽ đọc tuần tự từ đầu đến cuối.

⭐ 7. File requirements.txt
text
Copy code
python-telegram-bot==20.7
schedule
pytz
⭐ 8. Deploy Bot 24/7 Trên Railway.app (Miễn Phí)
👉 Bước 1: Đăng nhập Railway
https://railway.app → Sign in with GitHub

👉 Bước 2: Tạo Project
New Project

"Deploy from GitHub Repo"

Chọn repo chứa bot của bạn

👉 Bước 3: Thêm Environment Variables
Vào tab Variables, thêm:

Key	Value
BOT_TOKEN	Token từ BotFather
CHAT_ID	ID Telegram của bạn

👉 Bước 4: Chỉnh Start Command
Vào tab:

Settings → Nixpacks → Start Command

Đặt:

nginx
Copy code
python bot.py
👉 Bước 5: Railway build & chạy bot
Vào tab Logs để xem:

lua
Copy code
Bot is running... Scheduling VN time...
→ Bot đang hoạt động.

⭐ 9. Reset tiến độ học
Bot tạo file state.json để nhớ đã học đến đâu.

Để reset lại từ đầu:

Xoá file state.json trên Railway container, hoặc sửa thành:

json
Copy code
{"index": 0}
⭐ 10. Lỗi thường gặp & cách xử lý
❌ Bot không gửi tin
Kiểm tra:

Token sai?

Chat ID sai?

Bot bị Block?

Sai Start Command?

❌ Railway báo “no open ports detected”
→ Không sao, vì bot không dùng Web Service.
Railway vẫn chạy bot bình thường.

⭐ 11. Test bot ngay lập tức
Muốn bot gửi thử để test:

Chỉnh config.json thành thời gian 1–2 phút nữa:

json
Copy code
"hour": 22,
"minute": 05
Commit & push

Railway auto-deploy

Bot sẽ gửi đúng giờ đó.

🎉 Kết thúc
Bạn đã có bộ hướng dẫn đầy đủ để:

Tạo Telegram Bot

Lấy token & chat ID

Cấu hình bot

Deploy chạy 24/7 trên Railway

Học từ vựng tự động mỗi ngày

Chúc bạn học tiếng Anh thật hiệu quả! 🚀🔥
