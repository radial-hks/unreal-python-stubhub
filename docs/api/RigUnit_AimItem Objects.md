## RigUnit_AimItem Objects

```python
class RigUnit_AimItem(RigUnit_HighlevelBaseMutable)
```

Aligns the rotation of a primary and secondary axis of a bone to a global target.
Note: This node operates in global space!

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_AimBone.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``debug_settings`` (RigUnit_AimBone_DebugSettings):  [Read-Write] The debug setting for the node
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``item`` (RigElementKey):  [Read-Write] The name of the item to align
- ``primary`` (RigUnit_AimItem_Target):  [Read-Write] The primary target for the aim
- ``secondary`` (RigUnit_AimItem_Target):  [Read-Write] The secondary target for the aim - also referred to as PoleVector / UpVector
- ``weight`` (float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_AimItem.__init__"></a>

#### __init__

```python
def __init__(
    execute_context: ControlRigExecuteContext = [],
    item: RigElementKey = [RigElementType.NONE, "None"],
    primary: RigUnit_AimItem_Target = [
        1.000000, [1.000000, 0.000000, 0.000000],
        [1.000000, 0.000000, 0.000000], ControlRigVectorKind.LOCATION,
        [RigElementType.BONE, "None"]
    ],
    secondary: RigUnit_AimItem_Target = [
        1.000000, [1.000000, 0.000000, 0.000000],
        [1.000000, 0.000000, 0.000000], ControlRigVectorKind.LOCATION,
        [RigElementType.BONE, "None"]
    ],
    weight: float = 0.000000,
    debug_settings: RigUnit_AimBone_DebugSettings = [
        False, 10.000000,
        [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
         [1.000000, 1.000000, 1.000000]]
    ]
) -> None
```

<a id="unreal.RigUnit_AimItem.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write] The name of the item to align

<a id="unreal.RigUnit_AimItem.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_AimItem.primary"></a>

#### primary

```python
@property
def primary() -> RigUnit_AimItem_Target
```

(RigUnit_AimItem_Target):  [Read-Write] The primary target for the aim

<a id="unreal.RigUnit_AimItem.primary"></a>

#### primary

```python
@primary.setter
def primary(value: RigUnit_AimItem_Target) -> None
```

<a id="unreal.RigUnit_AimItem.secondary"></a>

#### secondary

```python
@property
def secondary() -> RigUnit_AimItem_Target
```

(RigUnit_AimItem_Target):  [Read-Write] The secondary target for the aim - also referred to as PoleVector / UpVector

<a id="unreal.RigUnit_AimItem.secondary"></a>

#### secondary

```python
@secondary.setter
def secondary(value: RigUnit_AimItem_Target) -> None
```

<a id="unreal.RigUnit_AimItem.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_AimItem.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_AimItem.debug_settings"></a>

#### debug_settings

```python
@property
def debug_settings() -> RigUnit_AimBone_DebugSettings
```

(RigUnit_AimBone_DebugSettings):  [Read-Write] The debug setting for the node

<a id="unreal.RigUnit_AimItem.debug_settings"></a>

#### debug_settings

```python
@debug_settings.setter
def debug_settings(value: RigUnit_AimBone_DebugSettings) -> None
```

<a id="unreal.RigUnit_AimConstraint_WorldUp"></a>