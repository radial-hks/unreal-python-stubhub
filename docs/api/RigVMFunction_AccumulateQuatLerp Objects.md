## RigVMFunction_AccumulateQuatLerp Objects

```python
class RigVMFunction_AccumulateQuatLerp(RigVMFunction_AccumulateBase)
```

Interpolates two quaternions over time over and over again

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Accumulate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend`` (float):  [Read-Write]
- ``initial_value`` (Quat):  [Read-Write]
- ``integrate_delta_time`` (bool):  [Read-Write]
- ``result`` (Quat):  [Read-Write]
- ``target_value`` (Quat):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateQuatLerp.__init__"></a>

#### __init__

```python
def __init__(target_value: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             initial_value: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             blend: float = 0.000000,
             integrate_delta_time: bool = False,
             result: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.RigVMFunction_AccumulateQuatLerp.target_value"></a>

#### target_value

```python
@property
def target_value() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateQuatLerp.target_value"></a>

#### target_value

```python
@target_value.setter
def target_value(value: Quat) -> None
```

<a id="unreal.RigVMFunction_AccumulateQuatLerp.initial_value"></a>

#### initial_value

```python
@property
def initial_value() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateQuatLerp.initial_value"></a>

#### initial_value

```python
@initial_value.setter
def initial_value(value: Quat) -> None
```

<a id="unreal.RigVMFunction_AccumulateQuatLerp.blend"></a>

#### blend

```python
@property
def blend() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateQuatLerp.blend"></a>

#### blend

```python
@blend.setter
def blend(value: float) -> None
```

<a id="unreal.RigVMFunction_AccumulateQuatLerp.integrate_delta_time"></a>

#### integrate_delta_time

```python
@property
def integrate_delta_time() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateQuatLerp.integrate_delta_time"></a>

#### integrate_delta_time

```python
@integrate_delta_time.setter
def integrate_delta_time(value: bool) -> None
```

<a id="unreal.RigVMFunction_AccumulateQuatLerp.result"></a>

#### result

```python
@property
def result() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigUnit_AccumulateQuatLerp"></a>