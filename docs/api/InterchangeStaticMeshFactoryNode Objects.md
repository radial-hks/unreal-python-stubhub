## InterchangeStaticMeshFactoryNode Objects

```python
class InterchangeStaticMeshFactoryNode(InterchangeMeshFactoryNode)
```

namespace UE

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeFactoryNodes
- **File**: InterchangeStaticMeshFactoryNode.h

<a id="unreal.InterchangeStaticMeshFactoryNode.set_lod_screen_sizes"></a>

#### set_lod_screen_sizes

```python
def set_lod_screen_sizes(lod_screen_sizes: Array[float]) -> bool
```

x.set_lod_screen_sizes(lod_screen_sizes) -> bool
Sets the LOD Screen Sizes for the static mesh.

Args:
    lod_screen_sizes (Array[float]): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshFactoryNode.set_custom_support_face_remap"></a>

#### set_custom_support_face_remap

```python
def set_custom_support_face_remap(attribute_value: bool,
                                  add_apply_delegate: bool = True) -> bool
```

x.set_custom_support_face_remap(attribute_value, add_apply_delegate=True) -> bool
Set whether the static mesh is set up for use with physical material masks.

Args:
    attribute_value (bool): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshFactoryNode.set_custom_src_lightmap_index"></a>

#### set_custom_src_lightmap_index

```python
def set_custom_src_lightmap_index(attribute_value: int,
                                  add_apply_delegate: bool = True) -> bool
```

x.set_custom_src_lightmap_index(attribute_value, add_apply_delegate=True) -> bool
Set the index of the UV that is used as the source for generating lightmaps for the static mesh.

Args:
    attribute_value (int32): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshFactoryNode.set_custom_min_lightmap_resolution"></a>

#### set_custom_min_lightmap_resolution

```python
def set_custom_min_lightmap_resolution(attribute_value: int,
                                       add_apply_delegate: bool = True
                                       ) -> bool
```

x.set_custom_min_lightmap_resolution(attribute_value, add_apply_delegate=True) -> bool
Set the amount of padding used to pack UVs for the static mesh.

Args:
    attribute_value (int32): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshFactoryNode.set_custom_max_lumen_mesh_cards"></a>

#### set_custom_max_lumen_mesh_cards

```python
def set_custom_max_lumen_mesh_cards(attribute_value: int,
                                    add_apply_delegate: bool = True) -> bool
```

x.set_custom_max_lumen_mesh_cards(attribute_value, add_apply_delegate=True) -> bool
Set the maximum number of Lumen mesh cards to generate for this mesh.
More cards means that the surface will have better coverage, but will result in increased runtime overhead.
Set this to 0 to disable mesh card generation for this mesh.
The default is 12.

Args:
    attribute_value (int32): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshFactoryNode.set_custom_generate_lightmap_u_vs"></a>

#### set_custom_generate_lightmap_u_vs

```python
def set_custom_generate_lightmap_u_vs(attribute_value: bool,
                                      add_apply_delegate: bool = True) -> bool
```

x.set_custom_generate_lightmap_u_vs(attribute_value, add_apply_delegate=True) -> bool
Set whether the static mesh should generate lightmap UVs.

Args:
    attribute_value (bool): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshFactoryNode.set_custom_generate_distance_field_as_if_two_sided"></a>

#### set_custom_generate_distance_field_as_if_two_sided

```python
def set_custom_generate_distance_field_as_if_two_sided(
        attribute_value: bool, add_apply_delegate: bool = True) -> bool
```

x.set_custom_generate_distance_field_as_if_two_sided(attribute_value, add_apply_delegate=True) -> bool
Set whether to generate the distance field by treating every triangle hit as a front face.
This prevents the distance field from being discarded due to the mesh being open, but also lowers distance field ambient occlusion quality.

Args:
    attribute_value (bool): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshFactoryNode.set_custom_dst_lightmap_index"></a>

