## IKRig_FBIKBoneSettings Objects

```python
class IKRig_FBIKBoneSettings(Object)
```

IKRig FBIKBone Settings

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: IKRig_FBIKSolver.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone`` (Name):  [Read-Only] The bone these settings are applied to.
- ``max_x`` (float):  [Read-Write] Range is 0 to 180 (Default is 0). Degrees of rotation in the positive X direction to allow when joint is in "Limited" mode.
- ``max_y`` (float):  [Read-Write] Range is 0 to 180 (Default is 0). Degrees of rotation in the positive Y direction to allow when joint is in "Limited" mode.
- ``max_z`` (float):  [Read-Write] Range is 0 to 180 (Default is 0). Degrees of rotation in the positive Z direction to allow when joint is in "Limited" mode.
- ``min_x`` (float):  [Read-Write] Range is -180 to 0 (Default is 0). Degrees of rotation in the negative X direction to allow when joint is in "Limited" mode.
- ``min_y`` (float):  [Read-Write] Range is -180 to 0 (Default is 0). Degrees of rotation in the negative Y direction to allow when joint is in "Limited" mode.
- ``min_z`` (float):  [Read-Write] Range is -180 to 0 (Default is 0). Degrees of rotation in the negative Z direction to allow when joint is in "Limited" mode.
- ``position_stiffness`` (float):  [Read-Write] Range is 0 to 1 (Default is 0). At higher values, the bone will resist translational motion (forcing other bones to compensate).
- ``preferred_angles`` (Vector):  [Read-Write] The local Euler angles (in degrees) used to rotate this bone when the chain it belongs to is squashed.
  This happens by moving the effector at the tip of the chain towards the root of the chain.
  This can be used to coerce knees and elbows to bend in the anatomically "correct" direction without resorting to limits (which may require more iterations to converge).
- ``rotation_stiffness`` (float):  [Read-Write] Range is 0 to 1 (Default is 0). At higher values, the bone will resist rotating (forcing other bones to compensate).
- ``use_preferred_angles`` (bool):  [Read-Write] When true, this bone will "prefer" to rotate in the direction specified by the Preferred Angles when the chain it belongs to is compressed.
  Preferred Angles should be the first method used to fix bones that bend in the wrong direction (rather than limits).
  The resulting angles can be visualized on their own by temporarily setting the Solver iterations to 0 and moving the effectors.
- ``x`` (PBIKLimitType):  [Read-Write] Limit the rotation angle of the bone on the X axis.
  Free: can rotate freely in this axis.
  Limited: rotation is clamped between the min/max angles relative to the Skeletal Mesh reference pose.
  Locked: no rotation is allowed in this axis (will remain at reference pose angle).
- ``y`` (PBIKLimitType):  [Read-Write] Limit the rotation angle of the bone on the Y axis.
  Free: can rotate freely in this axis.
  Limited: rotation is clamped between the min/max angles relative to the Skeletal Mesh reference pose.
  Locked: no rotation is allowed in this axis (will remain at input pose angle).
- ``z`` (PBIKLimitType):  [Read-Write] Limit the rotation angle of the bone on the Z axis.
  Free: can rotate freely in this axis.
  Limited: rotation is clamped between the min/max angles relative to the Skeletal Mesh reference pose.
  Locked: no rotation is allowed in this axis (will remain at input pose angle).

<a id="unreal.IKRig_FBIKBoneSettings.bone"></a>

#### bone

```python
@property
def bone() -> Name
```

(Name):  [Read-Only] The bone these settings are applied to.

<a id="unreal.IKRig_FBIKBoneSettings.rotation_stiffness"></a>

#### rotation_stiffness

```python
@property
def rotation_stiffness() -> float
```

(float):  [Read-Write] Range is 0 to 1 (Default is 0). At higher values, the bone will resist rotating (forcing other bones to compensate).

<a id="unreal.IKRig_FBIKBoneSettings.rotation_stiffness"></a>

#### rotation_stiffness

```python
@rotation_stiffness.setter
def rotation_stiffness(value: float) -> None
```

<a id="unreal.IKRig_FBIKBoneSettings.position_stiffness"></a>

#### position_stiffness

```python
@property
def position_stiffness() -> float
```

(float):  [Read-Write] Range is 0 to 1 (Default is 0). At higher values, the bone will resist translational motion (forcing other bones to compensate).

<a id="unreal.IKRig_FBIKBoneSettings.position_stiffness"></a>

#### position_stiffness

```python
@position_stiffness.setter
def position_stiffness(value: float) -> None
```

<a id="unreal.IKRig_FBIKBoneSettings.x"></a>

#### x

```python
@property
def x() -> PBIKLimitType
```

(PBIKLimitType):  [Read-Write] Limit the rotation angle of the bone on the X axis.
Free: can rotate freely in this axis.
Limited: rotation is clamped between the min/max angles relative to the Skeletal Mesh reference pose.
Locked: no rotation is allowed in this axis (will remain at reference pose angle).

<a id="unreal.IKRig_FBIKBoneSettings.x"></a>

#### x

```python
@x.setter
def x(value: PBIKLimitType) -> None
```

<a id="unreal.IKRig_FBIKBoneSettings.min_x"></a>

#### min_x

```python
@property
def min_x() -> float
```

