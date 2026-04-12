## AesEntity Objects

```python
class AesEntity(BlueprintFunctionLibrary)
```

Function library to expose AesEntity Functions to Blueprints

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesEntity
- **File**: AesEntityBlueprintFunctionLibrary.h

<a id="unreal.AesEntity.update_texture2d_array_source"></a>

#### update\_texture2d\_array\_source

```python
@classmethod
def update_texture2d_array_source(cls,
                                  texture2d_array: Texture2DArray) -> None
```

X.update_texture2d_array_source(texture2d_array) -> None
Update Texture 2DArray Source

Args:
    texture2d_array (Texture2DArray):

<a id="unreal.AesEntity.triangulate_simple_polygon"></a>

#### triangulate\_simple\_polygon

```python
@classmethod
def triangulate_simple_polygon(cls, vertices: Array[Vector]) -> Array[int]
```

X.triangulate_simple_polygon(vertices) -> Array[int32]
Triangulate Simple Polygon

Args:
    vertices (Array[Vector]): 

Returns:
    Array[int32]:

<a id="unreal.AesEntity.set_source_textures"></a>

#### set\_source\_textures

```python
@classmethod
def set_source_textures(cls, texture2d_array: Texture2DArray,
                        textures: Array[Texture2D]) -> None
```

X.set_source_textures(texture2d_array, textures) -> None
Set Source Textures

Args:
    texture2d_array (Texture2DArray): 
    textures (Array[Texture2D]):

<a id="unreal.AesEntity.set_component_creation_method_to_instance"></a>

#### set\_component\_creation\_method\_to\_instance

```python
@classmethod
def set_component_creation_method_to_instance(
        cls, component: PrimitiveComponent) -> None
```

X.set_component_creation_method_to_instance(component) -> None
Set Component Creation Method to Instance

Args:
    component (PrimitiveComponent):

<a id="unreal.AesEntity.new_guid"></a>

#### new\_guid

```python
@classmethod
def new_guid(cls) -> int
```

X.new_guid() -> int64
New Guid

Returns:
    int64:

<a id="unreal.AesEntity.multi_thread_test"></a>

#### multi\_thread\_test

```python
@classmethod
def multi_thread_test(cls, component: InstancedStaticMeshComponent,
                      static_mesh: StaticMesh) -> None
```

X.multi_thread_test(component, static_mesh) -> None
Multi Thread Test

Args:
    component (InstancedStaticMeshComponent): 
    static_mesh (StaticMesh):

<a id="unreal.AesEntity.is_point_in_polygon"></a>

#### is\_point\_in\_polygon

```python
@classmethod
def is_point_in_polygon(cls, test_point: Vector,
                        polygon_points: Array[Vector]) -> bool
```

X.is_point_in_polygon(test_point, polygon_points) -> bool
Returns true if TestPoint is inside the polygon defined by PolygonPoints

Args:
    test_point (Vector): 
    polygon_points (Array[Vector]): 

Returns:
    bool:

<a id="unreal.AesEntity.get_source_textures"></a>

#### get\_source\_textures

```python
@classmethod
def get_source_textures(cls,
                        texture2d_array: Texture2DArray) -> Array[Texture2D]
```

X.get_source_textures(texture2d_array) -> Array[Texture2D]
Get Source Textures

Args:
    texture2d_array (Texture2DArray): 

Returns:
    Array[Texture2D]:

<a id="unreal.AesEntity.conv_world_location_to_lon_lat"></a>

#### conv\_world\_location\_to\_lon\_lat

```python
@classmethod
def conv_world_location_to_lon_lat(cls, world_context_object: Object,
                                   location: Vector) -> Vector
```

X.conv_world_location_to_lon_lat(world_context_object, location) -> Vector
空间直角坐标转经纬度坐标

Args:
    world_context_object (Object): 
    location (Vector): 空间直角坐标（厘米）

Returns:
    Vector: {经度，纬度，海拔向量}（厘米）

<a id="unreal.AesEntity.conv_quad_key_to_lon_lat"></a>

#### conv\_quad\_key\_to\_lon\_lat

```python
@classmethod
def conv_quad_key_to_lon_lat(
        cls,
        world_context_object: Object,
        quad_key: str,
        offset: Vector2D = [0.000000, 0.000000]) -> Tuple[Vector2D, str]
```

X.conv_quad_key_to_lon_lat(world_context_object, quad_key, offset=[0.000000, 0.000000]) -> (Vector2D, quad_key=str)
通过Tile索引值求得Tile中某点位的经纬度（0,0为Tile左上角点位）

Args:
    world_context_object (Object): 
    quad_key (str): Tile索引值
    offset (Vector2D): 点位UV偏移值

Returns:
    str: 

    quad_key (str): Tile索引值

<a id="unreal.AesEntity.conv_lon_lat_to_world_transform"></a>

#### conv\_lon\_lat\_to\_world\_transform

```python
@classmethod
def conv_lon_lat_to_world_transform(cls,
                                    world_context_object: Object,
                                    lon: float,
                                    lat: float,
                                    alt: float = 0.000000) -> Transform
```

X.conv_lon_lat_to_world_transform(world_context_object, lon, lat, alt=0.000000) -> Transform
通过经纬度坐标求得空间直角变换

Args:
    world_context_object (Object): 
    lon (double): 经度
    lat (double): 纬度
    alt (double): 海拔高度（厘米）

Returns:
    Transform:

<a id="unreal.AesEntity.conv_lon_lat_to_world_location"></a>

#### conv\_lon\_lat\_to\_world\_location

```python
@classmethod
def conv_lon_lat_to_world_location(cls,
                                   world_context_object: Object,
                                   lon: float,
                                   lat: float,
                                   alt: float = 0.000000) -> Vector
```

X.conv_lon_lat_to_world_location(world_context_object, lon, lat, alt=0.000000) -> Vector
经纬度坐标转空间直角坐标

Args:
    world_context_object (Object): 
    lon (double): 经度
    lat (double): 纬度
    alt (double): 海拔高度（厘米）

Returns:
    Vector: 空间直角坐标（厘米）

<a id="unreal.AesEntity.conv_lon_lat_to_quad_key"></a>

#### conv\_lon\_lat\_to\_quad\_key

```python
@classmethod
def conv_lon_lat_to_quad_key(cls, world_context_object: Object, lon: float,
                             lat: float, zoom: int) -> str
```

X.conv_lon_lat_to_quad_key(world_context_object, lon, lat, zoom) -> str
求当前经纬度在指定缩放级别时的Tile索引值

Args:
    world_context_object (Object): 
    lon (double): 经度
    lat (double): 纬度
    zoom (int32): 缩放级别

Returns:
    str:

<a id="unreal.AesEntitySettings"></a>