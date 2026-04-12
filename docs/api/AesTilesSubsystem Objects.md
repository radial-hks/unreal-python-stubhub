## AesTilesSubsystem Objects

```python
class AesTilesSubsystem(WorldSubsystem)
```

Aes Tiles Subsystem

**C++ Source:**

- **Plugin**: AesTilesEntity
- **Module**: AesTilesEntity
- **File**: AesTilesSubsystem.h

<a id="unreal.AesTilesSubsystem.create_aes_tiles_entity_with_out_grpc"></a>

#### create\_aes\_tiles\_entity\_with\_out\_grpc

```python
def create_aes_tiles_entity_with_out_grpc(uri: str) -> Optional[int]
```

x.create_aes_tiles_entity_with_out_grpc(uri) -> int64 or None
Create Aes Tiles Entity with Out GRPC

Args:
    uri (str): 

Returns:
    int64 or None: 

    out_eid (int64):

<a id="unreal.AesTilesSubsystem.create_aes_tiles_entity"></a>

#### create\_aes\_tiles\_entity

```python
def create_aes_tiles_entity(space_id: str, range_b_box: Array[Vector2D],
                            version: str) -> Optional[int]
```

x.create_aes_tiles_entity(space_id, range_b_box, version) -> int64 or None
Create Aes Tiles Entity

Args:
    space_id (str): 
    range_b_box (Array[Vector2D]): 
    version (str): 

Returns:
    int64 or None: 

    out_eid (int64):

<a id="unreal.WdpProjectEntity"></a>