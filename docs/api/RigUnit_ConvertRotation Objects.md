## RigUnit_ConvertRotation Objects

```python
class RigUnit_ConvertRotation(RigUnit)
```

Rig Unit Convert Rotation

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Converter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``input`` (Rotator):  [Read-Write]
- ``result`` (Quat):  [Read-Write]

<a id="unreal.RigUnit_ConvertRotation.__init__"></a>

#### __init__

```python
def __init__(input: Rotator = [0.000000, 0.000000, 0.000000],
             result: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.RigUnit_ConvertRotation.input"></a>

#### input

```python
@property
def input() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.RigUnit_ConvertRotation.input"></a>

#### input

```python
@input.setter
def input(value: Rotator) -> None
```

<a id="unreal.RigUnit_ConvertRotation.result"></a>

#### result

```python
@property
def result() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigUnit_ConvertVectorRotation"></a>