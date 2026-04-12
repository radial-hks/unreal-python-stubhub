## CesiumWgs84Ellipsoid Objects

```python
class CesiumWgs84Ellipsoid(BlueprintFunctionLibrary)
```

Cesium Wgs 84Ellipsoid

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumWgs84Ellipsoid.h

<a id="unreal.CesiumWgs84Ellipsoid.scale_to_geodetic_surface"></a>

#### scale\_to\_geodetic\_surface

```python
@classmethod
def scale_to_geodetic_surface(
        cls, earth_centered_earth_fixed_position: Vector) -> Vector
```

X.scale_to_geodetic_surface(earth_centered_earth_fixed_position) -> Vector
Scale the given Earth-Centered, Earth-Fixed position along the geodetic
surface normal so that it is on the surface of the ellipsoid. If the
position is near the center of the ellipsoid, the result will have the
value (0,0,0) because the surface position is undefined.

Args:
    earth_centered_earth_fixed_position (Vector): 

Returns:
    Vector:

<a id="unreal.CesiumWgs84Ellipsoid.longitude_latitude_height_to_earth_centered_earth_fixed"></a>

#### longitude\_latitude\_height\_to\_earth\_centered\_earth\_fixed

```python
@classmethod
def longitude_latitude_height_to_earth_centered_earth_fixed(
        cls, longitude_latitude_height: Vector) -> Vector
```

X.longitude_latitude_height_to_earth_centered_earth_fixed(longitude_latitude_height) -> Vector
Convert longitude in degrees (X), latitude in degrees (Y), and height above
the WGS84 ellipsoid in meters (Z) to Earth-Centered, Earth-Fixed (ECEF)
coordinates.

Args:
    longitude_latitude_height (Vector): 

Returns:
    Vector:

<a id="unreal.CesiumWgs84Ellipsoid.get_radii"></a>

#### get\_radii

```python
@classmethod
def get_radii(cls) -> Vector
```

X.get_radii() -> Vector
Gets the radii of the WGS84 ellipsoid in its x-, y-, and z-directions in
meters.

Returns:
    Vector:

<a id="unreal.CesiumWgs84Ellipsoid.get_minimum_radius"></a>

#### get\_minimum\_radius

```python
@classmethod
def get_minimum_radius(cls) -> float
```

X.get_minimum_radius() -> double
Gets the minimum radius of the WGS854 ellipsoid in any dimension, in
meters.

Returns:
    double:

<a id="unreal.CesiumWgs84Ellipsoid.get_maximum_radius"></a>

#### get\_maximum\_radius

```python
@classmethod
def get_maximum_radius(cls) -> float
```

X.get_maximum_radius() -> double
Gets the maximum radius of the WGS84 ellipsoid in any dimension, in meters.

Returns:
    double:

<a id="unreal.CesiumWgs84Ellipsoid.geodetic_surface_normal"></a>

#### geodetic\_surface\_normal

```python
@classmethod
def geodetic_surface_normal(
        cls, earth_centered_earth_fixed_position: Vector) -> Vector
```

X.geodetic_surface_normal(earth_centered_earth_fixed_position) -> Vector
Computes the normal of the plane tangent to the surface of the ellipsoid
at the provided Earth-Centered, Earth-Fixed position.

Args:
    earth_centered_earth_fixed_position (Vector): 

Returns:
    Vector:

<a id="unreal.CesiumWgs84Ellipsoid.earth_centered_earth_fixed_to_longitude_latitude_height"></a>

#### earth\_centered\_earth\_fixed\_to\_longitude\_latitude\_height

```python
@classmethod
def earth_centered_earth_fixed_to_longitude_latitude_height(
        cls, earth_centered_earth_fixed_position: Vector) -> Vector
```

X.earth_centered_earth_fixed_to_longitude_latitude_height(earth_centered_earth_fixed_position) -> Vector
Convert Earth-Centered, Earth-Fixed (ECEF) coordinates to longitude in
degrees (X), latitude in degrees (Y), and height above the WGS84 ellipsoid
in meters (Z). If the position is near the center of the Earth, the result
will have the value (0,0,0) because the longitude, latitude, and height are
undefined.

Args:
    earth_centered_earth_fixed_position (Vector): 

Returns:
    Vector:

<a id="unreal.GlobeAwareDefaultPawn"></a>