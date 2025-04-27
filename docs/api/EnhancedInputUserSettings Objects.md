## EnhancedInputUserSettings Objects

```python
class EnhancedInputUserSettings(SaveGame)
```

The Enhanced Input User Settings class is a place where you can put all of your Input Related settings
that you want your user to be able to change. Things like their key mappings, aim sensitivity, accessibility
settings, etc. This also provides a Registration point for Input Mappings Contexts (IMC) from possibly unloaded
plugins (i.e. Game Feature Plugins). You can register your IMC from a Game Feature Action plugin here, and then
have access to all the key mappings available. This is very useful for building settings screens because you can
now access all the mappings in your game, even if the entire plugin isn't loaded yet.

The user settings are stored on each UEnhancedPlayerInput object, so each instance of the settings can represent
a single User or Local Player.

To customize this for your game, you can create a subclass of it and change the "UserSettingsClass" in the
Enhanced Input Project Settings.

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: EnhancedInputUserSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_settings_applied`` (EnhancedInputUserSettingsApplied):  [Read-Write]
- ``on_settings_changed`` (EnhancedInputUserSettingsChanged):  [Read-Write]

<a id="unreal.EnhancedInputUserSettings.on_settings_changed"></a>

#### on_settings_changed

```python
@property
def on_settings_changed() -> EnhancedInputUserSettingsChanged
```

(EnhancedInputUserSettingsChanged):  [Read-Write]

<a id="unreal.EnhancedInputUserSettings.on_settings_changed"></a>

#### on_settings_changed

```python
@on_settings_changed.setter
def on_settings_changed(value: EnhancedInputUserSettingsChanged) -> None
```

<a id="unreal.EnhancedInputUserSettings.on_settings_applied"></a>

#### on_settings_applied

```python
@property
def on_settings_applied() -> EnhancedInputUserSettingsApplied
```

(EnhancedInputUserSettingsApplied):  [Read-Write]

<a id="unreal.EnhancedInputUserSettings.on_settings_applied"></a>

#### on_settings_applied

```python
@on_settings_applied.setter
def on_settings_applied(value: EnhancedInputUserSettingsApplied) -> None
```

<a id="unreal.EnhancedInputUserSettings.unregister_input_mapping_contexts"></a>

#### unregister_input_mapping_contexts

```python
def unregister_input_mapping_contexts(
        mapping_contexts: Set[InputMappingContext]) -> bool
```

x.unregister_input_mapping_contexts(mapping_contexts) -> bool
Removes multiple mapping contexts from the registered mapping contexts

Args:
    mapping_contexts (Set[InputMappingContext]): 

Returns:
    bool:

<a id="unreal.EnhancedInputUserSettings.unregister_input_mapping_context"></a>

#### unregister_input_mapping_context

```python
def unregister_input_mapping_context(imc: InputMappingContext) -> bool
```

x.unregister_input_mapping_context(imc) -> bool
Removes this mapping context from the registered mapping contexts

Args:
    imc (InputMappingContext): 

Returns:
    bool:

<a id="unreal.EnhancedInputUserSettings.un_map_player_key"></a>

#### un_map_player_key

```python
def un_map_player_key(args: MapPlayerKeyArgs) -> GameplayTagContainer
```

x.un_map_player_key(args) -> GameplayTagContainer
Unmaps a single player mapping that matches the given Mapping name, slot, and hardware device.

Args:
    args (MapPlayerKeyArgs): 

Returns:
    GameplayTagContainer: 

    failure_reason (GameplayTagContainer):

<a id="unreal.EnhancedInputUserSettings.set_key_profile"></a>

#### set_key_profile

```python
def set_key_profile(profile_id: GameplayTag) -> bool
```

x.set_key_profile(profile_id) -> bool
Changes the currently active key profile to the one with the given name. Returns true if the operation was successful.

Args:
    profile_id (GameplayTag): 

Returns:
    bool:

<a id="unreal.EnhancedInputUserSettings.save_settings"></a>

#### save_settings

```python
def save_settings() -> None
```

x.save_settings() -> None
Synchronously save the settings to a hardcoded save game slot. This will work for simple games,
but if you need to integrate it into an advanced save system you should Serialize this object out with the rest of your save data.

<a id="unreal.EnhancedInputUserSettings.reset_key_profile_to_default"></a>

#### reset_key_profile_to_default

```python
def reset_key_profile_to_default(
        profile_id: GameplayTag) -> GameplayTagContainer
```

x.reset_key_profile_to_default(profile_id) -> GameplayTagContainer
Resets the given key profile to default key mappings

Args:
    profile_id (GameplayTag): The ID of the key profile to reset

Returns:
    GameplayTagContainer: 

    failure_reason (GameplayTagContainer): Populated with failure reasons if the operation fails.

<a id="unreal.EnhancedInputUserSettings.reset_all_player_keys_in_row"></a>

#### reset_all_player_keys_in_row

```python
def reset_all_player_keys_in_row(
        args: MapPlayerKeyArgs) -> GameplayTagContainer
```

