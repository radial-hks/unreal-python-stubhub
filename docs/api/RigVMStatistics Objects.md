## RigVMStatistics Objects

```python
class RigVMStatistics(StructBase)
```

Rig VMStatistics

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMStatistics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``byte_code`` (RigVMByteCodeStatistics):  [Read-Only]
- ``bytes_for_caching`` (int32):  [Read-Only]
- ``bytes_for_cdo`` (int32):  [Read-Only]
- ``bytes_per_instance`` (int32):  [Read-Only]
- ``debug_memory`` (RigVMMemoryStatistics):  [Read-Only]
- ``literal_memory`` (RigVMMemoryStatistics):  [Read-Only]
- ``work_memory`` (RigVMMemoryStatistics):  [Read-Only]

<a id="unreal.RigVMStatistics.__init__"></a>

#### __init__

```python
def __init__(bytes_for_cdo: int = 0,
             bytes_per_instance: int = 0,
             literal_memory: RigVMMemoryStatistics = [0, 0, 0],
             work_memory: RigVMMemoryStatistics = [0, 0, 0],
             debug_memory: RigVMMemoryStatistics = [0, 0, 0],
             bytes_for_caching: int = 0,
             byte_code: RigVMByteCodeStatistics = [0, 0]) -> None
```

<a id="unreal.RigVMStatistics.bytes_for_cdo"></a>

#### bytes_for_cdo

```python
@property
def bytes_for_cdo() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigVMStatistics.bytes_per_instance"></a>

#### bytes_per_instance

```python
@property
def bytes_per_instance() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigVMStatistics.literal_memory"></a>

#### literal_memory

```python
@property
def literal_memory() -> RigVMMemoryStatistics
```

(RigVMMemoryStatistics):  [Read-Only]

<a id="unreal.RigVMStatistics.work_memory"></a>

#### work_memory

```python
@property
def work_memory() -> RigVMMemoryStatistics
```

(RigVMMemoryStatistics):  [Read-Only]

<a id="unreal.RigVMStatistics.debug_memory"></a>

#### debug_memory

```python
@property
def debug_memory() -> RigVMMemoryStatistics
```

(RigVMMemoryStatistics):  [Read-Only]

<a id="unreal.RigVMStatistics.bytes_for_caching"></a>

#### bytes_for_caching

```python
@property
def bytes_for_caching() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigVMStatistics.byte_code"></a>

#### byte_code

```python
@property
def byte_code() -> RigVMByteCodeStatistics
```

(RigVMByteCodeStatistics):  [Read-Only]

<a id="unreal.RigVMVariantRef"></a>