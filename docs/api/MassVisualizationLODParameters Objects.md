## MassVisualizationLODParameters Objects

```python
class MassVisualizationLODParameters(MassConstSharedFragment)
```

Mass Visualization LODParameters

**C++ Source:**

- **Plugin**: MassGameplay
- **Module**: MassRepresentation
- **File**: MassRepresentationFragments.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_lod_distance`` (float):  [Read-Write] Distances where each LOD becomes relevant
- ``buffer_hysteresis_on_distance_percentage`` (float):  [Read-Write]
- ``distance_to_frustum`` (float):  [Read-Write] Entities within this distance from frustum will be considered visible. Expressed in Unreal Units.
- ``distance_to_frustum_hysteresis`` (float):  [Read-Write] Once an entity is visible how far away from frustum does it need to get to lose "visible" state.
  Expressed in Unreal Units and is added to DistanceToFrustum to arrive at the final value to be used for testing.
- ``filter_tag`` (ScriptStruct):  [Read-Write] Filter these settings with specified tag
- ``lod_max_count`` (int32):  [Read-Write] Maximum limit for each entity per LOD
- ``visible_lod_distance`` (float):  [Read-Write]

<a id="unreal.MassVisualizationLODParameters.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.InterchangeTestFunction"></a>