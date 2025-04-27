## PlayerMappableKeySettings Objects

```python
class PlayerMappableKeySettings(Object)
```

Hold setting information of an Action Input or a Action Key Mapping for setting screen and save purposes.

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: PlayerMappableKeySettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``display_category`` (Text):  [Read-Write] The category that this player mapping is in
- ``display_name`` (Text):  [Read-Write] The localized display name of this key mapping. Use this when displaying the mappings to a user.
- ``metadata`` (Object):  [Read-Write] Metadata that can used to store any other related items to this key mapping such as icons, ability assets, etc.
- ``name`` (Name):  [Read-Write] A unique name for this player mapping to be saved with.
- ``supported_key_profiles`` (GameplayTagContainer):  [Read-Write] If this key mapping should only be added when a specific key profile is equipped, then set those here.

  If this is empty, then the key mapping will not be filtered out based on the current profile.

<a id="unreal.PlayerMappableKeySettings.metadata"></a>

#### metadata

```python
@property
def metadata() -> Object
```

(Object):  [Read-Only] Metadata that can used to store any other related items to this key mapping such as icons, ability assets, etc.

<a id="unreal.PlayerMappableKeySettings.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Only] A unique name for this player mapping to be saved with.

<a id="unreal.PlayerMappableKeySettings.display_name"></a>

#### display_name

```python
@property
def display_name() -> Text
```

(Text):  [Read-Only] The localized display name of this key mapping. Use this when displaying the mappings to a user.

<a id="unreal.PlayerMappableKeySettings.display_category"></a>

#### display_category

```python
@property
def display_category() -> Text
```

(Text):  [Read-Only] The category that this player mapping is in

<a id="unreal.PlayerMappableKeySettings.supported_key_profiles"></a>

#### supported_key_profiles

```python
@property
def supported_key_profiles() -> GameplayTagContainer
```

(GameplayTagContainer):  [Read-Only] If this key mapping should only be added when a specific key profile is equipped, then set those here.

If this is empty, then the key mapping will not be filtered out based on the current profile.

<a id="unreal.DisplayClusterBlueprint"></a>