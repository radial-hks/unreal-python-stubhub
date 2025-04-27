## RigVMExtendedExecuteContext Objects

```python
class RigVMExtendedExecuteContext(StructBase)
```

The execute context is used for mutable nodes to
indicate execution order.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMExecuteContext.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``debug_memory_storage_object`` (RigVMMemoryStorage):  [Read-Write] Deprecated 5.4
  deprecated: Please, use DebugMemoryStorage
- ``work_memory_storage_object`` (RigVMMemoryStorage):  [Read-Write] Deprecated 5.4
  deprecated: Please, use WorkMemoryStorage

<a id="unreal.RigVMExtendedExecuteContext.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.RigVMExtendedExecuteContext.work_memory_storage_object"></a>

#### work_memory_storage_object

```python
@property
def work_memory_storage_object() -> RigVMMemoryStorage
```

(RigVMMemoryStorage):  [Read-Write] Deprecated 5.4
deprecated: Please, use WorkMemoryStorage

<a id="unreal.RigVMExtendedExecuteContext.work_memory_storage_object"></a>

#### work_memory_storage_object

```python
@work_memory_storage_object.setter
def work_memory_storage_object(value: RigVMMemoryStorage) -> None
```

<a id="unreal.RigVMExtendedExecuteContext.debug_memory_storage_object"></a>

#### debug_memory_storage_object

```python
@property
def debug_memory_storage_object() -> RigVMMemoryStorage
```

(RigVMMemoryStorage):  [Read-Write] Deprecated 5.4
deprecated: Please, use DebugMemoryStorage

<a id="unreal.RigVMExtendedExecuteContext.debug_memory_storage_object"></a>

#### debug_memory_storage_object

```python
@debug_memory_storage_object.setter
def debug_memory_storage_object(value: RigVMMemoryStorage) -> None
```

<a id="unreal.RigPhysicsSolverID"></a>