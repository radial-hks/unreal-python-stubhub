## LocalPlayerSaveGame Objects

```python
class LocalPlayerSaveGame(SaveGame)
```

Abstract subclass of USaveGame that provides utility functions that let you associate a Save Game object with a specific local player.
These objects can also be loaded using the functions on GameplayStatics, but you would need to call functions like InitializeSaveGame manually.
For simple games, it is fine to blueprint this class directly and add parameters and override functions in blueprint,
but for complicated games you will want to subclass this in native code and set up proper versioning.

**C++ Source:**

- **Module**: Engine
- **File**: SaveGame.h

<a id="unreal.LocalPlayerSaveGame.was_save_requested"></a>

#### was_save_requested

```python
def was_save_requested() -> bool
```

x.was_save_requested() -> bool
Returns true if a save was ever requested, may still be in progress

Returns:
    bool:

<a id="unreal.LocalPlayerSaveGame.was_loaded"></a>

#### was_loaded

```python
def was_loaded() -> bool
```

x.was_loaded() -> bool
Returns true if this was loaded from an existing save

Returns:
    bool:

<a id="unreal.LocalPlayerSaveGame.was_last_save_successful"></a>

#### was_last_save_successful

```python
def was_last_save_successful() -> bool
```

x.was_last_save_successful() -> bool
Returns true if it has been saved at least once and the last save was successful

Returns:
    bool:

<a id="unreal.LocalPlayerSaveGame.save_game_to_slot_for_local_player"></a>

#### save_game_to_slot_for_local_player

```python
def save_game_to_slot_for_local_player() -> bool
```

x.save_game_to_slot_for_local_player() -> bool
Synchronously save using the slot and user index, stalling the main thread until it completes.
This will return true if the save was requested, and errors should be handled by the HandlePostSave function that will be called immediately.

Returns:
    bool:

<a id="unreal.LocalPlayerSaveGame.reset_to_default"></a>

#### reset_to_default

```python
def reset_to_default() -> None
```

x.reset_to_default() -> None
Resets all saved data to default values, called when the load fails or manually

<a id="unreal.LocalPlayerSaveGame.on_reset_to_default"></a>

#### on_reset_to_default

```python
def on_reset_to_default() -> None
```

x.on_reset_to_default() -> None
Blueprint event called to reset all saved data to default, called when the load fails or manually

<a id="unreal.LocalPlayerSaveGame.on_pre_save"></a>

#### on_pre_save

```python
def on_pre_save() -> None
```

x.on_pre_save() -> None
Blueprint event called before saving, do any game-specific fixup here

<a id="unreal.LocalPlayerSaveGame.on_post_save"></a>

#### on_post_save

```python
def on_post_save(success: bool) -> None
```

x.on_post_save(success) -> None
Blueprint event called after saving finishes with success/failure result

Args:
    success (bool):

<a id="unreal.LocalPlayerSaveGame.on_post_load"></a>

#### on_post_load

```python
def on_post_load() -> None
```

x.on_post_load() -> None
Blueprint event called after loading, is not called for newly created saves

<a id="unreal.LocalPlayerSaveGame.load_or_create_save_game_for_local_player"></a>

#### load_or_create_save_game_for_local_player

```python
@classmethod
def load_or_create_save_game_for_local_player(
        cls, save_game_class: Class, local_player_controller: PlayerController,
        slot_name: str) -> LocalPlayerSaveGame
```

X.load_or_create_save_game_for_local_player(save_game_class, local_player_controller, slot_name) -> LocalPlayerSaveGame
Synchronously loads a save game object in the specified slot for the local player, stalling the main thread until it completes.
This will return null for invalid parameters, but will create a new instance if the parameters are valid but loading fails.

Args:
    save_game_class (type(Class)): 
    local_player_controller (PlayerController): 
    slot_name (str): 

Returns:
    LocalPlayerSaveGame:

<a id="unreal.LocalPlayerSaveGame.is_save_in_progress"></a>

#### is_save_in_progress

```python
def is_save_in_progress() -> bool
```

x.is_save_in_progress() -> bool
Returns true if a save is in progress

Returns:
    bool:

<a id="unreal.LocalPlayerSaveGame.get_save_slot_name"></a>

#### get_save_slot_name

```python
def get_save_slot_name() -> str
```

x.get_save_slot_name() -> str
Returns the save slot name to use

Returns:
    str:

<a id="unreal.LocalPlayerSaveGame.get_saved_data_version"></a>

#### get_saved_data_version

```python
def get_saved_data_version() -> int
```

x.get_saved_data_version() -> int32
Returns the game-specific version number this was last saved/loaded as

Returns:
    int32:

<a id="unreal.LocalPlayerSaveGame.get_platform_user_index"></a>

#### get_platform_user_index

```python
def get_platform_user_index() -> int
```

x.get_platform_user_index() -> int32
Returns the user index to save to, based on Local Player by default

Returns:
    int32:

<a id="unreal.LocalPlayerSaveGame.get_platform_user_id"></a>

#### get_platform_user_id

```python
def get_platform_user_id() -> PlatformUserId
```

x.get_platform_user_id() -> PlatformUserId
Returns the platform user to save to, based on Local Player by default

Returns:
    PlatformUserId:

<a id="unreal.LocalPlayerSaveGame.get_local_player_controller"></a>

#### get_local_player_controller

```python
def get_local_player_controller() -> PlayerController
```

x.get_local_player_controller() -> PlayerController
Returns the local player controller this is associated with, this will be valid if it is ready to save

Returns:
    PlayerController:

<a id="unreal.LocalPlayerSaveGame.get_latest_data_version"></a>

#### get_latest_data_version

```python
def get_latest_data_version() -> int
```

x.get_latest_data_version() -> int32
Returns the latest save data version, this is used when the new data is saved

Returns:
    int32:

<a id="unreal.LocalPlayerSaveGame.get_invalid_data_version"></a>

#### get_invalid_data_version

```python
def get_invalid_data_version() -> int
```

x.get_invalid_data_version() -> int32
Returns the invalid save data version, which means it has never been saved/loaded

Returns:
    int32:

<a id="unreal.LocalPlayerSaveGame.async_save_game_to_slot_for_local_player"></a>

#### async_save_game_to_slot_for_local_player

```python
def async_save_game_to_slot_for_local_player() -> bool
```

x.async_save_game_to_slot_for_local_player() -> bool
Asynchronously save to the slot and user index.
This will return true if the save was requested, and errors should be handled by the HandlePostSave function after the save succeeds or fails

Returns:
    bool:

<a id="unreal.LocalPlayerSaveGame.async_load_or_create_save_game_for_local_player"></a>

#### async_load_or_create_save_game_for_local_player

```python
@classmethod
def async_load_or_create_save_game_for_local_player(
        cls, save_game_class: Class, local_player_controller: PlayerController,
        slot_name: str, delegate: OnLocalPlayerSaveGameLoaded) -> bool
```

X.async_load_or_create_save_game_for_local_player(save_game_class, local_player_controller, slot_name, delegate) -> bool
Asynchronously loads a save game object in the specified slot for the local player, if this returns true the delegate will get called later.
False means the load was never scheduled, otherwise it will create and initialize a new instance before calling the delegate if loading failed.

Args:
    save_game_class (type(Class)): 
    local_player_controller (PlayerController): 
    slot_name (str): 
    delegate (OnLocalPlayerSaveGameLoaded): 

Returns:
    bool:

<a id="unreal.SpringArmComponent"></a>