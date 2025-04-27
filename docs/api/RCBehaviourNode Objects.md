## RCBehaviourNode Objects

```python
class RCBehaviourNode(Object)
```

Base class for behaviour node which holds the logic to execute behaviour

**C++ Source:**

- **Plugin**: RemoteControl
- **Module**: RemoteControlLogic
- **File**: RCBehaviourNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``behavior_description`` (Text):  [Read-Write] Detailed description of what this behavior does, displayed in Action Panel's Header.
  Custom behavior blueprints can set this value in defaults to update the display name
- ``display_name`` (Text):  [Read-Write] User-friendly display name for this Behavior, displayed in Action Panel's Header.
  Custom behavior blueprints can set this value in defaults to update the display name

<a id="unreal.RCBehaviourBindNode"></a>