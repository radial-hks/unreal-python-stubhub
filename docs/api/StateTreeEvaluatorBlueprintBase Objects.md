## StateTreeEvaluatorBlueprintBase Objects

```python
class StateTreeEvaluatorBlueprintBase(StateTreeNodeBlueprintBase)
```

* Base class for Blueprint based evaluators.

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeModule
- **File**: StateTreeEvaluatorBlueprintBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``description`` (Text):  [Read-Write] Description of the node.
- ``icon_color`` (Color):  [Read-Write] Color of the icon.
- ``icon_name`` (Name):  [Read-Write] Name of the icon in format:
               StyleSetName | StyleName [ | SmallStyleName | StatusOverlayStyleName]
               SmallStyleName and StatusOverlayStyleName are optional.
               Example: "StateTreeEditorStyle|Node.Animation"

<a id="unreal.StateTreeEvaluatorBlueprintBase.receive_tree_stop"></a>

#### receive_tree_stop

```python
def receive_tree_stop() -> None
```

x.receive_tree_stop() -> None
Receive Tree Stop

<a id="unreal.StateTreeEvaluatorBlueprintBase.receive_tree_start"></a>

#### receive_tree_start

```python
def receive_tree_start() -> None
```

x.receive_tree_start() -> None
Receive Tree Start

<a id="unreal.StateTreeEvaluatorBlueprintBase.receive_tick"></a>

#### receive_tick

```python
def receive_tick(delta_time: float) -> None
```

x.receive_tick(delta_time) -> None
Receive Tick

Args:
    delta_time (float):

<a id="unreal.StateTreeTaskBlueprintBase"></a>