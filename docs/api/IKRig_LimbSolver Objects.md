## IKRig_LimbSolver Objects

```python
class IKRig_LimbSolver(IKRigSolver)
```

IKRig Limb Solver

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: IKRig_LimbSolver.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``average_pull`` (bool):  [Read-Write] Pull averaging only has a visual impact when we have more than 2 bones (3 links).
- ``enable_limit`` (bool):  [Read-Write] Enable/Disable rotational limits
- ``enable_twist_correction`` (bool):  [Read-Write] Enable Knee Twist correction, by comparing Foot FK with Foot IK orientation.
- ``end_bone_forward_axis`` (AxisType):  [Read-Write] Forward Axis for Foot bone.
- ``hinge_rotation_axis`` (AxisType):  [Read-Write] Hinge Bones Rotation Axis. This is essentially the plane normal for (hip - knee - foot).
- ``max_iterations`` (int32):  [Read-Write] Number of Max Iterations to reach the target
- ``min_rotation_angle`` (float):  [Read-Write] Only used if bEnableRotationLimit is enabled. Prevents the leg from folding onto itself,
  and forces at least this angle between Parent and Child bone.
- ``pull_distribution`` (float):  [Read-Write] Re-position limb to distribute pull: 0 = foot, 0.5 = balanced, 1.f = hip
- ``reach_precision`` (float):  [Read-Write] Precision (distance to the target)
- ``reach_step_alpha`` (float):  [Read-Write] Move end effector towards target. If we are compressing the chain, limit displacement.
- ``root_name`` (Name):  [Read-Only]

<a id="unreal.IKRig_LimbSolver.root_name"></a>

#### root_name

```python
@property
def root_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.IKRig_LimbSolver.reach_precision"></a>

#### reach_precision

```python
@property
def reach_precision() -> float
```

(float):  [Read-Write] Precision (distance to the target)

<a id="unreal.IKRig_LimbSolver.reach_precision"></a>

#### reach_precision

```python
@reach_precision.setter
def reach_precision(value: float) -> None
```

<a id="unreal.IKRig_LimbSolver.hinge_rotation_axis"></a>

#### hinge_rotation_axis

```python
@property
def hinge_rotation_axis() -> AxisType
```

(AxisType):  [Read-Write] Hinge Bones Rotation Axis. This is essentially the plane normal for (hip - knee - foot).

<a id="unreal.IKRig_LimbSolver.hinge_rotation_axis"></a>

#### hinge_rotation_axis

```python
@hinge_rotation_axis.setter
def hinge_rotation_axis(value: AxisType) -> None
```

<a id="unreal.IKRig_LimbSolver.max_iterations"></a>

#### max_iterations

```python
@property
def max_iterations() -> int
```

(int32):  [Read-Write] Number of Max Iterations to reach the target

<a id="unreal.IKRig_LimbSolver.max_iterations"></a>

#### max_iterations

```python
@max_iterations.setter
def max_iterations(value: int) -> None
```

<a id="unreal.IKRig_LimbSolver.enable_limit"></a>

#### enable_limit

```python
@property
def enable_limit() -> bool
```

(bool):  [Read-Write] Enable/Disable rotational limits

<a id="unreal.IKRig_LimbSolver.enable_limit"></a>

#### enable_limit

```python
@enable_limit.setter
def enable_limit(value: bool) -> None
```

<a id="unreal.IKRig_LimbSolver.min_rotation_angle"></a>

#### min_rotation_angle

```python
@property
def min_rotation_angle() -> float
```

(float):  [Read-Write] Only used if bEnableRotationLimit is enabled. Prevents the leg from folding onto itself,
and forces at least this angle between Parent and Child bone.

<a id="unreal.IKRig_LimbSolver.min_rotation_angle"></a>

#### min_rotation_angle

```python
@min_rotation_angle.setter
def min_rotation_angle(value: float) -> None
```

<a id="unreal.IKRig_LimbSolver.average_pull"></a>

#### average_pull

```python
@property
def average_pull() -> bool
```

(bool):  [Read-Write] Pull averaging only has a visual impact when we have more than 2 bones (3 links).

<a id="unreal.IKRig_LimbSolver.average_pull"></a>

#### average_pull

```python
@average_pull.setter
def average_pull(value: bool) -> None
```

<a id="unreal.IKRig_LimbSolver.pull_distribution"></a>

#### pull_distribution

```python
@property
def pull_distribution() -> float
```

(float):  [Read-Write] Re-position limb to distribute pull: 0 = foot, 0.5 = balanced, 1.f = hip

<a id="unreal.IKRig_LimbSolver.pull_distribution"></a>

#### pull_distribution

```python
@pull_distribution.setter
def pull_distribution(value: float) -> None
```

<a id="unreal.IKRig_LimbSolver.reach_step_alpha"></a>

#### reach_step_alpha

```python
@property
def reach_step_alpha() -> float
```

(float):  [Read-Write] Move end effector towards target. If we are compressing the chain, limit displacement.

<a id="unreal.IKRig_LimbSolver.reach_step_alpha"></a>

#### reach_step_alpha

```python
@reach_step_alpha.setter
def reach_step_alpha(value: float) -> None
```

<a id="unreal.IKRig_LimbSolver.enable_twist_correction"></a>

#### enable_twist_correction

```python
@property
def enable_twist_correction() -> bool
```

(bool):  [Read-Write] Enable Knee Twist correction, by comparing Foot FK with Foot IK orientation.

<a id="unreal.IKRig_LimbSolver.enable_twist_correction"></a>

#### enable_twist_correction

```python
@enable_twist_correction.setter
def enable_twist_correction(value: bool) -> None
```

<a id="unreal.IKRig_LimbSolver.end_bone_forward_axis"></a>

#### end_bone_forward_axis

```python
@property
def end_bone_forward_axis() -> AxisType
```

(AxisType):  [Read-Write] Forward Axis for Foot bone.

<a id="unreal.IKRig_LimbSolver.end_bone_forward_axis"></a>

#### end_bone_forward_axis

```python
@end_bone_forward_axis.setter
def end_bone_forward_axis(value: AxisType) -> None
```

<a id="unreal.IKRig_FBIKEffector"></a>