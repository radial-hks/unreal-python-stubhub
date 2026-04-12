## EarthGeoReferenceSystemFunctionLibrary Objects

```python
class EarthGeoReferenceSystemFunctionLibrary(BlueprintFunctionLibrary)
```

Earth Geo Reference System Function Library

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesEarth
- **File**: EarthGeoreferenceSystemFunctionLibrary.h

<a id="unreal.EarthGeoReferenceSystemFunctionLibrary.transform_world_location_to_lon_lat_alt"></a>

#### transform\_world\_location\_to\_lon\_lat\_alt

```python
@classmethod
def transform_world_location_to_lon_lat_alt(cls, earth: AesEarth,
                                            location: Vector) -> Vector
```

X.transform_world_location_to_lon_lat_alt(earth, location) -> Vector
Transform World Location to Lon Lat Alt

Args:
    earth (AesEarth): 
    location (Vector): 

Returns:
    Vector:

<a id="unreal.EarthGeoReferenceSystemFunctionLibrary.transform_world_locations_to_lon_lat_alts"></a>

#### transform\_world\_locations\_to\_lon\_lat\_alts

```python
@classmethod
def transform_world_locations_to_lon_lat_alts(
        cls, earth: AesEarth, locations: Array[Vector]) -> Array[Vector]
```

X.transform_world_locations_to_lon_lat_alts(earth, locations) -> Array[Vector]
Transform World Locations to Lon Lat Alts

Args:
    earth (AesEarth): 
    locations (Array[Vector]): 

Returns:
    Array[Vector]:

<a id="unreal.EarthGeoReferenceSystemFunctionLibrary.transform_world_box_to_lla_box"></a>

#### transform\_world\_box\_to\_lla\_box

```python
@classmethod
def transform_world_box_to_lla_box(cls, earth: AesEarth,
                                   local_location: Box) -> Box
```

X.transform_world_box_to_lla_box(earth, local_location) -> Box
Transform World Box to LLABox

Args:
    earth (AesEarth): 
    local_location (Box): 

Returns:
    Box:

<a id="unreal.EarthGeoReferenceSystemFunctionLibrary.transform_quadkey_to_world_transform"></a>

#### transform\_quadkey\_to\_world\_transform

```python
@classmethod
def transform_quadkey_to_world_transform(cls, earth: AesEarth,
                                         quadkey: str) -> Transform
```

X.transform_quadkey_to_world_transform(earth, quadkey) -> Transform
Transform Quadkey to World Transform

Args:
    earth (AesEarth): 
    quadkey (str): 

Returns:
    Transform:

<a id="unreal.EarthGeoReferenceSystemFunctionLibrary.transform_quadkey_to_world_location"></a>

#### transform\_quadkey\_to\_world\_location

```python
@classmethod
def transform_quadkey_to_world_location(cls, earth: AesEarth,
                                        quadkey: str) -> Vector
```

X.transform_quadkey_to_world_location(earth, quadkey) -> Vector
Transform Quadkey to World Location

Args:
    earth (AesEarth): 
    quadkey (str): 

Returns:
    Vector:

<a id="unreal.EarthGeoReferenceSystemFunctionLibrary.transform_lon_lat_to_world_rotation"></a>

#### transform\_lon\_lat\_to\_world\_rotation

```python
@classmethod
def transform_lon_lat_to_world_rotation(cls, earth: AesEarth,
                                        lon_lat: Vector2D) -> Rotator
```

X.transform_lon_lat_to_world_rotation(earth, lon_lat) -> Rotator
Transform Lon Lat to World Rotation

Args:
    earth (AesEarth): 
    lon_lat (Vector2D): 

Returns:
    Rotator:

<a id="unreal.EarthGeoReferenceSystemFunctionLibrary.transform_lon_lat_to_tile_xy"></a>

#### transform\_lon\_lat\_to\_tile\_xy

```python
@classmethod
def transform_lon_lat_to_tile_xy(cls, earth: AesEarth, lon: float, lat: float,
                                 tile_level: int) -> EarthTileInfo
```

X.transform_lon_lat_to_tile_xy(earth, lon, lat, tile_level) -> EarthTileInfo
Transform Lon Lat to Tile XY

Args:
    earth (AesEarth): 
    lon (double): 
    lat (double): 
    tile_level (int32): 

Returns:
    EarthTileInfo:

<a id="unreal.EarthGeoReferenceSystemFunctionLibrary.transform_lon_lat_to_quad_key"></a>

#### transform\_lon\_lat\_to\_quad\_key

```python
@classmethod
def transform_lon_lat_to_quad_key(cls, earth: AesEarth, lon: float, lat: float,
                                  tile_level: int) -> str
```

