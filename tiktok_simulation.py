# this is a fake tiktok checker simulator that was sold as a real product by "Botpalys encoder" who also obfuscated the script
# This script was deobfuscated by Vestige Group <3

import random
import string
import requests
import time
from datetime import datetime, timedelta

# Lists of real first and last names for email generation
FIRST_NAMES = [
    "emma", "liam", "olivia", "noah", "ava", "oliver", "isabella", "elijah",
    "sophia", "william", "mia", "james", "charlotte", "benjamin", "amelia",
    "lucas", "harper", "henry", "evelyn", "alexander", "abigail", "mason",
    "emily", "michael", "elizabeth", "ethan", "sofia", "daniel", "ella",
    "jacob", "camila", "logan", "aria", "jackson", "scarlett", "levi", "victoria",
    "sebastian", "madison", "mateo", "luna", "jack", "grace", "owen", "chloe",
    "theodore", "penelope", "aiden", "layla", "samuel", "riley"
]

LAST_NAMES = [
    "smith", "johnson", "williams", "brown", "jones", "garcia", "miller", "davis",
    "rodriguez", "martinez", "hernandez", "lopez", "gonzalez", "wilson", "anderson",
    "thomas", "taylor", "moore", "jackson", "martin", "lee", "perez", "thompson",
    "white", "harris", "sanchez", "clark", "ramirez", "lewis", "robinson",
    "walker", "young", "allen", "king", "wright", "scott", "torres", "nguyen",
    "hill", "flores", "green", "adams", "nelson", "baker", "hall", "rivera",
    "campbell", "mitchell", "carter", "roberts"
]

def generate_real_name_email():
    """Generate a realistic email using real names"""
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)

    # Randomly choose an email format
    formats = [
        f"{first_name}.{last_name}",
        f"{first_name}{last_name}",
        f"{first_name[0]}{last_name}",
        f"{first_name}{random.randint(1, 99)}",
        f"{first_name}_{last_name}",
        f"{last_name}.{first_name}",
        f"{first_name}{last_name}{random.randint(1970, 2005)}"
    ]

    username = random.choice(formats)
    return f"{username}@gmail.com", username, first_name, last_name

def generate_username_from_email(email_username):
    """Generate a username based on the email username"""
    # Remove numbers and special characters from the email username
    clean_username = ''.join([c for c in email_username if c.isalpha()])

    if len(clean_username) < 3:
        # If the cleaned username is too short, use a fallback
        prefixes = ["Pro", "Star", "Epic", "Cool", "Super", "Magic", "King", "Queen"]
        suffixes = ["Player", "Gamer", "Creator", "Master", "Legend", "Hero", "Warrior"]
        return f"{random.choice(prefixes)}{random.choice(suffixes)}{random.randint(1, 999)}"

    # Add some random numbers to make it look like a real username
    return f"{clean_username}{random.randint(1, 999)}"

def check_tiktok_account(email):
    """
    Check if a TikTok account exists with this email
    Returns: "hit" if account exists, "bad" if not
    """
    print(f"🔍 Checking TikTok for: {email}")
    time.sleep(1)

    # Simulate checking TikTok (random result)
    if random.random() > 0.7:  # 30% chance of account existing
        print("✅ TikTok account found!")
        return "hit"
    else:
        print("❌ No TikTok account found")
        return "bad"

def check_gmail_account(email):
    """
    Check if a Gmail account exists with this email
    Returns: "hit" if account exists, "bad" if not
    """
    print(f"📧 Checking Gmail for: {email}")
    time.sleep(1)

    # Simulate checking Gmail (random result)
    if random.random() > 0.5:  # 50% chance of account existing
        print("✅ Gmail account found!")
        return "hit"
    else:
        print("❌ No Gmail account found")
        return "bad"

def simulate_gmail_account_creation(email, first_name, last_name):
    """
    Simulate creating a Gmail account for hit TikTok accounts
    """
    print(f"🛠️ Creating Gmail account for: {email}")
    time.sleep(2)

    # Simulate account creation process
    print("📝 Filling account details...")
    time.sleep(1)
    print(f"👤 Name: {first_name} {last_name}")
    time.sleep(1)
    print("📧 Email address confirmed")
    time.sleep(1)
    print("🔐 Setting up password...")
    time.sleep(1)
    print("✅ Gmail account created successfully!")

    return True

def get_account_details(email, email_username):
    """Generate simulated account details for a hit"""
    username = generate_username_from_email(email_username)

    return {
        "username": username,
        "followers": random.randint(100, 1000000),
        "likes": random.randint(1000, 5000000),
        "videos": random.randint(1, 500),
        "verified": random.choice([True, False]),
        "seller": random.choice([True, False]),
        "region": random.choice(["US", "UK", "CA", "AU", "DE", "FR", "BR", "IN"]),
        "created": (datetime.now() - timedelta(days=random.randint(30, 1000))).strftime("%Y-%m-%d"),
        "gmail_link": f"https://mail.google.com/mail/u/0/?view=cm&fs=1&to={email}",
        "tiktok_link": f"https://www.tiktok.com/@{username}",
        "gmail_created": False
    }

