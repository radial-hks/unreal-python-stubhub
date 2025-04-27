## RCBehaviourRangeMapNode Objects

```python
class RCBehaviourRangeMapNode(RCBehaviourNode)
```

Uses the given properties and values to limit the values of the Controller and perform lerp operations for the values.

**C++ Source:**

- **Plugin**: RemoteControl
- **Module**: RemoteControlLogic
- **File**: RCBehaviourRangeMapNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``behavior_description`` (Text):  [Read-Write] Detailed description of what this behavior does, displayed in Action Panel's Header.
  Custom behavior blueprints can set this value in defaults to update the display name
- ``display_name`` (Text):  [Read-Write] User-friendly display name for this Behavior, displayed in Action Panel's Header.
  Custom behavior blueprints can set this value in defaults to update the display name

<a id="unreal.RCBehaviourRangeMapNode.on_passed"></a>

#### on_passed

```python
def on_passed(behaviour: RCBehaviour) -> None
```

x.on_passed(behaviour) -> None
On Passed

Args:
    behaviour (RCBehaviour):

<a id="unreal.RCBehaviourRangeMapNode.is_supported"></a>

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

<a id="unreal.RCBehaviourRangeMapNode.execute"></a>

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

<a id="unreal.RCBehaviourSetAssetByPathNode"></a>