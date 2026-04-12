## MeshHeatMapData Objects

```python
class MeshHeatMapData(StructBase)
```

Mesh Heat Map Data

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpDataV
- **File**: MeshHeatMapTools.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``colors`` (Array[LinearColor]):  [Read-Write]
- ``points`` (Array[Vector]):  [Read-Write]
- ``triangles`` (Array[int32]):  [Read-Write]

<a id="unreal.MeshHeatMapData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(points: Array[Vector] = [],
             colors: Array[LinearColor] = [],
             triangles: Array[int] = []) -> None
```

<a id="unreal.MeshHeatMapData.points"></a>

#### points

```python
@property
def points() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.MeshHeatMapData.points"></a>

#### points

```python
@points.setter
def points(value: Array[Vector]) -> None
```

<a id="unreal.MeshHeatMapData.colors"></a>

#### colors

```python
@property
def colors() -> Array[LinearColor]
```

(Array[LinearColor]):  [Read-Write]

<a id="unreal.MeshHeatMapData.colors"></a>

#### colors

```python
@colors.setter
def colors(value: Array[LinearColor]) -> None
```

<a id="unreal.MeshHeatMapData.triangles"></a>

#### triangles

```python
@property
def triangles() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.MeshHeatMapData.triangles"></a>

#### triangles

```python
@triangles.setter
def triangles(value: Array[int]) -> None
```

<a id="unreal.BatchPlaceAssetInfo"></a>