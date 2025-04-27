## RCBehaviourSetAssetByPathNode Objects

```python
class RCBehaviourSetAssetByPathNode(RCBehaviourNode)
```

Takes the string as a path and goes on to search for the Asset it is connected to, setting it to a Target Exposed Property.

**C++ Source:**

- **Plugin**: RemoteControl
- **Module**: RemoteControlLogic
- **File**: RCBehaviourSetAssetByPathNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``behavior_description`` (Text):  [Read-Write] Detailed description of what this behavior does, displayed in Action Panel's Header.
  Custom behavior blueprints can set this value in defaults to update the display name
- ``display_name`` (Text):  [Read-Write] User-friendly display name for this Behavior, displayed in Action Panel's Header.
  Custom behavior blueprints can set this value in defaults to update the display name

<a id="unreal.RCBehaviourSetAssetByPathNode.is_supported"></a>

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

<a id="unreal.RCBehaviourSetAssetByPathNode.execute"></a>

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

<a id="unreal.RCController"></a>