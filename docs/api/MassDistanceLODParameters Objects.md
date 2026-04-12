## MassDistanceLODParameters Objects

```python
class MassDistanceLODParameters(MassConstSharedFragment)
```

Simplest version of LOD Calculation based strictly on Distance parameters
   Compared to FMassVisualizationLODParameters, we:
   * Only include a single set of LOD Distances (radial distance from viewer)
   * we do not care about distance to Frustum
   * we do not care about Max Count

**C++ Source:**

- **Plugin**: MassGameplay
- **Module**: MassRepresentation
- **File**: MassRepresentationFragments.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``buffer_hysteresis_on_distance_percentage`` (float):  [Read-Write]
- ``filter_tag`` (ScriptStruct):  [Read-Write] Filter these settings with specified tag
- ``lod_distance`` (float):  [Read-Write] Distances where each LOD becomes relevant

<a id="unreal.MassDistanceLODParameters.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.MassVisualizationLODParameters"></a>