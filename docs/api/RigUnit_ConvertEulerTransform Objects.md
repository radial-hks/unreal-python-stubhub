## RigUnit_ConvertEulerTransform Objects

```python
class RigUnit_ConvertEulerTransform(RigUnit)
```

Rig Unit Convert Euler Transform

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Converter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``input`` (EulerTransform):  [Read-Write]
- ``result`` (Transform):  [Read-Write]

<a id="unreal.RigUnit_ConvertEulerTransform.__init__"></a>

#### __init__

```python
def __init__(
    input: EulerTransform = [[0.000000, 0.000000, 0.000000],
                             [0.000000, 0.000000, 0.000000],
                             [1.000000, 1.000000, 1.000000]],
    result: Transform = [[0.000000, 0.000000, 0.000000],
                         [-0.000000, 0.000000, 0.000000],
                         [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_ConvertEulerTransform.input"></a>

#### input

```python
@property
def input() -> EulerTransform
```

(EulerTransform):  [Read-Write]

<a id="unreal.RigUnit_ConvertEulerTransform.input"></a>

#### input

```python
@input.setter
def input(value: EulerTransform) -> None
```

<a id="unreal.RigUnit_ConvertEulerTransform.result"></a>

#### result

```python
@property
def result() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigUnit_ConvertRotation"></a>