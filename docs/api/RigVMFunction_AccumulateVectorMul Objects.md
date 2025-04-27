## RigVMFunction_AccumulateVectorMul Objects

```python
class RigVMFunction_AccumulateVectorMul(RigVMFunction_AccumulateBase)
```

Multiplies a vector over time over and over again

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Accumulate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``initial_value`` (Vector):  [Read-Write]
- ``integrate_delta_time`` (bool):  [Read-Write]
- ``multiplier`` (Vector):  [Read-Write]
- ``result`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateVectorMul.__init__"></a>

#### __init__

```python
def __init__(multiplier: Vector = [0.000000, 0.000000, 0.000000],
             initial_value: Vector = [0.000000, 0.000000, 0.000000],
             integrate_delta_time: bool = False,
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_AccumulateVectorMul.multiplier"></a>

#### multiplier

```python
@property
def multiplier() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateVectorMul.multiplier"></a>

#### multiplier

```python
@multiplier.setter
def multiplier(value: Vector) -> None
```

<a id="unreal.RigVMFunction_AccumulateVectorMul.initial_value"></a>

#### initial_value

```python
@property
def initial_value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateVectorMul.initial_value"></a>

#### initial_value

```python
@initial_value.setter
def initial_value(value: Vector) -> None
```

<a id="unreal.RigVMFunction_AccumulateVectorMul.integrate_delta_time"></a>

#### integrate_delta_time

```python
@property
def integrate_delta_time() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateVectorMul.integrate_delta_time"></a>

#### integrate_delta_time

```python
@integrate_delta_time.setter
def integrate_delta_time(value: bool) -> None
```

<a id="unreal.RigVMFunction_AccumulateVectorMul.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_AccumulateVectorMul"></a>