## CoordinateUtils Objects

```python
class CoordinateUtils(BlueprintFunctionLibrary)
```

Wdp Coordinate Utils

**C++ Source:**

- **Plugin**: WdpDataModel
- **Module**: WdpCoordinate
- **File**: WdpCoordinateUtils.h

<a id="unreal.CoordinateUtils.transform_location_web_to_unreal"></a>

#### transform\_location\_web\_to\_unreal

```python
@classmethod
def transform_location_web_to_unreal(cls,
                                     position: Vector) -> Optional[Vector]
```

X.transform_location_web_to_unreal(position) -> Vector or None
Transform web position to unreal coordinate system
Web: (lon,lat in geo system) or (xyz in enu system, right hand with unit meter), defined by GeoReference.ApiCRS
UE: left hand system, unit cm

Args:
    position (Vector): 

Returns:
    Vector or None: 

    out_ue_position (Vector):

<a id="unreal.CoordinateUtils.transform_location_web_to_ue"></a>

#### transform\_location\_web\_to\_ue

```python
@classmethod
def transform_location_web_to_ue(cls, position: Vector) -> Vector
```

X.transform_location_web_to_ue(position) -> Vector
Transform web position to unreal coordinate system
Web: (lon,lat in geo system) or (xyz in enu system, right hand with unit meter), defined by GeoReference.ApiCRS
UE: left hand system, unit cm
deprecated: Use TransformLocationWebToUnreal instead.

Args:
    position (Vector): 

Returns:
    Vector:

<a id="unreal.CoordinateUtils.transform_location_unreal_to_web"></a>

#### transform\_location\_unreal\_to\_web

```python
@classmethod
def transform_location_unreal_to_web(cls,
                                     position: Vector) -> Optional[Vector]
```

X.transform_location_unreal_to_web(position) -> Vector or None
Transform position from ue to web
UE: left hand system, unit cm
Web: (lon,lat in geo system) or (xyz in enu system, right hand with meter), defined by GeoReference.ApiCRS

Args:
    position (Vector): 

Returns:
    Vector or None: 

    out_web_position (Vector):

<a id="unreal.CoordinateUtils.transform_location_ue_to_web"></a>

#### transform\_location\_ue\_to\_web

```python
@classmethod
def transform_location_ue_to_web(cls, position: Vector) -> Vector
```

X.transform_location_ue_to_web(position) -> Vector
Transform position from ue to web
UE: left hand system, unit cm
Web: (lon,lat in geo system) or (xyz in enu system, right hand with meter), defined by GeoReference.ApiCRS
deprecated: Use TransformLocationUnrealToWeb instead.

Args:
    position (Vector): 

Returns:
    Vector:

<a id="unreal.CoordinateUtils.transform_location_ue_to_gis"></a>

#### transform\_location\_ue\_to\_gis

```python
@classmethod
def transform_location_ue_to_gis(cls, ue_position: Vector) -> Vector
```

X.transform_location_ue_to_gis(ue_position) -> Vector
Transform unreal coordinate system to (lon,lat,alt)

Args:
    ue_position (Vector): 

Returns:
    Vector:

<a id="unreal.CoordinateUtils.transform_location_gis_to_ue"></a>

#### transform\_location\_gis\_to\_ue

```python
@classmethod
def transform_location_gis_to_ue(cls, gis_position: Vector) -> Vector
```

X.transform_location_gis_to_ue(gis_position) -> Vector
Transform (lon,lat,alt) to unreal coordinate system

Args:
    gis_position (Vector): 

Returns:
    Vector:

<a id="unreal.CoordinateUtils.transform_location2d_web_to_unreal"></a>

#### transform\_location2d\_web\_to\_unreal

```python
@classmethod
def transform_location2d_web_to_unreal(
        cls, position2d: Vector2D) -> Optional[Vector2D]
```

X.transform_location2d_web_to_unreal(position2d) -> Vector2D or None
Transform Location 2DWeb to Unreal

Args:
    position2d (Vector2D): 

Returns:
    Vector2D or None: 

    out_ue_position2d (Vector2D):

<a id="unreal.CoordinateUtils.transform_location2d_unreal_to_web"></a>

#### transform\_location2d\_unreal\_to\_web

```python
@classmethod
def transform_location2d_unreal_to_web(
        cls, position2d: Vector2D) -> Optional[Vector2D]
```

X.transform_location2d_unreal_to_web(position2d) -> Vector2D or None
Transform Location 2DUnreal to Web

Args:
    position2d (Vector2D): 

Returns:
    Vector2D or None: 

    out_web_position2d (Vector2D):

<a id="unreal.WdpGeoReferenceEntity"></a>