#### set_custom_dst_lightmap_index

```python
def set_custom_dst_lightmap_index(attribute_value: int,
                                  add_apply_delegate: bool = True) -> bool
```

x.set_custom_dst_lightmap_index(attribute_value, add_apply_delegate=True) -> bool
Set the index of the UV that is used to store generated lightmaps for the static mesh.

Args:
    attribute_value (int32): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshFactoryNode.set_custom_distance_field_resolution_scale"></a>

#### set_custom_distance_field_resolution_scale

```python
def set_custom_distance_field_resolution_scale(attribute_value: float,
                                               add_apply_delegate: bool = True
                                               ) -> bool
```

x.set_custom_distance_field_resolution_scale(attribute_value, add_apply_delegate=True) -> bool
Set the scale to apply to the mesh when allocating the distance field volume texture.
The default scale is 1, which assumes that the mesh will be placed unscaled in the world.

Args:
    attribute_value (float): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshFactoryNode.set_custom_distance_field_replacement_mesh"></a>

#### set_custom_distance_field_replacement_mesh

```python
def set_custom_distance_field_replacement_mesh(
        attribute_value: SoftObjectPath,
        add_apply_delegate: bool = True) -> bool
```

x.set_custom_distance_field_replacement_mesh(attribute_value, add_apply_delegate=True) -> bool
Set the static mesh asset whose distance field will be used as the distance field for the imported mesh.

Args:
    attribute_value (SoftObjectPath): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshFactoryNode.set_custom_build_scale3d"></a>

#### set_custom_build_scale3d

```python
def set_custom_build_scale3d(attribute_value: Vector,
                             add_apply_delegate: bool = True) -> bool
```

x.set_custom_build_scale3d(attribute_value, add_apply_delegate=True) -> bool
Set the local scale that is applied when building the static mesh.

Args:
    attribute_value (Vector): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshFactoryNode.set_custom_build_reversed_index_buffer"></a>

#### set_custom_build_reversed_index_buffer

```python
def set_custom_build_reversed_index_buffer(attribute_value: bool,
                                           add_apply_delegate: bool = True
                                           ) -> bool
```

x.set_custom_build_reversed_index_buffer(attribute_value, add_apply_delegate=True) -> bool
Set whether the static mesh should build a reversed index buffer.

Args:
    attribute_value (bool): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshFactoryNode.set_custom_build_nanite"></a>

#### set_custom_build_nanite

```python
def set_custom_build_nanite(attribute_value: bool,
                            add_apply_delegate: bool = True) -> bool
```

x.set_custom_build_nanite(attribute_value, add_apply_delegate=True) -> bool
Set whether the static mesh factory should set the Nanite build setting. Return false if the attribute was not set.

Args:
    attribute_value (bool): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshFactoryNode.set_custom_auto_compute_lod_screen_sizes"></a>

#### set_custom_auto_compute_lod_screen_sizes

```python
def set_custom_auto_compute_lod_screen_sizes(attribute_value: bool) -> bool
```

x.set_custom_auto_compute_lod_screen_sizes(attribute_value) -> bool
Set whether the static mesh factory should auto compute LOD Screen Sizes. Return false if the attribute was not set.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshFactoryNode.remove_socket_ud"></a>

#### remove_socket_ud

```python
def remove_socket_ud(socket_uid: str) -> bool
```

x.remove_socket_ud(socket_uid) -> bool
Remove Socket Ud

Args:
    socket_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshFactoryNode.initialize_static_mesh_node"></a>

#### initialize_static_mesh_node

```python
def initialize_static_mesh_node(unique_id: str, display_label: str,
                                asset_class: str) -> None
```

x.initialize_static_mesh_node(unique_id, display_label, asset_class) -> None
Initialize node data.

Args:
    unique_id (str): The unique ID for this node.
    display_label (str): The name of the node.
    asset_class (str): The class the StaticMesh factory will create for this node.

