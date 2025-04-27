## PlayerMappableInputConfig Objects

```python
class PlayerMappableInputConfig(PrimaryDataAsset)
```

UPlayerMappableInputConfig

This represents one set of Player Mappable controller/keymappings. You can use this input config to create
the default mappings for your player to start with in your game. It provides an easy way to get only the player
mappable key actions, and it can be used to add multiple UInputMappingContext's at once to the player.

Populate this data asset with Input Mapping Contexts that have player mappable actions in them.

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: PlayerMappableInputConfig.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``config_display_name`` (Text):  [Read-Write] The display name that can be used
- ``config_name`` (Name):  [Read-Write] The unique name of this config that can be used when saving it
- ``contexts`` (Map[InputMappingContext, int32]):  [Read-Write] Mapping contexts that make up this Input Config with their associated priority.
- ``is_deprecated`` (bool):  [Read-Write] A flag that can be used to mark this Input Config as deprecated to your player/designers.
- ``metadata`` (Object):  [Read-Write] Metadata that can used to store any other related items to your key mapping such as icons, ability assets, etc.

<a id="unreal.PlayerMappableInputConfig.config_name"></a>

#### config_name

```python
@property
def config_name() -> Name
```

(Name):  [Read-Only] The unique name of this config that can be used when saving it

<a id="unreal.PlayerMappableInputConfig.config_display_name"></a>

#### config_display_name

```python
@property
def config_display_name() -> Text
```

(Text):  [Read-Only] The display name that can be used

<a id="unreal.PlayerMappableInputConfig.is_deprecated"></a>

#### is_deprecated

```python
@property
def is_deprecated() -> bool
```

(bool):  [Read-Only] A flag that can be used to mark this Input Config as deprecated to your player/designers.

<a id="unreal.PlayerMappableInputConfig.metadata"></a>

#### metadata

```python
@property
def metadata() -> Object
```

(Object):  [Read-Only] Metadata that can used to store any other related items to your key mapping such as icons, ability assets, etc.

<a id="unreal.PlayerMappableInputConfig.contexts"></a>

#### contexts

```python
@property
def contexts() -> Map[InputMappingContext, int]
```

(Map[InputMappingContext, int32]):  [Read-Only] Mapping contexts that make up this Input Config with their associated priority.

<a id="unreal.PlayerMappableInputConfig.reset_to_default"></a>

#### reset_to_default

```python
def reset_to_default() -> None
```

x.reset_to_default() -> None
Resets this mappable config to use the keys

<a id="unreal.PlayerMappableInputConfig.is_deprecated"></a>

#### is_deprecated

```python
def is_deprecated() -> bool
```

x.is_deprecated() -> bool
Is Deprecated

Returns:
    bool:

<a id="unreal.PlayerMappableInputConfig.get_player_mappable_keys"></a>

#### get_player_mappable_keys

```python
def get_player_mappable_keys() -> Array[EnhancedActionKeyMapping]
```

x.get_player_mappable_keys() -> Array[EnhancedActionKeyMapping]
Get all the player mappable keys in this config.

Returns:
    Array[EnhancedActionKeyMapping]:

<a id="unreal.PlayerMappableInputConfig.get_metadata"></a>

#### get_metadata

```python
def get_metadata() -> Object
```

x.get_metadata() -> Object
Get all the player mappable keys in this config.

Returns:
    Object:

<a id="unreal.PlayerMappableInputConfig.get_mapping_contexts"></a>

#### get_mapping_contexts

```python
def get_mapping_contexts() -> Map[InputMappingContext, int]
```

x.get_mapping_contexts() -> Map[InputMappingContext, int32]
Return all the Input Mapping contexts that

Returns:
    Map[InputMappingContext, int32]:

<a id="unreal.PlayerMappableInputConfig.get_mapping_by_name"></a>

#### get_mapping_by_name

```python
def get_mapping_by_name(mapping_name: Name) -> EnhancedActionKeyMapping
```

x.get_mapping_by_name(mapping_name) -> EnhancedActionKeyMapping
Returns the action key mapping for the mapping that matches the given name

Args:
    mapping_name (Name): 

Returns:
    EnhancedActionKeyMapping:

<a id="unreal.PlayerMappableInputConfig.get_keys_bound_to_action"></a>

#### get_keys_bound_to_action

```python
def get_keys_bound_to_action(
        action: InputAction) -> Array[EnhancedActionKeyMapping]
```

x.get_keys_bound_to_action(action) -> Array[EnhancedActionKeyMapping]
Returns all the keys mapped to a specific Input Action in this mapping config.

Args:
    action (InputAction): 

Returns:
    Array[EnhancedActionKeyMapping]:

<a id="unreal.PlayerMappableInputConfig.get_display_name"></a>

#### get_display_name

```python
def get_display_name() -> Text
```

x.get_display_name() -> Text
Get Display Name

Returns:
    Text:

<a id="unreal.PlayerMappableInputConfig.get_config_name"></a>

#### get_config_name

```python
def get_config_name() -> Name
```

x.get_config_name() -> Name
Get Config Name

Returns:
    Name:

<a id="unreal.PlayerMappableKeySettings"></a>