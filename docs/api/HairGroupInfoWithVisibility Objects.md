## HairGroupInfoWithVisibility Objects

```python
class HairGroupInfoWithVisibility(HairGroupInfo)
```

Hair Group Info with Visibility

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``group_id`` (int32):  [Read-Only]
- ``group_name`` (Name):  [Read-Only]
- ``is_visible`` (bool):  [Read-Write] Toggle hair group visibility. This visibility flag is not persistent to the asset, and exists only as a preview/helper mechanism
- ``max_curve_length`` (float):  [Read-Only]
- ``num_curve_vertices`` (int32):  [Read-Only]
- ``num_curves`` (int32):  [Read-Only]
- ``num_guide_vertices`` (int32):  [Read-Only]
- ``num_guides`` (int32):  [Read-Only]

<a id="unreal.HairGroupInfoWithVisibility.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.HairGroupCardsInfo"></a>