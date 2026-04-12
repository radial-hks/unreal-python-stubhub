## EarthSpatialDataLibrary Objects

```python
class EarthSpatialDataLibrary(BlueprintFunctionLibrary)
```

空间数据函数库

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthSpatialDataLibrary.h

<a id="unreal.EarthSpatialDataLibrary.signed_area2d"></a>

#### signed\_area2d

```python
@classmethod
def signed_area2d(cls, vertices: Array[Vector]) -> float
```

X.signed_area2d(vertices) -> double
计算带符号的多边形面积

Args:
    vertices (Array[Vector]): 

Returns:
    double:

<a id="unreal.EarthSpatialDataLibrary.offset_vertices_with_distances"></a>

#### offset\_vertices\_with\_distances

```python
@classmethod
def offset_vertices_with_distances(cls,
                                   connection_points: Array[bool],
                                   distances: Array[float],
                                   closed_loop: bool = True) -> Array[Vector]
```

X.offset_vertices_with_distances(connection_points, distances, closed_loop=True) -> Array[Vector]
对轮廓线应用偏移量

Args:
    connection_points (Array[bool]): 
    distances (Array[float]): 
    closed_loop (bool): 

Returns:
    Array[Vector]: 

    out_vertices (Array[Vector]):

<a id="unreal.EarthSpatialDataLibrary.offset_vertices"></a>

#### offset\_vertices

```python
@classmethod
def offset_vertices(cls,
                    connection_points: Array[bool],
                    distance: float = 1.000000,
                    closed_loop: bool = True) -> Array[Vector]
```

X.offset_vertices(connection_points, distance=1.000000, closed_loop=True) -> Array[Vector]
对轮廓线应用偏移量

Args:
    connection_points (Array[bool]): 
    distance (float): 
    closed_loop (bool): 

Returns:
    Array[Vector]: 

    out_vertices (Array[Vector]):

<a id="unreal.EarthSpatialDataLibrary.min_area_rectangle"></a>

#### min\_area\_rectangle

```python
@classmethod
def min_area_rectangle(
        cls, points: Array[Vector],
        sample_surface_normal: Vector) -> Tuple[Vector, Vector, Vector]
```

X.min_area_rectangle(points, sample_surface_normal) -> (out_rect_center=Vector, out_side_vector_x=Vector, out_side_vector_y=Vector)
获取最小面积矩形的参数，来源于UKismetMathLibrary::MinAreaRectangle，修改了返回的参数

Args:
    points (Array[Vector]): 
    sample_surface_normal (Vector): 

Returns:
    tuple: 

    out_rect_center (Vector): 

    out_side_vector_x (Vector): 

    out_side_vector_y (Vector):

<a id="unreal.EarthSpatialDataLibrary.lot_subdivision_polygon"></a>

#### lot\_subdivision\_polygon

```python
@classmethod
def lot_subdivision_polygon(
        cls,
        vertices: Array[Vector],
        random_stream: RandomStream,
        iterations: int = 3,
        minimum_lot_size: float = 1000000.000000,
        irregularity: float = 0.000000) -> Array[EarthPrimitiveFragment]
```

X.lot_subdivision_polygon(vertices, random_stream, iterations=3, minimum_lot_size=1000000.000000, irregularity=0.000000) -> Array[EarthPrimitiveFragment]
使用地块分割法分割多边形，可反复将多边形划分为更小的地块，并可控制最小尺寸、迭代次数和不规则度

Args:
    vertices (Array[Vector]): 输入的多边形轮廓线
    random_stream (RandomStream): 随机种子
    iterations (int32): 分割细分次数，1次会生成2个片元，2次会生成4个片元，以此类推
    minimum_lot_size (float): 小于此尺寸的片元将不再被分割，单位为平方厘米
    irregularity (float): 分割的不规则度，较小的值意味着分割会在一个片元的中点进行，较大的值则会产生大小不同的片元

Returns:
    Array[EarthPrimitiveFragment]:

