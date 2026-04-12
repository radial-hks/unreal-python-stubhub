## WdpGeometryBPLibrary Objects

```python
class WdpGeometryBPLibrary(BlueprintFunctionLibrary)
```

Wdp Geometry BPLibrary

**C++ Source:**

- **Plugin**: WdpCommon
- **Module**: WdpGeometry
- **File**: WdpGeometryBPLibrary.h

<a id="unreal.WdpGeometryBPLibrary.triangulate_polyline"></a>

#### triangulate\_polyline

```python
@classmethod
def triangulate_polyline(
        cls, polygon: WdpPolyline,
        width: float) -> Optional[Tuple[Array[Vector], Array[int]]]
```

X.triangulate_polyline(polygon, width) -> (out_vertexes=Array[Vector], out_triangles=Array[int32]) or None
Triangulate Polyline

Args:
    polygon (WdpPolyline): 
    width (double): 

Returns:
    tuple or None: 

    out_vertexes (Array[Vector]): 

    out_triangles (Array[int32]):

<a id="unreal.WdpGeometryBPLibrary.triangulate_polygon2d"></a>

#### triangulate\_polygon2d

```python
@classmethod
def triangulate_polygon2d(
    cls,
    polygon: WdpPolygon2D,
    level: WdpCurveSplitLevel = WdpCurveSplitLevel.LOW
) -> Optional[Tuple[Array[Vector2D], Array[int]]]
```

X.triangulate_polygon2d(polygon, level=WdpCurveSplitLevel.LOW) -> (out_vertexes=Array[Vector2D], out_triangles=Array[int32]) or None
Triangulate Polygon 2D

Args:
    polygon (WdpPolygon2D): 
    level (WdpCurveSplitLevel): 

Returns:
    tuple or None: 

    out_vertexes (Array[Vector2D]): 

    out_triangles (Array[int32]):

<a id="unreal.WdpGeometryBPLibrary.triangulate_polygon"></a>

#### triangulate\_polygon

```python
@classmethod
def triangulate_polygon(
        cls,
        polygon: WdpPolygon) -> Optional[Tuple[Array[Vector], Array[int]]]
```

X.triangulate_polygon(polygon) -> (out_vertexes=Array[Vector], out_triangles=Array[int32]) or None
Triangulate Polygon

Args:
    polygon (WdpPolygon): 

Returns:
    tuple or None: 

    out_vertexes (Array[Vector]): 

    out_triangles (Array[int32]):

<a id="unreal.WdpGeometryBPLibrary.polygon_to_polygon2d"></a>

#### polygon\_to\_polygon2d

```python
@classmethod
def polygon_to_polygon2d(cls, polygon: WdpPolygon) -> WdpPolygon2D
```

X.polygon_to_polygon2d(polygon) -> WdpPolygon2D
Polygon to Polygon 2D

Args:
    polygon (WdpPolygon): 

Returns:
    WdpPolygon2D:

<a id="unreal.WdpGeometryBPLibrary.polygon2d_to_polygon"></a>

#### polygon2d\_to\_polygon

```python
@classmethod
def polygon2d_to_polygon(cls,
                         polygon: WdpPolygon2D,
                         z: float = 0.000000) -> WdpPolygon
```

X.polygon2d_to_polygon(polygon, z=0.000000) -> WdpPolygon
Polygon 2DTo Polygon

Args:
    polygon (WdpPolygon2D): 
    z (double): 

Returns:
    WdpPolygon:

<a id="unreal.WdpGeometryBPLibrary.create_rectangle"></a>

#### create\_rectangle

```python
@classmethod
def create_rectangle(cls, start: Vector2D, end: Vector2D) -> WdpLoop2D
```

X.create_rectangle(start, end) -> WdpLoop2D
Create Rectangle

Args:
    start (Vector2D): 
    end (Vector2D): 

Returns:
    WdpLoop2D:

<a id="unreal.WdpGeometryBPLibrary.create_circle"></a>

#### create\_circle

```python
@classmethod
def create_circle(cls, origin: Vector2D, radius: float) -> WdpLoop2D
```

X.create_circle(origin, radius) -> WdpLoop2D
Create Circle

Args:
    origin (Vector2D): 
    radius (double): 

Returns:
    WdpLoop2D:

<a id="unreal.WdpGeometryBPLibrary.create_arc2d"></a>

#### create\_arc2d

```python
@classmethod
def create_arc2d(cls, start_point: Vector2D, end_point: Vector2D,
                 control_point: Vector2D) -> WdpArc2D
```

X.create_arc2d(start_point, end_point, control_point) -> WdpArc2D
Create Arc 2D

Args:
    start_point (Vector2D): 
    end_point (Vector2D): 
    control_point (Vector2D): 

Returns:
    WdpArc2D:

<a id="unreal.CoordinateUtils"></a>