## MVVMBlueprintPropertyPath Objects

```python
class MVVMBlueprintPropertyPath(StructBase)
```

Base path to properties for MVVM view models and widgets.

Used to associate properties within MVVM bindings in editor & during MVVM compilation

**C++ Source:**

- **Plugin**: ModelViewViewModel
- **Module**: ModelViewViewModelBlueprint
- **File**: MVVMPropertyPath.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``context_id`` (Guid):  [Read-Only]
- ``paths`` (Array[MVVMBlueprintFieldPath]):  [Read-Only] Reference to property for this binding.
- ``source`` (MVVMBlueprintFieldPathSource):  [Read-Only]
- ``widget_name`` (Name):  [Read-Only]

<a id="unreal.MVVMBlueprintPropertyPath.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.MVVMViewModelPropertyPath"></a>