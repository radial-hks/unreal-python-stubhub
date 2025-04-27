## RigUnit_TwoBoneIKSimpleTransforms Objects

```python
class RigUnit_TwoBoneIKSimpleTransforms(RigUnit_HighlevelBase)
```

Solves the two bone IK given transforms
Note: This node operates in world space!

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_TwoBoneIKSimple.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone_a_length`` (float):  [Read-Write] The length of the first bone.
  If set to 0.0 it will be determined by the hierarchy
- ``bone_b_length`` (float):  [Read-Write] The length of the second  bone.
  If set to 0.0 it will be determined by the hierarchy
- ``effector`` (Transform):  [Read-Write] The transform of the effector
- ``elbow`` (Transform):  [Read-Write] The resulting elbow transform
- ``enable_stretch`` (bool):  [Read-Write] If set to true the stretch feature of the solver will be enabled
- ``pole_vector`` (Vector):  [Read-Write] The position of the pole of the triangle
- ``primary_axis`` (Vector):  [Read-Write] The major axis being aligned - along the bone
- ``root`` (Transform):  [Read-Write] The transform of the root of the triangle
- ``secondary_axis`` (Vector):  [Read-Write] The minor axis being aligned - towards the polevector
- ``secondary_axis_weight`` (float):  [Read-Write] Determines how much the secondary axis roll is being applied
- ``stretch_maximum_ratio`` (float):  [Read-Write] The maximum allowed stretch ratio
- ``stretch_start_ratio`` (float):  [Read-Write] The ratio where the stretch starts

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms.__init__"></a>

#### __init__

```python
def __init__(
    root: Transform = [[0.000000, 0.000000, 0.000000],
                       [-0.000000, 0.000000, 0.000000],
                       [1.000000, 1.000000, 1.000000]],
    pole_vector: Vector = [0.000000, 0.000000, 0.000000],
    effector: Transform = [[0.000000, 0.000000, 0.000000],
                           [-0.000000, 0.000000, 0.000000],
                           [1.000000, 1.000000, 1.000000]],
    primary_axis: Vector = [0.000000, 0.000000, 0.000000],
    secondary_axis: Vector = [0.000000, 0.000000, 0.000000],
    secondary_axis_weight: float = 0.000000,
    enable_stretch: bool = False,
    stretch_start_ratio: float = 0.000000,
    stretch_maximum_ratio: float = 0.000000,
    bone_a_length: float = 0.000000,
    bone_b_length: float = 0.000000,
    elbow: Transform = [[0.000000, 0.000000, 0.000000],
                        [-0.000000, 0.000000, 0.000000],
                        [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms.root"></a>

#### root

```python
@property
def root() -> Transform
```

(Transform):  [Read-Write] The transform of the root of the triangle

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms.root"></a>

#### root

```python
@root.setter
def root(value: Transform) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms.pole_vector"></a>

#### pole_vector

```python
@property
def pole_vector() -> Vector
```

(Vector):  [Read-Write] The position of the pole of the triangle

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms.pole_vector"></a>

#### pole_vector

```python
@pole_vector.setter
def pole_vector(value: Vector) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms.effector"></a>

#### effector

```python
@property
def effector() -> Transform
```

(Transform):  [Read-Write] The transform of the effector

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms.effector"></a>

#### effector

```python
@effector.setter
def effector(value: Transform) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms.primary_axis"></a>

#### primary_axis

```python
@property
def primary_axis() -> Vector
```

(Vector):  [Read-Write] The major axis being aligned - along the bone

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms.primary_axis"></a>

#### primary_axis

```python
@primary_axis.setter
def primary_axis(value: Vector) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms.secondary_axis"></a>

#### secondary_axis

```python
@property
def secondary_axis() -> Vector
```

(Vector):  [Read-Write] The minor axis being aligned - towards the polevector

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms.secondary_axis"></a>

#### secondary_axis

```python
@secondary_axis.setter
def secondary_axis(value: Vector) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms.secondary_axis_weight"></a>

#### secondary_axis_weight

```python
@property
def secondary_axis_weight() -> float
```

(float):  [Read-Write] Determines how much the secondary axis roll is being applied

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms.secondary_axis_weight"></a>

#### secondary_axis_weight

```python
@secondary_axis_weight.setter
def secondary_axis_weight(value: float) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms.enable_stretch"></a>

#### enable_stretch

```python
@property
def enable_stretch() -> bool
```

(bool):  [Read-Write] If set to true the stretch feature of the solver will be enabled

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms.enable_stretch"></a>

#### enable_stretch

```python
@enable_stretch.setter
def enable_stretch(value: bool) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms.stretch_start_ratio"></a>

#### stretch_start_ratio

```python
@property
def stretch_start_ratio() -> float
```

(float):  [Read-Write] The ratio where the stretch starts

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms.stretch_start_ratio"></a>

#### stretch_start_ratio

```python
@stretch_start_ratio.setter
def stretch_start_ratio(value: float) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms.stretch_maximum_ratio"></a>

#### stretch_maximum_ratio

```python
@property
def stretch_maximum_ratio() -> float
```

(float):  [Read-Write] The maximum allowed stretch ratio

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms.stretch_maximum_ratio"></a>

#### stretch_maximum_ratio

```python
@stretch_maximum_ratio.setter
def stretch_maximum_ratio(value: float) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms.bone_a_length"></a>

#### bone_a_length

```python
@property
def bone_a_length() -> float
```

(float):  [Read-Write] The length of the first bone.
If set to 0.0 it will be determined by the hierarchy

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms.bone_a_length"></a>

#### bone_a_length

```python
@bone_a_length.setter
def bone_a_length(value: float) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms.bone_b_length"></a>

#### bone_b_length

```python
@property
def bone_b_length() -> float
```

(float):  [Read-Write] The length of the second  bone.
If set to 0.0 it will be determined by the hierarchy

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms.bone_b_length"></a>

#### bone_b_length

```python
@bone_b_length.setter
def bone_b_length(value: float) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms.elbow"></a>

#### elbow

```python
@property
def elbow() -> Transform
```

(Transform):  [Read-Write] The resulting elbow transform

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms.elbow"></a>

#### elbow

```python
@elbow.setter
def elbow(value: Transform) -> None
```

<a id="unreal.RigUnit_GetCandidates"></a>