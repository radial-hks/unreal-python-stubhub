## RigVMFunction_AccumulateTransformLerp Objects

```python
class RigVMFunction_AccumulateTransformLerp(RigVMFunction_AccumulateBase)
```

Interpolates two transforms over time over and over again

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Accumulate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend`` (float):  [Read-Write]
- ``initial_value`` (Transform):  [Read-Write]
- ``integrate_delta_time`` (bool):  [Read-Write]
- ``result`` (Transform):  [Read-Write]
- ``target_value`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateTransformLerp.__init__"></a>

#### __init__

```python
def __init__(
    target_value: Transform = [[0.000000, 0.000000, 0.000000],
                               [-0.000000, 0.000000, 0.000000],
                               [1.000000, 1.000000, 1.000000]],
    initial_value: Transform = [[0.000000, 0.000000, 0.000000],
                                [-0.000000, 0.000000, 0.000000],
                                [1.000000, 1.000000, 1.000000]],
    blend: float = 0.000000,
    integrate_delta_time: bool = False,
    result: Transform = [[0.000000, 0.000000, 0.000000],
                         [-0.000000, 0.000000, 0.000000],
                         [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigVMFunction_AccumulateTransformLerp.target_value"></a>

#### target_value

```python
@property
def target_value() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateTransformLerp.target_value"></a>

#### target_value

```python
@target_value.setter
def target_value(value: Transform) -> None
```

<a id="unreal.RigVMFunction_AccumulateTransformLerp.initial_value"></a>

#### initial_value

```python
@property
def initial_value() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateTransformLerp.initial_value"></a>

#### initial_value

```python
@initial_value.setter
def initial_value(value: Transform) -> None
```

<a id="unreal.RigVMFunction_AccumulateTransformLerp.blend"></a>

#### blend

```python
@property
def blend() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateTransformLerp.blend"></a>

#### blend

```python
@blend.setter
def blend(value: float) -> None
```

<a id="unreal.RigVMFunction_AccumulateTransformLerp.integrate_delta_time"></a>

#### integrate_delta_time

```python
@property
def integrate_delta_time() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateTransformLerp.integrate_delta_time"></a>

#### integrate_delta_time

```python
@integrate_delta_time.setter
def integrate_delta_time(value: bool) -> None
```

<a id="unreal.RigVMFunction_AccumulateTransformLerp.result"></a>

#### result

```python
@property
def result() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigUnit_AccumulateTransformLerp"></a>