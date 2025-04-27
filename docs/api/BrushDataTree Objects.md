## BrushDataTree Objects

```python
class BrushDataTree(StructBase)
```

Brush Data Tree

**C++ Source:**

- **Plugin**: Landmass
- **Module**: LandmassEditor
- **File**: LandmassManagerBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``brush_actors`` (Array[LandmassActor]):  [Read-Write]
- ``child_data_count`` (int32):  [Read-Write]
- ``current_level`` (int32):  [Read-Write]
- ``index_x0y0`` (int32):  [Read-Write]
- ``index_x0y1`` (int32):  [Read-Write]
- ``index_x1y0`` (int32):  [Read-Write]
- ``index_x1y1`` (int32):  [Read-Write]
- ``node_extents`` (Vector4):  [Read-Write]
- ``parent_index`` (int32):  [Read-Write]

<a id="unreal.BrushDataTree.__init__"></a>

#### __init__

```python
def __init__(
        current_level: int = 0,
        parent_index: int = 0,
        brush_actors: Array[LandmassActor] = [],
        index_x0y0: int = 0,
        index_x1y0: int = 0,
        index_x0y1: int = 0,
        index_x1y1: int = 0,
        child_data_count: int = 0,
        node_extents: Vector4 = [0.000000, 0.000000, 0.000000,
                                 0.000000]) -> None
```

<a id="unreal.BrushDataTree.current_level"></a>

#### current_level

```python
@property
def current_level() -> int
```

(int32):  [Read-Write]

<a id="unreal.BrushDataTree.current_level"></a>

#### current_level

```python
@current_level.setter
def current_level(value: int) -> None
```

<a id="unreal.BrushDataTree.parent_index"></a>

#### parent_index

```python
@property
def parent_index() -> int
```

(int32):  [Read-Write]

<a id="unreal.BrushDataTree.parent_index"></a>

#### parent_index

```python
@parent_index.setter
def parent_index(value: int) -> None
```

<a id="unreal.BrushDataTree.brush_actors"></a>

#### brush_actors

```python
@property
def brush_actors() -> Array[LandmassActor]
```

(Array[LandmassActor]):  [Read-Write]

<a id="unreal.BrushDataTree.brush_actors"></a>

#### brush_actors

```python
@brush_actors.setter
def brush_actors(value: Array[LandmassActor]) -> None
```

<a id="unreal.BrushDataTree.index_x0y0"></a>

#### index_x0y0

```python
@property
def index_x0y0() -> int
```

(int32):  [Read-Write]

<a id="unreal.BrushDataTree.index_x0y0"></a>

#### index_x0y0

```python
@index_x0y0.setter
def index_x0y0(value: int) -> None
```

<a id="unreal.BrushDataTree.index_x1y0"></a>

#### index_x1y0

```python
@property
def index_x1y0() -> int
```

(int32):  [Read-Write]

<a id="unreal.BrushDataTree.index_x1y0"></a>

#### index_x1y0

```python
@index_x1y0.setter
def index_x1y0(value: int) -> None
```

<a id="unreal.BrushDataTree.index_x0y1"></a>

#### index_x0y1

```python
@property
def index_x0y1() -> int
```

(int32):  [Read-Write]

<a id="unreal.BrushDataTree.index_x0y1"></a>

#### index_x0y1

```python
@index_x0y1.setter
def index_x0y1(value: int) -> None
```

<a id="unreal.BrushDataTree.index_x1y1"></a>

#### index_x1y1

```python
@property
def index_x1y1() -> int
```

(int32):  [Read-Write]

<a id="unreal.BrushDataTree.index_x1y1"></a>

#### index_x1y1

```python
@index_x1y1.setter
def index_x1y1(value: int) -> None
```

<a id="unreal.BrushDataTree.child_data_count"></a>

#### child_data_count

```python
@property
def child_data_count() -> int
```

(int32):  [Read-Write]

<a id="unreal.BrushDataTree.child_data_count"></a>

#### child_data_count

```python
@child_data_count.setter
def child_data_count(value: int) -> None
```

<a id="unreal.BrushDataTree.node_extents"></a>

#### node_extents

```python
@property
def node_extents() -> Vector4
```

(Vector4):  [Read-Write]

<a id="unreal.BrushDataTree.node_extents"></a>

#### node_extents

```python
@node_extents.setter
def node_extents(value: Vector4) -> None
```

<a id="unreal.LandmassLandscapeInfo"></a>