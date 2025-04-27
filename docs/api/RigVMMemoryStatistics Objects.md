## RigVMMemoryStatistics Objects

```python
class RigVMMemoryStatistics(StructBase)
```

Rig VMMemory Statistics

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMStatistics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``data_bytes`` (int32):  [Read-Only]
- ``register_count`` (int32):  [Read-Only]
- ``total_bytes`` (int32):  [Read-Only]

<a id="unreal.RigVMMemoryStatistics.__init__"></a>

#### __init__

```python
def __init__(register_count: int = 0,
             data_bytes: int = 0,
             total_bytes: int = 0) -> None
```

<a id="unreal.RigVMMemoryStatistics.register_count"></a>

#### register_count

```python
@property
def register_count() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigVMMemoryStatistics.data_bytes"></a>

#### data_bytes

```python
@property
def data_bytes() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigVMMemoryStatistics.total_bytes"></a>

#### total_bytes

```python
@property
def total_bytes() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigVMByteCodeStatistics"></a>