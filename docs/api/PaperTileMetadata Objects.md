## PaperTileMetadata Objects

```python
class PaperTileMetadata(StructBase)
```

Information about a single tile in a tile set

**C++ Source:**

- **Plugin**: Paper2D
- **Module**: Paper2D
- **File**: PaperTileSet.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collision_data`` (SpriteGeometryCollection):  [Read-Write] Collision data for the tile
- ``user_data_name`` (Name):  [Read-Write] A tag that can be used for grouping and categorizing (consider using it as the index into a UDataTable asset).

<a id="unreal.PaperTileMetadata.__init__"></a>

#### __init__

```python
def __init__(user_data_name: Name = "None") -> None
```

<a id="unreal.PaperTileMetadata.user_data_name"></a>

#### user_data_name

```python
@property
def user_data_name() -> Name
```

(Name):  [Read-Only] A tag that can be used for grouping and categorizing (consider using it as the index into a UDataTable asset).

<a id="unreal.PaperTerrainMaterialRule"></a>