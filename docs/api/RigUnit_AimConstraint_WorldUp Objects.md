## RigUnit_AimConstraint_WorldUp Objects

```python
class RigUnit_AimConstraint_WorldUp(StructBase)
```

Rig Unit Aim Constraint World Up

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_AimBone.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``kind`` (ControlRigVectorKind):  [Read-Write] The kind of target this is representing - can be a direction or a location
- ``space`` (RigElementKey):  [Read-Write] The space in which the target is expressed, use None to indicate world space
- ``target`` (Vector):  [Read-Write] The target to aim at - can be a direction or location based on the Kind setting

<a id="unreal.RigUnit_AimConstraint_WorldUp.__init__"></a>

#### __init__

```python
def __init__(target: Vector = [0.000000, 0.000000, 0.000000],
             kind: ControlRigVectorKind = ControlRigVectorKind.DIRECTION,
             space: RigElementKey = [RigElementType.NONE, "None"]) -> None
```

<a id="unreal.RigUnit_AimConstraint_WorldUp.target"></a>

#### target

```python
@property
def target() -> Vector
```

(Vector):  [Read-Write] The target to aim at - can be a direction or location based on the Kind setting

<a id="unreal.RigUnit_AimConstraint_WorldUp.target"></a>

#### target

```python
@target.setter
def target(value: Vector) -> None
```

<a id="unreal.RigUnit_AimConstraint_WorldUp.kind"></a>

#### kind

```python
@property
def kind() -> ControlRigVectorKind
```

(ControlRigVectorKind):  [Read-Write] The kind of target this is representing - can be a direction or a location

<a id="unreal.RigUnit_AimConstraint_WorldUp.kind"></a>

#### kind

```python
@kind.setter
def kind(value: ControlRigVectorKind) -> None
```

<a id="unreal.RigUnit_AimConstraint_WorldUp.space"></a>

#### space

```python
@property
def space() -> RigElementKey
```

(RigElementKey):  [Read-Write] The space in which the target is expressed, use None to indicate world space

<a id="unreal.RigUnit_AimConstraint_WorldUp.space"></a>

#### space

```python
@space.setter
def space(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_AimConstraint_AdvancedSettings"></a>