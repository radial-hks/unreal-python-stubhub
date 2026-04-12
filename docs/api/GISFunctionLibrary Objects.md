## GISFunctionLibrary Objects

```python
class GISFunctionLibrary(BlueprintFunctionLibrary)
```

51WORLD的标准GIS坐标系是WGS84
1、GIS经纬度坐标系（WGS84，CGCS2000）
支持WGS84(国际标准)  GCJ02(国标，高德，腾讯)  BD09(百度)   CGCS2000(新国标)

2、GIS投影坐标系
投影坐标系，可以通过参考基准点，通过平移，旋转算法来得到UE4的坐标值

3、北京54，西安80的GIS坐标系统很老了。

Gis带号
1、我国采用6度分带和3度分带
   地形图上公里网横坐标前2位就是带号，例如：1∶5万地形图上的横坐标为18576000，其中18即为带号，293300为纵坐标值。
在中华人民共和国陆地范围内,坐标(Y坐标,8位数,前两位是带号)带号小于等于23的肯定是6度带，大于等于24的肯定是3度带。

**C++ Source:**

- **Plugin**: GDALForUnreal
- **Module**: GDALForUnreal
- **File**: GISFunctionLibrary.h

<a id="unreal.GISFunctionLibrary.gis_xian80_to_wgs84"></a>

#### gis\_xian80\_to\_wgs84

```python
@classmethod
def gis_xian80_to_wgs84(cls, str_xian80_x: str, str_xian80_y: str,
                        band_num: int) -> Tuple[str, str]
```

X.gis_xian80_to_wgs84(str_xian80_x, str_xian80_y, band_num) -> (str_wgs84_lng=str, str_wgs84_lat=str)
GIS Xian 80 to WGS84

Args:
    str_xian80_x (str): 
    str_xian80_y (str): 
    band_num (int32): 

Returns:
    tuple: 

    str_wgs84_lng (str): 

    str_wgs84_lat (str):

<a id="unreal.GISFunctionLibrary.gis_wgs84_to_gcj02"></a>

#### gis\_wgs84\_to\_gcj02

```python
@classmethod
def gis_wgs84_to_gcj02(cls, str_wgs84_lng: str,
                       str_wgs84_lat: str) -> Tuple[str, str]
```

X.gis_wgs84_to_gcj02(str_wgs84_lng, str_wgs84_lat) -> (str_gcj02_lng=str, str_gcj02_lat=str)
GIS WGS84 to GCJ02

Args:
    str_wgs84_lng (str): 
    str_wgs84_lat (str): 

Returns:
    tuple: 

    str_gcj02_lng (str): 

    str_gcj02_lat (str):

<a id="unreal.GISFunctionLibrary.gis_wgs84_to_cgcs2000"></a>

#### gis\_wgs84\_to\_cgcs2000

```python
@classmethod
def gis_wgs84_to_cgcs2000(cls, str_wgs84_lng: str, str_wgs84_lat: str,
                          str_wgs84_height: str) -> Tuple[str, str, str]
```

X.gis_wgs84_to_cgcs2000(str_wgs84_lng, str_wgs84_lat, str_wgs84_height) -> (str_cgcs2000_lng=str, str_cgcs2000_lat=str, str_cgcs2000_height=str)
GIS WGS84 to CGCS2000

Args:
    str_wgs84_lng (str): 
    str_wgs84_lat (str): 
    str_wgs84_height (str): 

Returns:
    tuple: 

    str_cgcs2000_lng (str): 

    str_cgcs2000_lat (str): 

    str_cgcs2000_height (str):

<a id="unreal.GISFunctionLibrary.gis_wgs84_to_bd09"></a>

#### gis\_wgs84\_to\_bd09

```python
@classmethod
def gis_wgs84_to_bd09(cls, str_wgs84_long: str,
                      str_wgs84_lat: str) -> Tuple[str, str]
```

X.gis_wgs84_to_bd09(str_wgs84_long, str_wgs84_lat) -> (str_bd09_long=str, str_bd09_lat=str)
GIS WGS84 to BD09

