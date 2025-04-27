## RigControlSettings Objects

```python
class RigControlSettings(StructBase)
```

Rig Control Settings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigHierarchyElements.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``animatable`` (bool):  [Read-Write] Deprecated properties.
  deprecated: Use animation_type instead.
- ``animation_type`` (RigControlAnimationType):  [Read-Write]
- ``control_enum`` (Enum):  [Read-Write] If the control is integer it can use this enum to choose values
- ``control_type`` (RigControlType):  [Read-Write]
- ``customization`` (RigControlElementCustomization):  [Read-Write] The User interface customization used for a control
  This will be used as the default content for the space picker and other widgets
- ``display_name`` (Name):  [Read-Write]
- ``draw_limits`` (bool):  [Read-Write] True if the limits should be drawn in debug.
  For this to be enabled you need to have at least one min and max limit turned on.
- ``driven_controls`` (Array[RigElementKey]):  [Read-Write] The list of driven controls for this proxy control.
- ``filtered_channels`` (Array[RigControlTransformChannel]):  [Read-Write] Filtered Visible Transform channels. If this is empty everything is visible
- ``group_with_parent_control`` (bool):  [Read-Write] If set to true the animation channel will be grouped with the parent control in sequencer
- ``is_transient_control`` (bool):  [Read-Write] If the control is transient and only visible in the control rig editor
- ``limit_enabled`` (Array[RigControlLimitEnabled]):  [Read-Write] True if the control has limits.
- ``maximum_value`` (RigControlValue):  [Read-Write] The maximum limit of the control's value
- ``minimum_value`` (RigControlValue):  [Read-Write] The minimum limit of the control's value
- ``preferred_rotation_order`` (EulerRotationOrder):  [Read-Write] The euler rotation order this control prefers for animation, if we aren't using default UE rotator
- ``primary_axis`` (RigControlAxis):  [Read-Write] the primary axis to use for float controls
- ``restrict_space_switching`` (bool):  [Read-Write] Allow to space switch only to the available spaces
- ``shape_color`` (LinearColor):  [Read-Write]
- ``shape_enabled`` (bool):  [Read-Write]
  deprecated: Use animation_type or shape_visible instead.
- ``shape_name`` (Name):  [Read-Write] This is optional UI setting - this doesn't mean this is always used, but it is optional for manipulation layer to use this
- ``shape_visibility`` (RigControlVisibility):  [Read-Write] Defines how the shape visibility should be changed
- ``shape_visible`` (bool):  [Read-Write] Set to true if the shape is currently visible in 3d
- ``use_preferred_rotation_order`` (bool):  [Read-Write] Whether to use a specified rotation order or just use the default FRotator order and conversion functions

<a id="unreal.RigControlSettings.__init__"></a>

#### __init__

```python
def __init__(
        animation_type: RigControlAnimationType = RigControlAnimationType.
    ANIMATION_CONTROL,
        control_type: RigControlType = RigControlType.BOOL,
        display_name: Name = "None",
        primary_axis: RigControlAxis = RigControlAxis.X,
        limit_enabled: Array[RigControlLimitEnabled] = [],
        draw_limits: bool = False,
        minimum_value: RigControlValue = [],
        maximum_value: RigControlValue = [],
        shape_visible: bool = False,
        shape_visibility: RigControlVisibility = RigControlVisibility.
    USER_DEFINED,
        shape_name: Name = "None",
        shape_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
        is_transient_control: bool = False,
        control_enum: Enum = None,
        customization: RigControlElementCustomization = [[], []],
        driven_controls: Array[RigElementKey] = [],
        group_with_parent_control: bool = False,
        restrict_space_switching: bool = False,
        filtered_channels: Array[RigControlTransformChannel] = [],
        preferred_rotation_order: EulerRotationOrder = EulerRotationOrder.XYZ,
        use_preferred_rotation_order: bool = False) -> None
```

<a id="unreal.RigControlSettings.animation_type"></a>

#### animation_type

```python
@property
def animation_type() -> RigControlAnimationType
```

(RigControlAnimationType):  [Read-Write]

<a id="unreal.RigControlSettings.animation_type"></a>

#### animation_type

```python
@animation_type.setter
def animation_type(value: RigControlAnimationType) -> None
```

<a id="unreal.RigControlSettings.control_type"></a>

#### control_type

```python
@property
def control_type() -> RigControlType
```

(RigControlType):  [Read-Write]

