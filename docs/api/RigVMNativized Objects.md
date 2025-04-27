## RigVMNativized Objects

```python
class RigVMNativized(RigVM)
```

Rig VMNativized

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMNativized.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``debug_memory_storage_object`` (RigVMMemoryStorage):  [Read-Write] Deprecated 5.4,
  deprecated: Please use DefaultDebugMemoryStorage for compiling and DebugMemoryStorage in the ExtendedExecuteContext for intance execution
- ``literal_memory_storage_object`` (RigVMMemoryStorage):  [Read-Write] Deprecated 5.4
  deprecated: Please, use LiteralMemoryStorage
- ``work_memory_storage_object`` (RigVMMemoryStorage):  [Read-Write] Deprecated 5.4
  deprecated: Please, use DefaultWorkMemoryStorage for compiling and WorkMemoryStorage in the ExtendedExecuteContext for intance execution

<a id="unreal.RigVMUserWorkflowOptions"></a>