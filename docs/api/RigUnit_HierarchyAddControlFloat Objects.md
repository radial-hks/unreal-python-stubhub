## RigUnit_HierarchyAddControlFloat Objects

```python
class RigUnit_HierarchyAddControlFloat(RigUnit_HierarchyAddControlElement)
```

Adds a new control to the hierarchy
Note: This node only runs as part of the construction event.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``initial_value`` (float):  [Read-Write] * The initial value of the new control
- ``item`` (RigElementKey):  [Read-Write] * The resulting item
- ``name`` (Name):  [Read-Write] * The name of the new element to add
- ``offset_space`` (RigVMTransformSpace):  [Read-Write] * The space the offset is in
- ``offset_transform`` (Transform):  [Read-Write] * The offset transform of the new control
- ``parent`` (RigElementKey):  [Read-Write] * The parent of the new element to add
- ``settings`` (RigUnit_HierarchyAddControlFloat_Settings):  [Read-Write] * The settings for the control

<a id="unreal.RigUnit_HierarchyAddControlFloat.__init__"></a>

#### __init__

```python
def __init__(
    execute_context: ControlRigExecuteContext = [],
    parent: RigElementKey = [RigElementType.NONE, "None"],
    name: Name = "None",
    item: RigElementKey = [RigElementType.NONE, "None"],
    offset_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                   [-0.000000, 0.000000, 0.000000],
                                   [1.000000, 1.000000, 1.000000]],
    offset_space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE,
    initial_value: float = 0.000000,
    settings: RigUnit_HierarchyAddControlFloat_Settings = [
        RigControlAxis.X, False, [[True, True], 0.000000, 100.000000, True],
        [
            True, "Default", [1.000000, 0.000000, 0.000000, 1.000000],
            [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
             [1.000000, 1.000000, 1.000000]]
        ], [False, [], RigControlVisibility.BASED_ON_SELECTION], "None"
    ]
) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlFloat.initial_value"></a>

#### initial_value

```python
@property
def initial_value() -> float
```

(float):  [Read-Write] * The initial value of the new control

<a id="unreal.RigUnit_HierarchyAddControlFloat.initial_value"></a>

#### initial_value

```python
@initial_value.setter
def initial_value(value: float) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlFloat.settings"></a>

#### settings

```python
@property
def settings() -> RigUnit_HierarchyAddControlFloat_Settings
```

(RigUnit_HierarchyAddControlFloat_Settings):  [Read-Write] * The settings for the control

<a id="unreal.RigUnit_HierarchyAddControlFloat.settings"></a>

#### settings

```python
@settings.setter
def settings(value: RigUnit_HierarchyAddControlFloat_Settings) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlInteger_LimitSettings"></a>