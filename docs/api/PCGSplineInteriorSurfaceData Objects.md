## PCGSplineInteriorSurfaceData Objects

```python
class PCGSplineInteriorSurfaceData(PCGSurfaceData)
```

Represents a surface implicitly using the top-down 2D projection of a closed spline.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSplineInteriorSurfaceData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``keep_zero_density_points`` (bool):  [Read-Write]
- ``local_bounds`` (Box):  [Read-Only]
- ``metadata`` (PCGMetadata):  [Read-Only] Not accessible through blueprint to make sure the constness is preserved
- ``target_actor`` (Actor):  [Read-Write] Recipient of any artifacts generated using this data.
- ``transform`` (Transform):  [Read-Only]

<a id="unreal.PCGTextureData"></a>