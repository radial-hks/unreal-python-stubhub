## PlanetShape Objects

```python
class PlanetShape(EnumBase)
```

EPlanet Shape

**C++ Source:**

- **Plugin**: GeoReferencing
- **Module**: GeoReferencing
- **File**: GeoReferencingSystem.h

<a id="unreal.PlanetShape.FLAT_PLANET"></a>

#### FLAT_PLANET

0: The world geometry coordinates are expressed in a projected space such as a Mercator projection.
In this mode, Planet curvature is not considered and you might face errors related to projection on large environments

<a id="unreal.PlanetShape.ROUND_PLANET"></a>

#### ROUND_PLANET

1: The world geometry coordinates are expressed in a planet wide Cartesian frame,
placed on a specific location or at earth, or at the planet center.
You might need dynamic rebasing to avoid precision issues at large scales.

<a id="unreal.GooglePADErrorCode"></a>