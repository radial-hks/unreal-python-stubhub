## EditorLevelUtils Objects

```python
class EditorLevelUtils(Object)
```

Editor Level Utils

**C++ Source:**

- **Module**: UnrealEd
- **File**: EditorLevelUtils.h

<a id="unreal.EditorLevelUtils.set_level_visibility"></a>

#### set_level_visibility

```python
@classmethod
def set_level_visibility(
    cls,
    level: Level,
    should_be_visible: bool,
    force_layers_visible: bool,
    modify_mode: LevelVisibilityDirtyMode = LevelVisibilityDirtyMode.
    MODIFY_ON_CHANGE
) -> None
```

X.set_level_visibility(level, should_be_visible, force_layers_visible, modify_mode=LevelVisibilityDirtyMode.MODIFY_ON_CHANGE) -> None
Sets a level's visibility in the editor. Less efficient than SetLevelsVisibility when changing the visibility of multiple levels simultaneously.

Args:
    level (Level): The level to modify.
    should_be_visible (bool): The level's new visibility state.
    force_layers_visible (bool): If true and the level is visible, force the level's layers to be visible.
    modify_mode (LevelVisibilityDirtyMode): ELevelVisibilityDirtyMode mode value.

<a id="unreal.EditorLevelUtils.set_levels_visibility"></a>

#### set_levels_visibility

```python
@classmethod
def set_levels_visibility(
    cls,
    levels: Array[Level],
    should_be_visible: Array[bool],
    force_layers_visible: bool,
    modify_mode: LevelVisibilityDirtyMode = LevelVisibilityDirtyMode.
    MODIFY_ON_CHANGE
) -> None
```

X.set_levels_visibility(levels, should_be_visible, force_layers_visible, modify_mode=LevelVisibilityDirtyMode.MODIFY_ON_CHANGE) -> None
Sets a level's visibility in the editor. More efficient than SetLevelsVisibility when changing the visibility of multiple levels simultaneously.

Args:
    levels (Array[Level]): The levels to modify.
    should_be_visible (Array[bool]): The level's new visibility state for each level.
    force_layers_visible (bool): If true and the level is visible, force the level's layers to be visible.
    modify_mode (LevelVisibilityDirtyMode): ELevelVisibilityDirtyMode mode value.

<a id="unreal.EditorLevelUtils.move_selected_actors_to_level"></a>

#### move_selected_actors_to_level

```python
@classmethod
def move_selected_actors_to_level(cls,
                                  dest_level: LevelStreaming,
                                  warn_about_references: bool = True) -> int
```

X.move_selected_actors_to_level(dest_level, warn_about_references=True) -> int32
Moves the currently selected actors to the specified streaming level. The new actors will be selected

Args:
    dest_level (LevelStreaming): 
    warn_about_references (bool): Whether or not to show a modal warning about referenced actors that may no longer function after being moved

Returns:
    int32: The number of actors that were successfully moved to the new level

<a id="unreal.EditorLevelUtils.move_actors_to_level"></a>

#### move_actors_to_level

```python
@classmethod
def move_actors_to_level(cls,
                         actors_to_move: Array[Actor],
                         dest_streaming_level: LevelStreaming,
                         warn_about_references: bool = True,
                         warn_about_renaming: bool = True) -> int
```

X.move_actors_to_level(actors_to_move, dest_streaming_level, warn_about_references=True, warn_about_renaming=True) -> int32
Moves the specified list of actors to the specified streaming level. The new actors will be selected

Args:
    actors_to_move (Array[Actor]): List of actors to move
    dest_streaming_level (LevelStreaming): The destination streaming level of the current world to move the actors to
    warn_about_references (bool): Whether or not to show a modal warning about referenced actors that may no longer function after being moved
    warn_about_renaming (bool): 

Returns:
    int32: The number of actors that were successfully moved to the new level

<a id="unreal.EditorLevelUtils.make_level_current"></a>

#### make_level_current

