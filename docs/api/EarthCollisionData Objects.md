## EarthCollisionData Objects

```python
class EarthCollisionData(StructBase)
```

碰撞数据缓存结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthMeshFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bounds`` (Box):  [Read-Write] 包围盒
- ``index_buffer`` (Array[int32]):  [Read-Write] 索引缓冲区
- ``vertex_buffer`` (Array[Vector3f]):  [Read-Write] 顶点缓冲区

<a id="unreal.EarthCollisionData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    vertex_buffer: Array[Vector3f] = [],
    index_buffer: Array[int] = [],
    bounds: Box = [[0.000000, 0.000000, 0.000000],
                   [0.000000, 0.000000, 0.000000], False]
) -> None
```

<a id="unreal.EarthCollisionData.vertex_buffer"></a>

#### vertex\_buffer

```python
@property
def vertex_buffer() -> Array[Vector3f]
```

(Array[Vector3f]):  [Read-Write] 顶点缓冲区

<a id="unreal.EarthCollisionData.vertex_buffer"></a>

#### vertex\_buffer

```python
@vertex_buffer.setter
def vertex_buffer(value: Array[Vector3f]) -> None
```

<a id="unreal.EarthCollisionData.index_buffer"></a>

#### index\_buffer

```python
@property
def index_buffer() -> Array[int]
```

(Array[int32]):  [Read-Write] 索引缓冲区

<a id="unreal.EarthCollisionData.index_buffer"></a>

#### index\_buffer

```python
@index_buffer.setter
def index_buffer(value: Array[int]) -> None
```

<a id="unreal.EarthCollisionData.bounds"></a>

#### bounds

```python
@property
def bounds() -> Box
```

(Box):  [Read-Write] 包围盒

<a id="unreal.EarthCollisionData.bounds"></a>

#### bounds

```python
@bounds.setter
def bounds(value: Box) -> None
```

<a id="unreal.EarthStaticMeshAssetFragment"></a>