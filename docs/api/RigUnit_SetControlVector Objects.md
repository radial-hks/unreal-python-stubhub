## RigUnit_SetControlVector Objects

```python
class RigUnit_SetControlVector(RigUnitMutable)
```

SetControlVector is used to perform a change in the hierarchy by setting a single control's Vector value.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetControlTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control`` (Name):  [Read-Write] The name of the Control to set the transform for.
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``space`` (RigVMTransformSpace):  [Read-Write] Defines if the bone's transform should be set
  in local or global space.
- ``vector`` (Vector):  [Read-Write] The transform value to set for the given Control.
- ``weight`` (float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_SetControlVector.__init__"></a>

#### __init__

```python
def __init__(
        execute_context: ControlRigExecuteContext = [],
        control: Name = "None",
        weight: float = 0.000000,
        vector: Vector = [0.000000, 0.000000, 0.000000],
        space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE) -> None
```

<a id="unreal.RigUnit_SetControlVector.control"></a>

#### control

```python
@property
def control() -> Name
```

(Name):  [Read-Write] The name of the Control to set the transform for.

<a id="unreal.RigUnit_SetControlVector.control"></a>

#### control

```python
@control.setter
def control(value: Name) -> None
```

<a id="unreal.RigUnit_SetControlVector.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_SetControlVector.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_SetControlVector.vector"></a>

#### vector

```python
@property
def vector() -> Vector
```

(Vector):  [Read-Write] The transform value to set for the given Control.

<a id="unreal.RigUnit_SetControlVector.vector"></a>

#### vector

```python
@vector.setter
def vector(value: Vector) -> None
```

<a id="unreal.RigUnit_SetControlVector.space"></a>

#### space

```python
@property
def space() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write] Defines if the bone's transform should be set
in local or global space.

<a id="unreal.RigUnit_SetControlVector.space"></a>

#### space

```python
@space.setter
def space(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_SetControlRotator"></a>