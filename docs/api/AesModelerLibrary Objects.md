## AesModelerLibrary Objects

```python
class AesModelerLibrary(BlueprintFunctionLibrary)
```

Aes Modeler Library

**C++ Source:**

- **Plugin**: AesModeler
- **Module**: AesModeler
- **File**: AesModelerLibrary.h

<a id="unreal.AesModelerLibrary.switch_static_mesh_allow_cpu_access"></a>

#### switch\_static\_mesh\_allow\_cpu\_access

```python
@classmethod
def switch_static_mesh_allow_cpu_access(cls, static_mesh: StaticMesh,
                                        allow_cpu_access: bool) -> None
```

X.switch_static_mesh_allow_cpu_access(static_mesh, allow_cpu_access) -> None
Switch StaticMesh bAllowCPUAccess

Args:
    static_mesh (StaticMesh): 
    allow_cpu_access (bool):

<a id="unreal.AesModelerLibrary.save_thumbnail"></a>

#### save\_thumbnail

```python
@classmethod
def save_thumbnail(cls, obj: Object, img_res: int, output_dir: Text) -> None
```

X.save_thumbnail(obj, img_res, output_dir) -> None
Save Thumbnail

Args:
    obj (Object): 
    img_res (int32): 
    output_dir (Text):

<a id="unreal.AesModelerLibrary.save_prefab_without_window"></a>

#### save\_prefab\_without\_window

```python
@classmethod
def save_prefab_without_window(cls, modeler_entity: UrbanEntity,
                               entity_asset: UrbanEntityAsset,
                               prefab_name: str) -> None
```

X.save_prefab_without_window(modeler_entity, entity_asset, prefab_name) -> None
Save Prefab Without Window

Args:
    modeler_entity (UrbanEntity): 
    entity_asset (UrbanEntityAsset): 
    prefab_name (str):

<a id="unreal.AesModelerLibrary.get_tile_info_by_s2_id"></a>

#### get\_tile\_info\_by\_s2\_id

```python
@classmethod
def get_tile_info_by_s2_id(
        cls, s2_id_string: str) -> Tuple[Array[Vector2D], Vector2D]
```

X.get_tile_info_by_s2_id(s2_id_string) -> (out_corners=Array[Vector2D], out_center=Vector2D)
Get Tile Info by S2Id

Args:
    s2_id_string (str): 

Returns:
    tuple: 

    out_corners (Array[Vector2D]): 

    out_center (Vector2D):

<a id="unreal.AesModelerTool"></a>