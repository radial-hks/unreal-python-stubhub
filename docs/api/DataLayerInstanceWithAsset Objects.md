## DataLayerInstanceWithAsset Objects

```python
class DataLayerInstanceWithAsset(DataLayerInstance)
```

Data Layer Instance with Asset

**C++ Source:**

- **Module**: Engine
- **File**: DataLayerInstanceWithAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``data_layer_asset`` (DataLayerAsset):  [Read-Write]
- ``initial_runtime_state`` (DataLayerRuntimeState):  [Read-Write] Initial runtime state of this data layer instance. Only supported if it's runtime and not client/server only.
- ``is_included_in_actor_filter_default`` (bool):  [Read-Write] Whether actors assigned to this DataLayer are included by default when used in a filter
- ``is_initially_loaded_in_editor`` (bool):  [Read-Write] Determines the default value of the data layer's loaded state in editor if it hasn't been changed in data layer outliner by the user
- ``is_initially_visible`` (bool):  [Read-Write] Whether actors associated with the Data Layer should be initially visible in the viewport when loading the map
- ``override_block_on_slow_streaming`` (OverrideBlockOnSlowStreaming):  [Read-Write]

<a id="unreal.ExternalDataLayerInstance"></a>