import requests
import os
import json
import hashlib

# 1. Настройка окружения
# ПЕРЕД ЗАПУСКОМ ВВЕДИ В ТЕРМИНАЛЕ: export WEBEX_TOKEN=твой_токен
ACCESS_TOKEN = os.getenv("WEBEX_TOKEN")
STUDENT_TOKEN = os.getenv("STUDENT_TOKEN", "default_token")
HASH8 = hashlib.sha256(STUDENT_TOKEN.encode()).hexdigest()[:8]

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

def run_webex_lab():
    print(f"🚀 Starting Webex Lab for Hash: {HASH8}")
    
    # А. Получаем информацию о себе (me.json)
    me = requests.get("https://webexapis.com/v1/people/me", headers=HEADERS).json()
    with open("artifacts/day5/webex/me.json", "w") as f:
        json.dump(me, f, indent=4)

    # Б. Создаем комнату с хэшем в названии
    room_title = f"DevNet_Lab_{HASH8}"
    room_body = {"title": room_title}
    room_res = requests.post("https://webexapis.com/v1/rooms", headers=HEADERS, json=room_body).json()
    with open("artifacts/day5/webex/room_create.json", "w") as f:
        json.dump(room_res, f, indent=4)
    
    room_id = room_res.get("id")
    print(f"✅ Room '{room_title}' created!")

    # В. Отправляем сообщение
    msg_body = {
        "roomId": room_id,
        "text": f"Aibek Zhanbyrshy (Group IB-23-5b) completed Day 5 Lab. Token Hash: {HASH8}"
    }
    msg_res = requests.post("https://webexapis.com/v1/messages", headers=HEADERS, json=msg_body).json()
    with open("artifacts/day5/webex/message_post.json", "w") as f:
        json.dump(msg_res, f, indent=4)
    
    print(f"✅ Message sent to room!")

if __name__ == "__main__":
    if not ACCESS_TOKEN:
        print("❌ Error: WEBEX_TOKEN environment variable not set!")
    else:
        run_webex_lab()