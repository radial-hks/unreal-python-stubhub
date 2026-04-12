## CreateTileParams Objects

```python
class CreateTileParams(ParamsBase)
```

Create Tile Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: AesTilesAPI
- **File**: AesTilesAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``range_box`` (Array[Vector2D]):  [Read-Write]
- ``space_id`` (str):  [Read-Write]
- ``version`` (str):  [Read-Write]

<a id="unreal.CreateTileParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(space_id: str = "",
             range_box: Array[Vector2D] = [],
             version: str = "") -> None
```

<a id="unreal.CreateTileParams.space_id"></a>

#### space\_id

```python
@property
def space_id() -> str
```

(str):  [Read-Write]

<a id="unreal.CreateTileParams.space_id"></a>

#### space\_id

```python
@space_id.setter
def space_id(value: str) -> None
```

<a id="unreal.CreateTileParams.range_box"></a>

#### range\_box

```python
@property
def range_box() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.CreateTileParams.range_box"></a>

#### range\_box

```python
@range_box.setter
def range_box(value: Array[Vector2D]) -> None
```

<a id="unreal.CreateTileParams.version"></a>

#### version

```python
@property
def version() -> str
```

(str):  [Read-Write]

<a id="unreal.CreateTileParams.version"></a>

#### version

```python
@version.setter
def version(value: str) -> None
```

<a id="unreal.CreateTile_WithOutGRPCParams"></a>