## RigUnit_TwoBoneIKSimple Objects

```python
class RigUnit_TwoBoneIKSimple(RigUnit_HighlevelBaseMutable)
```

Solves the two bone IK given two bones.
Note: This node operates in world space!

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_TwoBoneIKSimple.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone_a`` (Name):  [Read-Write] The name of first bone
- ``bone_a_length`` (float):  [Read-Write] The length of the first bone.
  If set to 0.0 it will be determined by the hierarchy
- ``bone_b`` (Name):  [Read-Write] The name of second bone
- ``bone_b_length`` (float):  [Read-Write] The length of the second  bone.
  If set to 0.0 it will be determined by the hierarchy
- ``debug_settings`` (RigUnit_TwoBoneIKSimple_DebugSettings):  [Read-Write] The settings for debug drawing
- ``effector`` (Transform):  [Read-Write] The transform of the effector
- ``effector_bone`` (Name):  [Read-Write] The name of the effector bone (if exists)
- ``enable_stretch`` (bool):  [Read-Write] If set to true the stretch feature of the solver will be enabled
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``pole_vector`` (Vector):  [Read-Write] The polevector to use for the IK solver
  This can be a location or direction.
- ``pole_vector_kind`` (ControlRigVectorKind):  [Read-Write] The kind of pole vector this is representing - can be a direction or a location
- ``pole_vector_space`` (Name):  [Read-Write] The space in which the pole vector is expressed
- ``primary_axis`` (Vector):  [Read-Write] The major axis being aligned - along the bone
- ``propagate_to_children`` (bool):  [Read-Only] If set to true all of the global transforms of the children
  of this bone will be recalculated based on their local transforms.
  Note: This is computationally more expensive than turning it off.
- ``secondary_axis`` (Vector):  [Read-Write] The minor axis being aligned - towards the polevector
- ``secondary_axis_weight`` (float):  [Read-Write] Determines how much the secondary axis roll is being applied
- ``stretch_maximum_ratio`` (float):  [Read-Write] The maximum allowed stretch ratio
- ``stretch_start_ratio`` (float):  [Read-Write] The ratio where the stretch starts
- ``weight`` (float):  [Read-Write] The weight of the solver - how much the IK should be applied.

<a id="unreal.RigUnit_TwoBoneIKSimple.__init__"></a>

#### __init__

```python
def __init__(
    execute_context: ControlRigExecuteContext = [],
    bone_a: Name = "None",
    bone_b: Name = "None",
    effector_bone: Name = "None",
    effector: Transform = [[0.000000, 0.000000, 0.000000],
                           [-0.000000, 0.000000, 0.000000],
                           [1.000000, 1.000000, 1.000000]],
    primary_axis: Vector = [0.000000, 0.000000, 0.000000],
    secondary_axis: Vector = [0.000000, 0.000000, 0.000000],
    secondary_axis_weight: float = 0.000000,
    pole_vector: Vector = [0.000000, 0.000000, 0.000000],
    pole_vector_kind: ControlRigVectorKind = ControlRigVectorKind.DIRECTION,
    pole_vector_space: Name = "None",
    enable_stretch: bool = False,
    stretch_start_ratio: float = 0.000000,
    stretch_maximum_ratio: float = 0.000000,
    weight: float = 0.000000,
    bone_a_length: float = 0.000000,
    bone_b_length: float = 0.000000,
    propagate_to_children: bool = False,
    debug_settings: RigUnit_TwoBoneIKSimple_DebugSettings = [
        False, 10.000000,
        [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
         [1.000000, 1.000000, 1.000000]]
    ]
) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimple.bone_a"></a>

#### bone_a

```python
@property
def bone_a() -> Name
```

(Name):  [Read-Write] The name of first bone

<a id="unreal.RigUnit_TwoBoneIKSimple.bone_a"></a>

#### bone_a

```python
@bone_a.setter
def bone_a(value: Name) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimple.bone_b"></a>

#### bone_b

```python
@property
def bone_b() -> Name
```

(Name):  [Read-Write] The name of second bone

<a id="unreal.RigUnit_TwoBoneIKSimple.bone_b"></a>

#### bone_b

```python
@bone_b.setter
def bone_b(value: Name) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimple.effector_bone"></a>

#### effector_bone

```python
@property
def effector_bone() -> Name
```

(Name):  [Read-Write] The name of the effector bone (if exists)

<a id="unreal.RigUnit_TwoBoneIKSimple.effector_bone"></a>

#### effector_bone

```python
@effector_bone.setter
def effector_bone(value: Name) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimple.effector"></a>

#### effector

```python
@property
def effector() -> Transform
```

(Transform):  [Read-Write] The transform of the effector

<a id="unreal.RigUnit_TwoBoneIKSimple.effector"></a>

#### effector

```python
@effector.setter
def effector(value: Transform) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimple.primary_axis"></a>

#### primary_axis

```python
@property
def primary_axis() -> Vector
```

(Vector):  [Read-Write] The major axis being aligned - along the bone

<a id="unreal.RigUnit_TwoBoneIKSimple.primary_axis"></a>

#### primary_axis

```python
@primary_axis.setter
def primary_axis(value: Vector) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimple.secondary_axis"></a>

