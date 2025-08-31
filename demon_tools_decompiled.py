#!/usr/bin/env python3
# decompiled by VSTG
import os
import sys
import time
import random
import webbrowser
import requests
import base64
from datetime import datetime

# ANSI escape codes for colors
COLOR_RESET = "\033[0m"
COLOR_YELLOW = "\033[1;33m"
COLOR_BLUE = "\033[1;34m"
COLOR_CYAN = "\033[1;36m"
COLOR_RED = "\033[1;31m"
COLOR_PURPLE = "\033[1;35m"
COLOR_GREEN = "\033[1;32m"
COLOR_WHITE = "\033[1;37m"
COLOR_BLACK_ON_WHITE = "\033[30;47m"
# For gold, we use yellow as substitute (gold not available in ANSI)
COLOR_GOLD = "\033[1;33m"

# List of random ANSI colors codes for random color options
RANDOM_COLORS = [
    "\033[1;31m", "\033[1;32m", "\033[1;33m", "\033[1;34m",
    "\033[1;35m", "\033[1;36m", "\033[1;37m"
]

# Logo and menu ascii art (preserved exactly)
logo = r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠃⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠾⢛⠒⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣶⣄⡈⠓⢄⠠⡀⠀⠀⠀⣄⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣷⠀⠈⠱⡄⠑⣌⠆⠀⠀⡜⢻⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠳⡆⠐⢿⣆⠈⢿⠀⠀⡇⠘⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⡇⠀⠀⠈⢆⠈⠆⢸⠀⠀⢣⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣧⠀⠀⠈⢂⠀⡇⠀⠀⢨⠓⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣦⣤⠖⡏⡸⠀⣀⡴⠋⠀⠈⠢⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠁⣹⣿⣿⣿⣷⣾⠽⠖⠊⢹⣀⠄⠀⠀⠀⠈⢣⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⣇⣰⢫⢻⢉⠉⠀⣿⡆⠀⠀⡸⡏⠀⠀⠀⠀⠀⠀⢇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡇⡇⠈⢸⢸⢸⠀⠀⡇⡇⠀⠀⠁⠻⡄⡠⠂⠀⠀⠀⠘
⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠛⠓⡇⠀⠸⡆⢸⠀⢠⣿⠀⠀⠀⠀⣰⣿⣵⡆⠀⠀⠀⠀
⠈⢻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣦⣀⡇⠀⢧⡇⠀⠀⢺⡟⠀⠀⠀⢰⠉⣰⠟⠊⣠⠂⠀⡸
⠀⠀⢻⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢧⡙⠺⠿⡇⠀⠘⠇⠀⠀⢸⣧⠀⠀⢠⠃⣾⣌⠉⠩⠭⠍⣉⡇
⠀⠀⠀⠻⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⣋⠀⠈⠀⡳⣧⠀⠀⠀⠀⠀⢸⡏⠀⠀⡞⢰⠉⠉⠉⠉⠉⠓⢻⠃
⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⢀⣀⠠⠤⣤⣤⠤⠞⠓⢠⠈⡆⠀⢣⣸⣾⠆⠀⠀⠀⠀⠀⢀⣀⡼⠁⡿⠈⣉⣉⣒⡒⠢⡼⠀
⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣎⣽⣶⣤⡶⢋⣤⠃⣠⡦⢀⡼⢦⣾⡤⠚⣟⣁⣀⣀⣀⣀⠀⣀⣈⣀⣠⣾⣅⠀⠑⠂⠤⠌⣩⡇⠀
⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⣺⢁⣞⣉⡴⠟⡀⠀⠀⠀⠁⠸⡅⠀⠈⢷⠈⠏⠙⠀⢹⡛⠀⢉⠀⠀⠀⣀⣀⣼⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡟⢡⠖⣡⡴⠂⣀⣀⣀⣰⣁⣀⣀⣸⠀⠀⠀⠀⠈⠁⠀⠀⠈⠀⣠⠜⠋⣠⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⢿⣿⣿⣷⡟⢋⣥⣖⣉⠀⠈⢁⡀⠤⠚⠿⣷⡦⢀⣠⣀⠢⣄⣀⡠⠔⠋⠁⠀⣼⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠈⠻⣿⣿⢿⣛⣩⠤⠒⠉⠁⠀⠀⠀⠀⠀⠉⠒⢤⡀⠉⠁⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣤⣤⠴⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠤⠀⠀⠀⠀⠀⢩⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
DEMON TOOLS"""

menu = (
    "\x1b[1;92m\x1b[38;5;221m〖01〗--»\033[1;34m  \x1b[1;92m\x1b[38;5;48m⌯╼═══❬8ball pool═══╾⌯\x1b[0;34m\x1b\n"
    "\x1b[1;92m\x1b[38;5;222m〖02〗--»\033[1;34m  \x1b[1;92m\x1b[38;5;49m⌯╼═══❬Visa═══╾⌯\x1b[0;34m\x1b\n"
    "\x1b[1;92m\x1b[38;5;223m〖03〗--»\033[1;34m  \x1b[1;92m\x1b[38;5;47m⌯╼═══❬Hack picture═══╾⌯\x1b[0;34m\x1b\n"
    "\x1b[1;92m\x1b[38;5;224m〖04〗--»\033[1;34m  \x1b[1;92m\x1b[38;5;50m⌯╼═══❬Spam bot telegram═══╾⌯\x1b[0;34m\x1b\n"
    "\x1b[1;92m\x1b[38;5;225m〖05〗--»\033[1;34m  \x1b[1;92m\x1b[38;5;46m⌯╼═══❬Decode base64═══╾⌯\x1b[0;34m\x1b\n"
    "\x1b[1;92m\x1b[38;5;226m〖06〗--»\033[1;34m  \x1b[1;92m\x1b[38;5;45m⌯╼═══❬app editor═══╾⌯\x1b[0;34m\x1b\n"
    "\x1b[1;92m\x1b[38;5;227m〖07〗--»\033[1;34m  \x1b[1;92m\x1b[38;5;44m⌯╼═══❬app hacker═══╾⌯\x1b[0;34m\x1b\n"
    "\x1b[1;92m\x1b[38;5;228m〖08〗--»\033[1;34m  \x1b[1;92m\x1b[38;5;43m⌯╼═══❬rasm henanawa═══╾⌯\x1b[0;34m\x1b\n"
    "\x1b[1;92m\x1b[38;5;229m〖09〗--»\033[1;34m  \x1b[1;92m\x1b[38;5;42m⌯╼═══❬CODING PC═══╾⌯\x1b[0;34m\x1b\n"
    "\x1b[1;92m\x1b[38;5;230m〖10〗--»\033[1;34m  \x1b[1;92m\x1b[38;5;41m⌯╼═══❬Create your tool═══╾⌯\x1b[0;34m\x1b\n"
    "\x1b[1;92m\x1b[38;5;231m〖11〗--»\033[1;34m  \x1b[1;92m\x1b[38;5;40m⌯╼═══❬About-Pirates═══╾⌯\x1b[0;34m\x1b\n"
    "\x1b[1;92m\x1b[38;5;272m〖12〗--»\033[1;34m  \x1b[1;92m\x1b[38;5;39m⌯╼═══❬About-Demon═══╾⌯\x1b[0;34m\x1b\n"
    "\x1b[1;92m\x1b[38;5;273m〖13〗--»\033[1;34m  \x1b[1;92m\x1b[38;5;38m⌯╼═══❬Format hack═══╾⌯\x1b[0;34m\x1b"
)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def option1():
    # Option 1: 8ball pool
    # Clear screen after showing logo, then prompt for token and id in yellow color.
    clear_screen()
    print(logo)
    print(COLOR_YELLOW + "Enter token:" + COLOR_RESET, end=" ")
    token = input()
    print(COLOR_YELLOW + "Enter Id:" + COLOR_RESET, end=" ")
    chat_id = input()
    # Predefined accounts tuple

  # Comment by VSTG: some info was removed here
    accounts = ("iclip.com:196731 | Name = Call 911 | [PlayerID = 1250268938 | Tier = Gold |",
        "Hit Account    ‌                                                   tanzil8bp999@gmail.com:hunter | Name = Asif Hasan | PlayerID = 2936288197 | Tier = Emerald |",
        "Hit Account    ‌                                                 ar.sandeep.t@gmail.com:masala123 | Name = KENZY'S | PlayerID = 1000187985 | Tier = Silver |"
        "nathanj1087@gmail.com:Nathan07! | Name = Nathan | PlayerID = 2750300285 | Tier = Gold |  ",
" ofm54224@bcaoo.com:qweasdzx | Name = 8BallPoll | PlayerID = 3121215526 | Tier = Gold |  ")
    while True:
        for account in accounts:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"Account : {account}\nDay : {now}\nBy : @a_x0la"
            # Sending message to telegram bot via API
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            params = {"chat_id": chat_id, "text": message}
            try:
                response = requests.get(url, params=params)
                if response.status_code == 200:
                    print(COLOR_GREEN + f"Sent: {message}" + COLOR_RESET)
                else:
                    print(COLOR_RED + f"Failed to send for account {account}" + COLOR_RESET)
            except Exception as e:
                print(COLOR_RED + f"Error: {str(e)}" + COLOR_RESET)
            time.sleep(5)

def option2():
    # Option 2: VISA
    print(COLOR_BLUE + "VISA DEMON" + COLOR_RESET)
    print(COLOR_YELLOW + "Enter token:" + COLOR_RESET, end=" ")
    token = input()
    print(COLOR_YELLOW + "Enter Id:" + COLOR_RESET, end=" ")
    _ = input()  # Id not used in random generation
    print(COLOR_CYAN + "VISA HACK RANDOM START" + COLOR_RESET)
    while True:
        part1 = ''.join(str(random.randint(0,9)) for _ in range(16))
        part2 = f"{random.randint(1,30):02d}"
        part3 = str(random.randint(2025,2029))
        part4 = ''.join(str(random.randint(0,9)) for _ in range(3))
        output = f"RANDOM VISA \n{part1}|{part2}|{part3}|{part4}\nBY : @a_x0la"
        print(COLOR_CYAN + output + COLOR_RESET)
        time.sleep(1)

def option3():
    # Option 3: Hack picture coming soon
    print(COLOR_RED + "coming soon" + COLOR_RESET)

def option4():
    # Option 4: Spam Telegram Bot
    print(COLOR_PURPLE + "SPAM TELEGRAM BOT" + COLOR_RESET)
    print("Token bot:", end=" ")
    token = input()
    print("Id:", end=" ")
    chat_id = input()
    print("your massage:", end=" ")
    message_text = input()
    print("count massage:", end=" ")
    try:
        count = int(input())
    except:
        print(COLOR_RED + "Invalid count!" + COLOR_RESET)
        return
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {"chat_id": chat_id, "text": message_text}
    for i in range(count):
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                print(COLOR_GREEN + f"Sent message {i+1}" + COLOR_RESET)
            else:
                print(COLOR_RED + f"Failed to send message {i+1}" + COLOR_RESET)
        except Exception as e:
            print(COLOR_RED + f"Error: {str(e)}" + COLOR_RESET)
        time.sleep(1)

def option5():
    # Option 5: Decode base64
    print("PATH TOOL:", end=" ")
    path_tool = input().strip()
    try:
        with open(path_tool, "r") as f:
            encoded_content = f.read()
        decoded_bytes = base64.b64decode(encoded_content)
        decoded_str = decoded_bytes.decode("utf-8")
        with open(path_tool, "w") as f:
            f.write(decoded_str)
        print(COLOR_GREEN + "Decoded successfully" + COLOR_RESET)
    except Exception as e:
        print(COLOR_RED + "sorry unsuccessfully decoded" + COLOR_RESET)

def option6():
    # Option 6: EDITOR TOOLS
    print(COLOR_CYAN + "EDITOR TOOLS" + COLOR_RESET)
    print(COLOR_GREEN + "1-Alight motion Mod" + COLOR_RESET)
    print(COLOR_WHITE + "2-Cupcat Mod" + COLOR_RESET)
    print(COLOR_YELLOW + "3-Editor lesson Alight motion VIP" + COLOR_RESET)
    print("Choose option (1/2/3):", end=" ")
    choice = input().strip()
    if choice == "1":
        color_choice = random.choice(RANDOM_COLORS)
        print(color_choice + " wait for open this link APK" + COLOR_RESET)
        time.sleep(3)
        webbrowser.open("https://t.me/Kodi_Alight03/12458")
    elif choice == "2":
        color_choice = random.choice(RANDOM_COLORS)
        print(color_choice + " wait for open this link APK" + COLOR_RESET)
        time.sleep(3)
        webbrowser.open("https://t.me/j4ck_721/4283")
    elif choice == "3":
        color_choice = random.choice(RANDOM_COLORS)
        print(color_choice + " wait for open this link APK" + COLOR_RESET)
        time.sleep(3)
        webbrowser.open("https://youtube.com")
    else:
        print(COLOR_RED + "Invalid option" + COLOR_RESET)

def option7():
    # Option 7: App hacker (coming soon)
    print(COLOR_RED + "coming soon" + COLOR_RESET)

def option8():
    # Option 8: Open link (rasm henanawa)
    color_choice = random.choice(RANDOM_COLORS)
    print(color_choice + "wait for link open" + COLOR_RESET)
    time.sleep(3)
    webbrowser.open("https://play.google.com/store/apps/details?id=com.defianttech.diskdigger")

def option9():
    # Option 9: CODING PC
    # Print logo (START CODING) in mixed color (simulate by random color per print)
    mixed_color = random.choice(RANDOM_COLORS)
    print(mixed_color + "START CODING" + COLOR_RESET)
    print(COLOR_GREEN + "agar to coding atawet ba rasty chat bo @a_x0la bka agar natwet sarman maheshena" + COLOR_RESET)

def option10():
    # Option 10: Create your tool
    print(COLOR_GREEN + "TOOL" + COLOR_RESET)
    print(COLOR_GOLD + "wasf tool bka ba English" + COLOR_RESET)
    print("Output:", end=" ")
    description = input()
    # Simulate processing using AI making script (here we simply echo the input)
    if description:
        print(COLOR_GREEN + "Tools created" + COLOR_RESET)
    else:
        print(COLOR_RED + "ERROR @a_x0la" + COLOR_RESET)

def option11():
    # Option 11: About-Pirates
    print(COLOR_BLACK_ON_WHITE + "STAFF PIRATES" + COLOR_RESET)
    time.sleep(3)
    # For mixed color, we cycle through a random color selection
    mixed = random.choice(RANDOM_COLORS)
    message = "ستافێکی تازەی هاکە هەڵساوین یارمەتیدانی هەموو ئەندامەکانی ستاف بۆ بەرەو پێشچوونی هەموویان هیوادارم تووڵەکاتان بەدڵ بێت"
    print(mixed + message + COLOR_RESET)

def option12():
    # Option 12: Demon king
    # Print logo with random color changing every 1 second for 4 seconds
    end_time = time.time() + 4
    while time.time() < end_time:
        color_choice = random.choice(RANDOM_COLORS)
        print(color_choice + "Demon king" + COLOR_RESET, end="\r")
        time.sleep(1)
    print()  # for newline
    # Now print the info with color change every 1 second (simulate one iteration)
    info = (
        "Name : Demon\n"
        "City : Kirkuk\n"
        "Age : ?\n"
        "User : @a_x0la\n"
        "Tiktok : @a_x0la\n"
        "Chanell: @M4trix_404\n"
        "Chanell2: @Demonn404\n"
        "Join my Chanell"
    )
    # For a quick demonstration, change the color once every line
    lines = info.split("\n")
    for line in lines:
        color_choice = random.choice(RANDOM_COLORS)
        print(color_choice + line + COLOR_RESET)
        time.sleep(1)

def option13():
    # Option 13: Format hack (coming soon)
    print(COLOR_CYAN + "coming soon" + COLOR_RESET)

def main():
    # Print logo and menu
    print(logo)
    print("menu")
    print(menu)
    print("Choose an option (1-13):", end=" ")
    choice = input().strip()
    if choice == "1":
        option1()
    elif choice == "2":
        option2()
    elif choice == "3":
        option3()
    elif choice == "4":
        option4()
    elif choice == "5":
        option5()
    elif choice == "6":
        option6()
    elif choice == "7":
        option7()
    elif choice == "8":
        option8()
    elif choice == "9":
        option9()
    elif choice == "10":
        option10()
    elif choice == "11":
        option11()
    elif choice == "12":
        option12()
    elif choice == "13":
        option13()
    else:
        print(COLOR_RED + "Invalid choice!" + COLOR_RESET)

if __name__ == "__main__":
    main()
