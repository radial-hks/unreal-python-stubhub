## RigUnit_ConvertQuaternion Objects

```python
class RigUnit_ConvertQuaternion(RigUnit)
```

Rig Unit Convert Quaternion

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Converter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``input`` (Quat):  [Read-Write]
- ``result`` (Rotator):  [Read-Write]

<a id="unreal.RigUnit_ConvertQuaternion.__init__"></a>

#### __init__

```python
def __init__(input: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             result: Rotator = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigUnit_ConvertQuaternion.input"></a>

#### input

```python
@property
def input() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigUnit_ConvertQuaternion.input"></a>

#### input

```python
@input.setter
def input(value: Quat) -> None
```

<a id="unreal.RigUnit_ConvertQuaternion.result"></a>

#### result

```python
@property
def result() -> Rotator
```

(Rotator):  [Read-Only]

<a id="unreal.RigUnit_ConvertVectorToRotation"></a>