## Cloning a range setup for multiple users
```py
from pveautomate.automate import ProxmoxManager
from getpass import getpass

# Create a ProxmoxManager object
pm = ProxmoxManager(
    "https://proxmox.foo.bar/api2/json",
    "root@pam",
    getpass("Enter password: "),
    "node1",
)

# Assuming these users already exist
for user in ['matt@pve', 'dave@pve', 'kris@pve']:
    pm.create_range([100,101,102], user) # assuming 100,101,102 are template VMs that you want each user to have a copy of
```