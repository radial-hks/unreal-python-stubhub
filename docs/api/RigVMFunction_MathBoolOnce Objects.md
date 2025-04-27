## RigVMFunction_MathBoolOnce Objects

```python
class RigVMFunction_MathBoolOnce(RigVMFunction_MathBoolBase)
```

Returns true once the first time this node is hit

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathBool.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``duration`` (float):  [Read-Write] The duration in seconds at which the result is true
  Use 0 for a different result every time.
- ``result`` (bool):  [Read-Write]

<a id="unreal.RigVMFunction_MathBoolOnce.__init__"></a>

#### __init__

```python
def __init__(duration: float = 0.000000, result: bool = False) -> None
```

<a id="unreal.RigVMFunction_MathBoolOnce.duration"></a>

#### duration

```python
@property
def duration() -> float
```

(float):  [Read-Write] The duration in seconds at which the result is true
Use 0 for a different result every time.

<a id="unreal.RigVMFunction_MathBoolOnce.duration"></a>

#### duration

```python
@duration.setter
def duration(value: float) -> None
```

<a id="unreal.RigVMFunction_MathBoolOnce.result"></a>

#### result

```python
@property
def result() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigUnit_MathBoolOnce"></a>