## RigUnit_ConvertTransform Objects

```python
class RigUnit_ConvertTransform(RigUnit)
```

Rig Unit Convert Transform

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Converter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``input`` (Transform):  [Read-Write]
- ``result`` (EulerTransform):  [Read-Write]

<a id="unreal.RigUnit_ConvertTransform.__init__"></a>

#### __init__

```python
def __init__(
    input: Transform = [[0.000000, 0.000000, 0.000000],
                        [-0.000000, 0.000000, 0.000000],
                        [1.000000, 1.000000, 1.000000]],
    result: EulerTransform = [[0.000000, 0.000000, 0.000000],
                              [0.000000, 0.000000, 0.000000],
                              [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_ConvertTransform.input"></a>

#### input

```python
@property
def input() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigUnit_ConvertTransform.input"></a>

#### input

```python
@input.setter
def input(value: Transform) -> None
```

<a id="unreal.RigUnit_ConvertTransform.result"></a>

#### result

```python
@property
def result() -> EulerTransform
```

(EulerTransform):  [Read-Only]

<a id="unreal.RigUnit_ConvertEulerTransform"></a>