## RigUnit_DistributeRotation Objects

```python
class RigUnit_DistributeRotation(RigUnit_HighlevelBaseMutable)
```

Distributes rotations provided along a chain.
Each rotation is expressed by a quaternion and a ratio, where the ratio is between 0.0 and 1.0
Note: This node adds rotation in local space of each bone!

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DistributeRotation.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``end_bone`` (Name):  [Read-Write] The name of the last bone to align
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``propagate_to_children`` (bool):  [Read-Only] If set to true all of the global transforms of the children
  of this bone will be recalculated based on their local transforms.
  Note: This is computationally more expensive than turning it off.
- ``rotation_ease_type`` (RigVMAnimEasingType):  [Read-Only] The easing to use between to rotations.
- ``rotations`` (Array[RigUnit_DistributeRotation_Rotation]):  [Read-Write] The list of rotations to be applied
- ``start_bone`` (Name):  [Read-Write] The name of the first bone to align
- ``weight`` (float):  [Read-Write] The weight of the solver - how much the rotation should be applied

<a id="unreal.RigUnit_DistributeRotation.__init__"></a>

#### __init__

```python
def __init__(
        execute_context: ControlRigExecuteContext = [],
        start_bone: Name = "None",
        end_bone: Name = "None",
        rotations: Array[RigUnit_DistributeRotation_Rotation] = [],
        rotation_ease_type: RigVMAnimEasingType = RigVMAnimEasingType.LINEAR,
        weight: float = 0.000000,
        propagate_to_children: bool = False) -> None
```

<a id="unreal.RigUnit_DistributeRotation.start_bone"></a>

#### start_bone

```python
@property
def start_bone() -> Name
```

(Name):  [Read-Write] The name of the first bone to align

<a id="unreal.RigUnit_DistributeRotation.start_bone"></a>

#### start_bone

```python
@start_bone.setter
def start_bone(value: Name) -> None
```

<a id="unreal.RigUnit_DistributeRotation.end_bone"></a>

#### end_bone

```python
@property
def end_bone() -> Name
```

(Name):  [Read-Write] The name of the last bone to align

<a id="unreal.RigUnit_DistributeRotation.end_bone"></a>

#### end_bone

```python
@end_bone.setter
def end_bone(value: Name) -> None
```

<a id="unreal.RigUnit_DistributeRotation.rotations"></a>

#### rotations

```python
@property
def rotations() -> Array[RigUnit_DistributeRotation_Rotation]
```

(Array[RigUnit_DistributeRotation_Rotation]):  [Read-Write] The list of rotations to be applied

<a id="unreal.RigUnit_DistributeRotation.rotations"></a>

#### rotations

```python
@rotations.setter
def rotations(value: Array[RigUnit_DistributeRotation_Rotation]) -> None
```

<a id="unreal.RigUnit_DistributeRotation.rotation_ease_type"></a>

#### rotation_ease_type

```python
@property
def rotation_ease_type() -> RigVMAnimEasingType
```

(RigVMAnimEasingType):  [Read-Only] The easing to use between to rotations.

<a id="unreal.RigUnit_DistributeRotation.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] The weight of the solver - how much the rotation should be applied

<a id="unreal.RigUnit_DistributeRotation.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_DistributeRotation.propagate_to_children"></a>

#### propagate_to_children

```python
@property
def propagate_to_children() -> bool
```

(bool):  [Read-Only] If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

<a id="unreal.RigUnit_DistributeRotationForCollection"></a>