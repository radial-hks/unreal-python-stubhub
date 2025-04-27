## RigVMFunction_AlphaInterpVector Objects

```python
class RigVMFunction_AlphaInterpVector(RigVMFunction_SimBase)
```

Takes in a vector value and outputs an accumulated value with a customized scale and clamp

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_AlphaInterp.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bias`` (float):  [Read-Write]
- ``clamp_max`` (float):  [Read-Write]
- ``clamp_min`` (float):  [Read-Write]
- ``clamp_result`` (bool):  [Read-Only]
- ``interp_result`` (bool):  [Read-Only]
- ``interp_speed_decreasing`` (float):  [Read-Write]
- ``interp_speed_increasing`` (float):  [Read-Write]
- ``map_range`` (bool):  [Read-Only]
- ``out_range`` (InputRange):  [Read-Write]
- ``range`` (InputRange):  [Read-Write]
- ``result`` (Vector):  [Read-Write]
- ``scale`` (float):  [Read-Write]
- ``value`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_AlphaInterpVector.__init__"></a>

#### __init__

```python
def __init__(value: Vector = [0.000000, 0.000000, 0.000000],
             scale: float = 0.000000,
             bias: float = 0.000000,
             map_range: bool = False,
             range: InputRange = [0.000000, 1.000000],
             out_range: InputRange = [0.000000, 1.000000],
             clamp_result: bool = False,
             clamp_min: float = 0.000000,
             clamp_max: float = 0.000000,
             interp_result: bool = False,
             interp_speed_increasing: float = 0.000000,
             interp_speed_decreasing: float = 0.000000,
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_AlphaInterpVector.value"></a>

#### value

```python
@property
def value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_AlphaInterpVector.value"></a>

#### value

```python
@value.setter
def value(value: Vector) -> None
```

<a id="unreal.RigVMFunction_AlphaInterpVector.scale"></a>

#### scale

```python
@property
def scale() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_AlphaInterpVector.scale"></a>

#### scale

```python
@scale.setter
def scale(value: float) -> None
```

<a id="unreal.RigVMFunction_AlphaInterpVector.bias"></a>

#### bias

```python
@property
def bias() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_AlphaInterpVector.bias"></a>

#### bias

```python
@bias.setter
def bias(value: float) -> None
```

<a id="unreal.RigVMFunction_AlphaInterpVector.map_range"></a>

#### map_range

```python
@property
def map_range() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigVMFunction_AlphaInterpVector.range"></a>

#### range

```python
@property
def range() -> InputRange
```

(InputRange):  [Read-Write]

<a id="unreal.RigVMFunction_AlphaInterpVector.range"></a>

#### range

```python
@range.setter
def range(value: InputRange) -> None
```

<a id="unreal.RigVMFunction_AlphaInterpVector.out_range"></a>

#### out_range

```python
@property
def out_range() -> InputRange
```

(InputRange):  [Read-Write]

<a id="unreal.RigVMFunction_AlphaInterpVector.out_range"></a>

#### out_range

```python
@out_range.setter
def out_range(value: InputRange) -> None
```

<a id="unreal.RigVMFunction_AlphaInterpVector.clamp_result"></a>

#### clamp_result

```python
@property
def clamp_result() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigVMFunction_AlphaInterpVector.clamp_min"></a>

#### clamp_min

```python
@property
def clamp_min() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_AlphaInterpVector.clamp_min"></a>

#### clamp_min

```python
@clamp_min.setter
def clamp_min(value: float) -> None
```

<a id="unreal.RigVMFunction_AlphaInterpVector.clamp_max"></a>

#### clamp_max

```python
@property
def clamp_max() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_AlphaInterpVector.clamp_max"></a>

#### clamp_max

```python
@clamp_max.setter
def clamp_max(value: float) -> None
```

<a id="unreal.RigVMFunction_AlphaInterpVector.interp_result"></a>

#### interp_result

```python
@property
def interp_result() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigVMFunction_AlphaInterpVector.interp_speed_increasing"></a>

#### interp_speed_increasing

```python
@property
def interp_speed_increasing() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_AlphaInterpVector.interp_speed_increasing"></a>

#### interp_speed_increasing

```python
@interp_speed_increasing.setter
def interp_speed_increasing(value: float) -> None
```

<a id="unreal.RigVMFunction_AlphaInterpVector.interp_speed_decreasing"></a>

#### interp_speed_decreasing

```python
@property
def interp_speed_decreasing() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_AlphaInterpVector.interp_speed_decreasing"></a>

#### interp_speed_decreasing

```python
@interp_speed_decreasing.setter
def interp_speed_decreasing(value: float) -> None
```

<a id="unreal.RigVMFunction_AlphaInterpVector.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_AlphaInterpVector"></a>