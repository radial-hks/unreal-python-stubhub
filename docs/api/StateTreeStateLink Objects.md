## StateTreeStateLink Objects

```python
class StateTreeStateLink(StructBase)
```

Link to another state in StateTree

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeModule
- **File**: StateTreeTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``id`` (Guid):  [Read-Write] ID of the state linked to.
- ``link_type`` (StateTreeTransitionType):  [Read-Write] Type of the transition, used at edit time to describe e.g. next state (which is calculated at compile time).
- ``name`` (Name):  [Read-Write] Name of the state at the time of linking, used for error reporting.

<a id="unreal.StateTreeStateLink.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.ActorModifierCoreMetadata"></a>