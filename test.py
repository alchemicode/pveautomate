# This file is regularly changed for internal debugging convience
# I version control it for laughs, but it's not necesarily a useful reference implementation

from pveautomate.automate import ProxmoxManager
from getpass import getpass

# Create a ProxmoxManager object
pm = ProxmoxManager(
    "https://ccdc.goober.cloud/api2/json",
    "root@pam",
    getpass("Enter password: "),
    "ccdc",
)

# pm.clone_vm(1002, "loltest", pm.get_next_vm_id())

pm.assign_admin_vm_permissions(102, "matt@pve")
