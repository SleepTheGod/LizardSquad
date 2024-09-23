# LizardSquad Attack Script
Overview
The LizardSquad attack script is a Python-based tool designed for network testing and stress testing. It allows users to perform various types of attacks using customizable parameters. This script is intended for educational purposes and should only be used in compliance with local laws and regulations.

Features
Layer 4 attack methods
Multiple attack types including UDP flood, DNS flood, and SYN flood
Easy-to-use command-line interface
Concurrent attack handling
Prerequisites
Python 3.x
Basic understanding of networking concepts
Installation
Clone the repository:

git clone https://github.com/SleepTheGod/LizardSquad.git cd LizardSquad

(Optional) Create a virtual environment:

python3 -m venv venv source venv/bin/activate # On Windows use venv\Scripts\activate

Create a requirements.txt file (if you plan to add external libraries in the future):

touch requirements.txt

Install any required packages (if applicable):

pip install -r requirements.txt

Usage
Run the script using Python:

python lizard.py

Commands
std: Launch a standard UDP flood attack.
dns: Launch a DNS flood attack.
ovh: Launch an OVH attack.
vse: Launch a Source Engine Query attack.
syn: Launch a SYN flood attack.
help: Display the list of available commands.
exit: Exit the script.
Example
To launch a standard UDP flood attack:

std target_ip target_port attack_duration

Replace target_ip, target_port, and attack_duration with the appropriate values.

Disclaimer
This script is intended for educational and testing purposes only. Use it responsibly and ensure you have permission to test the networks and services you are targeting. Unauthorized use may result in legal consequences.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contributing
Contributions are welcome! If you would like to contribute to this project, please fork the repository and submit a pull request.

Contact
For any inquiries or issues, please contact the repository owner.
