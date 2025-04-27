## VRScoutingInteractor Objects

```python
class VRScoutingInteractor(VREditorInteractor)
```

Represents the interactor in the world

**C++ Source:**

- **Module**: VREditor
- **File**: VRScoutingInteractor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``flying_indicator_component`` (StaticMeshComponent):  [Read-Write] Shown in Navigation mode
- ``hand_mesh_component`` (StaticMeshComponent):  [Read-Write] Access to the current handmesh. Use ReplaceHandMeshComponent() to update the entire StaticMeshComponent.
- ``is_undo_redo_swipe_enabled`` (bool):  [Read-Write] Whether swiping left/right on touchpad/joystick triggers undo/redo
- ``receives_editor_input`` (bool):  [Read-Write] If set to true, then this interactor will be able to recieve input delegate callbacks when in the editor. Defaults to true since we will always want this interactor to consume input

<a id="unreal.VRScoutingInteractor.flying_indicator_component"></a>

#### flying_indicator_component

```python
@property
def flying_indicator_component() -> StaticMeshComponent
```

(StaticMeshComponent):  [Read-Only] Shown in Navigation mode

<a id="unreal.VRScoutingInteractor.receives_editor_input"></a>

#### receives_editor_input

```python
@property
def receives_editor_input() -> bool
```

(bool):  [Read-Write] If set to true, then this interactor will be able to recieve input delegate callbacks when in the editor. Defaults to true since we will always want this interactor to consume input

<a id="unreal.VRScoutingInteractor.receives_editor_input"></a>

#### receives_editor_input

```python
@receives_editor_input.setter
def receives_editor_input(value: bool) -> None
```

<a id="unreal.VRScoutingInteractor.set_gizmo_mode"></a>

#### set_gizmo_mode

```python
def set_gizmo_mode(gizmo_mode: GizmoHandleTypes) -> None
```

x.set_gizmo_mode(gizmo_mode) -> None
Sets the gizmo mode for selected object

Args:
    gizmo_mode (GizmoHandleTypes):

<a id="unreal.VRScoutingInteractor.get_selected_actors"></a>

#### get_selected_actors

```python
@classmethod
def get_selected_actors(cls) -> Array[Actor]
```

X.get_selected_actors() -> Array[Actor]
Gets all actors that are selected in the world editor

Returns:
    Array[Actor]:

<a id="unreal.VRScoutingInteractor.get_input_component"></a>

#### get_input_component

```python
def get_input_component() -> InputComponent
```

x.get_input_component() -> InputComponent
Returns the current InputComponent. This will be NULL unless bReceivesEditorInput is set to true.

Returns:
    InputComponent:

<a id="unreal.VRScoutingInteractor.get_gizmo_mode"></a>

#### get_gizmo_mode

```python
def get_gizmo_mode() -> GizmoHandleTypes
```

x.get_gizmo_mode() -> GizmoHandleTypes
Gets the gizmo mode for selected object

Returns:
    GizmoHandleTypes:

<a id="unreal.Factory"></a>