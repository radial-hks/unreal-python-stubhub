## CesiumOriginShiftMode Objects

```python
class CesiumOriginShiftMode(EnumBase)
```

Indicates how to shift the origin as the Actor to which a
CesiumOriginShiftComponent is attached moves.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumOriginShiftComponent.h

<a id="unreal.CesiumOriginShiftMode.DISABLED"></a>

#### DISABLED

0: This component is disabled and will have no effect.

<a id="unreal.CesiumOriginShiftMode.SWITCH_SUB_LEVELS_ONLY"></a>

#### SWITCH\_SUB\_LEVELS\_ONLY

1: The origin of the CesiumGeoreference will be changed when the Actor enters
a new sub-level, but it will otherwise not be modified as the Actor moves.
Any objects that are not anchored to the globe with a
CesiumGlobeAnchorComponent will appear to move when the Actor enters a
sub-level.

<a id="unreal.CesiumOriginShiftMode.CHANGE_CESIUM_GEOREFERENCE"></a>

#### CHANGE\_CESIUM\_GEOREFERENCE

2: The origin of the CesiumGeoreference will change as the Actor moves in
order to maintain small, precise coordinate values near the Actor, as well
as to keep the globe's local "up" direction aligned with the +Z axis. Any
objects that are not anchored to the globe with a
CesiumGlobeAnchorComponent will appear to move whenever the origin changes.

When using this mode, all Cesium3DTileset instances as well as any Actors
with a CesiumGlobeAnchorComponent need to be marked Movable, because these
objects _will_ be moved when the origin is shifted.

<a id="unreal.CesiumPropertyTableStatus"></a>