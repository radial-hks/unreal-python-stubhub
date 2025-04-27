## LevelEditorSubsystem Objects

```python
class LevelEditorSubsystem(EditorSubsystem)
```

ULevelEditorSubsystem
Subsystem for exposing Level Editor related functionality to scripts

**C++ Source:**

- **Module**: LevelEditor
- **File**: LevelEditorSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_editor_camera_moved`` (OnLevelEditorEditorCameraMoved):  [Read-Write] Expose EditorCameraMoved to blueprints
- ``on_map_changed`` (OnLevelEditorMapChanged):  [Read-Write] Expose MapChanged to blueprints. Note: This executes too early for some editor scripting, consider using OnMapOpened if this doesn't work for you.
- ``on_map_opened`` (OnLevelEditorMapOpened):  [Read-Write] Expose MapOpened to blueprints
- ``on_post_save_world`` (OnLevelEditorPostSaveWorld):  [Read-Write] Expose PostSaveWorld to blueprints
- ``on_pre_save_world`` (OnLevelEditorPreSaveWorld):  [Read-Write] Expose PreSaveWorld to blueprints

<a id="unreal.LevelEditorSubsystem.on_pre_save_world"></a>

#### on_pre_save_world

```python
@property
def on_pre_save_world() -> OnLevelEditorPreSaveWorld
```

(OnLevelEditorPreSaveWorld):  [Read-Write] Expose PreSaveWorld to blueprints

<a id="unreal.LevelEditorSubsystem.on_pre_save_world"></a>

#### on_pre_save_world

```python
@on_pre_save_world.setter
def on_pre_save_world(value: OnLevelEditorPreSaveWorld) -> None
```

<a id="unreal.LevelEditorSubsystem.on_post_save_world"></a>

#### on_post_save_world

```python
@property
def on_post_save_world() -> OnLevelEditorPostSaveWorld
```

(OnLevelEditorPostSaveWorld):  [Read-Write] Expose PostSaveWorld to blueprints

<a id="unreal.LevelEditorSubsystem.on_post_save_world"></a>

#### on_post_save_world

```python
@on_post_save_world.setter
def on_post_save_world(value: OnLevelEditorPostSaveWorld) -> None
```

<a id="unreal.LevelEditorSubsystem.on_editor_camera_moved"></a>

#### on_editor_camera_moved

```python
@property
def on_editor_camera_moved() -> OnLevelEditorEditorCameraMoved
```

(OnLevelEditorEditorCameraMoved):  [Read-Write] Expose EditorCameraMoved to blueprints

<a id="unreal.LevelEditorSubsystem.on_editor_camera_moved"></a>

#### on_editor_camera_moved

```python
@on_editor_camera_moved.setter
def on_editor_camera_moved(value: OnLevelEditorEditorCameraMoved) -> None
```

<a id="unreal.LevelEditorSubsystem.on_map_changed"></a>

#### on_map_changed

```python
@property
def on_map_changed() -> OnLevelEditorMapChanged
```

(OnLevelEditorMapChanged):  [Read-Write] Expose MapChanged to blueprints. Note: This executes too early for some editor scripting, consider using OnMapOpened if this doesn't work for you.

<a id="unreal.LevelEditorSubsystem.on_map_changed"></a>

#### on_map_changed

```python
@on_map_changed.setter
def on_map_changed(value: OnLevelEditorMapChanged) -> None
```

<a id="unreal.LevelEditorSubsystem.on_map_opened"></a>

#### on_map_opened

```python
@property
def on_map_opened() -> OnLevelEditorMapOpened
```

(OnLevelEditorMapOpened):  [Read-Write] Expose MapOpened to blueprints

<a id="unreal.LevelEditorSubsystem.on_map_opened"></a>

#### on_map_opened

```python
@on_map_opened.setter
def on_map_opened(value: OnLevelEditorMapOpened) -> None
```

<a id="unreal.LevelEditorSubsystem.set_current_level_by_name"></a>

#### set_current_level_by_name

```python
def set_current_level_by_name(level_name: Name) -> bool
```

x.set_current_level_by_name(level_name) -> bool
Set the current level used by the world editor.
If more than one level shares the same name, the first one encounter of that level name will be used.

