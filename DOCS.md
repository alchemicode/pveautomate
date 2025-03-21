<a id="pveautomate"></a>

# pveautomate

<a id="pveautomate.automate"></a>

# pveautomate.automate

<a id="pveautomate.automate.ProxmoxManager"></a>

## ProxmoxManager Objects

```python
class ProxmoxManager()
```

<a id="pveautomate.automate.ProxmoxManager.__init__"></a>

#### \_\_init\_\_

```python
def __init__(proxmox_url,
             proxmox_user,
             proxmox_password,
             node,
             verify_ssl=False)
```

Initialize the ProxmoxManager with the required parameters.

**Arguments**:

- `proxmox_url` _str_ - The URL of the Proxmox VE server.
- `proxmox_user` _str_ - The username to authenticate with.
- `proxmox_password` _str_ - The password to authenticate with.
- `node` _str_ - The Proxmox VE node to manage.
- `verify_ssl` _bool_ - Whether to verify SSL certificates. Defaults to False.

<a id="pveautomate.automate.ProxmoxManager.write_vm_data"></a>

#### write\_vm\_data

```python
def write_vm_data()
```

Write VM data to a CSV file.

This method is usually internal and is used to dump data on range VMs to a CSV file.

<a id="pveautomate.automate.ProxmoxManager.read_vm_data"></a>

#### read\_vm\_data

```python
def read_vm_data()
```

Read VM data from a CSV file.

This method is usually internal and is used to load data on range VMs from a CSV file.

<a id="pveautomate.automate.ProxmoxManager.authenticate"></a>

#### authenticate

```python
def authenticate(username=None, password=None)
```

Authenticate with the Proxmox VE host and obtain a ticket and CSRF token.

This method is usually internal and is used to authorize with the PVE host.

**Returns**:

- `tuple` - A tuple containing the ticket and CSRF token.

<a id="pveautomate.automate.ProxmoxManager.validate_creds"></a>

#### validate\_creds

```python
def validate_creds(username, password)
```

Validate arbitrary credentials

**Returns**:

- `bool` - True if credentials were accepted, otherwise false

<a id="pveautomate.automate.ProxmoxManager.get_next_vm_id"></a>

#### get\_next\_vm\_id

```python
def get_next_vm_id(ticket=None)
```

Get the next available VMID for clone/create operations.

**Arguments**:

- `ticket` _str, optional_ - The authentication ticket.
  

**Returns**:

- `int` - The next available VMID.

<a id="pveautomate.automate.ProxmoxManager.clone_vm"></a>

#### clone\_vm

```python
def clone_vm(template_id, new_name, new_id)
```

Clone a VM or template to a new VMID and assign a new name.

**Arguments**:

- `template_id` _int_ - The ID of the template to clone.
- `new_name` _str_ - The new name for the cloned VM.
- `new_id` _int_ - The new VMID for the cloned VM.
  

**Returns**:

- `dict` - The response data from the clone operation.

<a id="pveautomate.automate.ProxmoxManager.assign_admin_vm_permissions"></a>

#### assign\_admin\_vm\_permissions

```python
def assign_admin_vm_permissions(vm_id, user)
```

Assign admin permissions to a user for a given VMID.

**Arguments**:

- `vm_id` _int_ - The ID of the VM.
- `user` _str_ - The user to assign admin permissions to.

<a id="pveautomate.automate.ProxmoxManager.set_vm_desc"></a>

#### set\_vm\_desc

```python
def set_vm_desc(vm_id, desc)
```

Set the description (Notes) of a VMID.

**Arguments**:

- `vm_id` _int_ - The ID of the VM.
- `desc` _str_ - The description to set for the VM.

<a id="pveautomate.automate.ProxmoxManager.destroy_vm"></a>

#### destroy\_vm

```python
def destroy_vm(vmid)
```

Destroy a VM by its ID.

**Arguments**:

- `vmid` _int_ - The ID of the VM to destroy.

<a id="pveautomate.automate.ProxmoxManager.create_user"></a>

#### create\_user

