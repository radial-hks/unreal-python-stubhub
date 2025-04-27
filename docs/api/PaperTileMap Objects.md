## PaperTileMap Objects

```python
class PaperTileMap(Object)
```

A tile map is a 2D grid with a defined width and height (in tiles).  There can be multiple layers, each of which can specify which tile should appear in each cell of the map for that layer.

**C++ Source:**

- **Plugin**: Paper2D
- **Module**: Paper2D
- **File**: PaperTileMap.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_data`` (AssetImportData):  [Read-Only] Importing data and options used for this tile map
- ``background_color`` (LinearColor):  [Read-Write] The background color displayed in the tile map editor
- ``collision_thickness`` (float):  [Read-Write] The extrusion thickness of collision geometry when using a 3D collision domain
- ``hex_side_length`` (int32):  [Read-Write] The vertical height of the sides of the hex cell for a tile.
  Note: This value should already be included as part of the TileHeight, and is purely cosmetic; it only affects how the tile cursor preview is drawn.
- ``layer_grid_color`` (LinearColor):  [Read-Write] The color of the layer grid
- ``map_height`` (int32):  [Read-Write] Height of map (in tiles)
- ``map_width`` (int32):  [Read-Write] Width of map (in tiles)
- ``material`` (MaterialInterface):  [Read-Write] The material to use on a tile map instance if not overridden
- ``multi_tile_grid_color`` (LinearColor):  [Read-Write] The color of the multi tile grid
- ``multi_tile_grid_height`` (int32):  [Read-Write] Number of tiles the multi tile grid spans vertically. 0 removes horizontal lines
- ``multi_tile_grid_offset_x`` (int32):  [Read-Write] Number of tiles the multi tile grid is shifted to the right
- ``multi_tile_grid_offset_y`` (int32):  [Read-Write] Number of tiles the multi tile grid is shifted downwards
- ``multi_tile_grid_width`` (int32):  [Read-Write] Number of tiles the multi tile grid spans horizontally. 0 removes vertical lines
- ``pixels_per_unreal_unit`` (float):  [Read-Write] The scaling factor between pixels and Unreal units (cm) (e.g., 0.64 would make a 64 pixel wide tile take up 100 cm)
- ``projection_mode`` (TileMapProjectionMode):  [Read-Write] Tile map type
- ``separation_per_layer`` (float):  [Read-Write] The Z-separation between each layer of the tile map
- ``separation_per_tile_x`` (float):  [Read-Write] The Z-separation incurred as you travel in X (not strictly applied, batched tiles will be put at the same Z level)
- ``separation_per_tile_y`` (float):  [Read-Write] The Z-separation incurred as you travel in Y (not strictly applied, batched tiles will be put at the same Z level)
- ``sprite_collision_domain`` (SpriteCollisionMode):  [Read-Write] Collision domain (no collision, 2D, or 3D)
- ``tile_grid_color`` (LinearColor):  [Read-Write] The color of the tile grid
- ``tile_height`` (int32):  [Read-Write] Height of one tile (in pixels)
- ``tile_layers`` (Array[PaperTileLayer]):  [Read-Write] The list of layers
- ``tile_width`` (int32):  [Read-Write] Width of one tile (in pixels)

<a id="unreal.PaperTileMap.map_width"></a>

#### map_width

```python
@property
def map_width() -> int
```

(int32):  [Read-Only] Width of map (in tiles)

<a id="unreal.PaperTileMap.map_height"></a>

#### map_height

```python
@property
def map_height() -> int
```

(int32):  [Read-Only] Height of map (in tiles)

<a id="unreal.PaperTileMap.tile_width"></a>

#### tile_width

```python
@property
def tile_width() -> int
```

(int32):  [Read-Only] Width of one tile (in pixels)

<a id="unreal.PaperTileMap.tile_height"></a>

#### tile_height

```python
@property
def tile_height() -> int
```

(int32):  [Read-Only] Height of one tile (in pixels)

<a id="unreal.PaperTileMap.separation_per_layer"></a>

#### separation_per_layer

```python
@property
def separation_per_layer() -> float
```

(float):  [Read-Only] The Z-separation between each layer of the tile map

<a id="unreal.PaperTileMap.material"></a>

#### material

```python
@property
def material() -> MaterialInterface
```

(MaterialInterface):  [Read-Only] The material to use on a tile map instance if not overridden

<a id="unreal.PaperTileMap.tile_layers"></a>

#### tile_layers

```python
@property
def tile_layers() -> Array[PaperTileLayer]
```

(Array[PaperTileLayer]):  [Read-Only] The list of layers

<a id="unreal.PaperTileMap.collision_thickness"></a>

#### collision_thickness

```python
@property
def collision_thickness() -> float
```

(float):  [Read-Only] The extrusion thickness of collision geometry when using a 3D collision domain

<a id="unreal.PaperTileMap.sprite_collision_domain"></a>

#### sprite_collision_domain

```python
@property
def sprite_collision_domain() -> SpriteCollisionMode
```

(SpriteCollisionMode):  [Read-Only] Collision domain (no collision, 2D, or 3D)

<a id="unreal.PaperTileMap.projection_mode"></a>

#### projection_mode

```python
@property
def projection_mode() -> TileMapProjectionMode
```

(TileMapProjectionMode):  [Read-Only] Tile map type

<a id="unreal.PaperTileMapActor"></a>