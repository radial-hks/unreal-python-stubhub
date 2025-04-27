## PCGSplineProjectionData Objects

```python
class PCGSplineProjectionData(PCGProjectionData)
```

The projection of a spline onto a surface.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSplineData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``keep_zero_density_points`` (bool):  [Read-Write]
- ``metadata`` (PCGMetadata):  [Read-Only] Not accessible through blueprint to make sure the constness is preserved
- ``projected_position`` (InterpCurveVector2D):  [Read-Write]
- ``projection_params`` (PCGProjectionParams):  [Read-Only]
- ``source`` (PCGSpatialData):  [Read-Only]
- ``target`` (PCGSpatialData):  [Read-Only]
- ``target_actor`` (Actor):  [Read-Write] Recipient of any artifacts generated using this data.

<a id="unreal.PCGSplineProjectionData.projected_position"></a>

#### projected_position

```python
@property
def projected_position() -> InterpCurveVector2D
```

(InterpCurveVector2D):  [Read-Write]

<a id="unreal.PCGSplineProjectionData.projected_position"></a>

#### projected_position

```python
@projected_position.setter
def projected_position(value: InterpCurveVector2D) -> None
```

<a id="unreal.PCGSplineInteriorSurfaceData"></a>