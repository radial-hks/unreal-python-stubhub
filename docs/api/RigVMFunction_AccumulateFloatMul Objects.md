## RigVMFunction_AccumulateFloatMul Objects

```python
class RigVMFunction_AccumulateFloatMul(RigVMFunction_AccumulateBase)
```

Multiplies a value over time over and over again

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Accumulate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``initial_value`` (float):  [Read-Write]
- ``integrate_delta_time`` (bool):  [Read-Write]
- ``multiplier`` (float):  [Read-Write]
- ``result`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateFloatMul.__init__"></a>

#### __init__

```python
def __init__(multiplier: float = 0.000000,
             initial_value: float = 0.000000,
             integrate_delta_time: bool = False,
             result: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_AccumulateFloatMul.multiplier"></a>

#### multiplier

```python
@property
def multiplier() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateFloatMul.multiplier"></a>

#### multiplier

```python
@multiplier.setter
def multiplier(value: float) -> None
```

<a id="unreal.RigVMFunction_AccumulateFloatMul.initial_value"></a>

#### initial_value

```python
@property
def initial_value() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateFloatMul.initial_value"></a>

#### initial_value

```python
@initial_value.setter
def initial_value(value: float) -> None
```

<a id="unreal.RigVMFunction_AccumulateFloatMul.integrate_delta_time"></a>

#### integrate_delta_time

```python
@property
def integrate_delta_time() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateFloatMul.integrate_delta_time"></a>

#### integrate_delta_time

```python
@integrate_delta_time.setter
def integrate_delta_time(value: bool) -> None
```

<a id="unreal.RigVMFunction_AccumulateFloatMul.result"></a>

#### result

```python
@property
def result() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_AccumulateFloatMul"></a>