<a id="unreal.RigControlSettings.control_type"></a>

#### control_type

```python
@control_type.setter
def control_type(value: RigControlType) -> None
```

<a id="unreal.RigControlSettings.display_name"></a>

#### display_name

```python
@property
def display_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigControlSettings.display_name"></a>

#### display_name

```python
@display_name.setter
def display_name(value: Name) -> None
```

<a id="unreal.RigControlSettings.primary_axis"></a>

#### primary_axis

```python
@property
def primary_axis() -> RigControlAxis
```

(RigControlAxis):  [Read-Write] the primary axis to use for float controls

<a id="unreal.RigControlSettings.primary_axis"></a>

#### primary_axis

```python
@primary_axis.setter
def primary_axis(value: RigControlAxis) -> None
```

<a id="unreal.RigControlSettings.limit_enabled"></a>

#### limit_enabled

```python
@property
def limit_enabled() -> Array[RigControlLimitEnabled]
```

(Array[RigControlLimitEnabled]):  [Read-Write] True if the control has limits.

<a id="unreal.RigControlSettings.limit_enabled"></a>

#### limit_enabled

```python
@limit_enabled.setter
def limit_enabled(value: Array[RigControlLimitEnabled]) -> None
```

<a id="unreal.RigControlSettings.draw_limits"></a>

#### draw_limits

```python
@property
def draw_limits() -> bool
```

(bool):  [Read-Write] True if the limits should be drawn in debug.
For this to be enabled you need to have at least one min and max limit turned on.

<a id="unreal.RigControlSettings.draw_limits"></a>

#### draw_limits

```python
@draw_limits.setter
def draw_limits(value: bool) -> None
```

<a id="unreal.RigControlSettings.minimum_value"></a>

#### minimum_value

```python
@property
def minimum_value() -> RigControlValue
```

(RigControlValue):  [Read-Write] The minimum limit of the control's value

<a id="unreal.RigControlSettings.minimum_value"></a>

#### minimum_value

```python
@minimum_value.setter
def minimum_value(value: RigControlValue) -> None
```

<a id="unreal.RigControlSettings.maximum_value"></a>

#### maximum_value

```python
@property
def maximum_value() -> RigControlValue
```

(RigControlValue):  [Read-Write] The maximum limit of the control's value

<a id="unreal.RigControlSettings.maximum_value"></a>

#### maximum_value

```python
@maximum_value.setter
def maximum_value(value: RigControlValue) -> None
```

<a id="unreal.RigControlSettings.shape_visible"></a>

#### shape_visible

```python
@property
def shape_visible() -> bool
```

(bool):  [Read-Write] Set to true if the shape is currently visible in 3d

<a id="unreal.RigControlSettings.shape_visible"></a>

#### shape_visible

```python
@shape_visible.setter
def shape_visible(value: bool) -> None
```

<a id="unreal.RigControlSettings.b_gizmo_visible"></a>

#### b_gizmo_visible

```python
@property
def b_gizmo_visible() -> bool
```

deprecated: 'b_gizmo_visible' was renamed to 'shape_visible'.

<a id="unreal.RigControlSettings.b_gizmo_visible"></a>

#### b_gizmo_visible

```python
@b_gizmo_visible.setter
def b_gizmo_visible(value: bool) -> None
```

<a id="unreal.RigControlSettings.shape_visibility"></a>

#### shape_visibility

```python
@property
def shape_visibility() -> RigControlVisibility
```

(RigControlVisibility):  [Read-Write] Defines how the shape visibility should be changed

<a id="unreal.RigControlSettings.shape_visibility"></a>

#### shape_visibility

```python
@shape_visibility.setter
def shape_visibility(value: RigControlVisibility) -> None
```

<a id="unreal.RigControlSettings.shape_name"></a>

#### shape_name

```python
@property
def shape_name() -> Name
```

(Name):  [Read-Write] This is optional UI setting - this doesn't mean this is always used, but it is optional for manipulation layer to use this

<a id="unreal.RigControlSettings.shape_name"></a>

#### shape_name

```python
@shape_name.setter
def shape_name(value: Name) -> None
```

<a id="unreal.RigControlSettings.gizmo_name"></a>

#### gizmo_name

```python
@property
def gizmo_name() -> Name
```

deprecated: 'gizmo_name' was renamed to 'shape_name'.

<a id="unreal.RigControlSettings.gizmo_name"></a>

#### gizmo_name

```python
@gizmo_name.setter
def gizmo_name(value: Name) -> None
```

<a id="unreal.RigControlSettings.shape_color"></a>

#### shape_color

```python
@property
def shape_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigControlSettings.shape_color"></a>

