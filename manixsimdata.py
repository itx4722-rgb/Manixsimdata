import os
import requests
import sys
import time

# Colors
R='\033[1;31m'
G='\033[1;32m'
Y='\033[1;33m'
B='\033[1;34m'
C='\033[1;36m'
W='\033[1;37m'
RESET='\033[0m'

def clear():
    os.system("clear")

def banner():
    clear()
    art = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⣄⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⠀⠀⢢⣤⣀⣦⣄⡀⠙⣶⡘⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣀⣨⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣯⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣽⣿⣿⣿⣿⠟⠛⠛⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⣻⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⢿⣷⡀⠀⠀⠀⠀⠀⠀
⠀⠀⣴⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣷⣽⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⣾⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣯⠁⠀⠀⠀⠀
⠀⠀⠐⠛⢿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣷⣄⡀⠀⠀
⠀⠀⠀⠀⠘⠟⠿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⠇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠟⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣷⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    print(f"{B}{art}{RESET}")
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"{W}OWNER  : {G}MANI X KING")
    print(f"{W}TEAM   : {R}BLACK HAT HACKERS")
    print(f"{W}STATUS : {Y}DATABASE ACCESS ACTIVE")
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

def loading():
    print(f"\n{C}[+] Accessing Secure Database", end="")
    for i in range(5):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print("\n")

def open_map(addr):
    if not addr:
        return
    clean = addr.replace(" ", "+")
    url = f"https://www.google.com/maps/search/{clean}"
    print(f"{G}[+] Opening Google Maps...{RESET}")
    os.system(f"termux-open-url '{url}'")

def result_box(record):
    name = record.get("name", "N/A")
    cnic = record.get("cnic", "N/A")
    number = record.get("number", "N/A")
    address = record.get("address", "N/A")

    print(f"""{C}
╔══════════════════════════════════════╗
║            DATABASE RESULT           ║
╠══════════════════════════════════════╣
║ {W}NAME     : {G}{name}
║ {W}CNIC     : {G}{cnic}
║ {W}NUMBER   : {G}{number}
║ {W}ADDRESS  : {G}{address}
╠══════════════════════════════════════╣
║ {Y}Developed By Tool Owner MANI
╚══════════════════════════════════════╝
{RESET}""")

    if address != "N/A":
        open_map(address)

def fetch(num):
    banner()
    loading()
    url = f"https://wasif-ali-simdatabase-api.vercel.app/api/lookup?query={num}"

    try:
        res = requests.get(url, timeout=15).json()

        if not res:
            print(R + "No Records Found" + RESET)
            input("\nPress Enter to continue...")
            return

        if isinstance(res, list):
            print(f"{Y}[+] Multiple Records Found: {len(res)}\n")
            for r in res:
                result_box(r)
        elif isinstance(res, dict):
            result_box(res)
        else:
            print(R + "Unexpected API response format" + RESET)

    except Exception as e:
        print(R + f"API error or server down ({e})" + RESET)

    input("\nPress Enter to continue...")

def format_number(num):
    if num.startswith("03"):
        num = "92" + num[1:]
    return num

def main():
    while True:
        banner()
        print(f"\n{W}[01] Search Number")
        print(f"{W}[02] Search CNIC")
        print(f"{W}[03] WhatsApp Channel")
        print(f"{W}[00] Exit")

        cmd = input(f"\n{G}MANI@SYSTEM:$ ").strip()

        if cmd == "01":
            num = input(f"\n{Y}Enter Number (03xxxxxxxxx): {W}").strip()
            fetch(format_number(num))

        elif cmd == "02":
            cnic = input(f"\n{Y}Enter CNIC (xxxxxxxxxxxxx): {W}").strip()
            fetch(cnic)

        elif cmd == "03":
            os.system("termux-open-url https://whatsapp.com/channel/0029VbAkXZO6WaKm6826Fj3S")

        elif cmd == "00":
            sys.exit()

if __name__ == "__main__":
    main()
