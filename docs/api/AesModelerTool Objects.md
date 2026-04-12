## AesModelerTool Objects

```python
class AesModelerTool(BlueprintFunctionLibrary)
```

Aes Modeler Tool

**C++ Source:**

- **Plugin**: AesModeler
- **Module**: AesModeler
- **File**: AesModelerTool.h

<a id="unreal.AesModelerTool.update_mesh_uv"></a>

#### update\_mesh\_uv

```python
@classmethod
def update_mesh_uv(cls, static_mesh: StaticMesh, index: int,
                   new_material: MaterialInstanceConstant) -> None
```

X.update_mesh_uv(static_mesh, index, new_material) -> None
Update Mesh UV

Args:
    static_mesh (StaticMesh): 
    index (int32): 
    new_material (MaterialInstanceConstant):

<a id="unreal.AesModelerTool.recover_mesh_uv"></a>

#### recover\_mesh\_uv

```python
@classmethod
def recover_mesh_uv(cls, mesh: StaticMesh) -> None
```

X.recover_mesh_uv(mesh) -> None
Recover Mesh UV

Args:
    mesh (StaticMesh):

<a id="unreal.AesModelerTool.merge_material_for_static_mesh"></a>

#### merge\_material\_for\_static\_mesh

```python
@classmethod
def merge_material_for_static_mesh(
        cls, mesh: StaticMesh, colorlist: Array[LinearColor],
        indexlist: Array[int], base_material: Array[MaterialInstanceConstant],
        package_name: str, settings: MeshMergingSettings, myactor: Actor,
        materialindexlist: Array[int]) -> None
```

X.merge_material_for_static_mesh(mesh, colorlist, indexlist, base_material, package_name, settings, myactor, materialindexlist) -> None
Merge Material for Static Mesh

Args:
    mesh (StaticMesh): 
    colorlist (Array[LinearColor]): 
    indexlist (Array[int32]): 
    base_material (Array[MaterialInstanceConstant]): 
    package_name (str): 
    settings (MeshMergingSettings): 
    myactor (Actor): 
    materialindexlist (Array[int32]):

<a id="unreal.AesModelerTool.merge_dom_data"></a>

#### merge\_dom\_data

```python
@classmethod
def merge_dom_data(cls, dom_folder_path: str, target_tile_s2_id: str) -> None
```

X.merge_dom_data(dom_folder_path, target_tile_s2_id) -> None
Merge DOMData

Args:
    dom_folder_path (str): 
    target_tile_s2_id (str):

<a id="unreal.AesModelerTool.get_vertex_color_list"></a>

#### get\_vertex\_color\_list

```python
@classmethod
def get_vertex_color_list(cls, mesh: StaticMesh) -> Map[int, LinearColor]
```

X.get_vertex_color_list(mesh) -> Map[int32, LinearColor]
Get Vertex Color List

Args:
    mesh (StaticMesh): 

Returns:
    Map[int32, LinearColor]: 

    color_map (Map[int32, LinearColor]):

<a id="unreal.AesModelerTool.get_long_package_name"></a>

#### get\_long\_package\_name

```python
@classmethod
def get_long_package_name(cls, path: str) -> str
```

X.get_long_package_name(path) -> str
Get Long Package Name

Args:
    path (str): 

Returns:
    str:

<a id="unreal.AesModelerTool.create_texture2d_array"></a>

#### create\_texture2d\_array

```python
@classmethod
def create_texture2d_array(cls, input_textures: Array[Texture2D],
                           save_directory: str) -> Texture2DArray
```

X.create_texture2d_array(input_textures, save_directory) -> Texture2DArray
Create Texture 2DArray

Args:
    input_textures (Array[Texture2D]): 
    save_directory (str): 

Returns:
    Texture2DArray:

<a id="unreal.AesModelerTool.create_material_with_textures"></a>

#### create\_material\_with\_textures

```python
@classmethod
def create_material_with_textures(
        cls, save_directory: str, source_mat: Material,
        texture_list: Map[str, Texture2DArray]) -> MaterialInstanceConstant
```

X.create_material_with_textures(save_directory, source_mat, texture_list) -> MaterialInstanceConstant
Create Material with Textures

Args:
    save_directory (str): 
    source_mat (Material): 
    texture_list (Map[str, Texture2DArray]): 

Returns:
    MaterialInstanceConstant:

<a id="unreal.AesModelerTool.convert_resource_to_static_mesh"></a>

#### convert\_resource\_to\_static\_mesh

```python
@classmethod
def convert_resource_to_static_mesh(cls,
                                    input_resource: UrbanSceneBuildResource,
                                    myactor: Actor,
                                    settings: MeshMergingSettings) -> None
```

X.convert_resource_to_static_mesh(input_resource, myactor, settings) -> None
Convert Resource to Static Mesh

Args:
    input_resource (UrbanSceneBuildResource): 
    myactor (Actor): 
    settings (MeshMergingSettings):

<a id="unreal.AesModelerTool.close_distance_field"></a>

#### close\_distance\_field

```python
@classmethod
def close_distance_field(cls, mesh: StaticMesh) -> None
```

X.close_distance_field(mesh) -> None
Close Distance Field

Args:
    mesh (StaticMesh):

<a id="unreal.AesModelerTool.bake_texture_from_high_poly"></a>

#### bake\_texture\_from\_high\_poly

```python
@classmethod
def bake_texture_from_high_poly(cls, package_name: str,
                                use_settings: MeshApproximationSettings,
                                mesh: StaticMesh, myactor: Array[Actor],
                                texture_size: int, projection_dist: float,
                                need_material_id: bool) -> None
```

X.bake_texture_from_high_poly(package_name, use_settings, mesh, myactor, texture_size, projection_dist, need_material_id) -> None
Bake Texture from High Poly

Args:
    package_name (str): 
    use_settings (MeshApproximationSettings): 
    mesh (StaticMesh): 
    myactor (Array[Actor]): 
    texture_size (int32): 
    projection_dist (float): 
    need_material_id (bool):

<a id="unreal.AesModelerTool.adjust_vertex_color_hsv"></a>

#### adjust\_vertex\_color\_hsv

```python
@classmethod
def adjust_vertex_color_hsv(cls, mesh: StaticMesh,
                            adjust_hsv_value: Array[float]) -> None
```

X.adjust_vertex_color_hsv(mesh, adjust_hsv_value) -> None
Adjust Vertex Color HSV

Args:
    mesh (StaticMesh): 
    adjust_hsv_value (Array[float]):

<a id="unreal.AesModelerTool.adjust_vertex_color"></a>

#### adjust\_vertex\_color

```python
@classmethod
def adjust_vertex_color(cls, mesh: StaticMesh,
                        color_map: Map[int, LinearColor]) -> None
```

X.adjust_vertex_color(mesh, color_map) -> None
Adjust Vertex Color

Args:
    mesh (StaticMesh): 
    color_map (Map[int32, LinearColor]):

<a id="unreal.AesModelerTool.actor_approximate_from_dir"></a>

#### actor\_approximate\_from\_dir

```python
@classmethod
def actor_approximate_from_dir(cls, path: str,
                               use_settings: MeshApproximationSettings,
                               actors: Array[Actor]) -> None
```

X.actor_approximate_from_dir(path, use_settings, actors) -> None
void GenerateApproximation(const TArray<AActor*>& Actors, const UE::Geometry::FApproximateActorsImpl::FOptions& Options, UE::Geometry::FApproximateActorsImpl::FResults& ResultsOut);

Args:
    path (str): 
    use_settings (MeshApproximationSettings): 
    actors (Array[Actor]):

<a id="unreal.ModelerComponent"></a>