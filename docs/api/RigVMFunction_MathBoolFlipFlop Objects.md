## RigVMFunction_MathBoolFlipFlop Objects

```python
class RigVMFunction_MathBoolFlipFlop(RigVMFunction_MathBoolBase)
```

Returns true and false as a sequence.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathBool.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``duration`` (float):  [Read-Write] The duration in seconds at which the result won't change.
  Use 0 for a different result every time.
- ``result`` (bool):  [Read-Write]
- ``start_value`` (bool):  [Read-Write] The initial value to use for the flag

<a id="unreal.RigVMFunction_MathBoolFlipFlop.__init__"></a>

#### __init__

```python
def __init__(start_value: bool = False,
             duration: float = 0.000000,
             result: bool = False) -> None
```

<a id="unreal.RigVMFunction_MathBoolFlipFlop.start_value"></a>

#### start_value

```python
@property
def start_value() -> bool
```

(bool):  [Read-Write] The initial value to use for the flag

<a id="unreal.RigVMFunction_MathBoolFlipFlop.start_value"></a>

#### start_value

```python
@start_value.setter
def start_value(value: bool) -> None
```

<a id="unreal.RigVMFunction_MathBoolFlipFlop.duration"></a>

#### duration

```python
@property
def duration() -> float
```

(float):  [Read-Write] The duration in seconds at which the result won't change.
Use 0 for a different result every time.

<a id="unreal.RigVMFunction_MathBoolFlipFlop.duration"></a>

#### duration

```python
@duration.setter
def duration(value: float) -> None
```

<a id="unreal.RigVMFunction_MathBoolFlipFlop.result"></a>

#### result

```python
@property
def result() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigUnit_MathBoolFlipFlop"></a>