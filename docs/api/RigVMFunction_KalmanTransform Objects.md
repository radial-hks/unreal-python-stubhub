## RigVMFunction_KalmanTransform Objects

```python
class RigVMFunction_KalmanTransform(RigVMFunction_SimBase)
```

Averages a transform over time.
This uses a Kalman Filter internally.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Kalman.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``buffer_size`` (int32):  [Read-Only]
- ``result`` (Transform):  [Read-Write]
- ``value`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_KalmanTransform.__init__"></a>

#### __init__

```python
def __init__(
    value: Transform = [[0.000000, 0.000000, 0.000000],
                        [-0.000000, 0.000000, 0.000000],
                        [1.000000, 1.000000, 1.000000]],
    buffer_size: int = 0,
    result: Transform = [[0.000000, 0.000000, 0.000000],
                         [-0.000000, 0.000000, 0.000000],
                         [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigVMFunction_KalmanTransform.value"></a>

#### value

```python
@property
def value() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_KalmanTransform.value"></a>

#### value

```python
@value.setter
def value(value: Transform) -> None
```

<a id="unreal.RigVMFunction_KalmanTransform.buffer_size"></a>

#### buffer_size

```python
@property
def buffer_size() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigVMFunction_KalmanTransform.result"></a>

#### result

```python
@property
def result() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigUnit_KalmanTransform"></a>