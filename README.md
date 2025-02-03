# MAC Address Changer 🛠️

A simple Python script to change the MAC address of a network interface for privacy and security. You can either generate a random MAC address or input a custom one.

## 🚀 Features
- Change the MAC address of a network interface (e.g., `wlan0`, `eth0`)
- Generate a **random MAC address** or enter a **custom** one
- Works on **Linux** systems (requires `sudo` access)
- Verify if the MAC address change was successful

## 📦 Installation
Clone the repository:

```bash
git clone https://github.com/AmrAssi/AnonMAC.git
cd mac-changer-python
🛠️ Usage
Run the script with root privileges:

bash
Copy
Edit
sudo python3 mac_changer.py
Enter your network interface (e.g., wlan0, eth0).
Choose to generate a random MAC or enter one manually.
The script will disable the interface, change the MAC address, and re-enable it.
Example Output:
bash
Copy
Edit
Enter interface (e.g., eth0, wlan0): wlan0
Generate a random MAC? (y/n): y
Current MAC: 98:de:d0:13:75:af
[+] Changing MAC address of wlan0 to 02:ab:3d:45:67:89
New MAC: 02:ab:3d:45:67:89
[+] MAC address changed successfully!
🔍 Check Your MAC Address
To verify your MAC manually:

bash
Copy
Edit
ifconfig wlan0 | grep ether
⚠️ Disclaimer
This script is for educational and ethical purposes only. Changing MAC addresses may violate network policies. Use responsibly!

📜 License
MIT License

---
https://github.com/AmrAssi
