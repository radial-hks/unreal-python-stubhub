## RigUnit_HierarchyAddAnimationChannelScaleFloat Objects

```python
class RigUnit_HierarchyAddAnimationChannelScaleFloat(
        RigUnit_HierarchyAddElement)
```

Adds a new animation channel to the hierarchy
Note: This node only runs as part of the construction event.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``initial_value`` (float):  [Read-Write] * The initial value of the new animation channel
- ``item`` (RigElementKey):  [Read-Write] * The resulting item
- ``limits_enabled`` (RigUnit_HierarchyAddAnimationChannelSingleLimitSettings):  [Read-Write] * The enable settings for the limits
- ``maximum_value`` (float):  [Read-Write] * The maximum value for the animation channel
- ``minimum_value`` (float):  [Read-Write] * The initial value of the new animation channel
- ``name`` (Name):  [Read-Write] * The name of the new element to add
- ``parent`` (RigElementKey):  [Read-Write] * The parent of the new element to add

<a id="unreal.RigUnit_HierarchyAddAnimationChannelScaleFloat.__init__"></a>

#### __init__

```python
def __init__(
    execute_context: ControlRigExecuteContext = [],
    parent: RigElementKey = [RigElementType.NONE, "None"],
    name: Name = "None",
    item: RigElementKey = [RigElementType.NONE, "None"],
    initial_value: float = 0.000000,
    minimum_value: float = 0.000000,
    maximum_value: float = 0.000000,
    limits_enabled: RigUnit_HierarchyAddAnimationChannelSingleLimitSettings = [
        [True, True]
    ]
) -> None
```

<a id="unreal.RigUnit_HierarchyAddAnimationChannelScaleFloat.initial_value"></a>

#### initial_value

```python
@property
def initial_value() -> float
```

(float):  [Read-Write] * The initial value of the new animation channel

<a id="unreal.RigUnit_HierarchyAddAnimationChannelScaleFloat.initial_value"></a>

#### initial_value

```python
@initial_value.setter
def initial_value(value: float) -> None
```

<a id="unreal.RigUnit_HierarchyAddAnimationChannelScaleFloat.minimum_value"></a>

#### minimum_value

```python
@property
def minimum_value() -> float
```

(float):  [Read-Write] * The initial value of the new animation channel

<a id="unreal.RigUnit_HierarchyAddAnimationChannelScaleFloat.minimum_value"></a>

#### minimum_value

```python
@minimum_value.setter
def minimum_value(value: float) -> None
```

<a id="unreal.RigUnit_HierarchyAddAnimationChannelScaleFloat.maximum_value"></a>

#### maximum_value

```python
@property
def maximum_value() -> float
```

(float):  [Read-Write] * The maximum value for the animation channel

<a id="unreal.RigUnit_HierarchyAddAnimationChannelScaleFloat.maximum_value"></a>

#### maximum_value

```python
@maximum_value.setter
def maximum_value(value: float) -> None
```

<a id="unreal.RigUnit_HierarchyAddAnimationChannelScaleFloat.limits_enabled"></a>

#### limits_enabled

```python
@property
def limits_enabled(
) -> RigUnit_HierarchyAddAnimationChannelSingleLimitSettings
```

(RigUnit_HierarchyAddAnimationChannelSingleLimitSettings):  [Read-Write] * The enable settings for the limits

<a id="unreal.RigUnit_HierarchyAddAnimationChannelScaleFloat.limits_enabled"></a>

#### limits_enabled

```python
@limits_enabled.setter
def limits_enabled(
        value: RigUnit_HierarchyAddAnimationChannelSingleLimitSettings
) -> None
```

<a id="unreal.RigUnit_HierarchyAddAnimationChannelInteger"></a>