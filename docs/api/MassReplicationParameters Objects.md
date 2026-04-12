## MassReplicationParameters Objects

```python
class MassReplicationParameters(MassConstSharedFragment)
```

Mass Replication Parameters

**C++ Source:**

- **Plugin**: MassGameplay
- **Module**: MassReplication
- **File**: MassReplicationFragments.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bubble_info_class`` (type(Class)):  [Read-Write]
- ``buffer_hysteresis_on_distance_percentage`` (float):  [Read-Write] Hysteresis percentage on delta between the LOD distances
- ``lod_distance`` (float):  [Read-Write] Distance where each LOD becomes relevant
- ``lod_max_count`` (int32):  [Read-Write] Maximum limit of entity per LOD
- ``lod_max_count_per_viewer`` (int32):  [Read-Write] Maximum limit of entity per LOD per viewer
- ``replicator_class`` (type(Class)):  [Read-Write]
- ``update_interval`` (float):  [Read-Write] Distance where each LOD becomes relevant

<a id="unreal.MassReplicationParameters.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.SmartObjectAnnotationData"></a>