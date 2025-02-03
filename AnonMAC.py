import subprocess
import re
import random

def get_random_mac():
    """Generate a random MAC address."""
    return "02:%02x:%02x:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )

def change_mac(interface, new_mac):
    """Change the MAC address of the given interface."""
    print(f"[+] Changing MAC address of {interface} to {new_mac}")

    subprocess.run(["sudo", "ifconfig", interface, "down"])
    subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["sudo", "ifconfig", interface, "up"])

def get_current_mac(interface):
    """Get the current MAC address of an interface."""
    result = subprocess.run(["ifconfig", interface], capture_output=True, text=True)
    mac_address = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", result.stdout)
    return mac_address.group(0) if mac_address else None

if __name__ == "__main__":
    interface = input("Enter interface (e.g., eth0, wlan0): ")
    random_mac = input("Generate a random MAC? (y/n): ").strip().lower()

    new_mac = get_random_mac() if random_mac == "y" else input("Enter new MAC: ")

    old_mac = get_current_mac(interface)
    print(f"Current MAC: {old_mac}")

    change_mac(interface, new_mac)

    updated_mac = get_current_mac(interface)
    print(f"New MAC: {updated_mac}")

    if updated_mac == new_mac:
        print("[+] MAC address changed successfully!")
    else:
        print("[-] MAC address change failed.")