Args:
    str_wgs84_long (str): 
    str_wgs84_lat (str): 

Returns:
    tuple: 

    str_bd09_long (str): 

    str_bd09_lat (str):

<a id="unreal.GISFunctionLibrary.gis_ue_coord_to_long_lat_one_pivot"></a>

#### gis\_ue\_coord\_to\_long\_lat\_one\_pivot

```python
@classmethod
def gis_ue_coord_to_long_lat_one_pivot(
        cls,
        world_position: Vector,
        world_pivot: Vector,
        world_origin_long: str = "116.43859863",
        world_origin_lat: str = "39.95080618") -> GisInfo
```

X.gis_ue_coord_to_long_lat_one_pivot(world_position, world_pivot, world_origin_long="116.43859863", world_origin_lat="39.95080618") -> GisInfo
输入的ue4水平坐标数据
pivot的ue4水平坐标数据
参考pivot的gis坐标lat

Args:
    world_position (Vector): 
    world_pivot (Vector): 
    world_origin_long (str): 
    world_origin_lat (str): 

Returns:
    GisInfo:

<a id="unreal.GISFunctionLibrary.gis_ue_coord_to_long_lat_multi_pivots"></a>

#### gis\_ue\_coord\_to\_long\_lat\_multi\_pivots

```python
@classmethod
def gis_ue_coord_to_long_lat_multi_pivots(
        cls, loc: Vector, pivot_array: Array[GisInfo]) -> GisInfo
```

X.gis_ue_coord_to_long_lat_multi_pivots(loc, pivot_array) -> GisInfo
GIS UECoord to Long Lat Multi Pivots

Args:
    loc (Vector): 
    pivot_array (Array[GisInfo]): 

Returns:
    GisInfo:

<a id="unreal.GISFunctionLibrary.gis_long_lat_to_ue_coord_one_pivot"></a>

#### gis\_long\_lat\_to\_ue\_coord\_one\_pivot

```python
@classmethod
def gis_long_lat_to_ue_coord_one_pivot(cls,
                                       position_long: str,
                                       position_lat: str,
                                       world_pivot: Vector,
                                       world_origin_long: str = "116.43859863",
                                       world_origin_lat: str = "39.95080618",
                                       height: float = 0.000000) -> GisInfo
```

X.gis_long_lat_to_ue_coord_one_pivot(position_long, position_lat, world_pivot, world_origin_long="116.43859863", world_origin_lat="39.95080618", height=0.000000) -> GisInfo
输入的gis坐标long
输入的gis坐标lat
pivot的ue4水平坐标数据
参考pivot的gis坐标lat
参考pivot的gis坐标lat

Args:
    position_long (str): 
    position_lat (str): 
    world_pivot (Vector): 
    world_origin_long (str): 
    world_origin_lat (str): 
    height (float): 

Returns:
    GisInfo:

<a id="unreal.GISFunctionLibrary.gis_long_lat_to_ue_coord_multi_pivots"></a>

#### gis\_long\_lat\_to\_ue\_coord\_multi\_pivots

```python
@classmethod
def gis_long_lat_to_ue_coord_multi_pivots(cls,
                                          lng: str,
                                          lat: str,
                                          pivot_array: Array[GisInfo],
                                          height: float = 0.000000) -> GisInfo
```

X.gis_long_lat_to_ue_coord_multi_pivots(lng, lat, pivot_array, height=0.000000) -> GisInfo
输入的gis坐标long
输入的gis坐标lat
pivot1的ue4水平坐标数据

Args:
    lng (str): 
    lat (str): 
    pivot_array (Array[GisInfo]): 
    height (float): 

Returns:
    GisInfo:

<a id="unreal.GISFunctionLibrary.gis_gcj02_to_wgs84"></a>

#### gis\_gcj02\_to\_wgs84

```python
@classmethod
def gis_gcj02_to_wgs84(cls, str_gcj02_lng: str,
                       str_gcj02_lat: str) -> Tuple[str, str]
```

