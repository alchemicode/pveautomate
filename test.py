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

# print(pm.add_subnet_to_vnet("foobar", "192.167.1.0/24", "192.167.1.1"))
# print(pm.apply_sdn())
# print(pm.create_range([100,101], input("Enter user: ")))

for vm in range(102, 110):
    pm.destroy_vm(vm)

# for i in range(1, 13):
#    cidr = f"192.168.{i}.0/24"
#    gateway = f"192.168.{i}.1"
#    print(pm.add_subnet_to_vnet("foobar", cidr, gateway))
# pm.apply_sdn()

# print(pm.check_if_user("matt@pve"))
