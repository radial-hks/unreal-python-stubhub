## StartMiniMapParams Objects

```python
class StartMiniMapParams(ParamsBase)
```

Start Mini Map Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: MiniMapAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``display`` (MiniMapDisplay):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``mapping_anchors`` (Array[Vector2D]):  [Read-Write]
- ``source`` (MiniMapSource):  [Read-Write]
- ``type`` (str):  [Read-Write]

<a id="unreal.StartMiniMapParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    type: str = "",
    source: MiniMapSource = [
        "http://superapi.51aes.com/doc-static/images/static/MiniMap/Minimap.png",
        "http://superapi.51aes.com/doc-static/images/static/MiniMap/Minimap_needle.png",
        "http://superapi.51aes.com/doc-static/images/static/MiniMap/Minimap_mask.jpg",
        "http://superapi.51aes.com/doc-static/images/static/MiniMap/Minimap_outline.png"
    ],
    mapping_anchors: Array[Vector2D] = [],
    display: MiniMapDisplay = [[300.000000, 100.000000], 300,
                               "leftTop"]) -> None
```

<a id="unreal.StartMiniMapParams.type"></a>

#### type

```python
@property
def type() -> str
```

(str):  [Read-Write]

<a id="unreal.StartMiniMapParams.type"></a>

#### type

```python
@type.setter
def type(value: str) -> None
```

<a id="unreal.StartMiniMapParams.source"></a>

#### source

```python
@property
def source() -> MiniMapSource
```

(MiniMapSource):  [Read-Write]

<a id="unreal.StartMiniMapParams.source"></a>

#### source

```python
@source.setter
def source(value: MiniMapSource) -> None
```

<a id="unreal.StartMiniMapParams.mapping_anchors"></a>

#### mapping\_anchors

```python
@property
def mapping_anchors() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.StartMiniMapParams.mapping_anchors"></a>

#### mapping\_anchors

```python
@mapping_anchors.setter
def mapping_anchors(value: Array[Vector2D]) -> None
```

<a id="unreal.StartMiniMapParams.display"></a>

#### display

```python
@property
def display() -> MiniMapDisplay
```

(MiniMapDisplay):  [Read-Write]

<a id="unreal.StartMiniMapParams.display"></a>

#### display

```python
@display.setter
def display(value: MiniMapDisplay) -> None
```

<a id="unreal.MoveLinearData"></a>