## TextureBound Objects

```python
class TextureBound(StructBase)
```

Texture Bound

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: SuperAPI_Raster
- **File**: SuperAPI_RasterCommon.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``left_bottom_lat`` (str):  [Read-Write]
- ``left_bottom_lon`` (str):  [Read-Write]
- ``right_top_lat`` (str):  [Read-Write]
- ``right_top_lon`` (str):  [Read-Write]

<a id="unreal.TextureBound.__init__"></a>

#### \_\_init\_\_

```python
def __init__(left_bottom_lon: str = "",
             left_bottom_lat: str = "",
             right_top_lon: str = "",
             right_top_lat: str = "") -> None
```

<a id="unreal.TextureBound.left_bottom_lon"></a>

#### left\_bottom\_lon

```python
@property
def left_bottom_lon() -> str
```

(str):  [Read-Only]

<a id="unreal.TextureBound.left_bottom_lat"></a>

#### left\_bottom\_lat

```python
@property
def left_bottom_lat() -> str
```

(str):  [Read-Only]

<a id="unreal.TextureBound.right_top_lon"></a>

#### right\_top\_lon

```python
@property
def right_top_lon() -> str
```

(str):  [Read-Only]

<a id="unreal.TextureBound.right_top_lat"></a>

#### right\_top\_lat

```python
@property
def right_top_lat() -> str
```

(str):  [Read-Only]

<a id="unreal.BatchRangeVectorArray"></a>