<a id="unreal.InterchangeStaticMeshFactoryNode.get_socket_uids"></a>

#### get_socket_uids

```python
def get_socket_uids() -> Array[str]
```

x.get_socket_uids() -> Array[str]
Get Socket Uids

Returns:
    Array[str]: 

    out_socket_uids (Array[str]):

<a id="unreal.InterchangeStaticMeshFactoryNode.get_socket_uid_count"></a>

#### get_socket_uid_count

```python
def get_socket_uid_count() -> int
```

x.get_socket_uid_count() -> int32
Return the number of socket UIDs this static mesh has.

Returns:
    int32:

<a id="unreal.InterchangeStaticMeshFactoryNode.get_object_class"></a>

#### get_object_class

```python
def get_object_class() -> Class
```

x.get_object_class() -> type(Class)
Get the class this node creates.

Returns:
    type(Class):

<a id="unreal.InterchangeStaticMeshFactoryNode.get_lod_screen_sizes"></a>

#### get_lod_screen_sizes

```python
def get_lod_screen_sizes() -> Array[float]
```

x.get_lod_screen_sizes() -> Array[float]
Returns All the LOD Screen Sizes set for the static mesh.

Returns:
    Array[float]: 

    out_lod_screen_sizes (Array[float]):

<a id="unreal.InterchangeStaticMeshFactoryNode.get_lod_screen_size_count"></a>

#### get_lod_screen_size_count

```python
def get_lod_screen_size_count() -> int
```

x.get_lod_screen_size_count() -> int32
Returns the number of LOD Screen Sizes the static mesh has.

Returns:
    int32:

<a id="unreal.InterchangeStaticMeshFactoryNode.get_custom_support_face_remap"></a>

#### get_custom_support_face_remap

```python
def get_custom_support_face_remap() -> Optional[bool]
```

x.get_custom_support_face_remap() -> bool or None
Get whether the static mesh is set up for use with physical material masks.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeStaticMeshFactoryNode.get_custom_src_lightmap_index"></a>

#### get_custom_src_lightmap_index

```python
def get_custom_src_lightmap_index() -> Optional[int]
```

x.get_custom_src_lightmap_index() -> int32 or None
Get the index of the UV that is used as the source for generating lightmaps for the static mesh.

Returns:
    int32 or None: 

    attribute_value (int32):

<a id="unreal.InterchangeStaticMeshFactoryNode.get_custom_min_lightmap_resolution"></a>

#### get_custom_min_lightmap_resolution

```python
def get_custom_min_lightmap_resolution() -> Optional[int]
```

x.get_custom_min_lightmap_resolution() -> int32 or None
Get the amount of padding used to pack UVs for the static mesh.

Returns:
    int32 or None: 

    attribute_value (int32):

<a id="unreal.InterchangeStaticMeshFactoryNode.get_custom_max_lumen_mesh_cards"></a>

#### get_custom_max_lumen_mesh_cards

```python
def get_custom_max_lumen_mesh_cards() -> Optional[int]
```

x.get_custom_max_lumen_mesh_cards() -> int32 or None
Get the maximum number of Lumen mesh cards to generate for this mesh.
More cards means that the surface will have better coverage, but will result in increased runtime overhead.
Set this to 0 to disable mesh card generation for this mesh.
The default is 12.

Returns:
    int32 or None: 

    attribute_value (int32):

<a id="unreal.InterchangeStaticMeshFactoryNode.get_custom_generate_lightmap_u_vs"></a>

#### get_custom_generate_lightmap_u_vs

```python
def get_custom_generate_lightmap_u_vs() -> Optional[bool]
```

x.get_custom_generate_lightmap_u_vs() -> bool or None
Get whether the static mesh should generate lightmap UVs.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeStaticMeshFactoryNode.get_custom_generate_distance_field_as_if_two_sided"></a>

