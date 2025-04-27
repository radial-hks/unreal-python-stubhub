## RCBehaviourOnValueChangedNode Objects

```python
class RCBehaviourOnValueChangedNode(RCBehaviourNode)
```

On Value Changed Behaviour Node

This behaviour always returns true and thus executes all actions any time the Controller value is modified

**C++ Source:**

- **Plugin**: RemoteControl
- **Module**: RemoteControlLogic
- **File**: RCBehaviourOnValueChangedNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``behavior_description`` (Text):  [Read-Write] Detailed description of what this behavior does, displayed in Action Panel's Header.
  Custom behavior blueprints can set this value in defaults to update the display name
- ``display_name`` (Text):  [Read-Write] User-friendly display name for this Behavior, displayed in Action Panel's Header.
  Custom behavior blueprints can set this value in defaults to update the display name

<a id="unreal.RCBehaviourOnValueChangedNode.is_supported"></a>

#### is_supported

```python
def is_supported(behaviour: RCBehaviour) -> bool
```

x.is_supported(behaviour) -> bool
Is Supported

Args:
    behaviour (RCBehaviour): 

Returns:
    bool:

<a id="unreal.RCBehaviourOnValueChangedNode.execute"></a>

#### execute

```python
def execute(behaviour: RCBehaviour) -> bool
```

x.execute(behaviour) -> bool
Execute

Args:
    behaviour (RCBehaviour): 

Returns:
    bool:

<a id="unreal.RCBehaviourRangeMapNode"></a>