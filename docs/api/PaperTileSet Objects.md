## PaperTileSet Objects

```python
class PaperTileSet(Object)
```

A tile set is a collection of tiles pulled from a texture that can be used to fill out a tile map.
see: UPaperTileMap, UPaperTileMapComponent

**C++ Source:**

- **Plugin**: Paper2D
- **Module**: Paper2D
- **File**: PaperTileSet.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additional_source_textures`` (Array[Texture]):  [Read-Write] Additional source textures for other slots
- ``background_color`` (LinearColor):  [Read-Write] The background color displayed in the tile set viewer
- ``border_margin`` (IntMargin):  [Read-Write] The amount of padding around the border of the tile sheet (in pixels)
- ``drawing_offset`` (IntPoint):  [Read-Write] The drawing offset for tiles from this set (in pixels)
- ``per_tile_data`` (Array[PaperTileMetadata]):  [Read-Write] Per-tile information
- ``per_tile_spacing`` (IntPoint):  [Read-Write] The amount of padding between tiles in the tile sheet (in pixels)
- ``tile_sheet`` (Texture2D):  [Read-Write] The tile sheet texture associated with this tile set
- ``tile_size`` (IntPoint):  [Read-Write] The width and height of a single tile (in pixels)

<a id="unreal.PaperTileSet.tile_size"></a>

#### tile_size

```python
@property
def tile_size() -> IntPoint
```

(IntPoint):  [Read-Only] The width and height of a single tile (in pixels)

<a id="unreal.PaperTileSet.tile_sheet"></a>

#### tile_sheet

```python
@property
def tile_sheet() -> Texture2D
```

(Texture2D):  [Read-Only] The tile sheet texture associated with this tile set

<a id="unreal.PaperTileSet.border_margin"></a>

#### border_margin

```python
@property
def border_margin() -> IntMargin
```

(IntMargin):  [Read-Only] The amount of padding around the border of the tile sheet (in pixels)

<a id="unreal.PaperTileSet.per_tile_spacing"></a>

#### per_tile_spacing

```python
@property
def per_tile_spacing() -> IntPoint
```

(IntPoint):  [Read-Only] The amount of padding between tiles in the tile sheet (in pixels)

<a id="unreal.PaperTileSet.drawing_offset"></a>

#### drawing_offset

```python
@property
def drawing_offset() -> IntPoint
```

(IntPoint):  [Read-Only] The drawing offset for tiles from this set (in pixels)

<a id="unreal.MaterialExpressionSpriteTextureSampler"></a>