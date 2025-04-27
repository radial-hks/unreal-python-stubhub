## RigVMFunction_AccumulateQuatMul Objects

```python
class RigVMFunction_AccumulateQuatMul(RigVMFunction_AccumulateBase)
```

Multiplies a quaternion over time over and over again

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Accumulate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``flip_order`` (bool):  [Read-Write]
- ``initial_value`` (Quat):  [Read-Write]
- ``integrate_delta_time`` (bool):  [Read-Write]
- ``multiplier`` (Quat):  [Read-Write]
- ``result`` (Quat):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateQuatMul.__init__"></a>

#### __init__

```python
def __init__(multiplier: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             initial_value: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             flip_order: bool = False,
             integrate_delta_time: bool = False,
             result: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.RigVMFunction_AccumulateQuatMul.multiplier"></a>

#### multiplier

```python
@property
def multiplier() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateQuatMul.multiplier"></a>

#### multiplier

```python
@multiplier.setter
def multiplier(value: Quat) -> None
```

<a id="unreal.RigVMFunction_AccumulateQuatMul.initial_value"></a>

#### initial_value

```python
@property
def initial_value() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateQuatMul.initial_value"></a>

#### initial_value

```python
@initial_value.setter
def initial_value(value: Quat) -> None
```

<a id="unreal.RigVMFunction_AccumulateQuatMul.flip_order"></a>

#### flip_order

```python
@property
def flip_order() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateQuatMul.flip_order"></a>

#### flip_order

```python
@flip_order.setter
def flip_order(value: bool) -> None
```

<a id="unreal.RigVMFunction_AccumulateQuatMul.integrate_delta_time"></a>

#### integrate_delta_time

```python
@property
def integrate_delta_time() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateQuatMul.integrate_delta_time"></a>

#### integrate_delta_time

```python
@integrate_delta_time.setter
def integrate_delta_time(value: bool) -> None
```

<a id="unreal.RigVMFunction_AccumulateQuatMul.result"></a>

#### result

```python
@property
def result() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigUnit_AccumulateQuatMul"></a>