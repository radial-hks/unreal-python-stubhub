## InteractiveToolsPresetCollectionAsset Objects

```python
class InteractiveToolsPresetCollectionAsset(EditorConfigBase)
```

Implements an asset that can be used to store tool settings as a named preset

**C++ Source:**

- **Plugin**: ToolPresets
- **Module**: ToolPresetAsset
- **File**: ToolPresetAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collection_label`` (Text):  [Read-Write]
- ``per_tool_presets`` (Map[str, InteractiveToolPresetStore]):  [Read-Only] TODO: Currently there are no helper methods within this class, simply providing
  raw access to the underlying arrays and maps. This is intentional.
  Until the design of the preset concept is more firmly decided, it seems like a waste to
  implement a bunch of methods that we don't know if we actually want/need at the end.
  Once we are satisifed with the data structure, planned accessors and mutators will include
  support for adding, removing, renaming, saving and retrieving presets.

<a id="unreal.InteractiveToolsPresetCollectionAssetFactory"></a>