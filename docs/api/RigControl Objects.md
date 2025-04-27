## RigControl Objects

```python
class RigControl(RigElement)
```

Rig Control

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigControlHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``animatable`` (bool):  [Read-Write] If the control is animatable in sequencer
- ``control_enum`` (Enum):  [Read-Write] If the control is transient and only visible in the control rig editor
- ``control_type`` (RigControlType):  [Read-Write]
- ``display_name`` (Name):  [Read-Write]
- ``draw_limits`` (bool):  [Read-Write] True if the limits should be drawn in debug.
- ``gizmo_color`` (LinearColor):  [Read-Write]
- ``gizmo_enabled`` (bool):  [Read-Write] Set to true if the gizmo is enabled in 3d
- ``gizmo_name`` (Name):  [Read-Write] This is optional UI setting - this doesn't mean this is always used, but it is optional for manipulation layer to use this
- ``gizmo_transform`` (Transform):  [Read-Write]
- ``gizmo_visible`` (bool):  [Read-Write] Set to true if the gizmo is currently visible in 3d
- ``index`` (int32):  [Read-Only]
- ``initial_value`` (RigControlValue):  [Read-Only] The value that a control is reset to during begin play or when the
  control rig is instantiated.
- ``is_transient_control`` (bool):  [Read-Write] If the control is transient and only visible in the control rig editor
- ``limit_rotation`` (bool):  [Read-Write] True if the control has to obey rotation limits.
- ``limit_scale`` (bool):  [Read-Write] True if the control has to obey scale limits.
- ``limit_translation`` (bool):  [Read-Write] True if the control has to obey translation limits.
- ``maximum_value`` (RigControlValue):  [Read-Write] The maximum limit of the control's value
- ``minimum_value`` (RigControlValue):  [Read-Write] The minimum limit of the control's value
- ``name`` (Name):  [Read-Write]
- ``offset_transform`` (Transform):  [Read-Write] Used to offset a control in global space. This can be useful
  to offset a float control by rotating it or translating it.
- ``parent_index`` (int32):  [Read-Write]
- ``parent_name`` (Name):  [Read-Only]
- ``primary_axis`` (RigControlAxis):  [Read-Write] the primary axis to use for float controls
- ``space_index`` (int32):  [Read-Write]
- ``space_name`` (Name):  [Read-Only]
- ``value`` (RigControlValue):  [Read-Only] The current value of the control.

<a id="unreal.RigControl.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             index: int = 0,
             control_type: RigControlType = RigControlType.BOOL,
             display_name: Name = "None",
             parent_name: Name = "None",
             parent_index: int = 0,
             space_name: Name = "None",
             space_index: int = 0,
             offset_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                            [-0.000000, 0.000000, 0.000000],
                                            [1.000000, 1.000000, 1.000000]],
             initial_value: RigControlValue = [],
             value: RigControlValue = [],
             primary_axis: RigControlAxis = RigControlAxis.X,
             animatable: bool = False,
             limit_translation: bool = False,
             limit_rotation: bool = False,
             limit_scale: bool = False,
             draw_limits: bool = False,
             minimum_value: RigControlValue = [],
             maximum_value: RigControlValue = [],
             gizmo_enabled: bool = False,
             gizmo_visible: bool = False,
             gizmo_name: Name = "None",
             gizmo_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                           [-0.000000, 0.000000, 0.000000],
                                           [1.000000, 1.000000, 1.000000]],
             gizmo_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             is_transient_control: bool = False,
             control_enum: Enum = None) -> None
```

<a id="unreal.RigControl.control_type"></a>

#### control_type

```python
@property
def control_type() -> RigControlType
```

(RigControlType):  [Read-Write]

<a id="unreal.RigControl.control_type"></a>

#### control_type

```python
@control_type.setter
def control_type(value: RigControlType) -> None
```

<a id="unreal.RigControl.display_name"></a>

#### display_name

```python
@property
def display_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigControl.display_name"></a>

#### display_name

```python
@display_name.setter
def display_name(value: Name) -> None
```

<a id="unreal.RigControl.parent_name"></a>

#### parent_name

```python
@property
def parent_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.RigControl.parent_index"></a>

#### parent_index

```python
@property
def parent_index() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigControl.space_name"></a>

#### space_name

```python
@property
def space_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.RigControl.space_index"></a>

#### space_index

```python
@property
def space_index() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigControl.offset_transform"></a>

#### offset_transform

```python
@property
def offset_transform() -> Transform
```

(Transform):  [Read-Write] Used to offset a control in global space. This can be useful
to offset a float control by rotating it or translating it.

<a id="unreal.RigControl.offset_transform"></a>

#### offset_transform

```python
@offset_transform.setter
def offset_transform(value: Transform) -> None
```

<a id="unreal.RigControl.initial_value"></a>

#### initial_value

```python
@property
def initial_value() -> RigControlValue
```

(RigControlValue):  [Read-Only] The value that a control is reset to during begin play or when the
control rig is instantiated.

<a id="unreal.RigControl.value"></a>

#### value

```python
@property
def value() -> RigControlValue
```

(RigControlValue):  [Read-Only] The current value of the control.

<a id="unreal.RigControl.primary_axis"></a>

