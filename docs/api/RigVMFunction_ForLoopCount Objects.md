## RigVMFunction_ForLoopCount Objects

```python
class RigVMFunction_ForLoopCount(RigVMStructMutable)
```

Given a count, execute iteratively until the count is up

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_ForLoop.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``completed`` (RigVMExecuteContext):  [Read-Write]
- ``count`` (int32):  [Read-Write]
- ``execute_context`` (RigVMExecuteContext):  [Read-Write] * This property is used to chain multiple mutable nodes together
- ``index`` (int32):  [Read-Write]
- ``ratio`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_ForLoopCount.__init__"></a>

#### __init__

```python
def __init__(execute_context: RigVMExecuteContext = [],
             count: int = 0,
             index: int = 0,
             ratio: float = 0.000000,
             completed: RigVMExecuteContext = []) -> None
```

<a id="unreal.RigVMFunction_ForLoopCount.count"></a>

#### count

```python
@property
def count() -> int
```

(int32):  [Read-Write]

<a id="unreal.RigVMFunction_ForLoopCount.count"></a>

#### count

```python
@count.setter
def count(value: int) -> None
```

<a id="unreal.RigVMFunction_ForLoopCount.index"></a>

#### index

```python
@property
def index() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigVMFunction_ForLoopCount.ratio"></a>

#### ratio

```python
@property
def ratio() -> float
```

(float):  [Read-Only]

<a id="unreal.RigVMFunction_ForLoopCount.completed"></a>

#### completed

```python
@property
def completed() -> RigVMExecuteContext
```

(RigVMExecuteContext):  [Read-Only]

<a id="unreal.RigUnit_ForLoopCount"></a>