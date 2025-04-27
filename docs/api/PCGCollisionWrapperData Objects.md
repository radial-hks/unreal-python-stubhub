## PCGCollisionWrapperData Objects

```python
class PCGCollisionWrapperData(PCGSpatialData)
```

PCGCollision Wrapper Data

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCollisionWrapperData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``keep_zero_density_points`` (bool):  [Read-Write]
- ``metadata`` (PCGMetadata):  [Read-Only] Not accessible through blueprint to make sure the constness is preserved
- ``target_actor`` (Actor):  [Read-Write] Recipient of any artifacts generated using this data.

<a id="unreal.PCGDifferenceData"></a>