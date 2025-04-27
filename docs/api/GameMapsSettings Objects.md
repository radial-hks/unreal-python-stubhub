## GameMapsSettings Objects

```python
class GameMapsSettings(Object)
```

Game Maps Settings

**C++ Source:**

- **Module**: EngineSettings
- **File**: GameMapsSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``editor_startup_map`` (SoftObjectPath):  [Read-Write] If set, this map will be loaded when the Editor starts up.
- ``editor_template_map_overrides`` (Array[TemplateMapInfoOverride]):  [Read-Write] Map templates that should show up in the new level dialog. This will completely override the default maps chosen by the default editor
- ``four_player_splitscreen_layout`` (FourPlayerSplitScreenType):  [Read-Write] The viewport layout to use if the screen should be split and there are three local players
- ``game_default_map`` (SoftObjectPath):  [Read-Write] The map that will be loaded by default when no other map is loaded.
- ``game_instance_class`` (SoftClassPath):  [Read-Write] The class to use when instantiating the transient GameInstance class
- ``game_mode_class_aliases`` (Array[GameModeName]):  [Read-Write] List of GameModes to load when game= is specified in the URL (e.g. "DM" could be an alias for "MyProject.MyGameModeMP_DM")
- ``game_mode_map_prefixes`` (Array[GameModeName]):  [Read-Write] Overrides the GameMode to use when loading a map that starts with a specific prefix
- ``global_default_game_mode`` (SoftClassPath):  [Read-Write] GameMode to use if not specified in any other way. (e.g. per-map DefaultGameMode or on the URL).
- ``global_default_server_game_mode`` (SoftClassPath):  [Read-Write] GameMode to use if not specified in any other way. (e.g. per-map DefaultGameMode or on the URL) (DEDICATED SERVERS)
  If not set, the GlobalDefaultGameMode value will be used.
- ``local_map_options`` (str):  [Read-Write] The default options that will be appended to a map being loaded.
- ``offset_player_gamepad_ids`` (bool):  [Read-Write] If enabled, this will make so that gamepads start being assigned to the second controller ID in local multiplayer games.
  In PIE sessions with multiple windows, this has the same effect as enabling "Route 1st Gamepad to 2nd Client"
- ``server_default_map`` (SoftObjectPath):  [Read-Write] The map that will be loaded by default when no other map is loaded (DEDICATED SERVER).
- ``three_player_splitscreen_layout`` (ThreePlayerSplitScreenType):  [Read-Write] The viewport layout to use if the screen should be split and there are three local players
- ``transition_map`` (SoftObjectPath):  [Read-Write] The map loaded when transition from one map to another.
- ``two_player_splitscreen_layout`` (TwoPlayerSplitScreenType):  [Read-Write] The viewport layout to use if the screen should be split and there are two local players
- ``use_splitscreen`` (bool):  [Read-Write] Whether the screen should be split or not when multiple local players are present

<a id="unreal.GameMapsSettings.set_skip_assigning_gamepad_to_player1"></a>

#### set_skip_assigning_gamepad_to_player1

```python
def set_skip_assigning_gamepad_to_player1(
        skip_first_player: bool = True) -> None
```

x.set_skip_assigning_gamepad_to_player1(skip_first_player=True) -> None
Modify "Skip Assigning Gamepad to Player 1" GameMapsSettings option
note: This value is saved to local config when changed.

Args:
    skip_first_player (bool): If set connected game pads will only be assigned to the second and subsequent players

<a id="unreal.GameMapsSettings.get_skip_assigning_gamepad_to_player1"></a>

#### get_skip_assigning_gamepad_to_player1

```python
def get_skip_assigning_gamepad_to_player1() -> bool
```

x.get_skip_assigning_gamepad_to_player1() -> bool
Get Skip Assigning Gamepad to Player 1

Returns:
    bool:

<a id="unreal.GameMapsSettings.get_game_maps_settings"></a>

#### get_game_maps_settings

```python
@classmethod
def get_game_maps_settings(cls) -> GameMapsSettings
```

X.get_game_maps_settings() -> GameMapsSettings
Returns the game local maps settings

Returns:
    GameMapsSettings:

<a id="unreal.MeshDescriptionBase"></a>