## RigUnit_ToRigSpace_Rotation Objects

```python
class RigUnit_ToRigSpace_Rotation(RigUnit)
```

Converts a rotation from world space to rig (global) space

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_WorldSpace.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``global_`` (Quat):  [Read-Write] The result rotation in global / rig space
- ``value`` (Quat):  [Read-Write] The input rotation in world

<a id="unreal.RigUnit_ToRigSpace_Rotation.__init__"></a>

#### __init__

```python
def __init__(value: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             global_: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.RigUnit_ToRigSpace_Rotation.value"></a>

#### value

```python
@property
def value() -> Quat
```

(Quat):  [Read-Write] The input rotation in world

<a id="unreal.RigUnit_ToRigSpace_Rotation.value"></a>

#### value

```python
@value.setter
def value(value: Quat) -> None
```

<a id="unreal.RigUnit_ToRigSpace_Rotation.rotation"></a>

#### rotation

```python
@property
def rotation() -> Quat
```

deprecated: 'rotation' was renamed to 'value'.

<a id="unreal.RigUnit_ToRigSpace_Rotation.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Quat) -> None
```

<a id="unreal.RigUnit_ToRigSpace_Rotation.global_"></a>

#### global_

```python
@property
def global_() -> Quat
```

(Quat):  [Read-Only] The result rotation in global / rig space

<a id="unreal.RigUnit_BoneHarmonics_BoneTarget"></a>