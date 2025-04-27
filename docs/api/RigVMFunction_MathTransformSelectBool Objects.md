## RigVMFunction_MathTransformSelectBool Objects

```python
class RigVMFunction_MathTransformSelectBool(RigVMFunction_MathTransformBase)
```

Return one of the two values based on the condition

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``condition`` (bool):  [Read-Write]
- ``if_false`` (Transform):  [Read-Write]
- ``if_true`` (Transform):  [Read-Write]
- ``result`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformSelectBool.__init__"></a>

#### __init__

```python
def __init__(
    condition: bool = False,
    if_true: Transform = [[0.000000, 0.000000, 0.000000],
                          [-0.000000, 0.000000, 0.000000],
                          [1.000000, 1.000000, 1.000000]],
    if_false: Transform = [[0.000000, 0.000000, 0.000000],
                           [-0.000000, 0.000000, 0.000000],
                           [1.000000, 1.000000, 1.000000]],
    result: Transform = [[0.000000, 0.000000, 0.000000],
                         [-0.000000, 0.000000, 0.000000],
                         [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigVMFunction_MathTransformSelectBool.condition"></a>

#### condition

```python
@property
def condition() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformSelectBool.condition"></a>

#### condition

```python
@condition.setter
def condition(value: bool) -> None
```

<a id="unreal.RigVMFunction_MathTransformSelectBool.if_true"></a>

#### if_true

```python
@property
def if_true() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformSelectBool.if_true"></a>

#### if_true

```python
@if_true.setter
def if_true(value: Transform) -> None
```

<a id="unreal.RigVMFunction_MathTransformSelectBool.if_false"></a>

#### if_false

```python
@property
def if_false() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformSelectBool.if_false"></a>

#### if_false

```python
@if_false.setter
def if_false(value: Transform) -> None
```

<a id="unreal.RigVMFunction_MathTransformSelectBool.result"></a>

#### result

```python
@property
def result() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigUnit_MathTransformSelectBool"></a>