## PlayerKeyMapping Objects

```python
class PlayerKeyMapping(StructBase)
```

Represents a single key mapping that is set by the player

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: EnhancedInputUserSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``associated_input_action`` (InputAction):  [Read-Only] The input action associated with this player key mapping
- ``current_key`` (Key):  [Read-Only] The key that the player has mapped to
- ``default_key`` (Key):  [Read-Only] The default key that this mapping was set to in its input mapping context
- ``display_category`` (Text):  [Read-Only] Localized display category of this mapping
- ``display_name`` (Text):  [Read-Only] Localized display name of this mapping
- ``hardware_device_id`` (HardwareDeviceIdentifier):  [Read-Only] An optional Hardware Device specifier for this mapping
- ``is_dirty`` (bool):  [Read-Only] True if this key mapping is dirty (i.e. has been changed by the player)
- ``mapping_name`` (Name):  [Read-Only] The name of the mapping for this key
- ``slot`` (PlayerMappableKeySlot):  [Read-Only] What slot this key is mapped to

<a id="unreal.PlayerKeyMapping.__init__"></a>

#### __init__

```python
def __init__(mapping_name: Name = "None",
             display_name: Text = "",
             display_category: Text = "",
             slot: PlayerMappableKeySlot = PlayerMappableKeySlot.FIRST,
             is_dirty: bool = False,
             default_key: Key = [],
             current_key: Key = [],
             hardware_device_id: HardwareDeviceIdentifier = [
                 "None", "None", HardwareDevicePrimaryType.UNSPECIFIED, 0
             ],
             associated_input_action: InputAction = None) -> None
```

<a id="unreal.PlayerKeyMapping.mapping_name"></a>

#### mapping_name

```python
@property
def mapping_name() -> Name
```

(Name):  [Read-Only] The name of the mapping for this key

<a id="unreal.PlayerKeyMapping.display_name"></a>

#### display_name

```python
@property
def display_name() -> Text
```

(Text):  [Read-Only] Localized display name of this mapping

<a id="unreal.PlayerKeyMapping.display_category"></a>

#### display_category

```python
@property
def display_category() -> Text
```

(Text):  [Read-Only] Localized display category of this mapping

<a id="unreal.PlayerKeyMapping.slot"></a>

#### slot

```python
@property
def slot() -> PlayerMappableKeySlot
```

(PlayerMappableKeySlot):  [Read-Only] What slot this key is mapped to

<a id="unreal.PlayerKeyMapping.is_dirty"></a>

#### is_dirty

```python
@property
def is_dirty() -> bool
```

(bool):  [Read-Only] True if this key mapping is dirty (i.e. has been changed by the player)

<a id="unreal.PlayerKeyMapping.default_key"></a>

#### default_key

```python
@property
def default_key() -> Key
```

(Key):  [Read-Only] The default key that this mapping was set to in its input mapping context

<a id="unreal.PlayerKeyMapping.current_key"></a>

#### current_key

```python
@property
def current_key() -> Key
```

(Key):  [Read-Only] The key that the player has mapped to

<a id="unreal.PlayerKeyMapping.hardware_device_id"></a>

#### hardware_device_id

```python
@property
def hardware_device_id() -> HardwareDeviceIdentifier
```

(HardwareDeviceIdentifier):  [Read-Only] An optional Hardware Device specifier for this mapping

<a id="unreal.PlayerKeyMapping.associated_input_action"></a>

#### associated_input_action

```python
@property
def associated_input_action() -> InputAction
```

(InputAction):  [Read-Only] The input action associated with this player key mapping

<a id="unreal.HardwareDeviceIdentifier"></a>