## MassSimulationLODParameters Objects

```python
class MassSimulationLODParameters(MassConstSharedFragment)
```

Mass Simulation LODParameters

**C++ Source:**

- **Plugin**: MassGameplay
- **Module**: MassLOD
- **File**: MassSimulationLOD.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``buffer_hysteresis_on_distance_percentage`` (float):  [Read-Write] Hysteresis percentage on delta between the LOD distances
- ``lod_distance`` (float):  [Read-Write] Distance where each LOD becomes relevant
- ``lod_max_count`` (int32):  [Read-Write] Maximum limit of entity per LOD
- ``set_lod_tags`` (bool):  [Read-Write] If true, will set the associated LOD tag on the entity

<a id="unreal.MassSimulationLODParameters.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.MassSimulationVariableTickParameters"></a>