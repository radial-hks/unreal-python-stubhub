## RigUnit_GetControlVector Objects

```python
class RigUnit_GetControlVector(RigUnit)
```

GetControlVector is used to retrieve a single Vector from a hierarchy, can be used for Controls of type "Position" or "Scale".

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_GetControlTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control`` (Name):  [Read-Write] The name of the Control to retrieve the Vector for.
- ``maximum`` (Vector):  [Read-Write] The maximum value of the control.
- ``minimum`` (Vector):  [Read-Write] The minimum value of the control.
- ``space`` (RigVMTransformSpace):  [Read-Write] Defines if the Control's Vector should be retrieved
  in local or global space.
- ``vector`` (Vector):  [Read-Write] The current value of the control.

<a id="unreal.RigUnit_GetControlVector.__init__"></a>

#### __init__

```python
def __init__(control: Name = "None",
             space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE,
             vector: Vector = [0.000000, 0.000000, 0.000000],
             minimum: Vector = [0.000000, 0.000000, 0.000000],
             maximum: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigUnit_GetControlVector.control"></a>

#### control

```python
@property
def control() -> Name
```

(Name):  [Read-Write] The name of the Control to retrieve the Vector for.

<a id="unreal.RigUnit_GetControlVector.control"></a>

#### control

```python
@control.setter
def control(value: Name) -> None
```

<a id="unreal.RigUnit_GetControlVector.space"></a>

#### space

```python
@property
def space() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write] Defines if the Control's Vector should be retrieved
in local or global space.

<a id="unreal.RigUnit_GetControlVector.space"></a>

#### space

```python
@space.setter
def space(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_GetControlVector.vector"></a>

#### vector

```python
@property
def vector() -> Vector
```

(Vector):  [Read-Only] The current value of the control.

<a id="unreal.RigUnit_GetControlVector.minimum"></a>

#### minimum

```python
@property
def minimum() -> Vector
```

(Vector):  [Read-Only] The minimum value of the control.

<a id="unreal.RigUnit_GetControlVector.maximum"></a>

#### maximum

```python
@property
def maximum() -> Vector
```

(Vector):  [Read-Only] The maximum value of the control.

<a id="unreal.RigUnit_GetControlRotator"></a>