#### shape_color

```python
@shape_color.setter
def shape_color(value: LinearColor) -> None
```

<a id="unreal.RigControlSettings.gizmo_color"></a>

#### gizmo_color

```python
@property
def gizmo_color() -> LinearColor
```

deprecated: 'gizmo_color' was renamed to 'shape_color'.

<a id="unreal.RigControlSettings.gizmo_color"></a>

#### gizmo_color

```python
@gizmo_color.setter
def gizmo_color(value: LinearColor) -> None
```

<a id="unreal.RigControlSettings.is_transient_control"></a>

#### is_transient_control

```python
@property
def is_transient_control() -> bool
```

(bool):  [Read-Write] If the control is transient and only visible in the control rig editor

<a id="unreal.RigControlSettings.is_transient_control"></a>

#### is_transient_control

```python
@is_transient_control.setter
def is_transient_control(value: bool) -> None
```

<a id="unreal.RigControlSettings.control_enum"></a>

#### control_enum

```python
@property
def control_enum() -> Enum
```

(Enum):  [Read-Only] If the control is integer it can use this enum to choose values

<a id="unreal.RigControlSettings.customization"></a>

#### customization

```python
@property
def customization() -> RigControlElementCustomization
```

(RigControlElementCustomization):  [Read-Only] The User interface customization used for a control
This will be used as the default content for the space picker and other widgets

<a id="unreal.RigControlSettings.driven_controls"></a>

#### driven_controls

```python
@property
def driven_controls() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Only] The list of driven controls for this proxy control.

<a id="unreal.RigControlSettings.group_with_parent_control"></a>

#### group_with_parent_control

```python
@property
def group_with_parent_control() -> bool
```

(bool):  [Read-Only] If set to true the animation channel will be grouped with the parent control in sequencer

<a id="unreal.RigControlSettings.restrict_space_switching"></a>

#### restrict_space_switching

```python
@property
def restrict_space_switching() -> bool
```

(bool):  [Read-Only] Allow to space switch only to the available spaces

<a id="unreal.RigControlSettings.filtered_channels"></a>

#### filtered_channels

```python
@property
def filtered_channels() -> Array[RigControlTransformChannel]
```

(Array[RigControlTransformChannel]):  [Read-Only] Filtered Visible Transform channels. If this is empty everything is visible

<a id="unreal.RigControlSettings.preferred_rotation_order"></a>

#### preferred_rotation_order

```python
@property
def preferred_rotation_order() -> EulerRotationOrder
```

(EulerRotationOrder):  [Read-Only] The euler rotation order this control prefers for animation, if we aren't using default UE rotator

<a id="unreal.RigControlSettings.use_preferred_rotation_order"></a>

#### use_preferred_rotation_order

```python
@property
def use_preferred_rotation_order() -> bool
```

(bool):  [Read-Only] Whether to use a specified rotation order or just use the default FRotator order and conversion functions

<a id="unreal.RigControlSettings.animatable"></a>

#### animatable

```python
@property
def animatable() -> bool
```

(bool):  [Read-Write] Deprecated properties.
deprecated: Use animation_type instead.

<a id="unreal.RigControlSettings.animatable"></a>

#### animatable

```python
@animatable.setter
def animatable(value: bool) -> None
```

<a id="unreal.RigControlSettings.shape_enabled"></a>

#### shape_enabled

```python
@property
def shape_enabled() -> bool
```

(bool):  [Read-Write]
deprecated: Use animation_type or shape_visible instead.

<a id="unreal.RigControlSettings.shape_enabled"></a>

#### shape_enabled

```python
@shape_enabled.setter
def shape_enabled(value: bool) -> None
```

<a id="unreal.RigControlSettings.b_gizmo_enabled"></a>

#### b_gizmo_enabled

```python
@property
def b_gizmo_enabled() -> bool
```

deprecated: 'b_gizmo_enabled' was renamed to 'shape_enabled'.

<a id="unreal.RigControlSettings.b_gizmo_enabled"></a>

#### b_gizmo_enabled

```python
@b_gizmo_enabled.setter
def b_gizmo_enabled(value: bool) -> None
```

<a id="unreal.RigControlElementCustomization"></a>