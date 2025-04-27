## VREditorMode Objects

```python
class VREditorMode(VREditorModeBase)
```

VR Editor Mode. Extends editor viewports with functionality for VR controls and object manipulation

**C++ Source:**

- **Module**: VREditor
- **File**: VREditorMode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``interactor_class`` (Class):  [Read-Write] The controller to use when UnrealEd is in VR mode. Use VREditorInteractor get default editor behavior, or select a custom controller for special behavior
- ``teleporter_class`` (Class):  [Read-Write] The teleporter to use when UnrealEd is in VR mode. Use VREditorTeleporter to get default editor behavior, or select a custom teleporter

<a id="unreal.VREditorMode.interactor_class"></a>

#### interactor_class

```python
@property
def interactor_class() -> Class
```

(Class):  [Read-Write] The controller to use when UnrealEd is in VR mode. Use VREditorInteractor get default editor behavior, or select a custom controller for special behavior

<a id="unreal.VREditorMode.interactor_class"></a>

#### interactor_class

```python
@interactor_class.setter
def interactor_class(value: Class) -> None
```

<a id="unreal.VREditorMode.teleporter_class"></a>

#### teleporter_class

```python
@property
def teleporter_class() -> Class
```

(Class):  [Read-Write] The teleporter to use when UnrealEd is in VR mode. Use VREditorTeleporter to get default editor behavior, or select a custom teleporter

<a id="unreal.VREditorMode.teleporter_class"></a>

#### teleporter_class

```python
@teleporter_class.setter
def teleporter_class(value: Class) -> None
```

<a id="unreal.VREditorMode.set_game_view"></a>

#### set_game_view

```python
def set_game_view(game_view: bool) -> None
```

x.set_game_view(game_view) -> None
Display the scene more closely to how it would appear at runtime (as opposed to edit time).

Args:
    game_view (bool):

<a id="unreal.VREditorMode.is_in_game_view"></a>

#### is_in_game_view

```python
def is_in_game_view() -> bool
```

x.is_in_game_view() -> bool
Returns whether game view is currently active.

Returns:
    bool:

<a id="unreal.VREditorMode.get_world_scale_factor"></a>

#### get_world_scale_factor

```python
def get_world_scale_factor() -> float
```

x.get_world_scale_factor() -> float
Gets the world scale factor, which can be multiplied by a scale vector to convert to room space

Returns:
    float:

<a id="unreal.VREditorRadialFloatingUI"></a>