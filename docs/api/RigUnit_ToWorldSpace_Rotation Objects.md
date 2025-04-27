## RigUnit_ToWorldSpace_Rotation Objects

```python
class RigUnit_ToWorldSpace_Rotation(RigUnit)
```

Converts a rotation from rig (global) space to world space

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_WorldSpace.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``value`` (Quat):  [Read-Write] The input rotation in global / rig space
- ``world`` (Quat):  [Read-Write] The result rotation in world space

<a id="unreal.RigUnit_ToWorldSpace_Rotation.__init__"></a>

#### __init__

```python
def __init__(value: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             world: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.RigUnit_ToWorldSpace_Rotation.value"></a>

#### value

```python
@property
def value() -> Quat
```

(Quat):  [Read-Write] The input rotation in global / rig space

<a id="unreal.RigUnit_ToWorldSpace_Rotation.value"></a>

#### value

```python
@value.setter
def value(value: Quat) -> None
```

<a id="unreal.RigUnit_ToWorldSpace_Rotation.rotation"></a>

#### rotation

```python
@property
def rotation() -> Quat
```

deprecated: 'rotation' was renamed to 'value'.

<a id="unreal.RigUnit_ToWorldSpace_Rotation.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Quat) -> None
```

<a id="unreal.RigUnit_ToWorldSpace_Rotation.world"></a>

#### world

```python
@property
def world() -> Quat
```

(Quat):  [Read-Only] The result rotation in world space

<a id="unreal.RigUnit_ToRigSpace_Rotation"></a>