#### secondary_axis

```python
@property
def secondary_axis() -> Vector
```

(Vector):  [Read-Write] The minor axis being aligned - towards the polevector

<a id="unreal.RigUnit_TwoBoneIKSimple.secondary_axis"></a>

#### secondary_axis

```python
@secondary_axis.setter
def secondary_axis(value: Vector) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimple.secondary_axis_weight"></a>

#### secondary_axis_weight

```python
@property
def secondary_axis_weight() -> float
```

(float):  [Read-Write] Determines how much the secondary axis roll is being applied

<a id="unreal.RigUnit_TwoBoneIKSimple.secondary_axis_weight"></a>

#### secondary_axis_weight

```python
@secondary_axis_weight.setter
def secondary_axis_weight(value: float) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimple.pole_vector"></a>

#### pole_vector

```python
@property
def pole_vector() -> Vector
```

(Vector):  [Read-Write] The polevector to use for the IK solver
This can be a location or direction.

<a id="unreal.RigUnit_TwoBoneIKSimple.pole_vector"></a>

#### pole_vector

```python
@pole_vector.setter
def pole_vector(value: Vector) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimple.pole_vector_kind"></a>

#### pole_vector_kind

```python
@property
def pole_vector_kind() -> ControlRigVectorKind
```

(ControlRigVectorKind):  [Read-Write] The kind of pole vector this is representing - can be a direction or a location

<a id="unreal.RigUnit_TwoBoneIKSimple.pole_vector_kind"></a>

#### pole_vector_kind

```python
@pole_vector_kind.setter
def pole_vector_kind(value: ControlRigVectorKind) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimple.pole_vector_space"></a>

#### pole_vector_space

```python
@property
def pole_vector_space() -> Name
```

(Name):  [Read-Write] The space in which the pole vector is expressed

<a id="unreal.RigUnit_TwoBoneIKSimple.pole_vector_space"></a>

#### pole_vector_space

```python
@pole_vector_space.setter
def pole_vector_space(value: Name) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimple.enable_stretch"></a>

#### enable_stretch

```python
@property
def enable_stretch() -> bool
```

(bool):  [Read-Write] If set to true the stretch feature of the solver will be enabled

<a id="unreal.RigUnit_TwoBoneIKSimple.enable_stretch"></a>

#### enable_stretch

```python
@enable_stretch.setter
def enable_stretch(value: bool) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimple.stretch_start_ratio"></a>

#### stretch_start_ratio

```python
@property
def stretch_start_ratio() -> float
```

(float):  [Read-Write] The ratio where the stretch starts

<a id="unreal.RigUnit_TwoBoneIKSimple.stretch_start_ratio"></a>

#### stretch_start_ratio

```python
@stretch_start_ratio.setter
def stretch_start_ratio(value: float) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimple.stretch_maximum_ratio"></a>

#### stretch_maximum_ratio

```python
@property
def stretch_maximum_ratio() -> float
```

(float):  [Read-Write] The maximum allowed stretch ratio

<a id="unreal.RigUnit_TwoBoneIKSimple.stretch_maximum_ratio"></a>

#### stretch_maximum_ratio

```python
@stretch_maximum_ratio.setter
def stretch_maximum_ratio(value: float) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimple.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] The weight of the solver - how much the IK should be applied.

<a id="unreal.RigUnit_TwoBoneIKSimple.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimple.bone_a_length"></a>

#### bone_a_length

```python
@property
def bone_a_length() -> float
```

(float):  [Read-Write] The length of the first bone.
If set to 0.0 it will be determined by the hierarchy

<a id="unreal.RigUnit_TwoBoneIKSimple.bone_a_length"></a>

#### bone_a_length

```python
@bone_a_length.setter
def bone_a_length(value: float) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimple.bone_b_length"></a>

#### bone_b_length

```python
@property
def bone_b_length() -> float
```

(float):  [Read-Write] The length of the second  bone.
If set to 0.0 it will be determined by the hierarchy

<a id="unreal.RigUnit_TwoBoneIKSimple.bone_b_length"></a>

#### bone_b_length

```python
@bone_b_length.setter
def bone_b_length(value: float) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimple.propagate_to_children"></a>

#### propagate_to_children

```python
@property
def propagate_to_children() -> bool
```

(bool):  [Read-Only] If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

<a id="unreal.RigUnit_TwoBoneIKSimple.debug_settings"></a>

#### debug_settings

```python
@property
def debug_settings() -> RigUnit_TwoBoneIKSimple_DebugSettings
```

(RigUnit_TwoBoneIKSimple_DebugSettings):  [Read-Write] The settings for debug drawing

<a id="unreal.RigUnit_TwoBoneIKSimple.debug_settings"></a>

#### debug_settings

```python
@debug_settings.setter
def debug_settings(value: RigUnit_TwoBoneIKSimple_DebugSettings) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimplePerItem"></a>