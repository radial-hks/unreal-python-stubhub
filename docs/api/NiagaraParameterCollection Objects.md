## NiagaraParameterCollection Objects

```python
class NiagaraParameterCollection(Object)
```

Asset containing a collection of global parameters usable by Niagara. Similar to Material parameter collections,
any number of Niagara assets may reference attributes from this parameter collection and will get new values when they are changed.

A Niagara parameter collection can reference a Material parameter collection, so it is in sync with the values provided to a Material.
To use a value from a parameter collection in a Niagara system or emitter, add a reference to it from the Parameters panel (in the Niagara Parameter Collection section).

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraParameterCollection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``namespace`` (Name):  [Read-Write] Namespace for this parameter collection. Is enforced to be unique across all parameter collections.
- ``source_material_collection`` (MaterialParameterCollection):  [Read-Write] Optional set of MPC that can drive scalar and vector parameters

<a id="unreal.ComputeGraph"></a>