(float):  [Read-Write] Range is -180 to 0 (Default is 0). Degrees of rotation in the negative X direction to allow when joint is in "Limited" mode.

<a id="unreal.IKRig_FBIKBoneSettings.min_x"></a>

#### min_x

```python
@min_x.setter
def min_x(value: float) -> None
```

<a id="unreal.IKRig_FBIKBoneSettings.max_x"></a>

#### max_x

```python
@property
def max_x() -> float
```

(float):  [Read-Write] Range is 0 to 180 (Default is 0). Degrees of rotation in the positive X direction to allow when joint is in "Limited" mode.

<a id="unreal.IKRig_FBIKBoneSettings.max_x"></a>

#### max_x

```python
@max_x.setter
def max_x(value: float) -> None
```

<a id="unreal.IKRig_FBIKBoneSettings.y"></a>

#### y

```python
@property
def y() -> PBIKLimitType
```

(PBIKLimitType):  [Read-Write] Limit the rotation angle of the bone on the Y axis.
Free: can rotate freely in this axis.
Limited: rotation is clamped between the min/max angles relative to the Skeletal Mesh reference pose.
Locked: no rotation is allowed in this axis (will remain at input pose angle).

<a id="unreal.IKRig_FBIKBoneSettings.y"></a>

#### y

```python
@y.setter
def y(value: PBIKLimitType) -> None
```

<a id="unreal.IKRig_FBIKBoneSettings.min_y"></a>

#### min_y

```python
@property
def min_y() -> float
```

(float):  [Read-Write] Range is -180 to 0 (Default is 0). Degrees of rotation in the negative Y direction to allow when joint is in "Limited" mode.

<a id="unreal.IKRig_FBIKBoneSettings.min_y"></a>

#### min_y

```python
@min_y.setter
def min_y(value: float) -> None
```

<a id="unreal.IKRig_FBIKBoneSettings.max_y"></a>

#### max_y

```python
@property
def max_y() -> float
```

(float):  [Read-Write] Range is 0 to 180 (Default is 0). Degrees of rotation in the positive Y direction to allow when joint is in "Limited" mode.

<a id="unreal.IKRig_FBIKBoneSettings.max_y"></a>

#### max_y

```python
@max_y.setter
def max_y(value: float) -> None
```

<a id="unreal.IKRig_FBIKBoneSettings.z"></a>

#### z

```python
@property
def z() -> PBIKLimitType
```

(PBIKLimitType):  [Read-Write] Limit the rotation angle of the bone on the Z axis.
Free: can rotate freely in this axis.
Limited: rotation is clamped between the min/max angles relative to the Skeletal Mesh reference pose.
Locked: no rotation is allowed in this axis (will remain at input pose angle).

<a id="unreal.IKRig_FBIKBoneSettings.z"></a>

#### z

```python
@z.setter
def z(value: PBIKLimitType) -> None
```

<a id="unreal.IKRig_FBIKBoneSettings.min_z"></a>

#### min_z

```python
@property
def min_z() -> float
```

(float):  [Read-Write] Range is -180 to 0 (Default is 0). Degrees of rotation in the negative Z direction to allow when joint is in "Limited" mode.

<a id="unreal.IKRig_FBIKBoneSettings.min_z"></a>

#### min_z

```python
@min_z.setter
def min_z(value: float) -> None
```

<a id="unreal.IKRig_FBIKBoneSettings.max_z"></a>

#### max_z

```python
@property
def max_z() -> float
```

(float):  [Read-Write] Range is 0 to 180 (Default is 0). Degrees of rotation in the positive Z direction to allow when joint is in "Limited" mode.

<a id="unreal.IKRig_FBIKBoneSettings.max_z"></a>

#### max_z

```python
@max_z.setter
def max_z(value: float) -> None
```

<a id="unreal.IKRig_FBIKBoneSettings.use_preferred_angles"></a>

#### use_preferred_angles

```python
@property
def use_preferred_angles() -> bool
```

(bool):  [Read-Write] When true, this bone will "prefer" to rotate in the direction specified by the Preferred Angles when the chain it belongs to is compressed.
Preferred Angles should be the first method used to fix bones that bend in the wrong direction (rather than limits).
The resulting angles can be visualized on their own by temporarily setting the Solver iterations to 0 and moving the effectors.

<a id="unreal.IKRig_FBIKBoneSettings.use_preferred_angles"></a>

#### use_preferred_angles

```python
@use_preferred_angles.setter
def use_preferred_angles(value: bool) -> None
```

<a id="unreal.IKRig_FBIKBoneSettings.preferred_angles"></a>

#### preferred_angles

```python
@property
def preferred_angles() -> Vector
```

(Vector):  [Read-Write] The local Euler angles (in degrees) used to rotate this bone when the chain it belongs to is squashed.
This happens by moving the effector at the tip of the chain towards the root of the chain.
This can be used to coerce knees and elbows to bend in the anatomically "correct" direction without resorting to limits (which may require more iterations to converge).

<a id="unreal.IKRig_FBIKBoneSettings.preferred_angles"></a>

#### preferred_angles

```python
@preferred_angles.setter
def preferred_angles(value: Vector) -> None
```

<a id="unreal.IKRig_PBIKBoneSettings"></a>