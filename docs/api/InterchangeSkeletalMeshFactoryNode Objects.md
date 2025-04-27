## InterchangeSkeletalMeshFactoryNode Objects

```python
class InterchangeSkeletalMeshFactoryNode(InterchangeMeshFactoryNode)
```

Interchange Skeletal Mesh Factory Node

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeFactoryNodes
- **File**: InterchangeSkeletalMeshFactoryNode.h

<a id="unreal.InterchangeSkeletalMeshFactoryNode.set_custom_use_high_precision_skin_weights"></a>

#### set_custom_use_high_precision_skin_weights

```python
def set_custom_use_high_precision_skin_weights(attribute_value: bool,
                                               add_apply_delegate: bool = True
                                               ) -> bool
```

x.set_custom_use_high_precision_skin_weights(attribute_value, add_apply_delegate=True) -> bool
Set the skeletal mesh UseHighPrecisionSkinWeights setting.

Args:
    attribute_value (bool): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletalMeshFactoryNode.set_custom_threshold_uv"></a>

#### set_custom_threshold_uv

```python
def set_custom_threshold_uv(attribute_value: float,
                            add_apply_delegate: bool = True) -> bool
```

x.set_custom_threshold_uv(attribute_value, add_apply_delegate=True) -> bool
Set the skeletal mesh threshold value that is used to decide whether two UVs are equal.

Args:
    attribute_value (float): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletalMeshFactoryNode.set_custom_threshold_tangent_normal"></a>

#### set_custom_threshold_tangent_normal

```python
def set_custom_threshold_tangent_normal(attribute_value: float,
                                        add_apply_delegate: bool = True
                                        ) -> bool
```

x.set_custom_threshold_tangent_normal(attribute_value, add_apply_delegate=True) -> bool
Set the skeletal mesh threshold value that is used to decide whether two normals, tangents, or bi-normals are equal.

Args:
    attribute_value (float): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletalMeshFactoryNode.set_custom_threshold_position"></a>

#### set_custom_threshold_position

```python
def set_custom_threshold_position(attribute_value: float,
                                  add_apply_delegate: bool = True) -> bool
```

x.set_custom_threshold_position(attribute_value, add_apply_delegate=True) -> bool
Set the skeletal mesh threshold value that is used to decide whether two vertex positions are equal.

Args:
    attribute_value (float): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletalMeshFactoryNode.set_custom_skeleton_soft_object_path"></a>

#### set_custom_skeleton_soft_object_path

```python
def set_custom_skeleton_soft_object_path(
        attribute_value: SoftObjectPath) -> bool
```

x.set_custom_skeleton_soft_object_path(attribute_value) -> bool
Set the skeletal mesh factory skeleton UObject. Return false if the attribute could not be set.

Args:
    attribute_value (SoftObjectPath): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletalMeshFactoryNode.set_custom_physic_asset_soft_object_path"></a>

#### set_custom_physic_asset_soft_object_path

```python
def set_custom_physic_asset_soft_object_path(
        attribute_value: SoftObjectPath) -> bool
```

x.set_custom_physic_asset_soft_object_path(attribute_value) -> bool
Set a physics asset the skeletal mesh factory should use. Return false if the attribute could not be set.

Args:
    attribute_value (SoftObjectPath): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletalMeshFactoryNode.set_custom_morph_threshold_position"></a>

#### set_custom_morph_threshold_position

```python
def set_custom_morph_threshold_position(attribute_value: float,
                                        add_apply_delegate: bool = True
                                        ) -> bool
```

x.set_custom_morph_threshold_position(attribute_value, add_apply_delegate=True) -> bool
Set the skeletal mesh threshold value that is used to compare vertex position equality when computing morph target deltas.

Args:
    attribute_value (float): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletalMeshFactoryNode.set_custom_merge_morph_target_shape_with_same_name"></a>

#### set_custom_merge_morph_target_shape_with_same_name

```python
def set_custom_merge_morph_target_shape_with_same_name(
        attribute_value: bool) -> bool
```

x.set_custom_merge_morph_target_shape_with_same_name(attribute_value) -> bool
Set whether the skeletal mesh factory should merge morph target shape with the same name under one morph target. Return false if the attribute could not be set.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletalMeshFactoryNode.set_custom_import_vertex_attributes"></a>

#### set_custom_import_vertex_attributes

