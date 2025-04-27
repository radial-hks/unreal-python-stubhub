## VREditorFloatingUICreationContext Objects

```python
class VREditorFloatingUICreationContext(StructBase)
```

Creation parameters for AVREditorFloatingUI

**C++ Source:**

- **Module**: VREditor
- **File**: VREditorFloatingUI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``editor_ui_size`` (float):  [Read-Write] Optional override for "VREd.EditorUISize". Leave at 0 for default.
- ``hide_window_handles`` (bool):  [Read-Write] Turn off handles under window? (X-To-Close, movement bar...)
- ``mask_out_widget_background`` (bool):  [Read-Write] Turn off the widget's background to create a see-through look.
- ``no_close_button`` (bool):  [Read-Write] If bHideWindowHandles is false, this window doesn't have a close button. (
- ``panel_id`` (Name):  [Read-Write] ID that the UI system will use to identify the panel. MUST BE UNIQUE!
- ``panel_mesh`` (StaticMesh):  [Read-Write] Optional custom mesh to use for the VR window.
- ``panel_size`` (Vector2D):  [Read-Write] Panel size. Should match the size of the UMG passed in.
- ``panel_spawn_offset`` (Transform):  [Read-Write] Optional offset from HMD where the window opens. Pass FTransform::Identity for default logic - window will open at controller location.
- ``parent_actor`` (Actor):  [Read-Write]
- ``widget_class`` (type(Class)):  [Read-Write] Widget to open in the VR window. null to close an open window (if if matches the PanelID)

<a id="unreal.VREditorFloatingUICreationContext.__init__"></a>

#### __init__

```python
def __init__(widget_class: Class = None,
             panel_id: Name = "None",
             parent_actor: Actor = None,
             panel_spawn_offset: Transform = [[0.000000, 0.000000, 0.000000],
                                              [-0.000000, 0.000000, 0.000000],
                                              [1.000000, 1.000000, 1.000000]],
             panel_size: Vector2D = [0.000000, 0.000000],
             panel_mesh: StaticMesh = None,
             editor_ui_size: float = 0.000000,
             hide_window_handles: bool = False,
             mask_out_widget_background: bool = False,
             no_close_button: bool = False) -> None
```

<a id="unreal.VREditorFloatingUICreationContext.widget_class"></a>

#### widget_class

```python
@property
def widget_class() -> Class
```

(type(Class)):  [Read-Write] Widget to open in the VR window. null to close an open window (if if matches the PanelID)

<a id="unreal.VREditorFloatingUICreationContext.widget_class"></a>

#### widget_class

```python
@widget_class.setter
def widget_class(value: Class) -> None
```

<a id="unreal.VREditorFloatingUICreationContext.panel_id"></a>

#### panel_id

```python
@property
def panel_id() -> Name
```

(Name):  [Read-Write] ID that the UI system will use to identify the panel. MUST BE UNIQUE!

<a id="unreal.VREditorFloatingUICreationContext.panel_id"></a>

#### panel_id

```python
@panel_id.setter
def panel_id(value: Name) -> None
```

<a id="unreal.VREditorFloatingUICreationContext.parent_actor"></a>

#### parent_actor

```python
@property
def parent_actor() -> Actor
```

(Actor):  [Read-Write]

<a id="unreal.VREditorFloatingUICreationContext.parent_actor"></a>

#### parent_actor

```python
@parent_actor.setter
def parent_actor(value: Actor) -> None
```

<a id="unreal.VREditorFloatingUICreationContext.panel_spawn_offset"></a>

#### panel_spawn_offset

```python
@property
def panel_spawn_offset() -> Transform
```

(Transform):  [Read-Write] Optional offset from HMD where the window opens. Pass FTransform::Identity for default logic - window will open at controller location.

<a id="unreal.VREditorFloatingUICreationContext.panel_spawn_offset"></a>

#### panel_spawn_offset

```python
@panel_spawn_offset.setter
def panel_spawn_offset(value: Transform) -> None
```

<a id="unreal.VREditorFloatingUICreationContext.panel_size"></a>

#### panel_size

```python
@property
def panel_size() -> Vector2D
```

(Vector2D):  [Read-Write] Panel size. Should match the size of the UMG passed in.

<a id="unreal.VREditorFloatingUICreationContext.panel_size"></a>

#### panel_size

```python
@panel_size.setter
def panel_size(value: Vector2D) -> None
```

<a id="unreal.VREditorFloatingUICreationContext.panel_mesh"></a>

#### panel_mesh

```python
@property
def panel_mesh() -> StaticMesh
```

(StaticMesh):  [Read-Write] Optional custom mesh to use for the VR window.

<a id="unreal.VREditorFloatingUICreationContext.panel_mesh"></a>

#### panel_mesh

```python
@panel_mesh.setter
def panel_mesh(value: StaticMesh) -> None
```

<a id="unreal.VREditorFloatingUICreationContext.editor_ui_size"></a>

#### editor_ui_size

```python
@property
def editor_ui_size() -> float
```

(float):  [Read-Write] Optional override for "VREd.EditorUISize". Leave at 0 for default.

<a id="unreal.VREditorFloatingUICreationContext.editor_ui_size"></a>

#### editor_ui_size

```python
@editor_ui_size.setter
def editor_ui_size(value: float) -> None
```

<a id="unreal.VREditorFloatingUICreationContext.hide_window_handles"></a>

#### hide_window_handles

```python
@property
def hide_window_handles() -> bool
```

(bool):  [Read-Write] Turn off handles under window? (X-To-Close, movement bar...)

<a id="unreal.VREditorFloatingUICreationContext.hide_window_handles"></a>

#### hide_window_handles

```python
@hide_window_handles.setter
def hide_window_handles(value: bool) -> None
```

<a id="unreal.VREditorFloatingUICreationContext.mask_out_widget_background"></a>

#### mask_out_widget_background

```python
@property
def mask_out_widget_background() -> bool
```

(bool):  [Read-Write] Turn off the widget's background to create a see-through look.

<a id="unreal.VREditorFloatingUICreationContext.mask_out_widget_background"></a>

#### mask_out_widget_background

```python
@mask_out_widget_background.setter
def mask_out_widget_background(value: bool) -> None
```

<a id="unreal.VREditorFloatingUICreationContext.no_close_button"></a>

#### no_close_button

```python
@property
def no_close_button() -> bool
```

(bool):  [Read-Write] If bHideWindowHandles is false, this window doesn't have a close button. (

<a id="unreal.VREditorFloatingUICreationContext.no_close_button"></a>

#### no_close_button

```python
@no_close_button.setter
def no_close_button(value: bool) -> None
```

<a id="unreal.InputRayHit"></a>