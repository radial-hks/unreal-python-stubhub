## BimSnapResult Objects

```python
class BimSnapResult(StructBase)
```

Bim Snap Result

**C++ Source:**

- **Plugin**: WdpAssetLoader
- **Module**: BimAssetLoader
- **File**: DCPDataBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``snap_type`` (BimSnapType):  [Read-Write]
- ``snaped_edge_end_point`` (Vector):  [Read-Write] 吸附到边 边的起点
- ``snaped_edge_start_point`` (Vector):  [Read-Write] 吸附类型
- ``snaped_point_on_edge`` (Vector):  [Read-Write] 吸附到边 边的终点
- ``snaped_vertex_point`` (Vector):  [Read-Write] 吸附到边 当前点到吸附到边的 最短距离点
- ``snapped_edge_foot_point`` (Vector):  [Read-Write] 吸附到边  当前点到吸附到边 边上(最接近边上)的点
- ``snapped_face_normal`` (Vector):  [Read-Write] 吸附面 吸附的点
- ``snapped_face_point`` (Vector):  [Read-Write] 吸附到顶点 吸附的顶点

<a id="unreal.BimSnapResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        snap_type: BimSnapType = BimSnapType.VERTEX_SNAP,
        snaped_edge_start_point: Vector = [0.000000, 0.000000, 0.000000],
        snaped_edge_end_point: Vector = [0.000000, 0.000000, 0.000000],
        snaped_point_on_edge: Vector = [0.000000, 0.000000, 0.000000],
        snapped_edge_foot_point: Vector = [0.000000, 0.000000, 0.000000],
        snaped_vertex_point: Vector = [0.000000, 0.000000, 0.000000],
        snapped_face_point: Vector = [0.000000, 0.000000, 0.000000],
        snapped_face_normal: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.BimSnapResult.snap_type"></a>

#### snap\_type

```python
@property
def snap_type() -> BimSnapType
```

(BimSnapType):  [Read-Write]

<a id="unreal.BimSnapResult.snap_type"></a>

#### snap\_type

```python
@snap_type.setter
def snap_type(value: BimSnapType) -> None
```

<a id="unreal.BimSnapResult.snaped_edge_start_point"></a>

#### snaped\_edge\_start\_point

```python
@property
def snaped_edge_start_point() -> Vector
```

(Vector):  [Read-Write] 吸附类型

<a id="unreal.BimSnapResult.snaped_edge_start_point"></a>

#### snaped\_edge\_start\_point

```python
@snaped_edge_start_point.setter
def snaped_edge_start_point(value: Vector) -> None
```

<a id="unreal.BimSnapResult.snaped_edge_end_point"></a>

#### snaped\_edge\_end\_point

```python
@property
def snaped_edge_end_point() -> Vector
```

(Vector):  [Read-Write] 吸附到边 边的起点

<a id="unreal.BimSnapResult.snaped_edge_end_point"></a>

#### snaped\_edge\_end\_point

```python
@snaped_edge_end_point.setter
def snaped_edge_end_point(value: Vector) -> None
```

<a id="unreal.BimSnapResult.snaped_point_on_edge"></a>

#### snaped\_point\_on\_edge

```python
@property
def snaped_point_on_edge() -> Vector
```

(Vector):  [Read-Write] 吸附到边 边的终点

<a id="unreal.BimSnapResult.snaped_point_on_edge"></a>

#### snaped\_point\_on\_edge

```python
@snaped_point_on_edge.setter
def snaped_point_on_edge(value: Vector) -> None
```

<a id="unreal.BimSnapResult.snapped_edge_foot_point"></a>

#### snapped\_edge\_foot\_point

```python
@property
def snapped_edge_foot_point() -> Vector
```

(Vector):  [Read-Write] 吸附到边  当前点到吸附到边 边上(最接近边上)的点

<a id="unreal.BimSnapResult.snapped_edge_foot_point"></a>

#### snapped\_edge\_foot\_point

```python
@snapped_edge_foot_point.setter
def snapped_edge_foot_point(value: Vector) -> None
```

<a id="unreal.BimSnapResult.snaped_vertex_point"></a>

#### snaped\_vertex\_point

```python
@property
def snaped_vertex_point() -> Vector
```

(Vector):  [Read-Write] 吸附到边 当前点到吸附到边的 最短距离点

<a id="unreal.BimSnapResult.snaped_vertex_point"></a>

#### snaped\_vertex\_point

```python
@snaped_vertex_point.setter
def snaped_vertex_point(value: Vector) -> None
```

<a id="unreal.BimSnapResult.snapped_face_point"></a>

#### snapped\_face\_point

```python
@property
def snapped_face_point() -> Vector
```

(Vector):  [Read-Write] 吸附到顶点 吸附的顶点

<a id="unreal.BimSnapResult.snapped_face_point"></a>

#### snapped\_face\_point

```python
@snapped_face_point.setter
def snapped_face_point(value: Vector) -> None
```

<a id="unreal.BimSnapResult.snapped_face_normal"></a>

#### snapped\_face\_normal

```python
@property
def snapped_face_normal() -> Vector
```

(Vector):  [Read-Write] 吸附面 吸附的点

<a id="unreal.BimSnapResult.snapped_face_normal"></a>

#### snapped\_face\_normal

```python
@snapped_face_normal.setter
def snapped_face_normal(value: Vector) -> None
```

<a id="unreal.BimNodeOutlineStyle"></a>