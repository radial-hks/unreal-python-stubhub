## MapPlayerKeyArgs Objects

```python
class MapPlayerKeyArgs(StructBase)
```

Arguments that can be used when mapping a player key

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: EnhancedInputUserSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``create_matching_slot_if_needed`` (bool):  [Read-Write] If there is not a player mapping already with the same Slot and Hardware Device ID, then create a new mapping for this slot.
- ``defer_on_settings_changed_broadcast`` (bool):  [Read-Write] Defers setting changed delegates until the next frame if set to true.
- ``hardware_device_id`` (Name):  [Read-Write] An OPTIONAL specifier about what kind of hardware this mapping is for.
- ``mapping_name`` (Name):  [Read-Write] The name of the mapping for this key. This is either the default mapping name from an Input Action asset, or one
  that is overridden in the Input Mapping Context.
- ``new_key`` (Key):  [Read-Write] The new Key that this should be mapped to
- ``profile_id`` (GameplayTag):  [Read-Write] The Key Mapping Profile identifier that this mapping should be set on. If this is empty, then the currently equipped profile will be used.
- ``slot`` (PlayerMappableKeySlot):  [Read-Write] What slot this key mapping is for

<a id="unreal.MapPlayerKeyArgs.__init__"></a>

#### __init__

```python
def __init__(mapping_name: Name = "None",
             slot: PlayerMappableKeySlot = PlayerMappableKeySlot.FIRST,
             new_key: Key = [],
             hardware_device_id: Name = "None",
             profile_id: GameplayTag = ["None"],
             create_matching_slot_if_needed: bool = False,
             defer_on_settings_changed_broadcast: bool = False) -> None
```

<a id="unreal.MapPlayerKeyArgs.mapping_name"></a>

#### mapping_name

```python
@property
def mapping_name() -> Name
```

(Name):  [Read-Write] The name of the mapping for this key. This is either the default mapping name from an Input Action asset, or one
that is overridden in the Input Mapping Context.

<a id="unreal.MapPlayerKeyArgs.mapping_name"></a>

#### mapping_name

```python
@mapping_name.setter
def mapping_name(value: Name) -> None
```

<a id="unreal.MapPlayerKeyArgs.slot"></a>

#### slot

```python
@property
def slot() -> PlayerMappableKeySlot
```

(PlayerMappableKeySlot):  [Read-Write] What slot this key mapping is for

<a id="unreal.MapPlayerKeyArgs.slot"></a>

#### slot

```python
@slot.setter
def slot(value: PlayerMappableKeySlot) -> None
```

<a id="unreal.MapPlayerKeyArgs.new_key"></a>

#### new_key

```python
@property
def new_key() -> Key
```

(Key):  [Read-Write] The new Key that this should be mapped to

<a id="unreal.MapPlayerKeyArgs.new_key"></a>

#### new_key

```python
@new_key.setter
def new_key(value: Key) -> None
```

<a id="unreal.MapPlayerKeyArgs.hardware_device_id"></a>

#### hardware_device_id

```python
@property
def hardware_device_id() -> Name
```

(Name):  [Read-Write] An OPTIONAL specifier about what kind of hardware this mapping is for.

<a id="unreal.MapPlayerKeyArgs.hardware_device_id"></a>

#### hardware_device_id

```python
@hardware_device_id.setter
def hardware_device_id(value: Name) -> None
```

<a id="unreal.MapPlayerKeyArgs.profile_id"></a>

#### profile_id

```python
@property
def profile_id() -> GameplayTag
```

(GameplayTag):  [Read-Write] The Key Mapping Profile identifier that this mapping should be set on. If this is empty, then the currently equipped profile will be used.

<a id="unreal.MapPlayerKeyArgs.profile_id"></a>

#### profile_id

```python
@profile_id.setter
def profile_id(value: GameplayTag) -> None
```

<a id="unreal.MapPlayerKeyArgs.create_matching_slot_if_needed"></a>

#### create_matching_slot_if_needed

```python
@property
def create_matching_slot_if_needed() -> bool
```

(bool):  [Read-Write] If there is not a player mapping already with the same Slot and Hardware Device ID, then create a new mapping for this slot.

<a id="unreal.MapPlayerKeyArgs.create_matching_slot_if_needed"></a>

#### create_matching_slot_if_needed

```python
@create_matching_slot_if_needed.setter
def create_matching_slot_if_needed(value: bool) -> None
```

<a id="unreal.MapPlayerKeyArgs.defer_on_settings_changed_broadcast"></a>

#### defer_on_settings_changed_broadcast

```python
@property
def defer_on_settings_changed_broadcast() -> bool
```

(bool):  [Read-Write] Defers setting changed delegates until the next frame if set to true.

<a id="unreal.MapPlayerKeyArgs.defer_on_settings_changed_broadcast"></a>

#### defer_on_settings_changed_broadcast

```python
@defer_on_settings_changed_broadcast.setter
def defer_on_settings_changed_broadcast(value: bool) -> None
```

<a id="unreal.InstancedStruct"></a>