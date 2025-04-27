## MPCDIGeometryExportData Objects

```python
class MPCDIGeometryExportData(StructBase)
```

MPCDIGeometry Export Data

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterShaders
- **File**: MPCDIGeometryData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``normal`` (Array[Vector]):  [Read-Write]
- ``triangles`` (Array[int32]):  [Read-Write]
- ``uv`` (Array[Vector2D]):  [Read-Write]
- ``vertices`` (Array[Vector]):  [Read-Write]

<a id="unreal.MPCDIGeometryExportData.__init__"></a>

#### __init__

```python
def __init__(vertices: Array[Vector] = [],
             normal: Array[Vector] = [],
             uv: Array[Vector2D] = [],
             triangles: Array[int] = []) -> None
```

<a id="unreal.MPCDIGeometryExportData.vertices"></a>

#### vertices

```python
@property
def vertices() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.MPCDIGeometryExportData.vertices"></a>

#### vertices

```python
@vertices.setter
def vertices(value: Array[Vector]) -> None
```

<a id="unreal.MPCDIGeometryExportData.normal"></a>

#### normal

```python
@property
def normal() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.MPCDIGeometryExportData.normal"></a>

#### normal

```python
@normal.setter
def normal(value: Array[Vector]) -> None
```

<a id="unreal.MPCDIGeometryExportData.uv"></a>

#### uv

```python
@property
def uv() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.MPCDIGeometryExportData.uv"></a>

#### uv

```python
@uv.setter
def uv(value: Array[Vector2D]) -> None
```

<a id="unreal.MPCDIGeometryExportData.triangles"></a>

#### triangles

```python
@property
def triangles() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.MPCDIGeometryExportData.triangles"></a>

#### triangles

```python
@triangles.setter
def triangles(value: Array[int]) -> None
```

<a id="unreal.AnamorphicDistortionParameters"></a>