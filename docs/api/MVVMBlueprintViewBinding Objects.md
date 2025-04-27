## MVVMBlueprintViewBinding Objects

```python
class MVVMBlueprintViewBinding(StructBase)
```

MVVMBlueprint View Binding

**C++ Source:**

- **Plugin**: ModelViewViewModel
- **Module**: ModelViewViewModelBlueprint
- **File**: MVVMBlueprintViewBinding.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``binding_id`` (Guid):  [Read-Only] The unique ID of this binding.
- ``binding_type`` (MVVMBindingMode):  [Read-Write]
- ``compile`` (bool):  [Read-Write] The binding is visible in the editor, but is not compiled and cannot be used at runtime.
- ``conversion`` (MVVMBlueprintViewConversionPath):  [Read-Only]
- ``destination_path`` (MVVMBlueprintPropertyPath):  [Read-Only]
- ``enabled`` (bool):  [Read-Write] Whether the binding is enabled or disabled by default. The instance may enable the binding at runtime.
- ``override_execution_mode`` (MVVMExecutionMode):  [Read-Write]
- ``source_path`` (MVVMBlueprintPropertyPath):  [Read-Only]

<a id="unreal.MVVMBlueprintViewBinding.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.MVVMBindingExecTextCounter"></a>