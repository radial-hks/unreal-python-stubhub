## CesiumEllipsoid Objects

```python
class CesiumEllipsoid(DataAsset)
```

Cesium Ellipsoid

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumEllipsoid.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``radii`` (Vector):  [Read-Write] The radii of this ellipsoid.

  The X coordinate of the vector should be the radius of the largest axis and
  the Z coordinate should be the radius of the smallest axis.

<a id="unreal.CesiumEllipsoid.scale_to_geodetic_surface"></a>

#### scale\_to\_geodetic\_surface

```python
def scale_to_geodetic_surface(
        earth_centered_earth_fixed_position: Vector) -> Vector
```

x.scale_to_geodetic_surface(earth_centered_earth_fixed_position) -> Vector
Scale the given Ellipsoid-Centered, Ellipsoid-Fixed position along the
geodetic surface normal so that it is on the surface of the ellipsoid. If
the position is near the center of the ellipsoid, the result will have the
value (0,0,0) because the surface position is undefined.

Args:
    earth_centered_earth_fixed_position (Vector): 

Returns:
    Vector:

<a id="unreal.CesiumEllipsoid.longitude_latitude_height_to_ellipsoid_centered_ellipsoid_fixed"></a>

#### longitude\_latitude\_height\_to\_ellipsoid\_centered\_ellipsoid\_fixed

```python
def longitude_latitude_height_to_ellipsoid_centered_ellipsoid_fixed(
        longitude_latitude_height: Vector) -> Vector
```

x.longitude_latitude_height_to_ellipsoid_centered_ellipsoid_fixed(longitude_latitude_height) -> Vector
Convert longitude in degrees (X), latitude in degrees (Y), and height above
the ellipsoid in meters (Z) to Ellipsoid-Centered, Ellipsoid-Fixed (ECEF)
coordinates.

Args:
    longitude_latitude_height (Vector): 

Returns:
    Vector:

<a id="unreal.CesiumEllipsoid.get_radii"></a>

#### get\_radii

```python
def get_radii() -> Vector
```

x.get_radii() -> Vector
Gets the radii of the ellipsoid in its x-, y-, and z-directions in
meters.

Returns:
    Vector:

<a id="unreal.CesiumEllipsoid.get_minimum_radius"></a>

#### get\_minimum\_radius

```python
def get_minimum_radius() -> float
```

x.get_minimum_radius() -> double
Gets the minimum radius of the ellipsoid in any dimension, in
meters.

Returns:
    double:

<a id="unreal.CesiumEllipsoid.get_maximum_radius"></a>

#### get\_maximum\_radius

```python
def get_maximum_radius() -> float
```

x.get_maximum_radius() -> double
Gets the maximum radius of the ellipsoid in any dimension, in meters.

Returns:
    double:

<a id="unreal.CesiumEllipsoid.geodetic_surface_normal"></a>

#### geodetic\_surface\_normal

```python
def geodetic_surface_normal(
        earth_centered_earth_fixed_position: Vector) -> Vector
```

x.geodetic_surface_normal(earth_centered_earth_fixed_position) -> Vector
Computes the normal of the plane tangent to the surface of the ellipsoid
at the provided Ellipsoid-Centered, Ellipsoid-Fixed position.

Args:
    earth_centered_earth_fixed_position (Vector): 

Returns:
    Vector:

<a id="unreal.CesiumEllipsoid.ellipsoid_centered_ellipsoid_fixed_to_longitude_latitude_height"></a>

#### ellipsoid\_centered\_ellipsoid\_fixed\_to\_longitude\_latitude\_height

```python
def ellipsoid_centered_ellipsoid_fixed_to_longitude_latitude_height(
        earth_centered_earth_fixed_position: Vector) -> Vector
```

x.ellipsoid_centered_ellipsoid_fixed_to_longitude_latitude_height(earth_centered_earth_fixed_position) -> Vector
Convert Ellipsoid-Centered, Ellipsoid-Fixed (ECEF) coordinates to longitude
in degrees (X), latitude in degrees (Y), and height above the ellipsoid in
meters (Z). If the position is near the center of the Ellipsoid, the result
will have the value (0,0,0) because the longitude, latitude, and height are
undefined.

Args:
    earth_centered_earth_fixed_position (Vector): 

Returns:
    Vector:

<a id="unreal.CesiumEllipsoid.create"></a>

#### create

```python
@classmethod
def create(cls, radii: Vector) -> CesiumEllipsoid
```

X.create(radii) -> CesiumEllipsoid
Creates a new {
link: UCesiumEllipsoid} with the given radii. This is equivalent to ``` auto ellipsoid = NewObject<UCesiumEllipsoid>(); ellipsoid->SetRadii(Radii);

Args:
    radii (Vector): 

Returns:
    CesiumEllipsoid:

<a id="unreal.CesiumEncodedMetadataComponent"></a>