def save_results(emails_with_status):
    """Save results to a text file"""
    with open("tiktok_accounts_results.txt", "w", encoding="utf-8") as f:
        for email, status, details, email_username, gmail_created in emails_with_status:
            f.write(f"Email: {email}\n")
            f.write(f"Status: {status}\n")
            if status == "hit" and details:
                f.write(f"Username: {details['username']}\n")
                f.write(f"Followers: {details['followers']}\n")
                f.write(f"Likes: {details['likes']}\n")
                f.write(f"Videos: {details['videos']}\n")
                f.write(f"Verified: {details['verified']}\n")
                f.write(f"Seller: {details['seller']}\n")
                f.write(f"Region: {details['region']}\n")
                f.write(f"Created: {details['created']}\n")
                f.write(f"Gmail Link: {details['gmail_link']}\n")
                f.write(f"TikTok Link: {details['tiktok_link']}\n")
                if gmail_created:
                    f.write("Gmail Account: Created successfully\n")
            f.write("Checked by @f1rtx\n")
            f.write("-" * 40 + "\n")

def send_telegram_message(token, chat_id, message):
    """Send a message via Telegram bot"""
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        return response.status_code == 200
    except:
        return False

def format_hit_message(email, details, gmail_created=False):
    """Format a hit message for Telegram"""
    gmail_status = "✅ Created" if gmail_created else "❌ Not created"

    return f"""✅ <b>TikTok Hit Found!</b>
📧 Email: <code>{email}</code>
👤 Username: <code>{details['username']}</code>
👥 Followers: {details['followers']:,}
❤️ Likes: {details['likes']:,}
🎥 Videos: {details['videos']}
🏷 Verified: {'Yes' if details['verified'] else 'No'}
🛒 Seller: {'Yes' if details['seller'] else 'No'}
🌎 Region: {details['region']}
📅 Created: {details['created']}
📧 Gmail: {gmail_status}

🔗 <a href="{details['gmail_link']}">Login to Gmail</a>
🔗 <a href="{details['tiktok_link']}">View TikTok Profile</a>

Checked by @f1rtx"""

def format_bad_message(email):
    """Format a bad account message for Telegram"""
    return f"""❌ <b>No Account Found</b>

📧 Email: <code>{email}</code>
🔗 <a href="https://mail.google.com/mail/u/0/?view=cm&fs=1&to={email}">Try Gmail Login</a>
🔗 <a href="https://www.tiktok.com/login/phone-or-email/email">Try TikTok Login</a>

Checked by @f1rtx"""

def main():
    print("=== TikTok Account Checker Bot ===")

    # Get user information
    name = input("Enter your name: ")
    print(f"Hello {name}!")

    # Get bot credentials
    bot_token = input("Enter your bot token: ")
    chat_id = input("Enter your chat ID: ")

    num_emails = int(input("How many emails do you want to check? "))

    results = []

    for i in range(num_emails):
        print(f"\n{'='*50}")
        print(f"Checking email {i+1}/{num_emails}...")
        print(f"{'='*50}")

        # Generate random email with real name
        email, email_username, first_name, last_name = generate_real_name_email()
        print(f"📧 Generated email: {email}")

        # Step 1: Check TikTok account
        tiktok_status = check_tiktok_account(email)
        gmail_created = False

        if tiktok_status == "hit":
            print("🎯 TikTok account found - marking as HIT")
            details = get_account_details(email, email_username)

            # Ask if user wants to create Gmail account
            create_gmail = input("Do you want to create a Gmail account for this hit? (y/n): ").lower()
            if create_gmail in ['y', 'yes']:
                gmail_created = simulate_gmail_account_creation(email, first_name, last_name)
                if gmail_created:
                    print("✅ Gmail account created successfully!")

            message = format_hit_message(email, details, gmail_created)
            status = "hit"
        else:
            # Step 2: If no TikTok account, check Gmail
            print("🔄 No TikTok account found, checking Gmail...")
            gmail_status = check_gmail_account(email)

            if gmail_status == "hit":
                print("🎯 Gmail account found - marking as HIT")
                details = get_account_details(email, email_username)
                message = format_hit_message(email, details, False)
                status = "hit"
            else:
                print("💀 No accounts found anywhere - marking as BAD")
                message = format_bad_message(email)
                details = None
                status = "bad"

        # Send to Telegram
        print("📤 Sending result to Telegram...")
        if send_telegram_message(bot_token, chat_id, message):
            print("✅ Message sent successfully to Telegram!")
        else:
            print("❌ Failed to send message to Telegram.")

        results.append((email, status, details, email_username, gmail_created))

        # Add a small delay between requests
        time.sleep(2)

    # Save all results to file
    save_results(results)
    print(f"\nAll results saved to 'tiktok_accounts_results.txt'")

    # Count hits and bad accounts
    hits = sum(1 for _, status, _, _, _ in results if status == "hit")
    bads = num_emails - hits
    gmail_created_count = sum(1 for _, _, _, _, gmail_created in results if gmail_created)

    print(f"\nSummary: {hits} valid accounts found, {bads} invalid accounts")
    print(f"Gmail accounts created: {gmail_created_count}")
    print("\nProcess completed!")

if __name__ == "__main__":
    main()
