## GDALTransformLibrary Objects

```python
class GDALTransformLibrary(BlueprintFunctionLibrary)
```

GDALTransform Library

**C++ Source:**

- **Plugin**: GDALForUnreal
- **Module**: GDALForUnreal
- **File**: GDALTransform.h

<a id="unreal.GDALTransformLibrary.xyz_to_lon_lat_batch"></a>

#### xyz\_to\_lon\_lat\_batch

```python
@classmethod
def xyz_to_lon_lat_batch(cls,
                         xyz_array: Array[Vector],
                         geo_srs_from: str = "",
                         geo_srs_to: str = "") -> Optional[Array[Vector]]
```

X.xyz_to_lon_lat_batch(xyz_array, geo_srs_from="", geo_srs_to="") -> Array[Vector] or None
XYZTo Lon Lat Batch

Args:
    xyz_array (Array[Vector]): 
    geo_srs_from (str): 
    geo_srs_to (str): 

Returns:
    Array[Vector] or None: 

    out_lon_lat_array (Array[Vector]):

<a id="unreal.GDALTransformLibrary.xyz_to_lon_lat"></a>

#### xyz\_to\_lon\_lat

```python
@classmethod
def xyz_to_lon_lat(cls, xyz: Vector) -> Optional[Vector]
```

X.xyz_to_lon_lat(xyz) -> Vector or None
XYZTo Lon Lat

Args:
    xyz (Vector): 

Returns:
    Vector or None: 

    out_lon_lat (Vector):

<a id="unreal.GDALTransformLibrary.update_global_transform"></a>

#### update\_global\_transform

```python
@classmethod
def update_global_transform(cls, geo_srs_from: str, geo_srs_to: str) -> None
```

X.update_global_transform(geo_srs_from, geo_srs_to) -> None
Set new GeoSRSFrom and GeoSRSTo to GlobalTransform

Args:
    geo_srs_from (str): like: +proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs
    geo_srs_to (str): like: +proj=ortho +lon_0=100.0 +lat_0=30.0 +a=6371010 +units=m +no_defs

<a id="unreal.GDALTransformLibrary.lon_lat_to_xyz_batch"></a>

#### lon\_lat\_to\_xyz\_batch

```python
@classmethod
def lon_lat_to_xyz_batch(cls,
                         lon_lat_array: Array[Vector],
                         geo_srs_from: str = "",
                         geo_srs_to: str = "") -> Optional[Array[Vector]]
```

X.lon_lat_to_xyz_batch(lon_lat_array, geo_srs_from="", geo_srs_to="") -> Array[Vector] or None
Lon Lat to XYZBatch

Args:
    lon_lat_array (Array[Vector]): 
    geo_srs_from (str): 
    geo_srs_to (str): 

Returns:
    Array[Vector] or None: 

    out_xyz_array (Array[Vector]):

<a id="unreal.GDALTransformLibrary.lon_lat_to_xyz"></a>

#### lon\_lat\_to\_xyz

```python
@classmethod
def lon_lat_to_xyz(cls, lon_lat: Vector) -> Optional[Vector]
```

X.lon_lat_to_xyz(lon_lat) -> Vector or None
Lon Lat to XYZ

Args:
    lon_lat (Vector): 

Returns:
    Vector or None: 

    out_xyz (Vector):

<a id="unreal.GDALTransformLibrary.get_last_transform_params"></a>

#### get\_last\_transform\_params

```python
@classmethod
def get_last_transform_params(cls) -> Tuple[str, str]
```

X.get_last_transform_params() -> (out_geo_srs_from=str, out_geo_srs_to=str)
Get Last Transform Params

Returns:
    tuple: 

    out_geo_srs_from (str): 

    out_geo_srs_to (str):

<a id="unreal.GISFunctionLibrary"></a>