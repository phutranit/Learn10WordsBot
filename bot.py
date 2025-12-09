import json
import os
import schedule
import time
import datetime
import pytz
from telegram import Bot
from telegram.constants import ParseMode
import asyncio

# Load config
def load_config():
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)

config = load_config()

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
    title = config["title"]
    lines = [title]
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

    nums = config["words_per_day"]
    index = state["index"]
    end = index + nums

    if index >= len(words):
        await bot.send_message(
            chat_id=CHAT_ID,
            text="🎉 Bạn đã học hết toàn bộ từ vựng!",
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


def schedule_vietnam_time(hour, minute):
    vn = pytz.timezone("Asia/Ho_Chi_Minh")
    now_utc = datetime.datetime.now(pytz.utc)
    now_vn = now_utc.astimezone(vn)

    target = now_vn.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if target <= now_vn:
        target += datetime.timedelta(days=1)

    delta = (target - now_vn).total_seconds()

    print(f"⏳ Next run in {int(delta)} seconds — VN time {hour}:{minute}")

    schedule.every(int(delta)).seconds.do(run_once)

def run_once():
    asyncio.run(send_daily_words())
    c = load_config()
    schedule_vietnam_time(c["hour"], c["minute"])
    return schedule.CancelJob


if __name__ == "__main__":
    print("Bot is running with config.json...")
    schedule_vietnam_time(config["hour"], config["minute"])

    while True:
        schedule.run_pending()
        time.sleep(1)