```python
@classmethod
def make_level_current(cls, streaming_level: LevelStreaming) -> None
```

X.make_level_current(streaming_level) -> None
Makes the specified streaming level the current level for editing.
The current level is where actors are spawned to when calling SpawnActor

Args:
    streaming_level (LevelStreaming):

<a id="unreal.EditorLevelUtils.remove_level_from_world"></a>

#### remove_level_from_world

```python
@classmethod
def remove_level_from_world(cls,
                            level: Level,
                            clear_selection: bool = True,
                            reset_transaction_buffer: bool = True) -> bool
```

X.remove_level_from_world(level, clear_selection=True, reset_transaction_buffer=True) -> bool
Removes given level from the world. Note, this will only work for sub-levels in the main level.

Levels are not saved when added to the world. They can be saved with the "Save Map" function

Args:
    level (Level): Level asset to remove from the world.
    clear_selection (bool): If true, it will clear the editor selection.
    reset_transaction_buffer (bool): If true, it will reset the transaction buffer (i.e. clear undo history)

Returns:
    bool: True if the level was successfully removed.

<a id="unreal.EditorLevelUtils.add_level_to_world_with_transform"></a>

#### add_level_to_world_with_transform

```python
@classmethod
def add_level_to_world_with_transform(
        cls, world: World, level_package_name: str,
        level_streaming_class: Class,
        level_transform: Transform) -> LevelStreaming
```

X.add_level_to_world_with_transform(world, level_package_name, level_streaming_class, level_transform) -> LevelStreaming
Adds the named level package to the world at the given position.  Does nothing if the level already exists in the world.

Args:
    world (World): 
    level_package_name (str): The package name ("e.g /Game/MyLevel") of the level package to add.
    level_streaming_class (type(Class)): The streaming class type to use for the level.
    level_transform (Transform): The origin of the new level in the world.

Returns:
    LevelStreaming: The new level, or NULL if the level couldn't added.

<a id="unreal.EditorLevelUtils.add_level_to_world"></a>

#### add_level_to_world

```python
@classmethod
def add_level_to_world(cls, world: World, level_package_name: str,
                       level_streaming_class: Class) -> LevelStreaming
```

X.add_level_to_world(world, level_package_name, level_streaming_class) -> LevelStreaming
Adds the named level package to the world.  Does nothing if the level already exists in the world.

Levels are not saved when added to the world. They can be saved with the "Save Map" function

Args:
    world (World): 
    level_package_name (str): The package name ("e.g /Game/MyLevel") of the level package to add.
    level_streaming_class (type(Class)): The streaming class type to use for the level.

Returns:
    LevelStreaming: The new level, or NULL if the level couldn't added.

<a id="unreal.EditorLevelUtils.get_levels"></a>

#### get_levels

```python
@classmethod
def get_levels(cls, world: World) -> Array[Level]
```

X.get_levels(world) -> Array[Level]
Returns all levels for a world.

Args:
    world (World): World containing levels

Returns:
    Array[Level]: Set of all levels

<a id="unreal.EditorLevelUtils.create_new_streaming_level"></a>

#### create_new_streaming_level

```python
@classmethod
def create_new_streaming_level(
        cls,
        level_streaming_class: Class,
        new_level_path: str = "",
        move_selected_actors_into_new_level: bool = False) -> LevelStreaming
```

X.create_new_streaming_level(level_streaming_class, new_level_path="", move_selected_actors_into_new_level=False) -> LevelStreaming
Creates a new streaming level in the current world

Args:
    level_streaming_class (type(Class)): The streaming class type instead to use for the level.
    new_level_path (str): Optional path to the level package path format ("e.g /Game/MyLevel").  If empty, the user will be prompted during the save process.
    move_selected_actors_into_new_level (bool): If true, move any selected actors into the new level.

Returns:
    LevelStreaming: Returns the newly created level, or NULL on failure

<a id="unreal.EnumFactory"></a>