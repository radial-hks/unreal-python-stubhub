## RigUnit_ConvertVectorToRotation Objects

```python
class RigUnit_ConvertVectorToRotation(RigUnit)
```

Rig Unit Convert Vector to Rotation

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Converter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``input`` (Vector):  [Read-Write]
- ``result`` (Rotator):  [Read-Write]

<a id="unreal.RigUnit_ConvertVectorToRotation.__init__"></a>

#### __init__

```python
def __init__(input: Vector = [0.000000, 0.000000, 0.000000],
             result: Rotator = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigUnit_ConvertVectorToRotation.input"></a>

#### input

```python
@property
def input() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_ConvertVectorToRotation.input"></a>

#### input

```python
@input.setter
def input(value: Vector) -> None
```

<a id="unreal.RigUnit_ConvertVectorToRotation.result"></a>

#### result

```python
@property
def result() -> Rotator
```

(Rotator):  [Read-Only]

<a id="unreal.RigUnit_ConvertVectorToQuaternion"></a>