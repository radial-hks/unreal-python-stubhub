## RigVMFunction_AccumulateVectorAdd Objects

```python
class RigVMFunction_AccumulateVectorAdd(RigVMFunction_AccumulateBase)
```

Adds a vector over time over and over again

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Accumulate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``increment`` (Vector):  [Read-Write]
- ``initial_value`` (Vector):  [Read-Write]
- ``integrate_delta_time`` (bool):  [Read-Write]
- ``result`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateVectorAdd.__init__"></a>

#### __init__

```python
def __init__(increment: Vector = [0.000000, 0.000000, 0.000000],
             initial_value: Vector = [0.000000, 0.000000, 0.000000],
             integrate_delta_time: bool = False,
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_AccumulateVectorAdd.increment"></a>

#### increment

```python
@property
def increment() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateVectorAdd.increment"></a>

#### increment

```python
@increment.setter
def increment(value: Vector) -> None
```

<a id="unreal.RigVMFunction_AccumulateVectorAdd.initial_value"></a>

#### initial_value

```python
@property
def initial_value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateVectorAdd.initial_value"></a>

#### initial_value

```python
@initial_value.setter
def initial_value(value: Vector) -> None
```

<a id="unreal.RigVMFunction_AccumulateVectorAdd.integrate_delta_time"></a>

#### integrate_delta_time

```python
@property
def integrate_delta_time() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateVectorAdd.integrate_delta_time"></a>

#### integrate_delta_time

```python
@integrate_delta_time.setter
def integrate_delta_time(value: bool) -> None
```

<a id="unreal.RigVMFunction_AccumulateVectorAdd.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_AccumulateVectorAdd"></a>