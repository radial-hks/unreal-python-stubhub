## InterchangeMeshNode Objects

```python
class InterchangeMeshNode(InterchangeBaseNode)
```

Interchange Mesh Node

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeNodes
- **File**: InterchangeMeshNode.h

<a id="unreal.InterchangeMeshNode.set_slot_material_dependency_uid"></a>

#### set_slot_material_dependency_uid

```python
def set_slot_material_dependency_uid(slot_name: str,
                                     material_dependency_uid: str) -> bool
```

x.set_slot_material_dependency_uid(slot_name, material_dependency_uid) -> bool
Add the specified Material dependency to a specific slot name of this object.

Args:
    slot_name (str): 
    material_dependency_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeMeshNode.set_skinned_mesh"></a>

#### set_skinned_mesh

```python
def set_skinned_mesh(is_skinned_mesh: bool) -> bool
```

x.set_skinned_mesh(is_skinned_mesh) -> bool
Set the IsSkinnedMesh attribute to determine whether this node represents a skinned mesh.

Args:
    is_skinned_mesh (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMeshNode.set_skeleton_dependency_uid"></a>

#### set_skeleton_dependency_uid

```python
def set_skeleton_dependency_uid(dependency_uid: str) -> bool
```

x.set_skeleton_dependency_uid(dependency_uid) -> bool
Add the specified skeleton dependency to this object.

Args:
    dependency_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeMeshNode.set_scene_instance_uid"></a>

#### set_scene_instance_uid

```python
def set_scene_instance_uid(dependency_uid: str) -> bool
```

x.set_scene_instance_uid(dependency_uid) -> bool
Add the specified asset instance this scene node refers to.

Args:
    dependency_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeMeshNode.set_pay_load_key"></a>

#### set_pay_load_key

```python
def set_pay_load_key(pay_load_key: str,
                     pay_load_type: InterchangeMeshPayLoadType) -> None
```

x.set_pay_load_key(pay_load_key, pay_load_type) -> None
Set Pay Load Key

Args:
    pay_load_key (str): 
    pay_load_type (InterchangeMeshPayLoadType):

<a id="unreal.InterchangeMeshNode.set_morph_target_name"></a>

#### set_morph_target_name

```python
def set_morph_target_name(morph_target_name: str) -> bool
```

x.set_morph_target_name(morph_target_name) -> bool
Set the MorphTargetName attribute to determine the name of the morph target.

Args:
    morph_target_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeMeshNode.set_morph_target_dependency_uid"></a>

#### set_morph_target_dependency_uid

```python
def set_morph_target_dependency_uid(dependency_uid: str) -> bool
```

x.set_morph_target_dependency_uid(dependency_uid) -> bool
Add the specified morph target dependency to this object.

Args:
    dependency_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeMeshNode.set_morph_target"></a>

#### set_morph_target

```python
def set_morph_target(is_morph_target: bool) -> bool
```

x.set_morph_target(is_morph_target) -> bool
Set the IsMorphTarget attribute to determine whether this node represents a morph target.

Args:
    is_morph_target (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMeshNode.set_custom_vertex_count"></a>

#### set_custom_vertex_count

```python
def set_custom_vertex_count(attribute_value: int) -> bool
```

x.set_custom_vertex_count(attribute_value) -> bool
Set the vertex count of this mesh. Return false if the attribute could not be set.

Args:
    attribute_value (int32): 

Returns:
    bool:

<a id="unreal.InterchangeMeshNode.set_custom_uv_count"></a>

#### set_custom_uv_count

```python
def set_custom_uv_count(attribute_value: int) -> bool
```

x.set_custom_uv_count(attribute_value) -> bool
Set the UV count attribute of this mesh. Return false if the attribute could not be set.

Args:
    attribute_value (int32): 

Returns:
    bool:

<a id="unreal.InterchangeMeshNode.set_custom_polygon_count"></a>

#### set_custom_polygon_count

```python
def set_custom_polygon_count(attribute_value: int) -> bool
```

x.set_custom_polygon_count(attribute_value) -> bool
Set the polygon count of this mesh. Return false if the attribute could not be set.

Args:
    attribute_value (int32): 

Returns:
    bool:

<a id="unreal.InterchangeMeshNode.set_custom_has_vertex_tangent"></a>

#### set_custom_has_vertex_tangent

```python
def set_custom_has_vertex_tangent(attribute_value: bool) -> bool
```

x.set_custom_has_vertex_tangent(attribute_value) -> bool
Set the vertex tangent attribute of this mesh. Return false if the attribute could not be set.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMeshNode.set_custom_has_vertex_normal"></a>

#### set_custom_has_vertex_normal

```python
def set_custom_has_vertex_normal(attribute_value: bool) -> bool
```

x.set_custom_has_vertex_normal(attribute_value) -> bool
Set the vertex normal attribute of this mesh. Return false if the attribute could not be set.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMeshNode.set_custom_has_vertex_color"></a>

#### set_custom_has_vertex_color

```python
def set_custom_has_vertex_color(attribute_value: bool) -> bool
```

x.set_custom_has_vertex_color(attribute_value) -> bool
Set the vertex color attribute of this mesh. Return false if the attribute could not be set.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMeshNode.set_custom_has_vertex_binormal"></a>

#### set_custom_has_vertex_binormal

```python
def set_custom_has_vertex_binormal(attribute_value: bool) -> bool
```

x.set_custom_has_vertex_binormal(attribute_value) -> bool
Set the vertex bi-normal attribute of this mesh. Return false if the attribute could not be set.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMeshNode.set_custom_has_smooth_group"></a>

#### set_custom_has_smooth_group

```python
def set_custom_has_smooth_group(attribute_value: bool) -> bool
```

x.set_custom_has_smooth_group(attribute_value) -> bool
Set the smoothing group attribute of this mesh. Return false if the attribute could not be set.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMeshNode.set_custom_bounding_box"></a>

#### set_custom_bounding_box

```python
def set_custom_bounding_box(attribute_value: Box) -> bool
```

x.set_custom_bounding_box(attribute_value) -> bool
Set the bounding box of this mesh. Return false if the attribute could not be set.

Args:
    attribute_value (Box): 

Returns:
    bool:

<a id="unreal.InterchangeMeshNode.remove_slot_material_dependency_uid"></a>

#### remove_slot_material_dependency_uid

```python
def remove_slot_material_dependency_uid(slot_name: str) -> bool
```

x.remove_slot_material_dependency_uid(slot_name) -> bool
Remove the Material dependency associated with the given slot name from this object.

Args:
    slot_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeMeshNode.remove_skeleton_dependency_uid"></a>

#### remove_skeleton_dependency_uid

```python
def remove_skeleton_dependency_uid(dependency_uid: str) -> bool
```

x.remove_skeleton_dependency_uid(dependency_uid) -> bool
Remove the specified skeleton dependency from this object.

Args:
    dependency_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeMeshNode.remove_scene_instance_uid"></a>

#### remove_scene_instance_uid

```python
def remove_scene_instance_uid(dependency_uid: str) -> bool
```

x.remove_scene_instance_uid(dependency_uid) -> bool
Remove the specified asset instance this scene node refers to.

Args:
    dependency_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeMeshNode.remove_morph_target_dependency_uid"></a>

#### remove_morph_target_dependency_uid

```python
def remove_morph_target_dependency_uid(dependency_uid: str) -> bool
```

x.remove_morph_target_dependency_uid(dependency_uid) -> bool
Remove the specified morph target dependency from this object.

Args:
    dependency_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeMeshNode.is_skinned_mesh"></a>

#### is_skinned_mesh

```python
def is_skinned_mesh() -> bool
```

x.is_skinned_mesh() -> bool
Return true if this node represents a skinned mesh.

Returns:
    bool:

<a id="unreal.InterchangeMeshNode.is_morph_target"></a>

#### is_morph_target

```python
def is_morph_target() -> bool
```

x.is_morph_target() -> bool
Return true if this node represents a morph target.

Returns:
    bool:

<a id="unreal.InterchangeMeshNode.get_slot_material_dependency_uid"></a>

#### get_slot_material_dependency_uid

```python
def get_slot_material_dependency_uid(slot_name: str) -> Optional[str]
```

x.get_slot_material_dependency_uid(slot_name) -> str or None
Retrieve the specified Material dependency for a given slot of this object.

Args:
    slot_name (str): 

Returns:
    str or None: 

    out_material_dependency (str):

<a id="unreal.InterchangeMeshNode.get_slot_material_dependencies"></a>

#### get_slot_material_dependencies

```python
def get_slot_material_dependencies() -> Map[str, str]
```

x.get_slot_material_dependencies() -> Map[str, str]
Retrieve the correspondence table between slot names and assigned materials for this object.

Returns:
    Map[str, str]: 

    out_material_dependencies (Map[str, str]):

<a id="unreal.InterchangeMeshNode.get_skeleton_dependency"></a>

#### get_skeleton_dependency

```python
def get_skeleton_dependency(index: int) -> str
```

x.get_skeleton_dependency(index) -> str
Retrieve the specified skeleton dependency for this object.

Args:
    index (int32): 

Returns:
    str: 

    out_dependency (str):

<a id="unreal.InterchangeMeshNode.get_skeleton_dependencies"></a>

#### get_skeleton_dependencies

```python
def get_skeleton_dependencies() -> Array[str]
```

x.get_skeleton_dependencies() -> Array[str]
Retrieve the skeleton dependency for this object.

Returns:
    Array[str]: 

    out_dependencies (Array[str]):

<a id="unreal.InterchangeMeshNode.get_skeleton_dependecies_count"></a>

#### get_skeleton_dependecies_count

```python
def get_skeleton_dependecies_count() -> int
```

x.get_skeleton_dependecies_count() -> int32
Retrieve the number of skeleton dependencies for this object.

Returns:
    int32:

<a id="unreal.InterchangeMeshNode.get_scene_instance_uids_count"></a>

#### get_scene_instance_uids_count

```python
def get_scene_instance_uids_count() -> int
```

x.get_scene_instance_uids_count() -> int32
Retrieve the number of scene nodes instancing this mesh.

Returns:
    int32:

<a id="unreal.InterchangeMeshNode.get_scene_instance_uids"></a>

#### get_scene_instance_uids

```python
def get_scene_instance_uids() -> Array[str]
```

x.get_scene_instance_uids() -> Array[str]
Retrieve the asset instances this scene node refers to.

Returns:
    Array[str]: 

    out_dependencies (Array[str]):

<a id="unreal.InterchangeMeshNode.get_scene_instance_uid"></a>

#### get_scene_instance_uid

```python
def get_scene_instance_uid(index: int) -> str
```

x.get_scene_instance_uid(index) -> str
Retrieve the asset instance this scene node refers to.

Args:
    index (int32): 

Returns:
    str: 

    out_dependency (str):

<a id="unreal.InterchangeMeshNode.get_morph_target_name"></a>

#### get_morph_target_name

```python
def get_morph_target_name() -> Optional[str]
```

x.get_morph_target_name() -> str or None
Get the morph target name.
Return true if we successfully retrieved the MorphTargetName attribute.

Returns:
    str or None: 

    out_morph_target_name (str):

<a id="unreal.InterchangeMeshNode.get_morph_target_dependency"></a>

#### get_morph_target_dependency

```python
def get_morph_target_dependency(index: int) -> str
```

x.get_morph_target_dependency(index) -> str
Retrieve the specified morph target dependency for this object.

Args:
    index (int32): 

Returns:
    str: 

    out_dependency (str):

<a id="unreal.InterchangeMeshNode.get_morph_target_dependencies"></a>

#### get_morph_target_dependencies

```python
def get_morph_target_dependencies() -> Array[str]
```

x.get_morph_target_dependencies() -> Array[str]
Retrieve all morph target dependencies for this object.

Returns:
    Array[str]: 

    out_dependencies (Array[str]):

<a id="unreal.InterchangeMeshNode.get_morph_target_dependecies_count"></a>

#### get_morph_target_dependecies_count

```python
def get_morph_target_dependecies_count() -> int
```

x.get_morph_target_dependecies_count() -> int32
Retrieve the number of morph target dependencies for this object.

Returns:
    int32:

<a id="unreal.InterchangeMeshNode.get_custom_vertex_count"></a>

#### get_custom_vertex_count

```python
def get_custom_vertex_count() -> Optional[int]
```

x.get_custom_vertex_count() -> int32 or None
Query the vertex count of this mesh. Return false if the attribute was not set.

Returns:
    int32 or None: 

    attribute_value (int32):

<a id="unreal.InterchangeMeshNode.get_custom_uv_count"></a>

#### get_custom_uv_count

```python
def get_custom_uv_count() -> Optional[int]
```

x.get_custom_uv_count() -> int32 or None
Query the UV count of this mesh. Return false if the attribute was not set.

Returns:
    int32 or None: 

    attribute_value (int32):

<a id="unreal.InterchangeMeshNode.get_custom_polygon_count"></a>

#### get_custom_polygon_count

```python
def get_custom_polygon_count() -> Optional[int]
```

x.get_custom_polygon_count() -> int32 or None
Query the polygon count of this mesh. Return false if the attribute was not set.

Returns:
    int32 or None: 

    attribute_value (int32):

<a id="unreal.InterchangeMeshNode.get_custom_has_vertex_tangent"></a>

#### get_custom_has_vertex_tangent

```python
def get_custom_has_vertex_tangent() -> Optional[bool]
```

x.get_custom_has_vertex_tangent() -> bool or None
Query whether this mesh has vertex tangents. Return false if the attribute was not set.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeMeshNode.get_custom_has_vertex_normal"></a>

#### get_custom_has_vertex_normal

```python
def get_custom_has_vertex_normal() -> Optional[bool]
```

x.get_custom_has_vertex_normal() -> bool or None
Query whether this mesh has vertex normals. Return false if the attribute was not set.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeMeshNode.get_custom_has_vertex_color"></a>

#### get_custom_has_vertex_color

```python
def get_custom_has_vertex_color() -> Optional[bool]
```

x.get_custom_has_vertex_color() -> bool or None
Query whether this mesh has vertex colors. Return false if the attribute was not set.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeMeshNode.get_custom_has_vertex_binormal"></a>

#### get_custom_has_vertex_binormal

```python
def get_custom_has_vertex_binormal() -> Optional[bool]
```

x.get_custom_has_vertex_binormal() -> bool or None
Query whether this mesh has vertex bi-normals. Return false if the attribute was not set.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeMeshNode.get_custom_has_smooth_group"></a>

#### get_custom_has_smooth_group

```python
def get_custom_has_smooth_group() -> Optional[bool]
```

x.get_custom_has_smooth_group() -> bool or None
Query whether this mesh has smoothing groups. Return false if the attribute was not set.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeMeshNode.get_custom_bounding_box"></a>

#### get_custom_bounding_box

```python
def get_custom_bounding_box() -> Optional[Box]
```

x.get_custom_bounding_box() -> Box or None
Query the bounding box of this mesh. Return false if the attribute was not set.

Returns:
    Box or None: 

    attribute_value (Box):

<a id="unreal.InterchangeSceneNode"></a>