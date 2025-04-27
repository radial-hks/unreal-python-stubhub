## TileMapLibrary Objects

```python
class TileMapLibrary(BlueprintFunctionLibrary)
```

A collection of utility methods for working with tile map components
see: UPaperTileMap, UPaperTileMapComponent

**C++ Source:**

- **Plugin**: Paper2D
- **Module**: Paper2D
- **File**: TileMapBlueprintLibrary.h

<a id="unreal.TileMapLibrary.make_tile"></a>

#### make_tile

```python
@classmethod
def make_tile(cls, tile_index: int, tile_set: PaperTileSet, flip_h: bool,
              flip_v: bool, flip_d: bool) -> PaperTileInfo
```

X.make_tile(tile_index, tile_set, flip_h, flip_v, flip_d) -> PaperTileInfo
Creates a tile from the specified information

Args:
    tile_index (int32): 
    tile_set (PaperTileSet): 
    flip_h (bool): 
    flip_v (bool): 
    flip_d (bool): 

Returns:
    PaperTileInfo:

<a id="unreal.TileMapLibrary.get_tile_user_data"></a>

#### get_tile_user_data

```python
@classmethod
def get_tile_user_data(cls, tile: PaperTileInfo) -> Name
```

X.get_tile_user_data(tile) -> Name
Returns the user data name for the specified tile, or NAME_None if there is no user-specified data

Args:
    tile (PaperTileInfo): 

Returns:
    Name:

<a id="unreal.TileMapLibrary.get_tile_transform"></a>

#### get_tile_transform

```python
@classmethod
def get_tile_transform(cls, tile: PaperTileInfo) -> Transform
```

X.get_tile_transform(tile) -> Transform
Returns the transform for a tile

Args:
    tile (PaperTileInfo): 

Returns:
    Transform:

<a id="unreal.TileMapLibrary.break_tile"></a>

#### break_tile

```python
@classmethod
def break_tile(
        cls,
        tile: PaperTileInfo) -> Tuple[int, PaperTileSet, bool, bool, bool]
```

X.break_tile(tile) -> (tile_index=int32, tile_set=PaperTileSet, flip_h=bool, flip_v=bool, flip_d=bool)
Breaks out the information for a tile

Args:
    tile (PaperTileInfo): 

Returns:
    tuple: 

    tile_index (int32): 

    tile_set (PaperTileSet): 

    flip_h (bool): 

    flip_v (bool): 

    flip_d (bool):

<a id="unreal.EnvironmentQueryFactory"></a>