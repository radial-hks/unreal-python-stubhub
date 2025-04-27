## StateTreeNodeBlueprintBase Objects

```python
class StateTreeNodeBlueprintBase(Object)
```

State Tree Node Blueprint Base

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeModule
- **File**: StateTreeNodeBlueprintBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``description`` (Text):  [Read-Write] Description of the node.
- ``icon_color`` (Color):  [Read-Write] Color of the icon.
- ``icon_name`` (Name):  [Read-Write] Name of the icon in format:
               StyleSetName | StyleName [ | SmallStyleName | StatusOverlayStyleName]
               SmallStyleName and StatusOverlayStyleName are optional.
               Example: "StateTreeEditorStyle|Node.Animation"

<a id="unreal.StateTreeNodeBlueprintBase.send_event"></a>

#### send_event

```python
def send_event(event: StateTreeEvent) -> None
```

x.send_event(event) -> None
Sends event to the StateTree.

Args:
    event (StateTreeEvent):

<a id="unreal.StateTreeNodeBlueprintBase.request_transition"></a>

#### request_transition

```python
def request_transition(
    target_state: StateTreeStateLink,
    priority: StateTreeTransitionPriority = StateTreeTransitionPriority.NORMAL
) -> None
```

x.request_transition(target_state, priority=StateTreeTransitionPriority.NORMAL) -> None
Request state transition.

Args:
    target_state (StateTreeStateLink): 
    priority (StateTreeTransitionPriority):

<a id="unreal.StateTreeNodeBlueprintBase.receive_get_description"></a>

#### receive_get_description

```python
def receive_get_description(formatting: StateTreeNodeFormatting) -> Text
```

x.receive_get_description(formatting) -> Text
Event to implement to get node description.

Args:
    formatting (StateTreeNodeFormatting): 

Returns:
    Text:

<a id="unreal.StateTreeItemBlueprintBase"></a>