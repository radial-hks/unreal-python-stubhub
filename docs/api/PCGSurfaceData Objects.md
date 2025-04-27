## PCGSurfaceData Objects

```python
class PCGSurfaceData(PCGSpatialDataWithPointCache)
```

PCGSurface Data

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSurfaceData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``keep_zero_density_points`` (bool):  [Read-Write]
- ``local_bounds`` (Box):  [Read-Only]
- ``metadata`` (PCGMetadata):  [Read-Only] Not accessible through blueprint to make sure the constness is preserved
- ``target_actor`` (Actor):  [Read-Write] Recipient of any artifacts generated using this data.
- ``transform`` (Transform):  [Read-Only]

<a id="unreal.PCGSurfaceData.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.PCGSurfaceData.local_bounds"></a>

#### local_bounds

```python
@property
def local_bounds() -> Box
```

(Box):  [Read-Only]

<a id="unreal.PCGLandscapeData"></a>