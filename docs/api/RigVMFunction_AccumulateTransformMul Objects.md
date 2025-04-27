## RigVMFunction_AccumulateTransformMul Objects

```python
class RigVMFunction_AccumulateTransformMul(RigVMFunction_AccumulateBase)
```

Multiplies a transform over time over and over again

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Accumulate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``flip_order`` (bool):  [Read-Write]
- ``initial_value`` (Transform):  [Read-Write]
- ``integrate_delta_time`` (bool):  [Read-Write]
- ``multiplier`` (Transform):  [Read-Write]
- ``result`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateTransformMul.__init__"></a>

#### __init__

```python
def __init__(
    multiplier: Transform = [[0.000000, 0.000000, 0.000000],
                             [-0.000000, 0.000000, 0.000000],
                             [1.000000, 1.000000, 1.000000]],
    initial_value: Transform = [[0.000000, 0.000000, 0.000000],
                                [-0.000000, 0.000000, 0.000000],
                                [1.000000, 1.000000, 1.000000]],
    flip_order: bool = False,
    integrate_delta_time: bool = False,
    result: Transform = [[0.000000, 0.000000, 0.000000],
                         [-0.000000, 0.000000, 0.000000],
                         [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigVMFunction_AccumulateTransformMul.multiplier"></a>

#### multiplier

```python
@property
def multiplier() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateTransformMul.multiplier"></a>

#### multiplier

```python
@multiplier.setter
def multiplier(value: Transform) -> None
```

<a id="unreal.RigVMFunction_AccumulateTransformMul.initial_value"></a>

#### initial_value

```python
@property
def initial_value() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateTransformMul.initial_value"></a>

#### initial_value

```python
@initial_value.setter
def initial_value(value: Transform) -> None
```

<a id="unreal.RigVMFunction_AccumulateTransformMul.flip_order"></a>

#### flip_order

```python
@property
def flip_order() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateTransformMul.flip_order"></a>

#### flip_order

```python
@flip_order.setter
def flip_order(value: bool) -> None
```

<a id="unreal.RigVMFunction_AccumulateTransformMul.integrate_delta_time"></a>

#### integrate_delta_time

```python
@property
def integrate_delta_time() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateTransformMul.integrate_delta_time"></a>

#### integrate_delta_time

```python
@integrate_delta_time.setter
def integrate_delta_time(value: bool) -> None
```

<a id="unreal.RigVMFunction_AccumulateTransformMul.result"></a>

#### result

```python
@property
def result() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigUnit_AccumulateTransformMul"></a>