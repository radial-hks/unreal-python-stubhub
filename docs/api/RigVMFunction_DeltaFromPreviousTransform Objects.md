## RigVMFunction_DeltaFromPreviousTransform Objects

```python
class RigVMFunction_DeltaFromPreviousTransform(RigVMFunction_SimBase)
```

Computes the difference from the previous value going through the node

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_DeltaFromPrevious.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``delta`` (Transform):  [Read-Write]
- ``previous_value`` (Transform):  [Read-Write]
- ``value`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_DeltaFromPreviousTransform.__init__"></a>

#### __init__

```python
def __init__(
    value: Transform = [[0.000000, 0.000000, 0.000000],
                        [-0.000000, 0.000000, 0.000000],
                        [1.000000, 1.000000, 1.000000]],
    delta: Transform = [[0.000000, 0.000000, 0.000000],
                        [-0.000000, 0.000000, 0.000000],
                        [1.000000, 1.000000, 1.000000]],
    previous_value: Transform = [[0.000000, 0.000000, 0.000000],
                                 [-0.000000, 0.000000, 0.000000],
                                 [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigVMFunction_DeltaFromPreviousTransform.value"></a>

#### value

```python
@property
def value() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_DeltaFromPreviousTransform.value"></a>

#### value

```python
@value.setter
def value(value: Transform) -> None
```

<a id="unreal.RigVMFunction_DeltaFromPreviousTransform.delta"></a>

#### delta

```python
@property
def delta() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigVMFunction_DeltaFromPreviousTransform.previous_value"></a>

#### previous_value

```python
@property
def previous_value() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigUnit_DeltaFromPreviousTransform"></a>