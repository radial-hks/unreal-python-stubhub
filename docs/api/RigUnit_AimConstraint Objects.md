## RigUnit_AimConstraint Objects

```python
class RigUnit_AimConstraint(RigUnitMutable)
```

Rig Unit Aim Constraint

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_AimConstraint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aim_mode`` (AimMode):  [Read-Write] # How to perform an aim
- ``aim_targets`` (Array[AimTarget]):  [Read-Write]
- ``aim_vector`` (Vector):  [Read-Write] # Vector in the space of Named joint which will be aligned to the aim target
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``joint`` (Name):  [Read-Write]
- ``up_mode`` (AimMode):  [Read-Write] # How to perform an upvector stabilization
- ``up_targets`` (Array[AimTarget]):  [Read-Write]
- ``up_vector`` (Vector):  [Read-Write] # Vector in the space of Named joint which will be aligned to the up target for stabilization

<a id="unreal.RigUnit_AimConstraint.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             joint: Name = "None",
             aim_mode: AimMode = AimMode.AIM_AT_TARGET,
             up_mode: AimMode = AimMode.AIM_AT_TARGET,
             aim_vector: Vector = [0.000000, 0.000000, 0.000000],
             up_vector: Vector = [0.000000, 0.000000, 0.000000],
             aim_targets: Array[AimTarget] = [],
             up_targets: Array[AimTarget] = []) -> None
```

<a id="unreal.RigUnit_AimConstraint.joint"></a>

#### joint

```python
@property
def joint() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigUnit_AimConstraint.joint"></a>

#### joint

```python
@joint.setter
def joint(value: Name) -> None
```

<a id="unreal.RigUnit_AimConstraint.aim_mode"></a>

#### aim_mode

```python
@property
def aim_mode() -> AimMode
```

(AimMode):  [Read-Write] # How to perform an aim

<a id="unreal.RigUnit_AimConstraint.aim_mode"></a>

#### aim_mode

```python
@aim_mode.setter
def aim_mode(value: AimMode) -> None
```

<a id="unreal.RigUnit_AimConstraint.up_mode"></a>

#### up_mode

```python
@property
def up_mode() -> AimMode
```

(AimMode):  [Read-Write] # How to perform an upvector stabilization

<a id="unreal.RigUnit_AimConstraint.up_mode"></a>

#### up_mode

```python
@up_mode.setter
def up_mode(value: AimMode) -> None
```

<a id="unreal.RigUnit_AimConstraint.aim_vector"></a>

#### aim_vector

```python
@property
def aim_vector() -> Vector
```

(Vector):  [Read-Write] # Vector in the space of Named joint which will be aligned to the aim target

<a id="unreal.RigUnit_AimConstraint.aim_vector"></a>

#### aim_vector

```python
@aim_vector.setter
def aim_vector(value: Vector) -> None
```

<a id="unreal.RigUnit_AimConstraint.up_vector"></a>

#### up_vector

```python
@property
def up_vector() -> Vector
```

(Vector):  [Read-Write] # Vector in the space of Named joint which will be aligned to the up target for stabilization

<a id="unreal.RigUnit_AimConstraint.up_vector"></a>

#### up_vector

```python
@up_vector.setter
def up_vector(value: Vector) -> None
```

<a id="unreal.RigUnit_AimConstraint.aim_targets"></a>

#### aim_targets

```python
@property
def aim_targets() -> Array[AimTarget]
```

(Array[AimTarget]):  [Read-Write]

<a id="unreal.RigUnit_AimConstraint.aim_targets"></a>

#### aim_targets

```python
@aim_targets.setter
def aim_targets(value: Array[AimTarget]) -> None
```

<a id="unreal.RigUnit_AimConstraint.up_targets"></a>

#### up_targets

```python
@property
def up_targets() -> Array[AimTarget]
```

(Array[AimTarget]):  [Read-Write]

<a id="unreal.RigUnit_AimConstraint.up_targets"></a>

#### up_targets

```python
@up_targets.setter
def up_targets(value: Array[AimTarget]) -> None
```

<a id="unreal.RigUnit_ApplyFK"></a>