X.transform_lon_lat_to_quad_key(earth, lon, lat, tile_level) -> str
Transform Lon Lat to Quad Key

Args:
    earth (AesEarth): 
    lon (double): 
    lat (double): 
    tile_level (int32): 

Returns:
    str:

<a id="unreal.EarthGeoReferenceSystemFunctionLibrary.transform_lon_lat_alt_to_world_transform"></a>

#### transform\_lon\_lat\_alt\_to\_world\_transform

```python
@classmethod
def transform_lon_lat_alt_to_world_transform(cls, earth: AesEarth,
                                             lon_lat_alt: Vector) -> Transform
```

X.transform_lon_lat_alt_to_world_transform(earth, lon_lat_alt) -> Transform
Transform Lon Lat Alt to World Transform

Args:
    earth (AesEarth): 
    lon_lat_alt (Vector): 

Returns:
    Transform:

<a id="unreal.EarthGeoReferenceSystemFunctionLibrary.transform_lon_lat_alt_to_world_location"></a>

#### transform\_lon\_lat\_alt\_to\_world\_location

```python
@classmethod
def transform_lon_lat_alt_to_world_location(cls, earth: AesEarth,
                                            lon_lat_alt: Vector) -> Vector
```

X.transform_lon_lat_alt_to_world_location(earth, lon_lat_alt) -> Vector
Transform Lon Lat Alt to World Location

Args:
    earth (AesEarth): 
    lon_lat_alt (Vector): 

Returns:
    Vector:

<a id="unreal.EarthGeoReferenceSystemFunctionLibrary.transform_lon_lat_alts_to_world_locations"></a>

#### transform\_lon\_lat\_alts\_to\_world\_locations

```python
@classmethod
def transform_lon_lat_alts_to_world_locations(
        cls, earth: AesEarth, lon_lat_alts: Array[Vector]) -> Array[Vector]
```

X.transform_lon_lat_alts_to_world_locations(earth, lon_lat_alts) -> Array[Vector]
Transform Lon Lat Alts to World Locations

Args:
    earth (AesEarth): 
    lon_lat_alts (Array[Vector]): 

Returns:
    Array[Vector]:

<a id="unreal.EarthGeoReferenceSystemFunctionLibrary.transform_lla_box_to_world_box"></a>

#### transform\_lla\_box\_to\_world\_box

```python
@classmethod
def transform_lla_box_to_world_box(cls, earth: AesEarth,
                                   geo_location: Box2D) -> Box2D
```

X.transform_lla_box_to_world_box(earth, geo_location) -> Box2D
Transform LLABox to World Box

Args:
    earth (AesEarth): 
    geo_location (Box2D): 

Returns:
    Box2D:

<a id="unreal.EarthGeoReferenceSystemFunctionLibrary.get_tile_center_transform"></a>

#### get\_tile\_center\_transform

```python
@classmethod
def get_tile_center_transform(cls, earth: AesEarth, tile: EarthTileInfo,
                              altitude: float) -> Transform
```

X.get_tile_center_transform(earth, tile, altitude) -> Transform
Get Tile Center Transform

Args:
    earth (AesEarth): 
    tile (EarthTileInfo): 
    altitude (double): 

Returns:
    Transform:

<a id="unreal.EarthGeoReferenceSystemFunctionLibrary.get_tile_center_lon_lat"></a>

#### get\_tile\_center\_lon\_lat

```python
@classmethod
def get_tile_center_lon_lat(cls, earth: AesEarth,
                            tile: EarthTileInfo) -> Vector2D
```

X.get_tile_center_lon_lat(earth, tile) -> Vector2D
Get Tile Center Lon Lat

Args:
    earth (AesEarth): 
    tile (EarthTileInfo): 

Returns:
    Vector2D:

<a id="unreal.EarthGeoReferenceSystemFunctionLibrary.get_tile_center_location"></a>

#### get\_tile\_center\_location

```python
@classmethod
def get_tile_center_location(cls, earth: AesEarth, tile: EarthTileInfo,
                             altitude: float) -> Vector
```

X.get_tile_center_location(earth, tile, altitude) -> Vector
Get Tile Center Location

Args:
    earth (AesEarth): 
    tile (EarthTileInfo): 
    altitude (double): 

Returns:
    Vector:

<a id="unreal.EarthGeoReferenceSystemFunctionLibrary.convert_to_string"></a>

#### convert\_to\_string

```python
@classmethod
def convert_to_string(cls, value: float) -> str
```

X.convert_to_string(value) -> str
Convert to String

Args:
    value (double): 

Returns:
    str:

<a id="unreal.EarthInputProvider_EarthActor"></a>