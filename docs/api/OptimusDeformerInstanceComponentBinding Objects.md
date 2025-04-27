## OptimusDeformerInstanceComponentBinding Objects

```python
class OptimusDeformerInstanceComponentBinding(StructBase)
```

Defines a binding between a component provider in the graph and an actor component in the component hierarchy on
the actor whose deformable component we're bound to.

**C++ Source:**

- **Plugin**: DeformerGraph
- **Module**: OptimusCore
- **File**: OptimusDeformerInstance.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_name`` (Name):  [Read-Write] Component name to bind. This should be sanitized before storage.
- ``provider_name`` (Name):  [Read-Only] Binding name on deformer graph.

<a id="unreal.OptimusDeformerInstanceComponentBinding.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.CurveRemapPair"></a>