## WorldPartition Objects

```python
class WorldPartition(Object)
```

World Partition

**C++ Source:**

- **Module**: Engine
- **File**: WorldPartition.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_showing_hlo_ds_in_editor`` (bool):  [Read-Write] Whether HLODs should be allowed to be displayed in the editor for this map
- ``data_layers_logic_operator`` (WorldPartitionDataLayersLogicOperator):  [Read-Write]
- ``default_hlod_layer`` (HLODLayer):  [Read-Write] Default HLOD layer
- ``disable_content_bundles`` (bool):  [Read-Write] if set to true, this removes any content bundles from this world and also removes content bundle editing
- ``runtime_cells_transformer_stack`` (Array[RuntimeCellTransformerInstance]):  [Read-Write] Runtime cells transform stack objects
- ``server_streaming_mode`` (WorldPartitionServerStreamingMode):  [Read-Write]
- ``server_streaming_out_mode`` (WorldPartitionServerStreamingOutMode):  [Read-Write]

<a id="unreal.WorldPartitionPropertyOverride"></a>