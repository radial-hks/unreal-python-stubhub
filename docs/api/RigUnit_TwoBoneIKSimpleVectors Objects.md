## RigUnit_TwoBoneIKSimpleVectors Objects

```python
class RigUnit_TwoBoneIKSimpleVectors(RigUnit_HighlevelBase)
```

Solves the two bone IK given positions
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
- ``effector`` (Vector):  [Read-Write] The position of the effector
- ``elbow`` (Vector):  [Read-Write] The resulting elbow position
- ``enable_stretch`` (bool):  [Read-Write] If set to true the stretch feature of the solver will be enabled
- ``pole_vector`` (Vector):  [Read-Write] The position of the pole of the triangle
- ``root`` (Vector):  [Read-Write] The position of the root of the triangle
- ``stretch_maximum_ratio`` (float):  [Read-Write] The maximum allowed stretch ratio
- ``stretch_start_ratio`` (float):  [Read-Write] The ratio where the stretch starts

<a id="unreal.RigUnit_TwoBoneIKSimpleVectors.__init__"></a>

#### __init__

```python
def __init__(root: Vector = [0.000000, 0.000000, 0.000000],
             pole_vector: Vector = [0.000000, 0.000000, 0.000000],
             effector: Vector = [0.000000, 0.000000, 0.000000],
             enable_stretch: bool = False,
             stretch_start_ratio: float = 0.000000,
             stretch_maximum_ratio: float = 0.000000,
             bone_a_length: float = 0.000000,
             bone_b_length: float = 0.000000,
             elbow: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimpleVectors.root"></a>

#### root

```python
@property
def root() -> Vector
```

(Vector):  [Read-Write] The position of the root of the triangle

<a id="unreal.RigUnit_TwoBoneIKSimpleVectors.root"></a>

#### root

```python
@root.setter
def root(value: Vector) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimpleVectors.pole_vector"></a>

#### pole_vector

```python
@property
def pole_vector() -> Vector
```

(Vector):  [Read-Write] The position of the pole of the triangle

<a id="unreal.RigUnit_TwoBoneIKSimpleVectors.pole_vector"></a>

#### pole_vector

```python
@pole_vector.setter
def pole_vector(value: Vector) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimpleVectors.effector"></a>

#### effector

```python
@property
def effector() -> Vector
```

(Vector):  [Read-Write] The position of the effector

<a id="unreal.RigUnit_TwoBoneIKSimpleVectors.effector"></a>

#### effector

```python
@effector.setter
def effector(value: Vector) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimpleVectors.enable_stretch"></a>

#### enable_stretch

```python
@property
def enable_stretch() -> bool
```

(bool):  [Read-Write] If set to true the stretch feature of the solver will be enabled

<a id="unreal.RigUnit_TwoBoneIKSimpleVectors.enable_stretch"></a>

#### enable_stretch

```python
@enable_stretch.setter
def enable_stretch(value: bool) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimpleVectors.stretch_start_ratio"></a>

#### stretch_start_ratio

```python
@property
def stretch_start_ratio() -> float
```

(float):  [Read-Write] The ratio where the stretch starts

<a id="unreal.RigUnit_TwoBoneIKSimpleVectors.stretch_start_ratio"></a>

#### stretch_start_ratio

```python
@stretch_start_ratio.setter
def stretch_start_ratio(value: float) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimpleVectors.stretch_maximum_ratio"></a>

#### stretch_maximum_ratio

```python
@property
def stretch_maximum_ratio() -> float
```

(float):  [Read-Write] The maximum allowed stretch ratio

<a id="unreal.RigUnit_TwoBoneIKSimpleVectors.stretch_maximum_ratio"></a>

#### stretch_maximum_ratio

```python
@stretch_maximum_ratio.setter
def stretch_maximum_ratio(value: float) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimpleVectors.bone_a_length"></a>

#### bone_a_length

```python
@property
def bone_a_length() -> float
```

(float):  [Read-Write] The length of the first bone.
If set to 0.0 it will be determined by the hierarchy

<a id="unreal.RigUnit_TwoBoneIKSimpleVectors.bone_a_length"></a>

#### bone_a_length

```python
@bone_a_length.setter
def bone_a_length(value: float) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimpleVectors.bone_b_length"></a>

#### bone_b_length

```python
@property
def bone_b_length() -> float
```

(float):  [Read-Write] The length of the second  bone.
If set to 0.0 it will be determined by the hierarchy

<a id="unreal.RigUnit_TwoBoneIKSimpleVectors.bone_b_length"></a>

#### bone_b_length

```python
@bone_b_length.setter
def bone_b_length(value: float) -> None
```

<a id="unreal.RigUnit_TwoBoneIKSimpleVectors.elbow"></a>

#### elbow

```python
@property
def elbow() -> Vector
```

(Vector):  [Read-Only] The resulting elbow position

<a id="unreal.RigUnit_TwoBoneIKSimpleTransforms"></a>