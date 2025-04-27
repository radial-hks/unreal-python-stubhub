## StateTreeBlueprintPropertyRef Objects

```python
class StateTreeBlueprintPropertyRef(StateTreePropertyRef)
```

FStateTreeBlueprintPropertyRef is a PropertyRef intended to be used in State Tree Blueprint nodes like tasks, conditions or evaluators, but also as a StateTree parameter.

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeModule
- **File**: StateTreePropertyRef.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_optional`` (bool):  [Read-Write] If specified, the reference can be left unbound, otherwise the State Tree compiler report error if the reference is not bound.
- ``is_ref_to_array`` (bool):  [Read-Write] If specified, the reference is to an TArray<RefType>
- ``ref_type`` (StateTreePropertyRefType):  [Read-Write] Specifies the type of property to reference
- ``type_object`` (Object):  [Read-Write] Specifies the type of property to reference together with RefType, used for Enums, Structs, Objects and Classes.

<a id="unreal.StateTreeBlueprintPropertyRef.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.StateTreeReference"></a>