```python
def create_user(new_username, new_password, realm, name=None)
```

Create a new user in the given realm

**Arguments**:

- `new_username` _str_ - The username (typically short and lowercase, e.g 'john')
- `new_password` _str_ - The user's new password
- `realm` _str_ - Which realm the user belongs to (typically 'pve' or 'pam' unless your cluster has external authentication sources configured)
- `name` _str, optional_ - Human-readable long name for user (e.g. 'John Doe')

<a id="pveautomate.automate.ProxmoxManager.set_user_group"></a>

#### set\_user\_group

```python
def set_user_group(user, group)
```

Set the group of a user

**Arguments**:

- `user` _str_ - The username of the user (include realm, e.g. 'john@pve')
- `group` _str_ - The group to assign to the user

<a id="pveautomate.automate.ProxmoxManager.list_users"></a>

#### list\_users

```python
def list_users()
```

Internal method. Returns data array about active users in the cluster

<a id="pveautomate.automate.ProxmoxManager.check_if_user"></a>

#### check\_if\_user

```python
def check_if_user(find_userid)
```

Check wether or not given username exists in given realm

**Arguments**:

- `find_userid` _str_ - user id to search for (full userid, e.g. 'foo@pve')

<a id="pveautomate.automate.ProxmoxManager.destroy_range"></a>

#### destroy\_range

```python
def destroy_range()
```

Destroy all range VMs.

<a id="pveautomate.automate.ProxmoxManager.create_range"></a>

#### create\_range

```python
def create_range(ids, user)
```

Create cloned VMs for a given username.

**Arguments**:

- `ids` _list_ - A list of VMIDs to clone.
- `user` _str_ - The username to assign to the cloned VMs. Defaults to None.

<a id="pveautomate.automate.ProxmoxManager.apply_sdn"></a>

#### apply\_sdn

```python
def apply_sdn()
```

Apply SDN settings to the cluster.

<a id="pveautomate.automate.ProxmoxManager.add_subnet_to_vnet"></a>

#### add\_subnet\_to\_vnet

```python
def add_subnet_to_vnet(vnet_id, subnet_cidr, subnet_gateway)
```

Add a subnet to a given VNET ID.

**Arguments**:

- `vnet_id` _int_ - The ID of the VNET.
- `subnet_cidr` _str_ - The CIDR notation of the subnet to add.

<a id="pveautomate.automate.ProxmoxManager.destroy_subnet"></a>

#### destroy\_subnet

```python
def destroy_subnet(vnet, subnet_cidr)
```

Destroy a subnet from a given VNET ID.

**Arguments**:

- `vnet` _int_ - The ID of the VNET.
- `subnet_cidr` _str_ - The CIDR notation of the subnet to add.

<a id="pveautomate.automate.ProxmoxManager.set_vm_power_status"></a>

#### set\_vm\_power\_status

```python
def set_vm_power_status(vmid, state)
```

Set the power state of a VM

**Arguments**:

- `vmid` _int_ - The ID of the VM
- `state` _str_ - The desired state of the VM. One of "start", "stop", "reset", "shutdown", "suspend", "resume", or "reboot"

<a id="pveautomate.automate.ProxmoxManager.set_password"></a>

#### set\_password

```python
def set_password(user, passw)
```

Set the password of a user

**Arguments**:

- `user` _str_ - The username of the user (include realm, e.g. 'john@pve')
- `passw` _str_ - The new

<a id="pveautomate.automate.ProxmoxManager.snapshot_vm"></a>

#### snapshot\_vm

```python
def snapshot_vm(vmid,
                snapshot_name,
                description=None,
                vmstate=False,
                snode=None)
```

Create a snapshot for a given VMID.

**Arguments**:

- `vmid` _int_ - The ID of the VM.
- `snapshot_name` _str_ - The name of the snapshot.
- `description` _str, optional_ - The description of the snapshot.
- `vmstate` _bool, optional_ - Whether to save the VM state (RAM). Defaults to False.
- `snode` _str, optional_ - Node that the VM is on (if different than the API node)

