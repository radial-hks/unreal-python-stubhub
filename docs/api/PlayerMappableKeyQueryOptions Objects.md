## PlayerMappableKeyQueryOptions Objects

```python
class PlayerMappableKeyQueryOptions(StructBase)
```

Options when querying what keys are mapped to a specific action on the player mappable
key profile.

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: EnhancedInputUserSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``key_to_match`` (Key):  [Read-Write] If specified, then this key will be used to match against when checking if the key types and axis are the same.
- ``mapping_name`` (Name):  [Read-Write] The mapping name to search for
- ``match_basic_key_types`` (bool):  [Read-Write] If true, then only keys that have the same value for IsGamepadKey, IsTouch, and IsGesture will be included in the results of this query
- ``match_key_axis_type`` (bool):  [Read-Write] If true, then only keys that have the same value of IsAxis1D, IsAxis2D, and IsAxis3D will be included in the results of this query
- ``required_device_flags`` (int32):  [Read-Write] If set, then only player mappings whose Hardware Device Identifier that has the same flags as this will be included in the results
- ``required_device_type`` (HardwareDevicePrimaryType):  [Read-Write] If set, then only player mappings whose hardware device identifier that has the same primary input device type will be included in the results of this query
- ``slot_to_match`` (PlayerMappableKeySlot):  [Read-Write] The key slot that will be required to match if set. By default this is EPlayerMappableKeySlot::Unspecified, which will not filter by the slot at all.

<a id="unreal.PlayerMappableKeyQueryOptions.__init__"></a>

#### __init__

```python
def __init__(
        mapping_name: Name = "None",
        key_to_match: Key = [],
        slot_to_match: PlayerMappableKeySlot = PlayerMappableKeySlot.FIRST,
        match_basic_key_types: bool = False,
        match_key_axis_type: bool = False,
        required_device_type:
    HardwareDevicePrimaryType = HardwareDevicePrimaryType.UNSPECIFIED,
        required_device_flags: int = 0) -> None
```

<a id="unreal.PlayerMappableKeyQueryOptions.mapping_name"></a>

#### mapping_name

```python
@property
def mapping_name() -> Name
```

(Name):  [Read-Write] The mapping name to search for

<a id="unreal.PlayerMappableKeyQueryOptions.mapping_name"></a>

#### mapping_name

```python
@mapping_name.setter
def mapping_name(value: Name) -> None
```

<a id="unreal.PlayerMappableKeyQueryOptions.key_to_match"></a>

#### key_to_match

```python
@property
def key_to_match() -> Key
```

(Key):  [Read-Write] If specified, then this key will be used to match against when checking if the key types and axis are the same.

<a id="unreal.PlayerMappableKeyQueryOptions.key_to_match"></a>

#### key_to_match

```python
@key_to_match.setter
def key_to_match(value: Key) -> None
```

<a id="unreal.PlayerMappableKeyQueryOptions.slot_to_match"></a>

#### slot_to_match

```python
@property
def slot_to_match() -> PlayerMappableKeySlot
```

(PlayerMappableKeySlot):  [Read-Write] The key slot that will be required to match if set. By default this is EPlayerMappableKeySlot::Unspecified, which will not filter by the slot at all.

<a id="unreal.PlayerMappableKeyQueryOptions.slot_to_match"></a>

#### slot_to_match

```python
@slot_to_match.setter
def slot_to_match(value: PlayerMappableKeySlot) -> None
```

<a id="unreal.PlayerMappableKeyQueryOptions.match_basic_key_types"></a>

#### match_basic_key_types

```python
@property
def match_basic_key_types() -> bool
```

(bool):  [Read-Write] If true, then only keys that have the same value for IsGamepadKey, IsTouch, and IsGesture will be included in the results of this query

<a id="unreal.PlayerMappableKeyQueryOptions.match_basic_key_types"></a>

#### match_basic_key_types

```python
@match_basic_key_types.setter
def match_basic_key_types(value: bool) -> None
```

<a id="unreal.PlayerMappableKeyQueryOptions.match_key_axis_type"></a>

#### match_key_axis_type

```python
@property
def match_key_axis_type() -> bool
```

(bool):  [Read-Write] If true, then only keys that have the same value of IsAxis1D, IsAxis2D, and IsAxis3D will be included in the results of this query

<a id="unreal.PlayerMappableKeyQueryOptions.match_key_axis_type"></a>

#### match_key_axis_type

```python
@match_key_axis_type.setter
def match_key_axis_type(value: bool) -> None
```

<a id="unreal.PlayerMappableKeyQueryOptions.required_device_type"></a>

#### required_device_type

```python
@property
def required_device_type() -> HardwareDevicePrimaryType
```

(HardwareDevicePrimaryType):  [Read-Write] If set, then only player mappings whose hardware device identifier that has the same primary input device type will be included in the results of this query

<a id="unreal.PlayerMappableKeyQueryOptions.required_device_type"></a>

#### required_device_type

```python
@required_device_type.setter
def required_device_type(value: HardwareDevicePrimaryType) -> None
```

<a id="unreal.PlayerMappableKeyQueryOptions.required_device_flags"></a>

#### required_device_flags

```python
@property
def required_device_flags() -> int
```

(int32):  [Read-Write] If set, then only player mappings whose Hardware Device Identifier that has the same flags as this will be included in the results

<a id="unreal.PlayerMappableKeyQueryOptions.required_device_flags"></a>

#### required_device_flags

```python
@required_device_flags.setter
def required_device_flags(value: int) -> None
```

<a id="unreal.MappingQueryIssue"></a>