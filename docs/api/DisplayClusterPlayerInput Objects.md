## DisplayClusterPlayerInput Objects

```python
class DisplayClusterPlayerInput(EnhancedPlayerInput)
```

An object within PlayerController that processes player input.

This one is nDisplay specific implementation. It's responsible for replication
of UE native input within a cluster to support simulation determinism. Various
input sync policies might be implemented here.

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayCluster
- **File**: DisplayClusterPlayerInput.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``debug_exec_bindings`` (Array[KeyBind]):  [Read-Write] Generic bindings of keys to Exec()-compatible strings for development purposes only
- ``inverted_axis`` (Array[Name]):  [Read-Write] List of Axis Mappings that have been inverted

<a id="unreal.DisplayClusterPreviewShareComponent"></a>