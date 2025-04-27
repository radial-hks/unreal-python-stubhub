## AssetActionSupportCondition Objects

```python
class AssetActionSupportCondition(StructBase)
```

Asset Action Support Condition

**C++ Source:**

- **Module**: Blutility
- **File**: AssetActionUtility.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``failure_reason`` (str):  [Read-Write] This is the failure reason to reply to the user with if the condition above fails.
  If you fill in the reason, it will override the default failure text in the tooltip for the function menu option.
- ``filter`` (str):  [Read-Write] This is a content browser styled filter.  For example, ..._N AND VirtualTextureStreaming=FALSE, would require that
  asset tag VirtualTextureStreaming be false, and the asset name end in _N.

  You can learn more about the content browser search syntax in the "Advanced Search Syntax" documentation.
- ``show_in_menu_if_filter_fails`` (bool):  [Read-Write] If this filter does not pass, show the corresponding functions from the menu anyways.
  If true, the menu option will display with the error tooltip, but be disabled.
  If false, the menu options will be removed entirely.

<a id="unreal.AssetActionSupportCondition.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.RigVMEdGraphDisplaySettings"></a>