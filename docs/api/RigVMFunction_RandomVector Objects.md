## RigVMFunction_RandomVector Objects

```python
class RigVMFunction_RandomVector(RigVMFunction_MathBase)
```

Generates a random vector between a min and a max

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Random.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``duration`` (float):  [Read-Write] The duration at which the number won't change.
  Use 0 for a different number every time.
  A negative number (for ex: -1) results in an infinite duration.
- ``maximum`` (float):  [Read-Write]
- ``minimum`` (float):  [Read-Write]
- ``result`` (Vector):  [Read-Write]
- ``seed`` (int32):  [Read-Write]

<a id="unreal.RigVMFunction_RandomVector.__init__"></a>

#### __init__

```python
def __init__(seed: int = 0,
             minimum: float = 0.000000,
             maximum: float = 0.000000,
             duration: float = 0.000000,
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_RandomVector.seed"></a>

#### seed

```python
@property
def seed() -> int
```

(int32):  [Read-Write]

<a id="unreal.RigVMFunction_RandomVector.seed"></a>

#### seed

```python
@seed.setter
def seed(value: int) -> None
```

<a id="unreal.RigVMFunction_RandomVector.minimum"></a>

#### minimum

```python
@property
def minimum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_RandomVector.minimum"></a>

#### minimum

```python
@minimum.setter
def minimum(value: float) -> None
```

<a id="unreal.RigVMFunction_RandomVector.maximum"></a>

#### maximum

```python
@property
def maximum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_RandomVector.maximum"></a>

#### maximum

```python
@maximum.setter
def maximum(value: float) -> None
```

<a id="unreal.RigVMFunction_RandomVector.duration"></a>

#### duration

```python
@property
def duration() -> float
```

(float):  [Read-Write] The duration at which the number won't change.
Use 0 for a different number every time.
A negative number (for ex: -1) results in an infinite duration.

<a id="unreal.RigVMFunction_RandomVector.duration"></a>

#### duration

```python
@duration.setter
def duration(value: float) -> None
```

<a id="unreal.RigVMFunction_RandomVector.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_RandomVector"></a>