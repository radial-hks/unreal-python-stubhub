## RigVMFunction_DeltaFromPreviousQuat Objects

```python
class RigVMFunction_DeltaFromPreviousQuat(RigVMFunction_SimBase)
```

Computes the difference from the previous value going through the node

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_DeltaFromPrevious.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``delta`` (Quat):  [Read-Write]
- ``previous_value`` (Quat):  [Read-Write]
- ``value`` (Quat):  [Read-Write]

<a id="unreal.RigVMFunction_DeltaFromPreviousQuat.__init__"></a>

#### __init__

```python
def __init__(
        value: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
        delta: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
        previous_value: Quat = [0.000000, 0.000000, 0.000000,
                                1.000000]) -> None
```

<a id="unreal.RigVMFunction_DeltaFromPreviousQuat.value"></a>

#### value

```python
@property
def value() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_DeltaFromPreviousQuat.value"></a>

#### value

```python
@value.setter
def value(value: Quat) -> None
```

<a id="unreal.RigVMFunction_DeltaFromPreviousQuat.delta"></a>

#### delta

```python
@property
def delta() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigVMFunction_DeltaFromPreviousQuat.previous_value"></a>

#### previous_value

```python
@property
def previous_value() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigUnit_DeltaFromPreviousQuat"></a>