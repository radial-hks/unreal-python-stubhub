## MVVMBlueprintViewConversionFunction Objects

```python
class MVVMBlueprintViewConversionFunction(Object)
```

A conversion function converts between the source and destiation of a binding.

Internally that function may be using native C++, K2Nodes, UFunctions, Events, etc.

**C++ Source:**

- **Plugin**: ModelViewViewModel
- **Module**: ModelViewViewModelBlueprint
- **File**: MVVMBlueprintViewConversionFunction.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``conversion_function`` (MVVMBlueprintFunctionReference):  [Read-Only] Conversion reference. It can be simple, complex or a K2Node.
  note: The conversion is complex
- ``destination_path`` (MVVMBlueprintPropertyPath):  [Read-Only] Destination of the binding, currently only saved when the conversion function uses
  async nodes. Async graphs will handle value setting internally rather than using the MVVM subsystem.
- ``graph_name`` (Name):  [Read-Only] Name of the generated graph if a wrapper is needed.
- ``is_ubergraph_page`` (bool):  [Read-Only]
- ``saved_pins`` (Array[MVVMBlueprintPin]):  [Read-Only] The pin that are modified and we saved data.
  The data may not be modified. We used the default value of the K2Node in that case.
- ``wrapper_graph_transient`` (bool):  [Read-Only]

<a id="unreal.Function"></a>