```python
def set_custom_import_vertex_attributes(attribute_value: bool) -> bool
```

x.set_custom_import_vertex_attributes(attribute_value) -> bool
Set whether the skeletal mesh factory should import vertex attributes. Return false if the attribute could not be set.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletalMeshFactoryNode.set_custom_import_morph_target"></a>

#### set_custom_import_morph_target

```python
def set_custom_import_morph_target(attribute_value: bool) -> bool
```

x.set_custom_import_morph_target(attribute_value) -> bool
Set whether the skeletal mesh factory should create morph targets. Return false if the attribute could not be set.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletalMeshFactoryNode.set_custom_import_content_type"></a>

#### set_custom_import_content_type

```python
def set_custom_import_content_type(
        attribute_value: InterchangeSkeletalMeshContentType) -> bool
```

x.set_custom_import_content_type(attribute_value) -> bool
Set the skeletal mesh import content type. This content type determines whether the factory imports partial or full translated content. Return false if the attribute could not be set.

Args:
    attribute_value (InterchangeSkeletalMeshContentType): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletalMeshFactoryNode.set_custom_create_physics_asset"></a>

#### set_custom_create_physics_asset

```python
def set_custom_create_physics_asset(attribute_value: bool) -> bool
```

x.set_custom_create_physics_asset(attribute_value) -> bool
Set whether the skeletal mesh factory should create a physics asset. Return false if the attribute could not be set.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletalMeshFactoryNode.set_custom_bone_influence_limit"></a>

#### set_custom_bone_influence_limit

```python
def set_custom_bone_influence_limit(attribute_value: int,
                                    add_apply_delegate: bool = True) -> bool
```

x.set_custom_bone_influence_limit(attribute_value, add_apply_delegate=True) -> bool
Set the maximum number of bone influences to allow each vertex in this mesh to use.
If set higher than the limit determined by the project settings, it has no effect.
If set to 0, the value is taken from the DefaultBoneInfluenceLimit project setting.

Args:
    attribute_value (int32): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletalMeshFactoryNode.initialize_skeletal_mesh_node"></a>

#### initialize_skeletal_mesh_node

```python
def initialize_skeletal_mesh_node(unique_id: str, display_label: str,
                                  asset_class: str) -> None
```

x.initialize_skeletal_mesh_node(unique_id, display_label, asset_class) -> None
Initialize node data.
param:: UniqueID - The unique ID for this node.

Args:
    unique_id (str): 
    display_label (str): The name of the node.
    asset_class (str): The class the SkeletalMesh factory will create for this node.

<a id="unreal.InterchangeSkeletalMeshFactoryNode.get_object_class"></a>

#### get_object_class

```python
def get_object_class() -> Class
```

x.get_object_class() -> type(Class)
Get the class this node creates.

Returns:
    type(Class):

<a id="unreal.InterchangeSkeletalMeshFactoryNode.get_custom_use_high_precision_skin_weights"></a>

#### get_custom_use_high_precision_skin_weights

```python
def get_custom_use_high_precision_skin_weights() -> Optional[bool]
```

x.get_custom_use_high_precision_skin_weights() -> bool or None
Query the skeletal mesh UseHighPrecisionSkinWeights setting.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeSkeletalMeshFactoryNode.get_custom_threshold_uv"></a>

#### get_custom_threshold_uv

```python
def get_custom_threshold_uv() -> Optional[float]
```

x.get_custom_threshold_uv() -> float or None
Query the skeletal mesh threshold value that is used to decide whether two UVs are equal.

Returns:
    float or None: 

    attribute_value (float):

<a id="unreal.InterchangeSkeletalMeshFactoryNode.get_custom_threshold_tangent_normal"></a>

#### get_custom_threshold_tangent_normal

```python
def get_custom_threshold_tangent_normal() -> Optional[float]
```

x.get_custom_threshold_tangent_normal() -> float or None
Query the skeletal mesh threshold value that is used to decide whether two normals, tangents, or bi-normals are equal.

Returns:
    float or None: 

    attribute_value (float):

<a id="unreal.InterchangeSkeletalMeshFactoryNode.get_custom_threshold_position"></a>

#### get_custom_threshold_position

```python
def get_custom_threshold_position() -> Optional[float]
```