Args:
    level_name (Name): The name of the Level the actor belongs to (same name as in the ContentBrowser).

Returns:
    bool: True if the operation succeeds.

<a id="unreal.LevelEditorSubsystem.set_allows_cinematic_control"></a>

#### set_allows_cinematic_control

```python
def set_allows_cinematic_control(allow: bool,
                                 viewport_config_key: Name = "None") -> None
```

x.set_allows_cinematic_control(allow, viewport_config_key="None") -> None
Set Allows Cinematic Control

Args:
    allow (bool): 
    viewport_config_key (Name):

<a id="unreal.LevelEditorSubsystem.save_current_level"></a>

#### save_current_level

```python
def save_current_level() -> bool
```

x.save_current_level() -> bool
Saves the specified Level. Must already be saved at lease once to have a valid path.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.LevelEditorSubsystem.save_all_dirty_levels"></a>

#### save_all_dirty_levels

```python
def save_all_dirty_levels() -> bool
```

x.save_all_dirty_levels() -> bool
Saves all Level currently loaded by the World Editor.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.LevelEditorSubsystem.pilot_level_actor"></a>

#### pilot_level_actor

```python
def pilot_level_actor(actor_to_pilot: Actor,
                      viewport_config_key: Name = "None") -> None
```

x.pilot_level_actor(actor_to_pilot, viewport_config_key="None") -> None
Pilot Level Actor

Args:
    actor_to_pilot (Actor): 
    viewport_config_key (Name):

<a id="unreal.LevelEditorSubsystem.new_level_from_template"></a>

#### new_level_from_template

```python
def new_level_from_template(asset_path: str, template_asset_path: str) -> bool
```

x.new_level_from_template(asset_path, template_asset_path) -> bool
Close the current Persistent Level (without saving it). Create a new Level base on another level and save it. Load the new created level.

Args:
    asset_path (str): Asset Path of where the level will be saved. ie. /Game/MyFolder/MyAsset
    template_asset_path (str): Level to be used as Template. ie. /Game/MyFolder/MyAsset

Returns:
    bool: True if the operation succeeds.

<a id="unreal.LevelEditorSubsystem.new_level"></a>

#### new_level

```python
def new_level(asset_path: str, is_partitioned_world: bool = False) -> bool
```

x.new_level(asset_path, is_partitioned_world=False) -> bool
Close the current Persistent Level (without saving it). Create a new blank Level and save it. Load the new created level.

Args:
    asset_path (str): Asset Path of where the level will be saved. ie. /Game/MyFolder/MyAsset
    is_partitioned_world (bool): If true, new map is partitioned.

Returns:
    bool: True if the operation succeeds.

<a id="unreal.LevelEditorSubsystem.load_level"></a>

#### load_level

```python
def load_level(asset_path: str) -> bool
```

x.load_level(asset_path) -> bool
Close the current Persistent Level (without saving it). Loads the specified level.

Args:
    asset_path (str): Asset Path of the level to be loaded. ie. /Game/MyFolder/MyAsset

Returns:
    bool: True if the operation succeeds.

<a id="unreal.LevelEditorSubsystem.is_in_play_in_editor"></a>

#### is_in_play_in_editor

```python
def is_in_play_in_editor() -> bool
```

x.is_in_play_in_editor() -> bool
Is in Play in Editor

Returns:
    bool:

<a id="unreal.LevelEditorSubsystem.get_viewport_config_keys"></a>

#### get_viewport_config_keys

```python
def get_viewport_config_keys() -> Array[Name]
```

x.get_viewport_config_keys() -> Array[Name]
Get Viewport Config Keys

Returns:
    Array[Name]:

<a id="unreal.LevelEditorSubsystem.get_selection_set"></a>

#### get_selection_set

```python
def get_selection_set() -> TypedElementSelectionSet
```

x.get_selection_set() -> TypedElementSelectionSet
Get the selection set for the current world, you can use this to track
and create changes to the level editor's selection

Returns:
    TypedElementSelectionSet:

<a id="unreal.LevelEditorSubsystem.get_pilot_level_actor"></a>

#### get_pilot_level_actor

```python
def get_pilot_level_actor(viewport_config_key: Name = "None") -> Actor
```

x.get_pilot_level_actor(viewport_config_key="None") -> Actor
Get Pilot Level Actor

