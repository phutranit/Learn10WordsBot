import json
from telegram import Bot
import os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
STATE_FILE = "state.json"
WORDS_FILE = "vobeng.json"

bot = Bot(token=TOKEN)

def load_words():
    with open(WORDS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def load_state():
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"index": 0}

def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f)

def build_message(words):
    lines = ["📚 *10 từ vựng hôm nay:*"]
    for i, item in enumerate(words, 1):
        line = (
            f"{i}. *{item['w']}* — {item['m']}\n"
            f"   /{item['ipa']}/\n"
            f"   _{item['sample']}_"
        )
        lines.append(line)
    return "\n".join(lines)

def send_daily_words():
    words = load_words()
    state = load_state()

    start = state["index"]
    end = start + 10   # 🔥 gửi 10 từ mỗi ngày

    if start >= len(words):
        bot.send_message(chat_id=CHAT_ID, text="🎉 Bạn đã học hết từ vựng!", parse_mode="Markdown")
        return

    today_words = words[start:end]
    message = build_message(today_words)
    bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")

    state["index"] = end
    save_state(state)

if __name__ == "__main__":
    send_daily_words()
