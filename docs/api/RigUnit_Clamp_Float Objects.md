## RigUnit_Clamp_Float Objects

```python
class RigUnit_Clamp_Float(RigUnit)
```

Two args and a result of float type

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Float.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``max`` (float):  [Read-Write]
- ``min`` (float):  [Read-Write]
- ``result`` (float):  [Read-Write]
- ``value`` (float):  [Read-Write]

<a id="unreal.RigUnit_Clamp_Float.__init__"></a>

#### __init__

```python
def __init__(value: float = 0.000000,
             min: float = 0.000000,
             max: float = 0.000000,
             result: float = 0.000000) -> None
```

<a id="unreal.RigUnit_Clamp_Float.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_Clamp_Float.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.RigUnit_Clamp_Float.min"></a>

#### min

```python
@property
def min() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_Clamp_Float.min"></a>

#### min

```python
@min.setter
def min(value: float) -> None
```

<a id="unreal.RigUnit_Clamp_Float.max"></a>

#### max

```python
@property
def max() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_Clamp_Float.max"></a>

#### max

```python
@max.setter
def max(value: float) -> None
```

<a id="unreal.RigUnit_Clamp_Float.result"></a>

#### result

```python
@property
def result() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_MapRange_Float"></a>