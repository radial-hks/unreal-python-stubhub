## PCGLandscapeData Objects

```python
class PCGLandscapeData(PCGSurfaceData)
```

Landscape data access abstraction for PCG. Supports multi-landscape access, but it assumes that they are not overlapping.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGLandscapeData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``keep_zero_density_points`` (bool):  [Read-Write]
- ``landscapes`` (Array[LandscapeProxy]):  [Read-Write] TODO: add on property changed to clear cached data. This is used to populate the LandscapeInfos array.
- ``local_bounds`` (Box):  [Read-Only]
- ``metadata`` (PCGMetadata):  [Read-Only] Not accessible through blueprint to make sure the constness is preserved
- ``target_actor`` (Actor):  [Read-Write] Recipient of any artifacts generated using this data.
- ``transform`` (Transform):  [Read-Only]

<a id="unreal.PCGLandscapeData.landscapes"></a>

#### landscapes

```python
@property
def landscapes() -> Array[LandscapeProxy]
```

(Array[LandscapeProxy]):  [Read-Write] TODO: add on property changed to clear cached data. This is used to populate the LandscapeInfos array.

<a id="unreal.PCGLandscapeData.landscapes"></a>

#### landscapes

```python
@landscapes.setter
def landscapes(value: Array[LandscapeProxy]) -> None
```

<a id="unreal.PCGPolyLineData"></a>