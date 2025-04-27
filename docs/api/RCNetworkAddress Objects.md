## RCNetworkAddress Objects

```python
class RCNetworkAddress(StructBase)
```

Utility struct to represent IPv4 Network addresses.

**C++ Source:**

- **Plugin**: RemoteControl
- **Module**: RemoteControlCommon
- **File**: RemoteControlSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``class_a`` (uint8):  [Read-Write] Denotes the first octet of the IPv4 address (0-255.xxx.xxx.xxx)
- ``class_b`` (uint8):  [Read-Write] Denotes the second octet of the IPv4 address (xxx.0-255.xxx.xxx)
- ``class_c`` (uint8):  [Read-Write] Denotes the third octet of the IPv4 address (xxx.xxx.0-255.xxx)
- ``class_d`` (uint8):  [Read-Write] Denotes the fourth octet of the IPv4 address (xxx.xxx.xxx.0-255)

<a id="unreal.RCNetworkAddress.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.RCNetworkAddressRange"></a>