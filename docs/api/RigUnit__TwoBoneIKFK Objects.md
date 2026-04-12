## RigUnit\_TwoBoneIKFK Objects

```python
class RigUnit_TwoBoneIKFK(RigUnitMutable)
```

Rig Unit Two Bone IKFK

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_TwoBoneIKFK.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``end_effector`` (Transform):  [Read-Write] # Transform to use as the end effector of the IK system
- ``end_joint`` (Name):  [Read-Write]
- ``end_joint_fk_transform`` (Transform):  [Read-Write]
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``ik_blend`` (float):  [Read-Write] Float : IKBlend(Default : 0.0)             # Blend between 0.0 (FK) and 1.0 (IK)solutions
- ``mid_joint_fk_transform`` (Transform):  [Read-Write]
- ``pole_target`` (Vector):  [Read-Write] # Transform to use as the pole target(specifies the plane of solution)
- ``spin`` (float):  [Read-Write] Float: Spin(Default : 0.0) # Amount of twist to apply to the solution plane(Additive after application of Pole Target motion)
- ``start_joint`` (Name):  [Read-Write]
- ``start_joint_fk_transform`` (Transform):  [Read-Write] Transform : Start Joint FK Transform         # Transform for the Start Joint when in FK mode
  Transform: Mid Joint FK Transform           # Transform for the Mid Joint when in FK mode
  Transform : End Joint FK Transform          # Transform for the End Joint when in FK mode

<a id="unreal.RigUnit_TwoBoneIKFK.__init__"></a>

#### \_\_init\_\_

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             start_joint: Name = "None",
             end_joint: Name = "None",
             pole_target: Vector = [0.000000, 0.000000, 0.000000],
             spin: float = 0.000000,
             end_effector: Transform = [[0.000000, 0.000000, 0.000000],
                                        [-0.000000, 0.000000, 0.000000],
                                        [1.000000, 1.000000, 1.000000]],
             ik_blend: float = 0.000000) -> None
```

<a id="unreal.RigUnit_TwoBoneIKFK.start_joint"></a>

#### start\_joint

```python
@property
def start_joint() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigUnit_TwoBoneIKFK.start_joint"></a>

#### start\_joint

```python
@start_joint.setter
def start_joint(value: Name) -> None
```

<a id="unreal.RigUnit_TwoBoneIKFK.end_joint"></a>

#### end\_joint

```python
@property
def end_joint() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigUnit_TwoBoneIKFK.end_joint"></a>

#### end\_joint

```python
@end_joint.setter
def end_joint(value: Name) -> None
```

<a id="unreal.RigUnit_TwoBoneIKFK.pole_target"></a>

#### pole\_target

```python
@property
def pole_target() -> Vector
```

(Vector):  [Read-Write] # Transform to use as the pole target(specifies the plane of solution)

<a id="unreal.RigUnit_TwoBoneIKFK.pole_target"></a>

#### pole\_target

```python
@pole_target.setter
def pole_target(value: Vector) -> None
```

<a id="unreal.RigUnit_TwoBoneIKFK.spin"></a>

#### spin

```python
@property
def spin() -> float
```

(float):  [Read-Write] Float: Spin(Default : 0.0) # Amount of twist to apply to the solution plane(Additive after application of Pole Target motion)

<a id="unreal.RigUnit_TwoBoneIKFK.spin"></a>

#### spin

```python
@spin.setter
def spin(value: float) -> None
```

<a id="unreal.RigUnit_TwoBoneIKFK.end_effector"></a>

#### end\_effector

```python
@property
def end_effector() -> Transform
```

(Transform):  [Read-Write] # Transform to use as the end effector of the IK system

<a id="unreal.RigUnit_TwoBoneIKFK.end_effector"></a>

#### end\_effector

```python
@end_effector.setter
def end_effector(value: Transform) -> None
```

<a id="unreal.RigUnit_TwoBoneIKFK.ik_blend"></a>

#### ik\_blend

```python
@property
def ik_blend() -> float
```

(float):  [Read-Write] Float : IKBlend(Default : 0.0)             # Blend between 0.0 (FK) and 1.0 (IK)solutions

<a id="unreal.RigUnit_TwoBoneIKFK.ik_blend"></a>

#### ik\_blend

```python
@ik_blend.setter
def ik_blend(value: float) -> None
```

<a id="unreal.RigUnit_DrawContainerGetInstruction"></a>