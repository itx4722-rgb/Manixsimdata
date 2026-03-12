import os, requests, time, sys

# -------- Neon Colors --------
R='\033[1;31m'
G='\033[1;32m'
Y='\033[1;33m'
B='\033[1;34m'
C='\033[1;36m'
W='\033[1;37m'
RESET='\033[0m'

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def jbk_banner():
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

    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"{W} OWNER  : {G}MANI X KING")
    print(f"{W} TEAM   : {R}BLACK HAT HACKERS")
    print(f"{W} STATUS : {Y}DATABASE ACCESS ACTIVE")
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

def open_map(address):
    clean_addr = address.replace('null','').replace('no','').replace('-','').strip()
    search_url = f"https://www.google.com/maps/search/{clean_addr.replace(' ','+')}"
    print(f"\n{G}[+] Opening Map for Valid Location...{RESET}")
    os.system(f"termux-open-url '{search_url}'")

def fetch_data(num):

    jbk_banner()
    print(f"\n{W}[{G}*{W}] {C}BYPASSING DATABASE SECURITY...{RESET}")

    url=f"https://howler-database-api.vercel.app/api/lookup?phone={num}"

    try:

        res=requests.get(url,timeout=15).json()

        target_address=""

        print(f"\n{C}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print(f"{C}┃{W} 🔍 SEARCH RESULTS {C}┃")
        print(f"{C}┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")

        if res:

            for key,val in res.items():

                k_low=str(key).lower()

                if any(x in k_low for x in ["howler","developer","status","count","query","success"]):
                    continue

                if isinstance(val,list):

                    for item in val:

                        for k,v in item.items():

                            print(f"{C}┃ {G}{k.upper():<12} {W}: {str(v)[:25]:<25} {C}┃")

                            if "address" in k.lower():
                                target_address=v

                else:

                    print(f"{C}┃ {G}{key.upper():<12} {W}: {str(val)[:25]:<25} {C}┃")

                    if "address" in k_low:
                        target_address=val

        else:
            print(f"{C}┃ {R}[!] NO RECORDS FOUND {C}┃")

        print(f"{C}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

        if target_address:

            print(f"\n{Y}[>] Location Found: {W}{target_address}")

            ask=input(f"{G}[?] View on Google Maps? (y/n): ").lower()

            if ask=="y":
                open_map(target_address)

    except:
        print(f"{R}[!] ERROR: UNABLE TO CONNECT TO DATABASE.")

def main():

    while True:

        jbk_banner()

        print(f"\n {W}[{G}01{W}] {C}DATABASE SEARCH (MAPS ENABLED)")
        print(f" {W}[{G}02{W}] {C}WHATSAPP CHANNEL")
        print(f" {W}[{R}00{W}] {R}EXIT SYSTEM")

        cmd=input(f"\n {G}MANI{W}@{G}SYSTEM{W}:~$ ")

        if cmd=="01":

            n=input(f"\n {Y}[?] Enter Number (03xxxxxxxxx): ")

            fetch_data(n)

        elif cmd=="02":

            os.system("termux-open-url https://whatsapp.com/channel/0029VbAkXZO6WaKm6826Fj3S")

        elif cmd=="00":
            sys.exit()

if __name__=="__main__":
    main()
