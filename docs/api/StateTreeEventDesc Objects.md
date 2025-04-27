## StateTreeEventDesc Objects

```python
class StateTreeEventDesc(StructBase)
```

Editor representation of an event description.

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeEditorModule
- **File**: StateTreeState.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``consume_event_on_select`` (bool):  [Read-Write] If set to true, the event is consumed (later state selection cannot react to it) if state selection can be made.
- ``payload_struct`` (ScriptStruct):  [Read-Write] Event Payload Struct.
- ``tag`` (GameplayTag):  [Read-Write] Event Tag.

<a id="unreal.StateTreeEventDesc.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.StateTreeTransition"></a>