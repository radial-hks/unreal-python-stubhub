## PaperTileInfo Objects

```python
class PaperTileInfo(StructBase)
```

This is the contents of a tile map cell

**C++ Source:**

- **Plugin**: Paper2D
- **Module**: Paper2D
- **File**: PaperTileLayer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``packed_tile_index`` (int32):  [Read-Write] This is the index of the current tile within the tile set
- ``tile_set`` (PaperTileSet):  [Read-Write] The tile set that this tile comes from

<a id="unreal.PaperTileInfo.__init__"></a>

#### __init__

```python
def __init__(tile_index: int = 0,
             tile_set: PaperTileSet = None,
             flip_h: bool = False,
             flip_v: bool = False,
             flip_d: bool = False) -> None
```

<a id="unreal.PaperTileMetadata"></a>