#### get_custom_generate_distance_field_as_if_two_sided

```python
def get_custom_generate_distance_field_as_if_two_sided() -> Optional[bool]
```

x.get_custom_generate_distance_field_as_if_two_sided() -> bool or None
Get whether to generate the distance field by treating every triangle hit as a front face.
This prevents the distance field from being discarded due to the mesh being open, but also lowers distance field ambient occlusion quality.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeStaticMeshFactoryNode.get_custom_dst_lightmap_index"></a>

#### get_custom_dst_lightmap_index

```python
def get_custom_dst_lightmap_index() -> Optional[int]
```

x.get_custom_dst_lightmap_index() -> int32 or None
Get the index of the UV that is used to store generated lightmaps for the static mesh.

Returns:
    int32 or None: 

    attribute_value (int32):

<a id="unreal.InterchangeStaticMeshFactoryNode.get_custom_distance_field_resolution_scale"></a>

#### get_custom_distance_field_resolution_scale

```python
def get_custom_distance_field_resolution_scale() -> Optional[float]
```

x.get_custom_distance_field_resolution_scale() -> float or None
Get the scale to apply to the mesh when allocating the distance field volume texture.
The default scale is 1, which assumes that the mesh will be placed unscaled in the world.

Returns:
    float or None: 

    attribute_value (float):

<a id="unreal.InterchangeStaticMeshFactoryNode.get_custom_distance_field_replacement_mesh"></a>

#### get_custom_distance_field_replacement_mesh

```python
def get_custom_distance_field_replacement_mesh() -> Optional[SoftObjectPath]
```

x.get_custom_distance_field_replacement_mesh() -> SoftObjectPath or None
Get the static mesh asset whose distance field will be used as the distance field for the imported mesh.

Returns:
    SoftObjectPath or None: 

    attribute_value (SoftObjectPath):

<a id="unreal.InterchangeStaticMeshFactoryNode.get_custom_build_scale3d"></a>

#### get_custom_build_scale3d

```python
def get_custom_build_scale3d() -> Optional[Vector]
```

x.get_custom_build_scale3d() -> Vector or None
Get the local scale that is applied when building the static mesh.

Returns:
    Vector or None: 

    attribute_value (Vector):

<a id="unreal.InterchangeStaticMeshFactoryNode.get_custom_build_reversed_index_buffer"></a>

#### get_custom_build_reversed_index_buffer

```python
def get_custom_build_reversed_index_buffer() -> Optional[bool]
```

x.get_custom_build_reversed_index_buffer() -> bool or None
Get whether the static mesh should build a reversed index buffer.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeStaticMeshFactoryNode.get_custom_build_nanite"></a>

#### get_custom_build_nanite

```python
def get_custom_build_nanite() -> Optional[bool]
```

x.get_custom_build_nanite() -> bool or None
Get whether the static mesh factory should set the Nanite build setting. Return false if the attribute was not set.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeStaticMeshFactoryNode.get_custom_auto_compute_lod_screen_sizes"></a>

#### get_custom_auto_compute_lod_screen_sizes

```python
def get_custom_auto_compute_lod_screen_sizes() -> Optional[bool]
```

x.get_custom_auto_compute_lod_screen_sizes() -> bool or None
Get whether the static mesh factory should auto compute LOD Screen Sizes. Return false if the attribute was not set.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeStaticMeshFactoryNode.add_socket_uids"></a>

#### add_socket_uids

```python
def add_socket_uids(socket_uids: Array[str]) -> bool
```

x.add_socket_uids(socket_uids) -> bool
Add Socket Uids

Args:
    socket_uids (Array[str]): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshFactoryNode.add_socket_uid"></a>

#### add_socket_uid

```python
def add_socket_uid(socket_uid: str) -> bool
```

x.add_socket_uid(socket_uid) -> bool
Add Socket Uid

Args:
    socket_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshLodDataNode"></a>