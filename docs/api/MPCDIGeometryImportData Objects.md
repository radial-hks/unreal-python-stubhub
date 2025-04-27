## MPCDIGeometryImportData Objects

```python
class MPCDIGeometryImportData(StructBase)
```

MPCDIGeometry Import Data

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterShaders
- **File**: MPCDIGeometryData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``height`` (int32):  [Read-Write]
- ``vertices`` (Array[Vector]):  [Read-Write]
- ``width`` (int32):  [Read-Write]

<a id="unreal.MPCDIGeometryImportData.__init__"></a>

#### __init__

```python
def __init__(width: int = 0,
             height: int = 0,
             vertices: Array[Vector] = []) -> None
```

<a id="unreal.MPCDIGeometryImportData.width"></a>

#### width

```python
@property
def width() -> int
```

(int32):  [Read-Write]

<a id="unreal.MPCDIGeometryImportData.width"></a>

#### width

```python
@width.setter
def width(value: int) -> None
```

<a id="unreal.MPCDIGeometryImportData.height"></a>

#### height

```python
@property
def height() -> int
```

(int32):  [Read-Write]

<a id="unreal.MPCDIGeometryImportData.height"></a>

#### height

```python
@height.setter
def height(value: int) -> None
```

<a id="unreal.MPCDIGeometryImportData.vertices"></a>

#### vertices

```python
@property
def vertices() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.MPCDIGeometryImportData.vertices"></a>

#### vertices

```python
@vertices.setter
def vertices(value: Array[Vector]) -> None
```

<a id="unreal.MPCDIGeometryExportData"></a>