<a id="unreal.EarthSpatialDataLibrary.loop_is_clockwise"></a>

#### loop\_is\_clockwise

```python
@classmethod
def loop_is_clockwise(cls, points: Array[Vector]) -> bool
```

X.loop_is_clockwise(points) -> bool
Loop Is Clockwise

Args:
    points (Array[Vector]): 

Returns:
    bool:

<a id="unreal.EarthSpatialDataLibrary.is_valid_transform"></a>

#### is\_valid\_transform

```python
@classmethod
def is_valid_transform(cls, transform: Transform) -> bool
```

X.is_valid_transform(transform) -> bool
检查Transform是否有效

Args:
    transform (Transform): 

Returns:
    bool:

<a id="unreal.EarthSpatialDataLibrary.is_polygon_self_intersecting"></a>

#### is\_polygon\_self\_intersecting

```python
@classmethod
def is_polygon_self_intersecting(cls, points: Array[Vector2D],
                                 allow_looping: bool) -> bool
```

X.is_polygon_self_intersecting(points, allow_looping) -> bool
Is Polygon Self Intersecting

Args:
    points (Array[Vector2D]): 
    allow_looping (bool): 

Returns:
    bool:

<a id="unreal.EarthSpatialDataLibrary.is_point_in_polygon"></a>

#### is\_point\_in\_polygon

```python
@classmethod
def is_point_in_polygon(cls, test_point: Vector,
                        polygon_points: Array[Vector]) -> bool
```

X.is_point_in_polygon(test_point, polygon_points) -> bool
Is Point in Polygon

Args:
    test_point (Vector): 
    polygon_points (Array[Vector]): 

Returns:
    bool:

<a id="unreal.EarthSpatialDataLibrary.is_point2d_in_polygon2d"></a>

#### is\_point2d\_in\_polygon2d

```python
@classmethod
def is_point2d_in_polygon2d(cls, point: Vector2D,
                            polygon_points: Array[Vector2D]) -> bool
```

X.is_point2d_in_polygon2d(point, polygon_points) -> bool
Is Point 2DIn Polygon 2D

Args:
    point (Vector2D): 
    polygon_points (Array[Vector2D]): 

Returns:
    bool:

<a id="unreal.EarthSpatialDataLibrary.fuse_closed_point"></a>

#### fuse\_closed\_point

```python
@classmethod
def fuse_closed_point(cls, snap_distance: float,
                      closed_loop: bool) -> Array[Vector]
```

X.fuse_closed_point(snap_distance, closed_loop) -> Array[Vector]
熔合靠近的点

Args:
    snap_distance (float): 
    closed_loop (bool): 

Returns:
    Array[Vector]: 

    nodes (Array[Vector]):

<a id="unreal.EarthSpatialDataLibrary.flatten_to_zero"></a>

#### flatten\_to\_zero

```python
@classmethod
def flatten_to_zero(cls) -> Array[Vector]
```

X.flatten_to_zero() -> Array[Vector]
Flatten to Zero

Returns:
    Array[Vector]: 

    points (Array[Vector]):

<a id="unreal.EarthSpatialDataLibrary.flatten_pos_z"></a>

#### flatten\_pos\_z

```python
@classmethod
def flatten_pos_z(cls, z_offset: float) -> Array[Vector]
```

X.flatten_pos_z(z_offset) -> Array[Vector]
Flatten Pos Z

Args:
    z_offset (float): 

Returns:
    Array[Vector]: 

    points (Array[Vector]):

<a id="unreal.EarthSpatialDataLibrary.facet"></a>

#### facet

```python
@classmethod
def facet(cls,
          tolerance: float = 0.000100,
          closed_loop: bool = True) -> Array[Vector]
```

X.facet(tolerance=0.000100, closed_loop=True) -> Array[Vector]
平滑轮廓线

Args:
    tolerance (float): 
    closed_loop (bool): 

Returns:
    Array[Vector]: 

    out_vertices (Array[Vector]):

<a id="unreal.EarthSplineComponent"></a>