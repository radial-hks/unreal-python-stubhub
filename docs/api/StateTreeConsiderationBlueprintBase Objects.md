## StateTreeConsiderationBlueprintBase Objects

```python
class StateTreeConsiderationBlueprintBase(StateTreeNodeBlueprintBase)
```

* Base class for Blueprint based Considerations.

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeModule
- **File**: StateTreeConsiderationBlueprintBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``description`` (Text):  [Read-Write] Description of the node.
- ``icon_color`` (Color):  [Read-Write] Color of the icon.
- ``icon_name`` (Name):  [Read-Write] Name of the icon in format:
               StyleSetName | StyleName [ | SmallStyleName | StatusOverlayStyleName]
               SmallStyleName and StatusOverlayStyleName are optional.
               Example: "StateTreeEditorStyle|Node.Animation"

<a id="unreal.StateTreeConsiderationBlueprintBase.receive_get_score"></a>

#### receive_get_score

```python
def receive_get_score() -> float
```

x.receive_get_score() -> float
Receive Get Score

Returns:
    float:

<a id="unreal.StateTreeEvaluatorBlueprintBase"></a>