x.reset_all_player_keys_in_row(args) -> GameplayTagContainer
Resets each player mapped key to it's default value from the Input Mapping Context that it was registered from.
If a key did not come from an IMC (i.e. it was added additionally by the player) then it will be reset to EKeys::Invalid.

Args:
    args (MapPlayerKeyArgs): Arguments that contain the mapping name and profile ID to find the mapping to reset.

Returns:
    GameplayTagContainer: 

    failure_reason (GameplayTagContainer): Populated with failure reasons if the operation fails.

<a id="unreal.EnhancedInputUserSettings.register_input_mapping_contexts"></a>

#### register_input_mapping_contexts

```python
def register_input_mapping_contexts(
        mapping_contexts: Set[InputMappingContext]) -> bool
```

x.register_input_mapping_contexts(mapping_contexts) -> bool
Registers multiple mapping contexts with the settings

Args:
    mapping_contexts (Set[InputMappingContext]): 

Returns:
    bool:

<a id="unreal.EnhancedInputUserSettings.register_input_mapping_context"></a>

#### register_input_mapping_context

```python
def register_input_mapping_context(imc: InputMappingContext) -> bool
```

x.register_input_mapping_context(imc) -> bool
Registers this mapping context with the user settings. This will iterate all the key mappings
in the context and create an initial Player Mappable Key for every mapping that is marked as mappable.

Args:
    imc (InputMappingContext): 

Returns:
    bool:

<a id="unreal.EnhancedInputUserSettings.map_player_key"></a>

#### map_player_key

```python
def map_player_key(args: MapPlayerKeyArgs) -> GameplayTagContainer
```

x.map_player_key(args) -> GameplayTagContainer
Sets the player mapped key on the current key profile.

Args:
    args (MapPlayerKeyArgs): 

Returns:
    GameplayTagContainer: 

    failure_reason (GameplayTagContainer):

<a id="unreal.EnhancedInputUserSettings.is_mapping_context_registered"></a>

#### is_mapping_context_registered

```python
def is_mapping_context_registered(imc: InputMappingContext) -> bool
```

x.is_mapping_context_registered(imc) -> bool
Returns true if this mapping context is currently registered with the settings

Args:
    imc (InputMappingContext): 

Returns:
    bool:

<a id="unreal.EnhancedInputUserSettings.get_key_profile_with_identifier"></a>

#### get_key_profile_with_identifier

```python
def get_key_profile_with_identifier(
        profile_id: GameplayTag) -> EnhancedPlayerMappableKeyProfile
```

x.get_key_profile_with_identifier(profile_id) -> EnhancedPlayerMappableKeyProfile
Returns the key profile with the given name if one exists. Null if one doesn't exist

Args:
    profile_id (GameplayTag): 

Returns:
    EnhancedPlayerMappableKeyProfile:

<a id="unreal.EnhancedInputUserSettings.get_current_key_profile_identifier"></a>

#### get_current_key_profile_identifier

```python
def get_current_key_profile_identifier() -> GameplayTag
```

x.get_current_key_profile_identifier() -> GameplayTag
Gets the currently selected key profile

Returns:
    GameplayTag:

<a id="unreal.EnhancedInputUserSettings.get_current_key_profile"></a>

#### get_current_key_profile

```python
def get_current_key_profile() -> EnhancedPlayerMappableKeyProfile
```

x.get_current_key_profile() -> EnhancedPlayerMappableKeyProfile
Get the current key profile that the user has set

Returns:
    EnhancedPlayerMappableKeyProfile:

<a id="unreal.EnhancedInputUserSettings.find_mappings_in_row"></a>

#### find_mappings_in_row

```python
def find_mappings_in_row(mapping_name: Name) -> Set[PlayerKeyMapping]
```

x.find_mappings_in_row(mapping_name) -> Set[PlayerKeyMapping]
Returns a set of all player key mappings for the given mapping name.

Args:
    mapping_name (Name): 

Returns:
    Set[PlayerKeyMapping]:

<a id="unreal.EnhancedInputUserSettings.create_new_key_profile"></a>

#### create_new_key_profile

```python
def create_new_key_profile(
    args: PlayerMappableKeyProfileCreationArgs
) -> EnhancedPlayerMappableKeyProfile
```

x.create_new_key_profile(args) -> EnhancedPlayerMappableKeyProfile
Creates a new profile with this name and type.

Args:
    args (PlayerMappableKeyProfileCreationArgs): 

Returns:
    EnhancedPlayerMappableKeyProfile:

<a id="unreal.EnhancedInputUserSettings.async_save_settings"></a>

#### async_save_settings

```python
def async_save_settings() -> None
```

x.async_save_settings() -> None
Asynchronously save the settings to a hardcoded save game slot. This will work for simple games,
but if you need to integrate it into an advanced save system you should Serialize this object out with the rest of your save data.

OnAsyncSaveComplete will be called upon save completion.

<a id="unreal.EnhancedInputUserSettings.apply_settings"></a>

#### apply_settings

```python
def apply_settings() -> None
```

x.apply_settings() -> None
Apply any custom input settings to your user. By default, this will just broadcast the OnSettingsApplied delegate
which is a useful hook to maybe rebuild some UI or do other user facing updates.

<a id="unreal.EnhancedInputComponent"></a>