## HardwareDeviceIdentifier Objects

```python
class HardwareDeviceIdentifier(StructBase)
```

An identifier that can be used to determine what input devices are available based on the FInputDeviceScope.
These mappings should match a FInputDeviceScope that is used by an IInputDevice

**C++ Source:**

- **Module**: Engine
- **File**: InputSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``hardware_device_identifier`` (Name):  [Read-Write] The name of this hardware device.
  This should correspond with a FInputDeviceScope that is used by an IInputDevice
- ``input_class_name`` (Name):  [Read-Write] The name of the Input Class that uses this hardware device.
  This should correspond with a FInputDeviceScope that is used by an IInputDevice
- ``primary_device_type`` (HardwareDevicePrimaryType):  [Read-Write] The generic type that this hardware identifies as. This can be used to easily determine behaviors
- ``supported_features_mask`` (int32):  [Read-Write] Flags that represent this hardware device's traits

<a id="unreal.HardwareDeviceIdentifier.__init__"></a>

#### __init__

```python
def __init__(input_class_name: Name = "None",
             hardware_device_identifier: Name = "None",
             primary_device_type:
             HardwareDevicePrimaryType = HardwareDevicePrimaryType.UNSPECIFIED,
             supported_features_mask: int = 0) -> None
```

<a id="unreal.HardwareDeviceIdentifier.input_class_name"></a>

#### input_class_name

```python
@property
def input_class_name() -> Name
```

(Name):  [Read-Only] The name of the Input Class that uses this hardware device.
This should correspond with a FInputDeviceScope that is used by an IInputDevice

<a id="unreal.HardwareDeviceIdentifier.hardware_device_identifier"></a>

#### hardware_device_identifier

```python
@property
def hardware_device_identifier() -> Name
```

(Name):  [Read-Only] The name of this hardware device.
This should correspond with a FInputDeviceScope that is used by an IInputDevice

<a id="unreal.HardwareDeviceIdentifier.primary_device_type"></a>

#### primary_device_type

```python
@property
def primary_device_type() -> HardwareDevicePrimaryType
```

(HardwareDevicePrimaryType):  [Read-Only] The generic type that this hardware identifies as. This can be used to easily determine behaviors

<a id="unreal.HardwareDeviceIdentifier.supported_features_mask"></a>

#### supported_features_mask

```python
@property
def supported_features_mask() -> int
```

(int32):  [Read-Only] Flags that represent this hardware device's traits

<a id="unreal.GameplayTagContainer"></a>