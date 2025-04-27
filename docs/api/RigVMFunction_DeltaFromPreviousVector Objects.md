## RigVMFunction_DeltaFromPreviousVector Objects

```python
class RigVMFunction_DeltaFromPreviousVector(RigVMFunction_SimBase)
```

Computes the difference from the previous value going through the node

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_DeltaFromPrevious.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``delta`` (Vector):  [Read-Write]
- ``previous_value`` (Vector):  [Read-Write]
- ``value`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_DeltaFromPreviousVector.__init__"></a>

#### __init__

```python
def __init__(value: Vector = [0.000000, 0.000000, 0.000000],
             delta: Vector = [0.000000, 0.000000, 0.000000],
             previous_value: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_DeltaFromPreviousVector.value"></a>

#### value

```python
@property
def value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_DeltaFromPreviousVector.value"></a>

#### value

```python
@value.setter
def value(value: Vector) -> None
```

<a id="unreal.RigVMFunction_DeltaFromPreviousVector.delta"></a>

#### delta

```python
@property
def delta() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_DeltaFromPreviousVector.previous_value"></a>

#### previous_value

```python
@property
def previous_value() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_DeltaFromPreviousVector"></a>