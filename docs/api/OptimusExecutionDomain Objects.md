## OptimusExecutionDomain Objects

```python
class OptimusExecutionDomain(StructBase)
```

A struct to hold onto a single-level domain for controlling a kernel's execution domain.
The reason it's in a struct is so that we can apply a property panel customization for it
to make it easier to select from a pre-defined list of execution domains.

**C++ Source:**

- **Plugin**: DeformerGraph
- **Module**: OptimusCore
- **File**: OptimusExecutionDomain.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``expression`` (str):  [Read-Write]
- ``name`` (Name):  [Read-Write] The name of the execution domain that this kernel operates on.
- ``type`` (OptimusExecutionDomainType):  [Read-Write]

<a id="unreal.OptimusExecutionDomain.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.Optimus_ShaderBinding"></a>