X.gis_gcj02_to_wgs84(str_gcj02_lng, str_gcj02_lat) -> (str_wgs84_lng=str, str_wgs84_lat=str)
GIS GCJ02 to WGS84

Args:
    str_gcj02_lng (str): 
    str_gcj02_lat (str): 

Returns:
    tuple: 

    str_wgs84_lng (str): 

    str_wgs84_lat (str):

<a id="unreal.GISFunctionLibrary.gis_gcj02_to_bd09"></a>

#### gis\_gcj02\_to\_bd09

```python
@classmethod
def gis_gcj02_to_bd09(cls, str_gcj02_long: str,
                      str_gcj02_lat: str) -> Tuple[str, str]
```

X.gis_gcj02_to_bd09(str_gcj02_long, str_gcj02_lat) -> (str_bd09_long=str, str_bd09_lat=str)
GIS GCJ02 to BD09

Args:
    str_gcj02_long (str): 
    str_gcj02_lat (str): 

Returns:
    tuple: 

    str_bd09_long (str): 

    str_bd09_lat (str):

<a id="unreal.GISFunctionLibrary.gis_cgcs2000_to_wgs84"></a>

#### gis\_cgcs2000\_to\_wgs84

```python
@classmethod
def gis_cgcs2000_to_wgs84(cls, str_cgcs2000_lng: str, str_cgcs2000_lat: str,
                          str_cgcs2000_height: str) -> Tuple[str, str, str]
```

X.gis_cgcs2000_to_wgs84(str_cgcs2000_lng, str_cgcs2000_lat, str_cgcs2000_height) -> (str_wgs84_lng=str, str_wgs84_lat=str, str_wgs84_height=str)
GIS CGCS2000 to WGS84

Args:
    str_cgcs2000_lng (str): 
    str_cgcs2000_lat (str): 
    str_cgcs2000_height (str): 

Returns:
    tuple: 

    str_wgs84_lng (str): 

    str_wgs84_lat (str): 

    str_wgs84_height (str):

<a id="unreal.GISFunctionLibrary.gis_beijing54_to_wgs84"></a>

#### gis\_beijing54\_to\_wgs84

```python
@classmethod
def gis_beijing54_to_wgs84(cls, str_beijing54_x: str, str_beijing54_y: str,
                           band_num: int) -> Tuple[str, str]
```

X.gis_beijing54_to_wgs84(str_beijing54_x, str_beijing54_y, band_num) -> (str_wgs84_lng=str, str_wgs84_lat=str)
GIS Beijing 54 to WGS84

Args:
    str_beijing54_x (str): 
    str_beijing54_y (str): 
    band_num (int32): 

Returns:
    tuple: 

    str_wgs84_lng (str): 

    str_wgs84_lat (str):

<a id="unreal.GISFunctionLibrary.gis_bd09_to_wgs84"></a>

#### gis\_bd09\_to\_wgs84

```python
@classmethod
def gis_bd09_to_wgs84(cls, str_bd09_long: str,
                      str_bd09_lat: str) -> Tuple[str, str]
```

X.gis_bd09_to_wgs84(str_bd09_long, str_bd09_lat) -> (str_wgs84_long=str, str_wgs84_lat=str)
GIS BD09 to WGS84

Args:
    str_bd09_long (str): 
    str_bd09_lat (str): 

Returns:
    tuple: 

    str_wgs84_long (str): 

    str_wgs84_lat (str):

<a id="unreal.GISFunctionLibrary.gis_bd09_to_gcj02"></a>

#### gis\_bd09\_to\_gcj02

```python
@classmethod
def gis_bd09_to_gcj02(cls, str_bd09_long: str,
                      str_bd09_lat: str) -> Tuple[str, str]
```

X.gis_bd09_to_gcj02(str_bd09_long, str_bd09_lat) -> (str_gcj02_long=str, str_gcj02_lat=str)
GIS BD09 to GCJ02

Args:
    str_bd09_long (str): 
    str_bd09_lat (str): 

Returns:
    tuple: 

    str_gcj02_long (str): 

    str_gcj02_lat (str):

<a id="unreal.WdpGeometryBPLibrary"></a>