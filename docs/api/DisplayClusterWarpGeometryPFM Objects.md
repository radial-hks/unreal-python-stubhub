## DisplayClusterWarpGeometryPFM Objects

```python
class DisplayClusterWarpGeometryPFM(StructBase)
```

3D geometry that can be used for warping, in an PFM-like format
UE scale used: 1 unit = 1 centimeter

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterWarp
- **File**: DisplayClusterWarpGeometry.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``height`` (int32):  [Read-Write] Number of vertices vertically.
- ``vertices`` (Array[Vector]):  [Read-Write] An array with vertices. The total number of vertices in this array must be equal to Width*Height.
- ``width`` (int32):  [Read-Write] Number of vertices horizontally.

<a id="unreal.DisplayClusterWarpGeometryPFM.__init__"></a>

#### __init__

```python
def __init__(width: int = 0,
             height: int = 0,
             vertices: Array[Vector] = []) -> None
```

<a id="unreal.DisplayClusterWarpGeometryPFM.width"></a>

#### width

```python
@property
def width() -> int
```

(int32):  [Read-Write] Number of vertices horizontally.

<a id="unreal.DisplayClusterWarpGeometryPFM.width"></a>

#### width

```python
@width.setter
def width(value: int) -> None
```

<a id="unreal.DisplayClusterWarpGeometryPFM.height"></a>

#### height

```python
@property
def height() -> int
```

(int32):  [Read-Write] Number of vertices vertically.

<a id="unreal.DisplayClusterWarpGeometryPFM.height"></a>

#### height

```python
@height.setter
def height(value: int) -> None
```

<a id="unreal.DisplayClusterWarpGeometryPFM.vertices"></a>

#### vertices

```python
@property
def vertices() -> Array[Vector]
```

(Array[Vector]):  [Read-Write] An array with vertices. The total number of vertices in this array must be equal to Width*Height.

<a id="unreal.DisplayClusterWarpGeometryPFM.vertices"></a>

#### vertices

```python
@vertices.setter
def vertices(value: Array[Vector]) -> None
```

<a id="unreal.DisplayClusterWarpGeometryOBJ"></a>