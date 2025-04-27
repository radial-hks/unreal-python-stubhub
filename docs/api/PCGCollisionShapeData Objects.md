## PCGCollisionShapeData Objects

```python
class PCGCollisionShapeData(PCGSpatialDataWithPointCache)
```

PCGCollision Shape Data

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCollisionShapeData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``keep_zero_density_points`` (bool):  [Read-Write]
- ``metadata`` (PCGMetadata):  [Read-Only] Not accessible through blueprint to make sure the constness is preserved
- ``target_actor`` (Actor):  [Read-Write] Recipient of any artifacts generated using this data.
- ``transform`` (Transform):  [Read-Only]

<a id="unreal.PCGCollisionShapeData.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.PCGCombinePointsSettings"></a>