#### primary_axis

```python
@property
def primary_axis() -> RigControlAxis
```

(RigControlAxis):  [Read-Write] the primary axis to use for float controls

<a id="unreal.RigControl.primary_axis"></a>

#### primary_axis

```python
@primary_axis.setter
def primary_axis(value: RigControlAxis) -> None
```

<a id="unreal.RigControl.animatable"></a>

#### animatable

```python
@property
def animatable() -> bool
```

(bool):  [Read-Write] If the control is animatable in sequencer

<a id="unreal.RigControl.animatable"></a>

#### animatable

```python
@animatable.setter
def animatable(value: bool) -> None
```

<a id="unreal.RigControl.limit_translation"></a>

#### limit_translation

```python
@property
def limit_translation() -> bool
```

(bool):  [Read-Write] True if the control has to obey translation limits.

<a id="unreal.RigControl.limit_translation"></a>

#### limit_translation

```python
@limit_translation.setter
def limit_translation(value: bool) -> None
```

<a id="unreal.RigControl.limit_rotation"></a>

#### limit_rotation

```python
@property
def limit_rotation() -> bool
```

(bool):  [Read-Write] True if the control has to obey rotation limits.

<a id="unreal.RigControl.limit_rotation"></a>

#### limit_rotation

```python
@limit_rotation.setter
def limit_rotation(value: bool) -> None
```

<a id="unreal.RigControl.limit_scale"></a>

#### limit_scale

```python
@property
def limit_scale() -> bool
```

(bool):  [Read-Write] True if the control has to obey scale limits.

<a id="unreal.RigControl.limit_scale"></a>

#### limit_scale

```python
@limit_scale.setter
def limit_scale(value: bool) -> None
```

<a id="unreal.RigControl.draw_limits"></a>

#### draw_limits

```python
@property
def draw_limits() -> bool
```

(bool):  [Read-Write] True if the limits should be drawn in debug.

<a id="unreal.RigControl.draw_limits"></a>

#### draw_limits

```python
@draw_limits.setter
def draw_limits(value: bool) -> None
```

<a id="unreal.RigControl.minimum_value"></a>

#### minimum_value

```python
@property
def minimum_value() -> RigControlValue
```

(RigControlValue):  [Read-Write] The minimum limit of the control's value

<a id="unreal.RigControl.minimum_value"></a>

#### minimum_value

```python
@minimum_value.setter
def minimum_value(value: RigControlValue) -> None
```

<a id="unreal.RigControl.maximum_value"></a>

#### maximum_value

```python
@property
def maximum_value() -> RigControlValue
```

(RigControlValue):  [Read-Write] The maximum limit of the control's value

<a id="unreal.RigControl.maximum_value"></a>

#### maximum_value

```python
@maximum_value.setter
def maximum_value(value: RigControlValue) -> None
```

<a id="unreal.RigControl.gizmo_enabled"></a>

#### gizmo_enabled

```python
@property
def gizmo_enabled() -> bool
```

(bool):  [Read-Write] Set to true if the gizmo is enabled in 3d

<a id="unreal.RigControl.gizmo_enabled"></a>

#### gizmo_enabled

```python
@gizmo_enabled.setter
def gizmo_enabled(value: bool) -> None
```

<a id="unreal.RigControl.gizmo_visible"></a>

#### gizmo_visible

```python
@property
def gizmo_visible() -> bool
```

(bool):  [Read-Write] Set to true if the gizmo is currently visible in 3d

<a id="unreal.RigControl.gizmo_visible"></a>

#### gizmo_visible

```python
@gizmo_visible.setter
def gizmo_visible(value: bool) -> None
```

<a id="unreal.RigControl.gizmo_name"></a>

#### gizmo_name

```python
@property
def gizmo_name() -> Name
```

(Name):  [Read-Write] This is optional UI setting - this doesn't mean this is always used, but it is optional for manipulation layer to use this

<a id="unreal.RigControl.gizmo_name"></a>

#### gizmo_name

```python
@gizmo_name.setter
def gizmo_name(value: Name) -> None
```

<a id="unreal.RigControl.gizmo_transform"></a>

#### gizmo_transform

```python
@property
def gizmo_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigControl.gizmo_transform"></a>

#### gizmo_transform

```python
@gizmo_transform.setter
def gizmo_transform(value: Transform) -> None
```

<a id="unreal.RigControl.gizmo_color"></a>

#### gizmo_color

```python
@property
def gizmo_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigControl.gizmo_color"></a>

#### gizmo_color

```python
@gizmo_color.setter
def gizmo_color(value: LinearColor) -> None
```

<a id="unreal.RigControl.is_transient_control"></a>

#### is_transient_control

```python
@property
def is_transient_control() -> bool
```

(bool):  [Read-Write] If the control is transient and only visible in the control rig editor

<a id="unreal.RigControl.is_transient_control"></a>

#### is_transient_control

```python
@is_transient_control.setter
def is_transient_control(value: bool) -> None
```

<a id="unreal.RigControl.control_enum"></a>

#### control_enum

```python
@property
def control_enum() -> Enum
```

(Enum):  [Read-Only] If the control is transient and only visible in the control rig editor

<a id="unreal.RigCurve"></a>