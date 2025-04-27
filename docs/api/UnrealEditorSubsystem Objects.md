## UnrealEditorSubsystem Objects

```python
class UnrealEditorSubsystem(EditorSubsystem)
```

UUnrealEditorSubsystem
Subsystem for exposing editor functionality to scripts

**C++ Source:**

- **Module**: UnrealEd
- **File**: UnrealEditorSubsystem.h

<a id="unreal.UnrealEditorSubsystem.set_level_viewport_camera_info"></a>

#### set_level_viewport_camera_info

```python
def set_level_viewport_camera_info(camera_location: Vector,
                                   camera_rotation: Rotator) -> None
```

x.set_level_viewport_camera_info(camera_location, camera_rotation) -> None
Sets information about the camera position for the primary level editor viewport.
In the UnrealEd module instead of Level Editor as it uses FLevelEditorViewportClient which is in this module

Args:
    camera_location (Vector): Location the camera will be moved to.
    camera_rotation (Rotator): Rotation the camera will be set to.

<a id="unreal.UnrealEditorSubsystem.get_level_viewport_camera_info"></a>

#### get_level_viewport_camera_info

```python
def get_level_viewport_camera_info() -> Optional[Tuple[Vector, Rotator]]
```

x.get_level_viewport_camera_info() -> (camera_location=Vector, camera_rotation=Rotator) or None
Gets information about the camera position for the primary level editor viewport.  In non-editor builds, these will be zeroed
In the UnrealEd module instead of Level Editor as it uses FLevelEditorViewportClient which is in this module

Returns:
    tuple or None: Whether or not we were able to get a camera for a level editing viewport

    camera_location (Vector): (out) Current location of the level editing viewport camera, or zero if none found

    camera_rotation (Rotator): (out) Current rotation of the level editing viewport camera, or zero if none found

<a id="unreal.UnrealEditorSubsystem.get_game_world"></a>

#### get_game_world

```python
def get_game_world() -> World
```

x.get_game_world() -> World
Get Game World

Returns:
    World:

<a id="unreal.UnrealEditorSubsystem.get_editor_world"></a>

#### get_editor_world

```python
def get_editor_world() -> World
```

x.get_editor_world() -> World
Find the World in the world editor. It can then be used as WorldContext by other libraries like GameplayStatics.

Returns:
    World: The World used by the world editor.

<a id="unreal.VariableFrameStrippingSettingsFactory"></a>