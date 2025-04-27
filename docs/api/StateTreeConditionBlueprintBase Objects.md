## StateTreeConditionBlueprintBase Objects

```python
class StateTreeConditionBlueprintBase(StateTreeNodeBlueprintBase)
```

* Base class for Blueprint based Conditions.

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeModule
- **File**: StateTreeConditionBlueprintBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``description`` (Text):  [Read-Write] Description of the node.
- ``icon_color`` (Color):  [Read-Write] Color of the icon.
- ``icon_name`` (Name):  [Read-Write] Name of the icon in format:
               StyleSetName | StyleName [ | SmallStyleName | StatusOverlayStyleName]
               SmallStyleName and StatusOverlayStyleName are optional.
               Example: "StateTreeEditorStyle|Node.Animation"

<a id="unreal.StateTreeConditionBlueprintBase.receive_test_condition"></a>

#### receive_test_condition

```python
def receive_test_condition() -> bool
```

x.receive_test_condition() -> bool
Receive Test Condition

Returns:
    bool:

<a id="unreal.StateTreeConsiderationBlueprintBase"></a>