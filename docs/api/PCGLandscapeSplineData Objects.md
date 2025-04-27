## PCGLandscapeSplineData Objects

```python
class PCGLandscapeSplineData(PCGPolyLineData)
```

PCGLandscape Spline Data

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGLandscapeSplineData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``keep_zero_density_points`` (bool):  [Read-Write]
- ``metadata`` (PCGMetadata):  [Read-Only] Not accessible through blueprint to make sure the constness is preserved
- ``spline`` (LandscapeSplinesComponent):  [Read-Write]
- ``target_actor`` (Actor):  [Read-Write] Recipient of any artifacts generated using this data.

<a id="unreal.PCGLandscapeSplineData.spline"></a>

#### spline

```python
@property
def spline() -> LandscapeSplinesComponent
```

(LandscapeSplinesComponent):  [Read-Write]

<a id="unreal.PCGLandscapeSplineData.spline"></a>

#### spline

```python
@spline.setter
def spline(value: LandscapeSplinesComponent) -> None
```

<a id="unreal.PCGPointData"></a>