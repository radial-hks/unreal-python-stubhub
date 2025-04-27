## RigUnit_TwistBones Objects

```python
class RigUnit_TwistBones(RigUnit_HighlevelBaseMutable)
```

Creates a gradient of twist rotation along a chain.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_TwistBones.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``end_bone`` (Name):  [Read-Write] The name of the last bone to twist
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``pole_axis`` (Vector):  [Read-Only] The axis to use for the pole vector for each bone
- ``propagate_to_children`` (bool):  [Read-Only] If set to true all of the global transforms of the children
  of this bone will be recalculated based on their local transforms.
  Note: This is computationally more expensive than turning it off.
- ``start_bone`` (Name):  [Read-Write] The name of the first bone to twist
- ``twist_axis`` (Vector):  [Read-Only] The axis to twist the bones around
- ``twist_ease_type`` (RigVMAnimEasingType):  [Read-Only] The easing to use between two twists.
- ``weight`` (float):  [Read-Write] The weight of the solver - how much the rotation should be applied

<a id="unreal.RigUnit_TwistBones.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             start_bone: Name = "None",
             end_bone: Name = "None",
             twist_axis: Vector = [0.000000, 0.000000, 0.000000],
             pole_axis: Vector = [0.000000, 0.000000, 0.000000],
             twist_ease_type: RigVMAnimEasingType = RigVMAnimEasingType.LINEAR,
             weight: float = 0.000000,
             propagate_to_children: bool = False) -> None
```

<a id="unreal.RigUnit_TwistBones.start_bone"></a>

#### start_bone

```python
@property
def start_bone() -> Name
```

(Name):  [Read-Write] The name of the first bone to twist

<a id="unreal.RigUnit_TwistBones.start_bone"></a>

#### start_bone

```python
@start_bone.setter
def start_bone(value: Name) -> None
```

<a id="unreal.RigUnit_TwistBones.end_bone"></a>

#### end_bone

```python
@property
def end_bone() -> Name
```

(Name):  [Read-Write] The name of the last bone to twist

<a id="unreal.RigUnit_TwistBones.end_bone"></a>

#### end_bone

```python
@end_bone.setter
def end_bone(value: Name) -> None
```

<a id="unreal.RigUnit_TwistBones.twist_axis"></a>

#### twist_axis

```python
@property
def twist_axis() -> Vector
```

(Vector):  [Read-Only] The axis to twist the bones around

<a id="unreal.RigUnit_TwistBones.pole_axis"></a>

#### pole_axis

```python
@property
def pole_axis() -> Vector
```

(Vector):  [Read-Only] The axis to use for the pole vector for each bone

<a id="unreal.RigUnit_TwistBones.twist_ease_type"></a>

#### twist_ease_type

```python
@property
def twist_ease_type() -> RigVMAnimEasingType
```

(RigVMAnimEasingType):  [Read-Only] The easing to use between two twists.

<a id="unreal.RigUnit_TwistBones.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] The weight of the solver - how much the rotation should be applied

<a id="unreal.RigUnit_TwistBones.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_TwistBones.propagate_to_children"></a>

#### propagate_to_children

```python
@property
def propagate_to_children() -> bool
```

(bool):  [Read-Only] If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

<a id="unreal.RigUnit_TwistBonesPerItem"></a>