## InputClampConstants Objects

```python
class InputClampConstants(StructBase)
```

Input modifier with clamping and interpolation

**C++ Source:**

- **Module**: Engine
- **File**: InputScaleBias.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``clamp_max`` (float):  [Read-Write]
- ``clamp_min`` (float):  [Read-Write]
- ``clamp_result`` (bool):  [Read-Write]
- ``interp_result`` (bool):  [Read-Write]
- ``interp_speed_decreasing`` (float):  [Read-Write]
- ``interp_speed_increasing`` (float):  [Read-Write]

<a id="unreal.InputClampConstants.__init__"></a>

#### __init__

```python
def __init__(clamp_result: bool = False,
             interp_result: bool = False,
             clamp_min: float = 0.000000,
             clamp_max: float = 0.000000,
             interp_speed_increasing: float = 0.000000,
             interp_speed_decreasing: float = 0.000000) -> None
```

<a id="unreal.InputClampConstants.clamp_result"></a>

#### clamp_result

```python
@property
def clamp_result() -> bool
```

(bool):  [Read-Write]

<a id="unreal.InputClampConstants.clamp_result"></a>

#### clamp_result

```python
@clamp_result.setter
def clamp_result(value: bool) -> None
```

<a id="unreal.InputClampConstants.interp_result"></a>

#### interp_result

```python
@property
def interp_result() -> bool
```

(bool):  [Read-Write]

<a id="unreal.InputClampConstants.interp_result"></a>

#### interp_result

```python
@interp_result.setter
def interp_result(value: bool) -> None
```

<a id="unreal.InputClampConstants.clamp_min"></a>

#### clamp_min

```python
@property
def clamp_min() -> float
```

(float):  [Read-Write]

<a id="unreal.InputClampConstants.clamp_min"></a>

#### clamp_min

```python
@clamp_min.setter
def clamp_min(value: float) -> None
```

<a id="unreal.InputClampConstants.clamp_max"></a>

#### clamp_max

```python
@property
def clamp_max() -> float
```

(float):  [Read-Write]

<a id="unreal.InputClampConstants.clamp_max"></a>

#### clamp_max

```python
@clamp_max.setter
def clamp_max(value: float) -> None
```

<a id="unreal.InputClampConstants.interp_speed_increasing"></a>

#### interp_speed_increasing

```python
@property
def interp_speed_increasing() -> float
```

(float):  [Read-Write]

<a id="unreal.InputClampConstants.interp_speed_increasing"></a>

#### interp_speed_increasing

```python
@interp_speed_increasing.setter
def interp_speed_increasing(value: float) -> None
```

<a id="unreal.InputClampConstants.interp_speed_decreasing"></a>

#### interp_speed_decreasing

```python
@property
def interp_speed_decreasing() -> float
```

(float):  [Read-Write]

<a id="unreal.InputClampConstants.interp_speed_decreasing"></a>

#### interp_speed_decreasing

```python
@interp_speed_decreasing.setter
def interp_speed_decreasing(value: float) -> None
```

<a id="unreal.InputClampState"></a>