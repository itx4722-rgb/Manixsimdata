import os, requests, sys, time

# ---------------- Neon Colors ----------------
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
B = '\033[1;34m'
C = '\033[1;36m'
W = '\033[1;37m'
RESET = '\033[0m'

# ---------------- Clear Screen ----------------
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

# ---------------- Banner + ASCII Art ----------------
def neon_banner():
    clear()
    
    # ---------------- ASCII ART ----------------
    ascii_art = [
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⣄⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⣀⠀⠀⢢⣤⣀⣦⣄⡀⠙⣶⡘⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⣀⣀⣨⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣯⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⢀⣽⣿⣿⣿⣿⠟⠛⠛⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠘⣻⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⢿⣷⡀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⣴⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣷⣽⣷⣄⠀⠀⠀⠀⠀",
        "⠀⠀⠀⣾⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣯⠁⠀⠀⠀⠀",
        "⠀⠀⠐⠛⢿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣷⣄⡀⠀⠀",
        "⠀⠀⠀⠀⠘⠟⠿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⠇⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠟⠋⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣷⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀"
    ]
    for line in ascii_art:
        print(f"{B}{line}{RESET}")
        time.sleep(0.03)  # thoda fast animation

    # ---------------- MANI Banner ----------------
    banner_frames = [
        f"{C}███╗   ██╗ ███╗   ██╗ ███╗   ██╗ ██╗",
        f"{G}████╗  ████║ ████╗  ██║ ████╗  ██║ ██║",
        f"{Y}██╔██╗ ██╔██║ ██╔██╗ ██║ ██╔██╗ ██║ ██║",
        f"{B}██║╚██╗██║╚██║ ██║╚██╗██║ ██║╚██╗██║ ██║",
        f"{R}██║ ╚████║ ╚██║ ██║ ╚████║ ██║ ╚████║ ██║",
        f"{W}╚═╝  ╚═══╝  ╚═╝ ╚═╝  ╚═══╝ ╚═╝  ╚═══╝ ╚═╝"
    ]
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    for frame in banner_frames:
        print(frame)
        time.sleep(0.1)
    print(f"{Y}                 MANI TOOLKIT")
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"{W} [+] OWNER  : {G}MANI")
    print(f"{W} [+] TEAM   : {G}MANI")
    print(f"{W} [+] STATUS : {Y}DATABASE ACCESS ACTIVE")
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

# ---------------- Loading Animation ----------------
def loading(msg="Loading"):
    for i in range(6):
        dots = '.' * (i % 4)
        print(f"{G}[+] {msg}{dots} {RESET}", end='\r')
        time.sleep(0.4)
    print(" " * 50, end='\r')

# ---------------- Open Google Maps ----------------
def open_map(address):
    clean_addr = address.replace('null','').replace('no','').replace('-','').strip()
    search_url = f"https://www.google.com/maps/search/{clean_addr.replace(' ','+')}"
    print(f"\n{G}[+] Opening Map for Valid Location...{RESET}")
    os.system(f"termux-open-url '{search_url}'")

# ---------------- Fetch Data ----------------
def fetch_data(num):
    neon_banner()
    loading("Bypassing Database Security")
    url = f"https://howler-database-api.vercel.app/api/lookup?phone={num}"
    target_address = ""
    try:
        res = requests.get(url, timeout=15).json()
        print(f"\n{C}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print(f"{C}┃{W} 🔍 SEARCH RESULTS {C}┃")
        print(f"{C}┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")

        if res:
            for key,val in res.items():
                k_low = str(key).lower()
                if any(x in k_low for x in ["howler","developer","status","count","query","success"]):
                    continue
                if isinstance(val,list):
                    for item in val:
                        for k,v in item.items():
                            print(f"{C}┃ {G}{k.upper():<12} {W}: {str(v)[:25]:<25} {C}┃")
                            if "address" in k.lower() and v and "no" not in str(v).lower() and "null" not in str(v).lower():
                                target_address = v
                else:
                    print(f"{C}┃ {G}{key.upper():<12} {W}: {str(val)[:25]:<25} {C}┃")
                    if "address" in k_low and val and "no" not in str(val).lower() and "null" not in str(val).lower():
                        target_address = val
        else:
            print(f"{C}┃ {R}NO RECORDS FOUND {C}┃")
        print(f"{C}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

        if target_address and len(target_address) > 3:
            print(f"\n{Y}[>] Location Found: {W}{target_address}")
            ask = input(f"{G}[?] View on Google Maps? (y/n): {W}").lower()
            if ask == 'y':
                open_map(target_address)
        else:
            print(f"\n{R}[!] No valid map location found for this record.")

    except:
        print(f"{R}[!] ERROR: UNABLE TO CONNECT TO DATABASE.")
        input(f"\n{Y}Press ENTER to return...")

# ---------------- Main Menu ----------------
def main():
    while True:
        neon_banner()
        print(f"\n {W}[{G}01{W}] {C}DATABASE SEARCH (MAPS ENABLED)")
        print(f" {W}[{G}02{W}] {C}MANI CHANNEL")
        print(f" {W}[{R}00{W}] {R}EXIT SYSTEM")
        print(f"\n {C}────────────────────────────────────────────")

        cmd = input(f" {G}MANI{W}@{G}SYSTEM{W}:~$ ")

        if cmd == '01':
            n = input(f"\n {Y}[?] Enter Number (03xxxxxxxxx): ")
            fetch_data(n)

        elif cmd == '02':
            os.system("termux-open-url https://whatsapp.com/channel/0029VbAkXZO6WaKm6826Fj3S")

        elif cmd == '00':
            sys.exit()

# ---------------- Run ----------------
if __name__ == "__main__":
    main()
