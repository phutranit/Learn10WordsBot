import json
import os
import schedule
import time
from telegram import Bot
from telegram.constants import ParseMode

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))

WORDS_FILE = "vobeng.json"
STATE_FILE = "state.json"

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
    for i, item in enumerate(words, start=1):
        part = (
            f"{i}. *{item['w']}* — {item['m']}\n"
            f"   _{item['ipa']}_\n"
            f"   *Ví dụ:* {item['sample']}\n"
        )
        lines.append(part)
    return "\n".join(lines)

async def send_daily_words():
    words = load_words()
    state = load_state()

    index = state["index"]
    end = index + 10

    if index >= len(words):
        await bot.send_message(
            chat_id=CHAT_ID,
            text="🎉 Bạn đã học hết từ vựng!",
            parse_mode=ParseMode.MARKDOWN
        )
        return

    today_words = words[index:end]
    message = build_message(today_words)

    await bot.send_message(
        chat_id=CHAT_ID,
        text=message,
        parse_mode=ParseMode.MARKDOWN
    )

    state["index"] = end
    save_state(state)

def job():
    import asyncio
    asyncio.run(send_daily_words())

# Lên lịch chạy lúc 22:15 hằng ngày
schedule.every().day.at("22:40").do(job)

if __name__ == "__main__":
    print("Bot is running... Waiting for 22:15 everyday.")
    while True:
        schedule.run_pending()
        time.sleep(1)
