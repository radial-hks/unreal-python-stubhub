## SmartObjectAnnotationData Objects

```python
class SmartObjectAnnotationData(StructBase)
```

Per ZoneGraphData smart object look up data.

**C++ Source:**

- **Plugin**: MassGameplay
- **Module**: MassSmartObjects
- **File**: SmartObjectZoneAnnotations.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``affected_lanes`` (Array[int32]):  [Read-Only]
- ``data_handle`` (ZoneGraphDataHandle):  [Read-Only] Handle of the ZoneGraphData that this smart object annotation data is associated to
- ``lane_to_lane_location_indices_lookup`` (Map[int32, SmartObjectLaneLocationIndices]):  [Read-Only]
- ``smart_object_lane_locations`` (Array[SmartObjectLaneLocation]):  [Read-Only]
- ``smart_object_to_lane_location_index_lookup`` (Map[SmartObjectHandle, int32]):  [Read-Only]

<a id="unreal.SmartObjectAnnotationData.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.MassRepresentationParameters"></a>