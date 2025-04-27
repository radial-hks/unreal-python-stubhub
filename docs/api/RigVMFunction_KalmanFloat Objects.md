## RigVMFunction_KalmanFloat Objects

```python
class RigVMFunction_KalmanFloat(RigVMFunction_SimBase)
```

Averages a value over time.
This uses a Kalman Filter internally.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Kalman.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``buffer_size`` (int32):  [Read-Only]
- ``result`` (float):  [Read-Write]
- ``value`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_KalmanFloat.__init__"></a>

#### __init__

```python
def __init__(value: float = 0.000000,
             buffer_size: int = 0,
             result: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_KalmanFloat.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_KalmanFloat.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.RigVMFunction_KalmanFloat.buffer_size"></a>

#### buffer_size

```python
@property
def buffer_size() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigVMFunction_KalmanFloat.result"></a>

#### result

```python
@property
def result() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_KalmanFloat"></a>