x.get_custom_threshold_position() -> float or None
Query the skeletal mesh threshold value that is used to decide whether two vertex positions are equal.

Returns:
    float or None: 

    attribute_value (float):

<a id="unreal.InterchangeSkeletalMeshFactoryNode.get_custom_skeleton_soft_object_path"></a>

#### get_custom_skeleton_soft_object_path

```python
def get_custom_skeleton_soft_object_path() -> Optional[SoftObjectPath]
```

x.get_custom_skeleton_soft_object_path() -> SoftObjectPath or None
Query the skeletal mesh factory skeleton UObject. Return false if the attribute was not set.

Returns:
    SoftObjectPath or None: 

    attribute_value (SoftObjectPath):

<a id="unreal.InterchangeSkeletalMeshFactoryNode.get_custom_physic_asset_soft_object_path"></a>

#### get_custom_physic_asset_soft_object_path

```python
def get_custom_physic_asset_soft_object_path() -> Optional[SoftObjectPath]
```

x.get_custom_physic_asset_soft_object_path() -> SoftObjectPath or None
Query a physics asset the skeletal mesh factory should use. Return false if the attribute was not set.

Returns:
    SoftObjectPath or None: 

    attribute_value (SoftObjectPath):

<a id="unreal.InterchangeSkeletalMeshFactoryNode.get_custom_morph_threshold_position"></a>

#### get_custom_morph_threshold_position

```python
def get_custom_morph_threshold_position() -> Optional[float]
```

x.get_custom_morph_threshold_position() -> float or None
Query the skeletal mesh threshold value that is used to compare vertex position equality when computing morph target deltas.

Returns:
    float or None: 

    attribute_value (float):

<a id="unreal.InterchangeSkeletalMeshFactoryNode.get_custom_merge_morph_target_shape_with_same_name"></a>

#### get_custom_merge_morph_target_shape_with_same_name

```python
def get_custom_merge_morph_target_shape_with_same_name() -> Optional[bool]
```

x.get_custom_merge_morph_target_shape_with_same_name() -> bool or None
Query whether the skeletal mesh factory should merge morph target shape with the same name under one morph target. Return false if the attribute was not set.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeSkeletalMeshFactoryNode.get_custom_import_vertex_attributes"></a>

#### get_custom_import_vertex_attributes

```python
def get_custom_import_vertex_attributes() -> Optional[bool]
```

x.get_custom_import_vertex_attributes() -> bool or None
Query whether the skeletal mesh factory should import vertex attributes. Return false if the attribute was not set.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeSkeletalMeshFactoryNode.get_custom_import_morph_target"></a>

#### get_custom_import_morph_target

```python
def get_custom_import_morph_target() -> Optional[bool]
```

x.get_custom_import_morph_target() -> bool or None
Query whether the skeletal mesh factory should create morph targets. Return false if the attribute was not set.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeSkeletalMeshFactoryNode.get_custom_import_content_type"></a>

#### get_custom_import_content_type

```python
def get_custom_import_content_type(
) -> Optional[InterchangeSkeletalMeshContentType]
```

x.get_custom_import_content_type() -> InterchangeSkeletalMeshContentType or None
Query the skeletal mesh import content type. This content type determines whether the factory imports partial or full translated content. Return false if the attribute was not set.

Returns:
    InterchangeSkeletalMeshContentType or None: 

    attribute_value (InterchangeSkeletalMeshContentType):

<a id="unreal.InterchangeSkeletalMeshFactoryNode.get_custom_create_physics_asset"></a>

#### get_custom_create_physics_asset

```python
def get_custom_create_physics_asset() -> Optional[bool]
```

x.get_custom_create_physics_asset() -> bool or None
Query whether the skeletal mesh factory should create a physics asset. Return false if the attribute was not set.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeSkeletalMeshFactoryNode.get_custom_bone_influence_limit"></a>

#### get_custom_bone_influence_limit

```python
def get_custom_bone_influence_limit() -> Optional[int]
```

x.get_custom_bone_influence_limit() -> int32 or None
Query the maximum number of bone influences to allow each vertex in this mesh to use.
If set higher than the limit determined by the project settings, it has no effect.
If set to 0, the value is taken from the DefaultBoneInfluenceLimit project setting.

Returns:
    int32 or None: 

    attribute_value (int32):

<a id="unreal.InterchangeSkeletalMeshLodDataNode"></a>