## GeometryScriptSimpleMeshBuffers Objects

```python
class GeometryScriptSimpleMeshBuffers(StructBase)
```

Geometry Script Simple Mesh Buffers

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshBasicEditFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``normals`` (Array[Vector]):  [Read-Write]
- ``tri_group_i_ds`` (Array[int32]):  [Read-Write]
- ``triangles`` (Array[IntVector]):  [Read-Write]
- ``uv0`` (Array[Vector2D]):  [Read-Write]
- ``uv1`` (Array[Vector2D]):  [Read-Write]
- ``uv2`` (Array[Vector2D]):  [Read-Write]
- ``uv3`` (Array[Vector2D]):  [Read-Write]
- ``uv4`` (Array[Vector2D]):  [Read-Write]
- ``uv5`` (Array[Vector2D]):  [Read-Write]
- ``uv6`` (Array[Vector2D]):  [Read-Write]
- ``uv7`` (Array[Vector2D]):  [Read-Write]
- ``vertex_colors`` (Array[LinearColor]):  [Read-Write]
- ``vertices`` (Array[Vector]):  [Read-Write]

<a id="unreal.GeometryScriptSimpleMeshBuffers.__init__"></a>

#### __init__

```python
def __init__(vertices: Array[Vector] = [],
             normals: Array[Vector] = [],
             uv0: Array[Vector2D] = [],
             uv1: Array[Vector2D] = [],
             uv2: Array[Vector2D] = [],
             uv3: Array[Vector2D] = [],
             uv4: Array[Vector2D] = [],
             uv5: Array[Vector2D] = [],
             uv6: Array[Vector2D] = [],
             uv7: Array[Vector2D] = [],
             vertex_colors: Array[LinearColor] = [],
             triangles: Array[IntVector] = [],
             tri_group_i_ds: Array[int] = []) -> None
```

<a id="unreal.GeometryScriptSimpleMeshBuffers.vertices"></a>

#### vertices

```python
@property
def vertices() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.GeometryScriptSimpleMeshBuffers.vertices"></a>

#### vertices

```python
@vertices.setter
def vertices(value: Array[Vector]) -> None
```

<a id="unreal.GeometryScriptSimpleMeshBuffers.normals"></a>

#### normals

```python
@property
def normals() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.GeometryScriptSimpleMeshBuffers.normals"></a>

#### normals

```python
@normals.setter
def normals(value: Array[Vector]) -> None
```

<a id="unreal.GeometryScriptSimpleMeshBuffers.uv0"></a>

#### uv0

```python
@property
def uv0() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.GeometryScriptSimpleMeshBuffers.uv0"></a>

#### uv0

```python
@uv0.setter
def uv0(value: Array[Vector2D]) -> None
```

<a id="unreal.GeometryScriptSimpleMeshBuffers.uv1"></a>

#### uv1

```python
@property
def uv1() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.GeometryScriptSimpleMeshBuffers.uv1"></a>

#### uv1

```python
@uv1.setter
def uv1(value: Array[Vector2D]) -> None
```

<a id="unreal.GeometryScriptSimpleMeshBuffers.uv2"></a>

#### uv2

```python
@property
def uv2() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.GeometryScriptSimpleMeshBuffers.uv2"></a>

#### uv2

```python
@uv2.setter
def uv2(value: Array[Vector2D]) -> None
```

<a id="unreal.GeometryScriptSimpleMeshBuffers.uv3"></a>

#### uv3

```python
@property
def uv3() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.GeometryScriptSimpleMeshBuffers.uv3"></a>

#### uv3

```python
@uv3.setter
def uv3(value: Array[Vector2D]) -> None
```

<a id="unreal.GeometryScriptSimpleMeshBuffers.uv4"></a>

#### uv4

```python
@property
def uv4() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.GeometryScriptSimpleMeshBuffers.uv4"></a>

#### uv4

```python
@uv4.setter
def uv4(value: Array[Vector2D]) -> None
```

<a id="unreal.GeometryScriptSimpleMeshBuffers.uv5"></a>

#### uv5

```python
@property
def uv5() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.GeometryScriptSimpleMeshBuffers.uv5"></a>

#### uv5

```python
@uv5.setter
def uv5(value: Array[Vector2D]) -> None
```

<a id="unreal.GeometryScriptSimpleMeshBuffers.uv6"></a>

#### uv6

```python
@property
def uv6() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.GeometryScriptSimpleMeshBuffers.uv6"></a>

#### uv6

```python
@uv6.setter
def uv6(value: Array[Vector2D]) -> None
```

<a id="unreal.GeometryScriptSimpleMeshBuffers.uv7"></a>

#### uv7

```python
@property
def uv7() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.GeometryScriptSimpleMeshBuffers.uv7"></a>

#### uv7

```python
@uv7.setter
def uv7(value: Array[Vector2D]) -> None
```

<a id="unreal.GeometryScriptSimpleMeshBuffers.vertex_colors"></a>

#### vertex_colors

```python
@property
def vertex_colors() -> Array[LinearColor]
```

(Array[LinearColor]):  [Read-Write]

<a id="unreal.GeometryScriptSimpleMeshBuffers.vertex_colors"></a>

#### vertex_colors

```python
@vertex_colors.setter
def vertex_colors(value: Array[LinearColor]) -> None
```

<a id="unreal.GeometryScriptSimpleMeshBuffers.triangles"></a>

#### triangles

```python
@property
def triangles() -> Array[IntVector]
```

(Array[IntVector]):  [Read-Write]

<a id="unreal.GeometryScriptSimpleMeshBuffers.triangles"></a>

#### triangles

```python
@triangles.setter
def triangles(value: Array[IntVector]) -> None
```

<a id="unreal.GeometryScriptSimpleMeshBuffers.tri_group_i_ds"></a>

#### tri_group_i_ds

```python
@property
def tri_group_i_ds() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.GeometryScriptSimpleMeshBuffers.tri_group_i_ds"></a>

#### tri_group_i_ds

```python
@tri_group_i_ds.setter
def tri_group_i_ds(value: Array[int]) -> None
```

<a id="unreal.GeometryScriptAppendMeshOptions"></a>