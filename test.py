# This file is regularly changed for internal debugging convience
# I version control it for laughs, but it's not necesarily a useful reference implementation

from pveautomate.automate import ProxmoxManager
from getpass import getpass

# Create a ProxmoxManager object
pm = ProxmoxManager(
    "https://pve.goober.cloud/api2/json",
    "root@pam",
    getpass("Enter password: "),
    "pve1",
)

stuff = pm.snapshot_vm(100, "testsnap2", "wheee", False, "pve6")

print(str(stuff))
