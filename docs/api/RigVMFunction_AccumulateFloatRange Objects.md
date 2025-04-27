## RigVMFunction_AccumulateFloatRange Objects

```python
class RigVMFunction_AccumulateFloatRange(RigVMFunction_AccumulateBase)
```

Accumulates the min and max values over time

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Accumulate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``maximum`` (float):  [Read-Write]
- ``minimum`` (float):  [Read-Write]
- ``value`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateFloatRange.__init__"></a>

#### __init__

```python
def __init__(value: float = 0.000000,
             minimum: float = 0.000000,
             maximum: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_AccumulateFloatRange.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateFloatRange.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.RigVMFunction_AccumulateFloatRange.minimum"></a>

#### minimum

```python
@property
def minimum() -> float
```

(float):  [Read-Only]

<a id="unreal.RigVMFunction_AccumulateFloatRange.maximum"></a>

#### maximum

```python
@property
def maximum() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_AccumulateFloatRange"></a>