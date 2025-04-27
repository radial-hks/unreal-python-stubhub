## RigVMFunction_AccumulateFloatLerp Objects

```python
class RigVMFunction_AccumulateFloatLerp(RigVMFunction_AccumulateBase)
```

Interpolates two values over time over and over again

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Accumulate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend`` (float):  [Read-Write]
- ``initial_value`` (float):  [Read-Write]
- ``integrate_delta_time`` (bool):  [Read-Write]
- ``result`` (float):  [Read-Write]
- ``target_value`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateFloatLerp.__init__"></a>

#### __init__

```python
def __init__(target_value: float = 0.000000,
             initial_value: float = 0.000000,
             blend: float = 0.000000,
             integrate_delta_time: bool = False,
             result: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_AccumulateFloatLerp.target_value"></a>

#### target_value

```python
@property
def target_value() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateFloatLerp.target_value"></a>

#### target_value

```python
@target_value.setter
def target_value(value: float) -> None
```

<a id="unreal.RigVMFunction_AccumulateFloatLerp.initial_value"></a>

#### initial_value

```python
@property
def initial_value() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateFloatLerp.initial_value"></a>

#### initial_value

```python
@initial_value.setter
def initial_value(value: float) -> None
```

<a id="unreal.RigVMFunction_AccumulateFloatLerp.blend"></a>

#### blend

```python
@property
def blend() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateFloatLerp.blend"></a>

#### blend

```python
@blend.setter
def blend(value: float) -> None
```

<a id="unreal.RigVMFunction_AccumulateFloatLerp.integrate_delta_time"></a>

#### integrate_delta_time

```python
@property
def integrate_delta_time() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateFloatLerp.integrate_delta_time"></a>

#### integrate_delta_time

```python
@integrate_delta_time.setter
def integrate_delta_time(value: bool) -> None
```

<a id="unreal.RigVMFunction_AccumulateFloatLerp.result"></a>

#### result

```python
@property
def result() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_AccumulateFloatLerp"></a>