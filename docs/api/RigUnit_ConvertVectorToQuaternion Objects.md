## RigUnit_ConvertVectorToQuaternion Objects

```python
class RigUnit_ConvertVectorToQuaternion(RigUnit)
```

Rig Unit Convert Vector to Quaternion

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Converter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``input`` (Vector):  [Read-Write]
- ``result`` (Quat):  [Read-Write]

<a id="unreal.RigUnit_ConvertVectorToQuaternion.__init__"></a>

#### __init__

```python
def __init__(input: Vector = [0.000000, 0.000000, 0.000000],
             result: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.RigUnit_ConvertVectorToQuaternion.input"></a>

#### input

```python
@property
def input() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_ConvertVectorToQuaternion.input"></a>

#### input

```python
@input.setter
def input(value: Vector) -> None
```

<a id="unreal.RigUnit_ConvertVectorToQuaternion.result"></a>

#### result

```python
@property
def result() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigUnit_ConvertRotationToVector"></a>