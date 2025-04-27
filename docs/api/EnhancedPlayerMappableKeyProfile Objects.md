## EnhancedPlayerMappableKeyProfile Objects

```python
class EnhancedPlayerMappableKeyProfile(Object)
```

Represents one "Profile" that a user can have for their player mappable keys

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: EnhancedInputUserSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``display_name`` (Text):  [Read-Write] The localized display name of this profile
- ``owning_user_id`` (PlatformUserId):  [Read-Only] The platform user id of the owning Local Player of this profile.
- ``player_mapped_keys`` (Map[Name, KeyMappingRow]):  [Read-Write] A map of "Mapping Row Name" to all key mappings associated with it.
  Note: Dirty mappings will be serialized from UEnhancedInputUserSettings::Serialize
- ``profile_identifier`` (GameplayTag):  [Read-Write] The ID of this profile. This can be used by each Key Mapping to filter down which profile is required for it be equipped.

<a id="unreal.EnhancedPlayerMappableKeyProfile.profile_identifier"></a>

#### profile_identifier

```python
@property
def profile_identifier() -> GameplayTag
```

(GameplayTag):  [Read-Only] The ID of this profile. This can be used by each Key Mapping to filter down which profile is required for it be equipped.

<a id="unreal.EnhancedPlayerMappableKeyProfile.owning_user_id"></a>

#### owning_user_id

```python
@property
def owning_user_id() -> PlatformUserId
```

(PlatformUserId):  [Read-Only] The platform user id of the owning Local Player of this profile.

<a id="unreal.EnhancedPlayerMappableKeyProfile.display_name"></a>

#### display_name

```python
@property
def display_name() -> Text
```

(Text):  [Read-Write] The localized display name of this profile

<a id="unreal.EnhancedPlayerMappableKeyProfile.display_name"></a>

#### display_name

```python
@display_name.setter
def display_name(value: Text) -> None
```

<a id="unreal.EnhancedPlayerMappableKeyProfile.player_mapped_keys"></a>

#### player_mapped_keys

```python
@property
def player_mapped_keys() -> Map[Name, KeyMappingRow]
```

(Map[Name, KeyMappingRow]):  [Read-Only] A map of "Mapping Row Name" to all key mappings associated with it.
Note: Dirty mappings will be serialized from UEnhancedInputUserSettings::Serialize

<a id="unreal.EnhancedPlayerMappableKeyProfile.to_string"></a>

#### to_string

```python
def to_string() -> str
```

x.to_string() -> str
Returns a string that can be used to debug the current key mappings.

Returns:
    str:

<a id="unreal.EnhancedPlayerMappableKeyProfile.set_display_name"></a>

#### set_display_name

```python
def set_display_name(new_display_name: Text) -> None
```

x.set_display_name(new_display_name) -> None
Set Display Name

Args:
    new_display_name (Text):

<a id="unreal.EnhancedPlayerMappableKeyProfile.reset_to_default"></a>

#### reset_to_default

```python
def reset_to_default() -> None
```

x.reset_to_default() -> None
Resets all the key mappings in this profile to their default value from their Input Mapping Context.

<a id="unreal.EnhancedPlayerMappableKeyProfile.reset_mapping_to_default"></a>

#### reset_mapping_to_default

```python
def reset_mapping_to_default(mapping_name: Name) -> None
```

x.reset_mapping_to_default(mapping_name) -> None
Resets every player key mapping to this mapping back to it's default value

Args:
    mapping_name (Name):

<a id="unreal.EnhancedPlayerMappableKeyProfile.query_player_mapped_keys"></a>

#### query_player_mapped_keys

```python
def query_player_mapped_keys(
        options: PlayerMappableKeyQueryOptions) -> Tuple[int, Array[Key]]
```

x.query_player_mapped_keys(options) -> (int32, out_keys=Array[Key])
OUT

Args:
    options (PlayerMappableKeyQueryOptions): 

Returns:
    Array[Key]: 

    out_keys (Array[Key]):

<a id="unreal.EnhancedPlayerMappableKeyProfile.k2_find_key_mapping"></a>

#### k2_find_key_mapping

```python
def k2_find_key_mapping(args: MapPlayerKeyArgs) -> PlayerKeyMapping
```

x.k2_find_key_mapping(args) -> PlayerKeyMapping
K2 Find Key Mapping

Args:
    args (MapPlayerKeyArgs): 

Returns:
    PlayerKeyMapping: 

    out_key_mapping (PlayerKeyMapping):

<a id="unreal.EnhancedPlayerMappableKeyProfile.get_profile_identifer"></a>

#### get_profile_identifer

```python
def get_profile_identifer() -> GameplayTag
```

x.get_profile_identifer() -> GameplayTag
Get Profile Identifer

Returns:
    GameplayTag:

<a id="unreal.EnhancedPlayerMappableKeyProfile.get_profile_display_name"></a>

#### get_profile_display_name

```python
def get_profile_display_name() -> Text
```

x.get_profile_display_name() -> Text
Get the localized display name for this profile

Returns:
    Text:

<a id="unreal.EnhancedPlayerMappableKeyProfile.get_player_mapping_rows"></a>

#### get_player_mapping_rows

```python
def get_player_mapping_rows() -> Map[Name, KeyMappingRow]
```

x.get_player_mapping_rows() -> Map[Name, KeyMappingRow]
Get all known key mappings for this profile.

This returns a map of "Mapping Name" -> Player Mappings to that name

Returns:
    Map[Name, KeyMappingRow]:

<a id="unreal.EnhancedPlayerMappableKeyProfile.get_mapping_names_for_key"></a>

#### get_mapping_names_for_key

```python
def get_mapping_names_for_key(key: Key) -> Tuple[int, Array[Name]]
```

x.get_mapping_names_for_key(key) -> (int32, out_mapping_names=Array[Name])
OUT

Args:
    key (Key): 

Returns:
    Array[Name]: 

    out_mapping_names (Array[Name]):

<a id="unreal.EnhancedPlayerMappableKeyProfile.get_mapped_keys_in_row"></a>

#### get_mapped_keys_in_row

```python
def get_mapped_keys_in_row(mapping_name: Name) -> Tuple[int, Array[Key]]
```

x.get_mapped_keys_in_row(mapping_name) -> (int32, out_keys=Array[Key])
OUT

Args:
    mapping_name (Name): 

Returns:
    Array[Key]: 

    out_keys (Array[Key]):

<a id="unreal.EnhancedPlayerMappableKeyProfile.dump_profile_to_log"></a>

#### dump_profile_to_log

```python
def dump_profile_to_log() -> None
```

x.dump_profile_to_log() -> None
A helper function to print out all the current profile settings to the log.

<a id="unreal.EnhancedPlayerMappableKeyProfile.does_mapping_pass_query_options"></a>

#### does_mapping_pass_query_options

```python
def does_mapping_pass_query_options(
        player_mapping: PlayerKeyMapping,
        options: PlayerMappableKeyQueryOptions) -> bool
```

x.does_mapping_pass_query_options(player_mapping, options) -> bool
Returns true if the given player key mapping passes the query filter provided.

Args:
    player_mapping (PlayerKeyMapping): 
    options (PlayerMappableKeyQueryOptions): 

Returns:
    bool:

<a id="unreal.EnhancedInputUserSettings"></a>