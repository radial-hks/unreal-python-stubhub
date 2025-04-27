## RigVMFunction_AccumulateVectorLerp Objects

```python
class RigVMFunction_AccumulateVectorLerp(RigVMFunction_AccumulateBase)
```

Interpolates two vectors over time over and over again

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Accumulate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend`` (float):  [Read-Write]
- ``initial_value`` (Vector):  [Read-Write]
- ``integrate_delta_time`` (bool):  [Read-Write]
- ``result`` (Vector):  [Read-Write]
- ``target_value`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateVectorLerp.__init__"></a>

#### __init__

```python
def __init__(target_value: Vector = [0.000000, 0.000000, 0.000000],
             initial_value: Vector = [0.000000, 0.000000, 0.000000],
             blend: float = 0.000000,
             integrate_delta_time: bool = False,
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_AccumulateVectorLerp.target_value"></a>

#### target_value

```python
@property
def target_value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateVectorLerp.target_value"></a>

#### target_value

```python
@target_value.setter
def target_value(value: Vector) -> None
```

<a id="unreal.RigVMFunction_AccumulateVectorLerp.initial_value"></a>

#### initial_value

```python
@property
def initial_value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateVectorLerp.initial_value"></a>

#### initial_value

```python
@initial_value.setter
def initial_value(value: Vector) -> None
```

<a id="unreal.RigVMFunction_AccumulateVectorLerp.blend"></a>

#### blend

```python
@property
def blend() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateVectorLerp.blend"></a>

#### blend

```python
@blend.setter
def blend(value: float) -> None
```

<a id="unreal.RigVMFunction_AccumulateVectorLerp.integrate_delta_time"></a>

#### integrate_delta_time

```python
@property
def integrate_delta_time() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateVectorLerp.integrate_delta_time"></a>

#### integrate_delta_time

```python
@integrate_delta_time.setter
def integrate_delta_time(value: bool) -> None
```

<a id="unreal.RigVMFunction_AccumulateVectorLerp.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_AccumulateVectorLerp"></a>