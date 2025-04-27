## OptimusResourceDescription Objects

```python
class OptimusResourceDescription(Object)
```

Optimus Resource Description

**C++ Source:**

- **Plugin**: DeformerGraph
- **Module**: OptimusCore
- **File**: OptimusResourceDescription.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_binding`` (OptimusComponentSourceBinding):  [Read-Only] The component binding that this resource description is bound to
- ``data_domain`` (OptimusDataDomain):  [Read-Write] The data domain for this resource.
- ``data_type`` (OptimusDataTypeRef):  [Read-Write] The the data type of each element of the resource
- ``resource_name`` (Name):  [Read-Write]

<a id="unreal.OptimusResourceDescription.resource_name"></a>

#### resource_name

```python
@property
def resource_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.OptimusVariableDescription"></a>