## RigVMFunction_DeltaFromPreviousFloat Objects

```python
class RigVMFunction_DeltaFromPreviousFloat(RigVMFunction_SimBase)
```

Computes the difference from the previous value going through the node

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_DeltaFromPrevious.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``delta`` (float):  [Read-Write]
- ``previous_value`` (float):  [Read-Write]
- ``value`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_DeltaFromPreviousFloat.__init__"></a>

#### __init__

```python
def __init__(value: float = 0.000000,
             delta: float = 0.000000,
             previous_value: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_DeltaFromPreviousFloat.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_DeltaFromPreviousFloat.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.RigVMFunction_DeltaFromPreviousFloat.delta"></a>

#### delta

```python
@property
def delta() -> float
```

(float):  [Read-Only]

<a id="unreal.RigVMFunction_DeltaFromPreviousFloat.previous_value"></a>

#### previous_value

```python
@property
def previous_value() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_DeltaFromPreviousFloat"></a>