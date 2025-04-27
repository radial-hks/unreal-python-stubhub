## RigVMByteCodeStatistics Objects

```python
class RigVMByteCodeStatistics(StructBase)
```

Rig VMByte Code Statistics

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMStatistics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``data_bytes`` (int32):  [Read-Only]
- ``instruction_count`` (int32):  [Read-Only]

<a id="unreal.RigVMByteCodeStatistics.__init__"></a>

#### __init__

```python
def __init__(instruction_count: int = 0, data_bytes: int = 0) -> None
```

<a id="unreal.RigVMByteCodeStatistics.instruction_count"></a>

#### instruction_count

```python
@property
def instruction_count() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigVMByteCodeStatistics.data_bytes"></a>

#### data_bytes

```python
@property
def data_bytes() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigVMStatistics"></a>