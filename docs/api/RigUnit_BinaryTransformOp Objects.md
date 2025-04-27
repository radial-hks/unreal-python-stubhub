## RigUnit_BinaryTransformOp Objects

```python
class RigUnit_BinaryTransformOp(RigUnit)
```

Two args and a result of Transform type

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Transform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``argument0`` (Transform):  [Read-Write]
- ``argument1`` (Transform):  [Read-Write]
- ``result`` (Transform):  [Read-Write]

<a id="unreal.RigUnit_BinaryTransformOp.__init__"></a>

#### __init__

```python
def __init__(
    argument0: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]],
    argument1: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]],
    result: Transform = [[0.000000, 0.000000, 0.000000],
                         [-0.000000, 0.000000, 0.000000],
                         [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_BinaryTransformOp.argument0"></a>

#### argument0

```python
@property
def argument0() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigUnit_BinaryTransformOp.argument0"></a>

#### argument0

```python
@argument0.setter
def argument0(value: Transform) -> None
```

<a id="unreal.RigUnit_BinaryTransformOp.argument1"></a>

#### argument1

```python
@property
def argument1() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigUnit_BinaryTransformOp.argument1"></a>

#### argument1

```python
@argument1.setter
def argument1(value: Transform) -> None
```

<a id="unreal.RigUnit_BinaryTransformOp.result"></a>

#### result

```python
@property
def result() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigUnit_MultiplyTransform"></a>