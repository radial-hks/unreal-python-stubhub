## RigVMFunction_KalmanVector Objects

```python
class RigVMFunction_KalmanVector(RigVMFunction_SimBase)
```

Averages a value over time.
This uses a Kalman Filter internally.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Kalman.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``buffer_size`` (int32):  [Read-Only]
- ``result`` (Vector):  [Read-Write]
- ``value`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_KalmanVector.__init__"></a>

#### __init__

```python
def __init__(value: Vector = [0.000000, 0.000000, 0.000000],
             buffer_size: int = 0,
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_KalmanVector.value"></a>

#### value

```python
@property
def value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_KalmanVector.value"></a>

#### value

```python
@value.setter
def value(value: Vector) -> None
```

<a id="unreal.RigVMFunction_KalmanVector.buffer_size"></a>

#### buffer_size

```python
@property
def buffer_size() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigVMFunction_KalmanVector.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_KalmanVector"></a>