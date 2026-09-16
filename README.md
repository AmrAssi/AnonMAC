![AnonMAC — Python and Linux networking](https://raw.githubusercontent.com/AmrAssi/AmrAssi/main/assets/headers/anonmac.svg)
# AnonMAC

A small Python learning utility for changing a Linux network interface's MAC address and reading back the result.

[Source](AnonMAC.py) · [Systems portfolio](https://github.com/AmrAssi/Amr-Assi-Portfolio)

## Implemented behavior

1. Ask for the interface name.
2. Generate a locally administered MAC address beginning with `02`, or accept a user-supplied address.
3. Bring the interface down, apply the address with `ifconfig`, and bring it up.
4. Read the current address and compare it with the requested value.

```mermaid
flowchart LR
    Input["Interface + requested MAC"] --> Down["Interface down"]
    Down --> Change["Apply address"]
    Change --> Up["Interface up"]
    Up --> Verify["Read back and compare"]
```

## Requirements and use

Linux, Python 3, `ifconfig` (usually supplied by `net-tools`), and permission to administer the selected interface.

```bash
git clone https://github.com/AmrAssi/AnonMAC.git
cd AnonMAC
sudo python3 AnonMAC.py
```

Use a local console and a disposable lab interface: the script brings that interface down and can interrupt its connection.

## Current scope

This is a learning script, not a network-management service. It has not been exercised on a live interface as part of this documentation update. The implementation does not validate all user input, inspect every subprocess exit code, or restore the original address automatically. Changes are not configured to persist across reboot.

The script uses Python's standard library; no `pip` packages are required.

## What I practiced

Python functions, subprocess argument lists, reading command output, regular expressions, and the relationship between interface state and link-layer configuration.

[Back to my profile](https://github.com/AmrAssi)

## License

MIT.