Args:
    viewport_config_key (Name): 

Returns:
    Actor:

<a id="unreal.LevelEditorSubsystem.get_current_level"></a>

#### get_current_level

```python
def get_current_level() -> Level
```

x.get_current_level() -> Level
Get the current level used by the world editor.

Returns:
    Level: The current level

<a id="unreal.LevelEditorSubsystem.get_allows_cinematic_control"></a>

#### get_allows_cinematic_control

```python
def get_allows_cinematic_control(viewport_config_key: Name = "None") -> bool
```

x.get_allows_cinematic_control(viewport_config_key="None") -> bool
Get Allows Cinematic Control

Args:
    viewport_config_key (Name): 

Returns:
    bool:

<a id="unreal.LevelEditorSubsystem.get_active_viewport_config_key"></a>

#### get_active_viewport_config_key

```python
def get_active_viewport_config_key() -> Name
```

x.get_active_viewport_config_key() -> Name
Get Active Viewport Config Key

Returns:
    Name:

<a id="unreal.LevelEditorSubsystem.eject_pilot_level_actor"></a>

#### eject_pilot_level_actor

```python
def eject_pilot_level_actor(viewport_config_key: Name = "None") -> None
```

x.eject_pilot_level_actor(viewport_config_key="None") -> None
Eject Pilot Level Actor

Args:
    viewport_config_key (Name):

<a id="unreal.LevelEditorSubsystem.editor_set_viewport_realtime"></a>

#### editor_set_viewport_realtime

```python
def editor_set_viewport_realtime(realtime: bool,
                                 viewport_config_key: Name = "None") -> None
```

x.editor_set_viewport_realtime(realtime, viewport_config_key="None") -> None
Editor Set Viewport Realtime

Args:
    realtime (bool): 
    viewport_config_key (Name):

<a id="unreal.LevelEditorSubsystem.editor_set_game_view"></a>

#### editor_set_game_view

```python
def editor_set_game_view(game_view: bool,
                         viewport_config_key: Name = "None") -> None
```

x.editor_set_game_view(game_view, viewport_config_key="None") -> None
Editor Set Game View

Args:
    game_view (bool): 
    viewport_config_key (Name):

<a id="unreal.LevelEditorSubsystem.editor_request_end_play"></a>

#### editor_request_end_play

```python
def editor_request_end_play() -> None
```

x.editor_request_end_play() -> None
Editor Request End Play

<a id="unreal.LevelEditorSubsystem.editor_request_begin_play"></a>

#### editor_request_begin_play

```python
def editor_request_begin_play() -> None
```

x.editor_request_begin_play() -> None
Editor Request Begin Play

<a id="unreal.LevelEditorSubsystem.editor_play_simulate"></a>

#### editor_play_simulate

```python
def editor_play_simulate() -> None
```

x.editor_play_simulate() -> None
Editor Play Simulate

<a id="unreal.LevelEditorSubsystem.editor_invalidate_viewports"></a>

#### editor_invalidate_viewports

```python
def editor_invalidate_viewports() -> None
```

x.editor_invalidate_viewports() -> None
Editor Invalidate Viewports

<a id="unreal.LevelEditorSubsystem.editor_get_game_view"></a>

#### editor_get_game_view

```python
def editor_get_game_view(viewport_config_key: Name = "None") -> bool
```

x.editor_get_game_view(viewport_config_key="None") -> bool
Editor Get Game View

Args:
    viewport_config_key (Name): 

Returns:
    bool:

<a id="unreal.LevelEditorSubsystem.build_light_maps"></a>

#### build_light_maps

```python
def build_light_maps(quality: LightingBuildQuality = LightingBuildQuality.
                     QUALITY_PRODUCTION,
                     with_reflection_captures: bool = False) -> bool
```

x.build_light_maps(quality=LightingBuildQuality.QUALITY_PRODUCTION, with_reflection_captures=False) -> bool
Build Light Maps and optionally the reflection captures.

Args:
    quality (LightingBuildQuality): One of the enum LightingBuildQuality value. Default is Quality_Production.
    with_reflection_captures (bool): Build the related reflection captures after building the light maps.

Returns:
    bool: True if build was successful.

<a id="unreal.MouseCursorInteractor"></a>