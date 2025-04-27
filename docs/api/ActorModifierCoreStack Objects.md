## ActorModifierCoreStack Objects

```python
class ActorModifierCoreStack(ActorModifierCoreBase)
```

A modifier stack contains modifiers and is also a modifier by itself

**C++ Source:**

- **Plugin**: ActorModifierCore
- **Module**: ActorModifierCore
- **File**: ActorModifierCoreStack.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled
- ``modifier_profiling`` (bool):  [Read-Write] Enable profiling for the modifiers in this stack
- ``modifiers`` (Array[ActorModifierCoreBase]):  [Read-Only] Contains actual modifiers in the stack

<a id="unreal.TagCollectionModifierStack"></a>