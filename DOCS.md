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
def authenticate()
```

Authenticate with the Proxmox VE host and obtain a ticket and CSRF token.

This method is usually internal and is used to authorize with the PVE host.

**Returns**:

- `tuple` - A tuple containing the ticket and CSRF token.

<a id="pveautomate.automate.ProxmoxManager.get_next_vm_id"></a>

#### get\_next\_vm\_id

```python
def get_next_vm_id(ticket)
```

Get the next available VMID for clone/create operations.

**Arguments**:

- `ticket` _str_ - The authentication ticket.
  

**Returns**:

- `int` - The next available VMID.

<a id="pveautomate.automate.ProxmoxManager.clone_vm"></a>

#### clone\_vm

```python
def clone_vm(ticket, csrf_token, template_id, new_name, new_id)
```

Clone a VM or template to a new VMID and assign a new name.

**Arguments**:

- `ticket` _str_ - The authentication ticket.
- `csrf_token` _str_ - The CSRF prevention token.
- `template_id` _int_ - The ID of the template to clone.
- `new_name` _str_ - The new name for the cloned VM.
- `new_id` _int_ - The new VMID for the cloned VM.
  

**Returns**:

- `dict` - The response data from the clone operation.

<a id="pveautomate.automate.ProxmoxManager.assign_admin_vm_permissions"></a>

#### assign\_admin\_vm\_permissions

```python
def assign_admin_vm_permissions(ticket, csrf_token, vm_id, user)
```

Assign admin permissions to a user for a given VMID.

**Arguments**:

- `ticket` _str_ - The authentication ticket.
- `csrf_token` _str_ - The CSRF prevention token.
- `vm_id` _int_ - The ID of the VM.
- `user` _str_ - The user to assign admin permissions to.

<a id="pveautomate.automate.ProxmoxManager.set_vm_desc"></a>

#### set\_vm\_desc

```python
def set_vm_desc(ticket, csrf_token, vm_id, desc)
```

Set the description (Notes) of a VMID.

**Arguments**:

- `ticket` _str_ - The authentication ticket.
- `csrf_token` _str_ - The CSRF prevention token.
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

<a id="pveautomate.automate.ProxmoxManager.destroy_range"></a>

#### destroy\_range

```python
def destroy_range()
```

Destroy all range VMs.

This method is intended for internal use and may not be suitable for a library.

<a id="pveautomate.automate.ProxmoxManager.create_win_range"></a>

#### create\_win\_range

```python
def create_win_range(user=None)
```

Create three cloned VMs for a given username.

This method is intended for internal use and may not be suitable for a library.

**Arguments**:

- `user` _str_ - The username to assign to the cloned VMs. Defaults to None.
