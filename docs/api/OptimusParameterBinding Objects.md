## OptimusParameterBinding Objects

```python
class OptimusParameterBinding(StructBase)
```

Optimus Parameter Binding

**C++ Source:**

- **Plugin**: DeformerGraph
- **Module**: OptimusCore
- **File**: OptimusBindingTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``data_domain`` (OptimusDataDomain):  [Read-Write]
- ``data_type`` (OptimusDataTypeRef):  [Read-Write]
- ``name`` (OptimusValidatedName):  [Read-Write]
- ``support_atomic_if_compatible_data_type`` (bool):  [Read-Write] Int type resource can optionally support atomic writes, memory is zero-initialized
- ``support_read`` (bool):  [Read-Write] Optionally support both read and write

<a id="unreal.OptimusParameterBinding.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.OptimusParameterBindingArray"></a>