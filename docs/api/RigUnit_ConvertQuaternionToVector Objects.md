## RigUnit_ConvertQuaternionToVector Objects

```python
class RigUnit_ConvertQuaternionToVector(RigUnit)
```

Rig Unit Convert Quaternion to Vector

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Converter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``input`` (Quat):  [Read-Write]
- ``result`` (Vector):  [Read-Write]

<a id="unreal.RigUnit_ConvertQuaternionToVector.__init__"></a>

#### __init__

```python
def __init__(input: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigUnit_ConvertQuaternionToVector.input"></a>

#### input

```python
@property
def input() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigUnit_ConvertQuaternionToVector.input"></a>

#### input

```python
@input.setter
def input(value: Quat) -> None
```

<a id="unreal.RigUnit_ConvertQuaternionToVector.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_ToSwingAndTwist"></a>