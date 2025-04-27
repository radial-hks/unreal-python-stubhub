## HLODLayer Objects

```python
class HLODLayer(Object)
```

HLODLayer

**C++ Source:**

- **Module**: Engine
- **File**: HLODLayer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cell_size`` (int32):  [Read-Write] Cell size of the runtime grid created to encompass HLOD actors generated for this HLOD Layer
- ``hlod_actor_class`` (type(Class)):  [Read-Write] Specify a custom HLOD Actor class, the default is AWorldPartitionHLOD
- ``hlod_builder_class`` (type(Class)):  [Read-Write] HLOD Builder class
- ``hlod_builder_settings`` (HLODBuilderSettings):  [Read-Only]
- ``hlod_modifier_class`` (type(Class)):  [Read-Write] HLOD Modifier class, to allow changes to the HLOD at runtime
- ``is_spatially_loaded`` (bool):  [Read-Write] Whether HLOD actors generated for this layer will be spatially loaded
- ``layer_type`` (HLODLayerType):  [Read-Write] Type of HLOD generation to use
- ``loading_range`` (double):  [Read-Write] Loading range of the runtime grid created to encompass HLOD actors generated for this HLOD Layer
- ``parent_layer`` (HLODLayer):  [Read-Write] HLOD Layer to assign to the generated HLOD actors

<a id="unreal.NavigationDataChunkActor"></a>