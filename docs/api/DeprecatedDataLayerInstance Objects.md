## DeprecatedDataLayerInstance Objects

```python
class DeprecatedDataLayerInstance(DataLayerInstance)
```

Class used for Runtime Conversion of the Deprecated UDataLayer Class to UDataLayerInstance + UDataLayerAsset.
This class is not to be inherited. It is solely used by AWorldDatalayers to convert UDataLayers to UDataLayerInstances on Level Boot.
You will need to run the DataLayerToAsset CommandLet to convert the deprecated datalayers to UDataLayerAssets and UDataLayerInstanceWithAsset.

**C++ Source:**

- **Module**: Engine
- **File**: DeprecatedDataLayerInstance.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``data_layer_type`` (DataLayerType):  [Read-Write]
- ``debug_color`` (Color):  [Read-Write]
- ``initial_runtime_state`` (DataLayerRuntimeState):  [Read-Write] Initial runtime state of this data layer instance. Only supported if it's runtime and not client/server only.
- ``is_initially_loaded_in_editor`` (bool):  [Read-Write] Determines the default value of the data layer's loaded state in editor if it hasn't been changed in data layer outliner by the user
- ``is_initially_visible`` (bool):  [Read-Write] Whether actors associated with the Data Layer should be initially visible in the viewport when loading the map
- ``override_block_on_slow_streaming`` (OverrideBlockOnSlowStreaming):  [Read-Write]

<a id="unreal.WorldPartitionDestructibleHLODComponent"></a>