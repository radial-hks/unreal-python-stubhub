## RigUnit_ConvertRotationToVector Objects

```python
class RigUnit_ConvertRotationToVector(RigUnit)
```

Rig Unit Convert Rotation to Vector

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Converter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``input`` (Rotator):  [Read-Write]
- ``result`` (Vector):  [Read-Write]

<a id="unreal.RigUnit_ConvertRotationToVector.__init__"></a>

#### __init__

```python
def __init__(input: Rotator = [0.000000, 0.000000, 0.000000],
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigUnit_ConvertRotationToVector.input"></a>

#### input

```python
@property
def input() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.RigUnit_ConvertRotationToVector.input"></a>

#### input

```python
@input.setter
def input(value: Rotator) -> None
```

<a id="unreal.RigUnit_ConvertRotationToVector.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_ConvertQuaternionToVector"></a>