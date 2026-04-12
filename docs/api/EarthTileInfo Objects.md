## EarthTileInfo Objects

```python
class EarthTileInfo(StructBase)
```

Earth Tile Info

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesEarth
- **File**: EarthGeoreferenceSystemFunctionLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``marker_coordinate`` (IntPoint):  [Read-Write]
- ``marker_level`` (int32):  [Read-Write]

<a id="unreal.EarthTileInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(marker_level: int = 0,
             marker_coordinate: IntPoint = [0, 0]) -> None
```

<a id="unreal.EarthTileInfo.marker_level"></a>

#### marker\_level

```python
@property
def marker_level() -> int
```

(int32):  [Read-Write]

<a id="unreal.EarthTileInfo.marker_level"></a>

#### marker\_level

```python
@marker_level.setter
def marker_level(value: int) -> None
```

<a id="unreal.EarthTileInfo.marker_coordinate"></a>

#### marker\_coordinate

```python
@property
def marker_coordinate() -> IntPoint
```

(IntPoint):  [Read-Write]

<a id="unreal.EarthTileInfo.marker_coordinate"></a>

#### marker\_coordinate

```python
@marker_coordinate.setter
def marker_coordinate(value: IntPoint) -> None
```

<a id="unreal.EarthTilesetDataInfo"></a>