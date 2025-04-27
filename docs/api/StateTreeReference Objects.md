## StateTreeReference Objects

```python
class StateTreeReference(StructBase)
```

Struct to hold reference to a StateTree asset along with values to parameterized it.

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeModule
- **File**: StateTreeReference.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``parameters`` (InstancedPropertyBag):  [Read-Write]
- ``property_overrides`` (Array[Guid]):  [Read-Write] Array of overridden properties. Non-overridden properties will inherit the values from the StateTree default parameters.
- ``state_tree`` (StateTree):  [Read-Write]

<a id="unreal.StateTreeReference.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.StateTreeStructRef"></a>