import os, requests, sys

# Colors
R='\033[1;31m'
G='\033[1;32m'
Y='\033[1;33m'
B='\033[1;34m'
C='\033[1;36m'
W='\033[1;37m'
RESET='\033[0m'

def clear():
    os.system('clear')

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

def open_map(addr):

    clean=addr.replace(" ","+")
    url=f"https://www.google.com/maps/search/{clean}"

    print(f"\n{G}[+] Opening Google Maps...{RESET}")

    os.system(f"termux-open-url '{url}'")

def fetch(num):

    banner()

    print(f"\n{C}[+] Searching database...{RESET}")

    url=f"https://wasif-ali-pak-sim-info.vercel.app/API/lookup.js?query={num}"

    try:

        data=requests.get(url,timeout=15).json()

        print(f"\n{C}━━━━━━━━ RESULT ━━━━━━━━{RESET}")

        address=""

        if data:

            for k,v in data.items():

                print(f"{G}{k.upper()} {W}: {v}")

                if "address" in k.lower():
                    address=v

        else:

            print(f"{R}No records found{RESET}")

        if address:

            ask=input(f"\n{Y}Open location in map? (y/n): ")

            if ask=="y":
                open_map(address)

    except:

        print(f"{R}API ERROR OR SERVER DOWN{RESET}")

def main():

    while True:

        banner()

        print(f"\n{W}[{G}1{W}] Search Number")
        print(f"{W}[{G}2{W}] WhatsApp Channel")
        print(f"{W}[{R}0{W}] Exit")

        cmd=input(f"\n{G}MANI@SYSTEM:$ ")

        if cmd=="1":

            num=input(f"\n{Y}Enter Number (03xxxxxxxxx): ")

            fetch(num)

        elif cmd=="2":

            os.system("termux-open-url https://whatsapp.com/channel/0029VbAkXZO6WaKm6826Fj3S")

        elif cmd=="0":

            sys.exit()

if __name__=="__main__":
    main()
