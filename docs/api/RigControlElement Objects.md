## RigControlElement Objects

```python
class RigControlElement(RigMultiParentElement)
```

Rig Control Element

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigHierarchyElements.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``created_at_instruction_index`` (int32):  [Read-Write]
- ``index`` (int32):  [Read-Only]
- ``key`` (RigElementKey):  [Read-Only]
- ``preferred_euler_angles`` (RigPreferredEulerAngles):  [Read-Write]
- ``selected`` (bool):  [Read-Write]
- ``settings`` (RigControlSettings):  [Read-Write]
- ``sub_index`` (int32):  [Read-Only]

<a id="unreal.RigControlElement.__init__"></a>

#### __init__

```python
def __init__(
    key: RigElementKey = [RigElementType.NONE, "None"],
    index: int = 0,
    sub_index: int = 0,
    created_at_instruction_index: int = 0,
    selected: bool = False,
    settings: RigControlSettings = [
        RigControlAnimationType.ANIMATION_CONTROL,
        RigControlType.EULER_TRANSFORM, "None", RigControlAxis.X, [], True, [],
        [], True, RigControlVisibility.USER_DEFINED, "Default",
        [1.000000, 0.000000, 0.000000, 1.000000], False, None, [[], []], [],
        False, False, [], EulerRotationOrder.YZX, False
    ],
    preferred_euler_angles: RigPreferredEulerAngles = [
        EulerRotationOrder.YZX, [0.000000, 0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000]
    ]
) -> None
```

<a id="unreal.RigControlElement.settings"></a>

#### settings

```python
@property
def settings() -> RigControlSettings
```

(RigControlSettings):  [Read-Only]

<a id="unreal.RigControlElement.preferred_euler_angles"></a>

#### preferred_euler_angles

```python
@property
def preferred_euler_angles() -> RigPreferredEulerAngles
```

(RigPreferredEulerAngles):  [Read-Only]

<a id="unreal.RigPreferredEulerAngles"></a>