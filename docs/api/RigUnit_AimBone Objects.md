## RigUnit_AimBone Objects

```python
class RigUnit_AimBone(RigUnit_HighlevelBaseMutable)
```

Aligns the rotation of a primary and secondary axis of a bone to a global target.
Note: This node operates in global space!

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_AimBone.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone`` (Name):  [Read-Write] The name of the bone to align
- ``debug_settings`` (RigUnit_AimBone_DebugSettings):  [Read-Write] The debug setting for the node
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``primary`` (RigUnit_AimBone_Target):  [Read-Write] The primary target for the aim
- ``propagate_to_children`` (bool):  [Read-Only] If set to true all of the global transforms of the children
  of this bone will be recalculated based on their local transforms.
  Note: This is computationally more expensive than turning it off.
- ``secondary`` (RigUnit_AimBone_Target):  [Read-Write] The secondary target for the aim - also referred to as PoleVector / UpVector
- ``weight`` (float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_AimBone.__init__"></a>

#### __init__

```python
def __init__(
    execute_context: ControlRigExecuteContext = [],
    bone: Name = "None",
    primary: RigUnit_AimBone_Target = [
        1.000000, [1.000000, 0.000000, 0.000000],
        [1.000000, 0.000000, 0.000000], ControlRigVectorKind.LOCATION, "None"
    ],
    secondary: RigUnit_AimBone_Target = [
        1.000000, [1.000000, 0.000000, 0.000000],
        [1.000000, 0.000000, 0.000000], ControlRigVectorKind.LOCATION, "None"
    ],
    weight: float = 0.000000,
    propagate_to_children: bool = False,
    debug_settings: RigUnit_AimBone_DebugSettings = [
        False, 10.000000,
        [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
         [1.000000, 1.000000, 1.000000]]
    ]
) -> None
```

<a id="unreal.RigUnit_AimBone.bone"></a>

#### bone

```python
@property
def bone() -> Name
```

(Name):  [Read-Write] The name of the bone to align

<a id="unreal.RigUnit_AimBone.bone"></a>

#### bone

```python
@bone.setter
def bone(value: Name) -> None
```

<a id="unreal.RigUnit_AimBone.primary"></a>

#### primary

```python
@property
def primary() -> RigUnit_AimBone_Target
```

(RigUnit_AimBone_Target):  [Read-Write] The primary target for the aim

<a id="unreal.RigUnit_AimBone.primary"></a>

#### primary

```python
@primary.setter
def primary(value: RigUnit_AimBone_Target) -> None
```

<a id="unreal.RigUnit_AimBone.secondary"></a>

#### secondary

```python
@property
def secondary() -> RigUnit_AimBone_Target
```

(RigUnit_AimBone_Target):  [Read-Write] The secondary target for the aim - also referred to as PoleVector / UpVector

<a id="unreal.RigUnit_AimBone.secondary"></a>

#### secondary

```python
@secondary.setter
def secondary(value: RigUnit_AimBone_Target) -> None
```

<a id="unreal.RigUnit_AimBone.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_AimBone.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_AimBone.propagate_to_children"></a>

#### propagate_to_children

```python
@property
def propagate_to_children() -> bool
```

(bool):  [Read-Only] If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

<a id="unreal.RigUnit_AimBone.debug_settings"></a>

#### debug_settings

```python
@property
def debug_settings() -> RigUnit_AimBone_DebugSettings
```

(RigUnit_AimBone_DebugSettings):  [Read-Write] The debug setting for the node

<a id="unreal.RigUnit_AimBone.debug_settings"></a>

#### debug_settings

```python
@debug_settings.setter
def debug_settings(value: RigUnit_AimBone_DebugSettings) -> None
```

<a id="unreal.RigUnit_AimItem"></a>