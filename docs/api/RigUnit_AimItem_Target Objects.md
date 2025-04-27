## RigUnit_AimItem_Target Objects

```python
class RigUnit_AimItem_Target(StructBase)
```

Rig Unit Aim Item Target

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_AimBone.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``axis`` (Vector):  [Read-Write] The axis to align with the aim on this target
- ``kind`` (ControlRigVectorKind):  [Read-Write] The kind of target this is representing - can be a direction or a location
- ``space`` (RigElementKey):  [Read-Write] The space in which the target is expressed
- ``target`` (Vector):  [Read-Write] The target to aim at - can be a direction or location based on the Kind setting
- ``weight`` (float):  [Read-Write] The amount of aim rotation to apply on this target.

<a id="unreal.RigUnit_AimItem_Target.__init__"></a>

#### __init__

```python
def __init__(weight: float = 0.000000,
             axis: Vector = [0.000000, 0.000000, 0.000000],
             target: Vector = [0.000000, 0.000000, 0.000000],
             kind: ControlRigVectorKind = ControlRigVectorKind.DIRECTION,
             space: RigElementKey = [RigElementType.NONE, "None"]) -> None
```

<a id="unreal.RigUnit_AimItem_Target.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] The amount of aim rotation to apply on this target.

<a id="unreal.RigUnit_AimItem_Target.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_AimItem_Target.axis"></a>

#### axis

```python
@property
def axis() -> Vector
```

(Vector):  [Read-Write] The axis to align with the aim on this target

<a id="unreal.RigUnit_AimItem_Target.axis"></a>

#### axis

```python
@axis.setter
def axis(value: Vector) -> None
```

<a id="unreal.RigUnit_AimItem_Target.target"></a>

#### target

```python
@property
def target() -> Vector
```

(Vector):  [Read-Write] The target to aim at - can be a direction or location based on the Kind setting

<a id="unreal.RigUnit_AimItem_Target.target"></a>

#### target

```python
@target.setter
def target(value: Vector) -> None
```

<a id="unreal.RigUnit_AimItem_Target.kind"></a>

#### kind

```python
@property
def kind() -> ControlRigVectorKind
```

(ControlRigVectorKind):  [Read-Write] The kind of target this is representing - can be a direction or a location

<a id="unreal.RigUnit_AimItem_Target.kind"></a>

#### kind

```python
@kind.setter
def kind(value: ControlRigVectorKind) -> None
```

<a id="unreal.RigUnit_AimItem_Target.space"></a>

#### space

```python
@property
def space() -> RigElementKey
```

(RigElementKey):  [Read-Write] The space in which the target is expressed

<a id="unreal.RigUnit_AimItem_Target.space"></a>

#### space

```python
@space.setter
def space(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_AimBone_DebugSettings"></a>