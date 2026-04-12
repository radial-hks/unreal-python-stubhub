## InterchangeSceneNode Objects

```python
class InterchangeSceneNode(InterchangeBaseNode)
```

The scene node represents a transform node in the scene.
Scene nodes can have user-defined attributes. Use UInterchangeUserDefinedAttributesAPI to get and set user-defined attribute data.

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeNodes
- **File**: InterchangeSceneNode.h

<a id="unreal.InterchangeSceneNode.set_slot_material_dependency_uid"></a>

#### set\_slot\_material\_dependency\_uid

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

<a id="unreal.InterchangeSceneNode.set_morph_target_curve_weight"></a>

#### set\_morph\_target\_curve\_weight

```python
def set_morph_target_curve_weight(morph_target_name: str,
                                  weight: float) -> bool
```

x.set_morph_target_curve_weight(morph_target_name, weight) -> bool
Set MorphTarget with given weight.

Args:
    morph_target_name (str): 
    weight (float): 

Returns:
    bool:

<a id="unreal.InterchangeSceneNode.set_global_bind_pose_reference_for_mesh_ui_ds"></a>

#### set\_global\_bind\_pose\_reference\_for\_mesh\_ui\_ds

```python
def set_global_bind_pose_reference_for_mesh_ui_ds(
        global_bind_pose_reference_for_mesh_ui_ds: Map[str, Matrix]) -> None
```

x.set_global_bind_pose_reference_for_mesh_ui_ds(global_bind_pose_reference_for_mesh_ui_ds) -> None
Set the Global Bind Pose Referenced for MeshUIDs.

Args:
    global_bind_pose_reference_for_mesh_ui_ds (Map[str, Matrix]):

<a id="unreal.InterchangeSceneNode.set_custom_time_zero_local_transform"></a>

#### set\_custom\_time\_zero\_local\_transform

```python
def set_custom_time_zero_local_transform(
        base_node_container: InterchangeBaseNodeContainer,
        attribute_value: Transform,
        reset_cache: bool = True) -> bool
```

x.set_custom_time_zero_local_transform(base_node_container, attribute_value, reset_cache=True) -> bool
Set the local transform of the time-zero scene node.

Args:
    base_node_container (InterchangeBaseNodeContainer): 
    attribute_value (Transform): 
    reset_cache (bool): 

Returns:
    bool:

<a id="unreal.InterchangeSceneNode.set_custom_pivot_node_transform"></a>

#### set\_custom\_pivot\_node\_transform

```python
def set_custom_pivot_node_transform(attribute_value: Transform) -> bool
```

x.set_custom_pivot_node_transform(attribute_value) -> bool
Set the node pivot geometric offset.

Args:
    attribute_value (Transform): 

Returns:
    bool:

<a id="unreal.InterchangeSceneNode.set_custom_local_transform"></a>

#### set\_custom\_local\_transform

```python
def set_custom_local_transform(
        base_node_container: InterchangeBaseNodeContainer,
        attribute_value: Transform,
        reset_cache: bool = True) -> bool
```

x.set_custom_local_transform(base_node_container, attribute_value, reset_cache=True) -> bool
Set the default scene node local transform.
The default transform is the local transform of the node (no bind pose, no time evaluation).

Args:
    base_node_container (InterchangeBaseNodeContainer): 
    attribute_value (Transform): 
    reset_cache (bool): 

Returns:
    bool:

<a id="unreal.InterchangeSceneNode.set_custom_has_bind_pose"></a>

#### set\_custom\_has\_bind\_pose

```python
def set_custom_has_bind_pose(has_bind_pose: bool) -> bool
```

x.set_custom_has_bind_pose(has_bind_pose) -> bool
Sets if Joint has Bind Pose. Automatic T0 usage will be configured in case if the Skeleton contanis at least 1 Joint without BindPose.

Args:
    has_bind_pose (bool): 

Returns:
    bool:

<a id="unreal.InterchangeSceneNode.set_custom_geometric_transform"></a>

#### set\_custom\_geometric\_transform

```python
def set_custom_geometric_transform(attribute_value: Transform) -> bool
```

x.set_custom_geometric_transform(attribute_value) -> bool
Set the geometric offset. Any mesh attached to this scene node will be offset using this transform.

Args:
    attribute_value (Transform): 

Returns:
    bool:

<a id="unreal.InterchangeSceneNode.set_custom_bind_pose_local_transform"></a>

#### set\_custom\_bind\_pose\_local\_transform

```python
def set_custom_bind_pose_local_transform(
        base_node_container: InterchangeBaseNodeContainer,
        attribute_value: Transform,
        reset_cache: bool = True) -> bool
```

x.set_custom_bind_pose_local_transform(base_node_container, attribute_value, reset_cache=True) -> bool
Set the local transform of the bind pose scene node.

Args:
    base_node_container (InterchangeBaseNodeContainer): 
    attribute_value (Transform): 
    reset_cache (bool): 

Returns:
    bool:

<a id="unreal.InterchangeSceneNode.set_custom_asset_instance_uid"></a>

#### set\_custom\_asset\_instance\_uid

```python
def set_custom_asset_instance_uid(attribute_value: str) -> bool
```

x.set_custom_asset_instance_uid(attribute_value) -> bool
Add an asset for this scene node to instantiate.

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeSceneNode.set_custom_animation_asset_uid_to_play"></a>

#### set\_custom\_animation\_asset\_uid\_to\_play

```python
def set_custom_animation_asset_uid_to_play(attribute_value: str) -> bool
```

x.set_custom_animation_asset_uid_to_play(attribute_value) -> bool
Set the Animation Asset To Play by this Scene Node. Only relevant for SkeletalMeshActors (that is, SceneNodes that are instantiating Skeletal Meshes).

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeSceneNode.remove_specialized_type"></a>

#### remove\_specialized\_type

```python
def remove_specialized_type(specialized_type: str) -> bool
```

x.remove_specialized_type(specialized_type) -> bool
Remove Specialized Type

Args:
    specialized_type (str): 

Returns:
    bool:

<a id="unreal.InterchangeSceneNode.remove_slot_material_dependency_uid"></a>

#### remove\_slot\_material\_dependency\_uid

```python
def remove_slot_material_dependency_uid(slot_name: str) -> bool
```

x.remove_slot_material_dependency_uid(slot_name) -> bool
Remove the Material dependency associated with the given slot name from this object.

Args:
    slot_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeSceneNode.is_specialized_type_contains"></a>

#### is\_specialized\_type\_contains

```python
def is_specialized_type_contains(specialized_type: str) -> bool
```

x.is_specialized_type_contains(specialized_type) -> bool
Is Specialized Type Contains

Args:
    specialized_type (str): 

Returns:
    bool:

<a id="unreal.InterchangeSceneNode.get_specialized_types"></a>

#### get\_specialized\_types

```python
def get_specialized_types() -> Array[str]
```

x.get_specialized_types() -> Array[str]
Get Specialized Types

Returns:
    Array[str]: 

    out_specialized_types (Array[str]):

<a id="unreal.InterchangeSceneNode.get_specialized_type_count"></a>

#### get\_specialized\_type\_count

```python
def get_specialized_type_count() -> int
```

x.get_specialized_type_count() -> int32
Get the specialized type this scene node represents (for example, Joint or LODGroup).

Returns:
    int32:

<a id="unreal.InterchangeSceneNode.get_specialized_type"></a>

#### get\_specialized\_type

```python
def get_specialized_type(index: int) -> str
```

x.get_specialized_type(index) -> str
Get Specialized Type

Args:
    index (int32): 

Returns:
    str: 

    out_specialized_type (str):

<a id="unreal.InterchangeSceneNode.get_slot_material_dependency_uid"></a>

#### get\_slot\_material\_dependency\_uid

```python
def get_slot_material_dependency_uid(slot_name: str) -> Optional[str]
```

x.get_slot_material_dependency_uid(slot_name) -> str or None
Retrieve the Material dependency for a given slot of this object.

Args:
    slot_name (str): 

Returns:
    str or None: 

    out_material_dependency (str):

<a id="unreal.InterchangeSceneNode.get_slot_material_dependencies"></a>

#### get\_slot\_material\_dependencies

```python
def get_slot_material_dependencies() -> Map[str, str]
```

x.get_slot_material_dependencies() -> Map[str, str]
Retrieve the correspondence table between slot names and assigned materials for this object.

Returns:
    Map[str, str]: 

    out_material_dependencies (Map[str, str]):

<a id="unreal.InterchangeSceneNode.get_morph_target_curve_weights"></a>

#### get\_morph\_target\_curve\_weights

```python
def get_morph_target_curve_weights() -> Map[str, float]
```

x.get_morph_target_curve_weights() -> Map[str, float]
Get MorphTargets and their weights.

Returns:
    Map[str, float]: 

    out_morph_target_curve_weights (Map[str, float]):

<a id="unreal.InterchangeSceneNode.get_global_bind_pose_reference_for_mesh_uid"></a>

#### get\_global\_bind\_pose\_reference\_for\_mesh\_uid

```python
def get_global_bind_pose_reference_for_mesh_uid(
        mesh_uid: str) -> Optional[Matrix]
```

x.get_global_bind_pose_reference_for_mesh_uid(mesh_uid) -> Matrix or None
Get the Global Bind Pose Reference for given MeshUID.

Args:
    mesh_uid (str): 

Returns:
    Matrix or None: 

    global_bind_pose_reference (Matrix):

<a id="unreal.InterchangeSceneNode.get_custom_time_zero_local_transform"></a>

#### get\_custom\_time\_zero\_local\_transform

```python
def get_custom_time_zero_local_transform() -> Optional[Transform]
```

x.get_custom_time_zero_local_transform() -> Transform or None
Get the local transform of the time-zero scene node.

Returns:
    Transform or None: 

    attribute_value (Transform):

<a id="unreal.InterchangeSceneNode.get_custom_time_zero_global_transform"></a>

#### get\_custom\_time\_zero\_global\_transform

```python
def get_custom_time_zero_global_transform(
        base_node_container: InterchangeBaseNodeContainer,
        global_offset_transform: Transform,
        force_recache: bool = False) -> Optional[Transform]
```

x.get_custom_time_zero_global_transform(base_node_container, global_offset_transform, force_recache=False) -> Transform or None
Get the global transform of the time-zero scene node. This value is computed from the local transforms of all parent time-zero scene nodes.

Args:
    base_node_container (InterchangeBaseNodeContainer): 
    global_offset_transform (Transform): 
    force_recache (bool): 

Returns:
    Transform or None: 

    attribute_value (Transform):

<a id="unreal.InterchangeSceneNode.get_custom_pivot_node_transform"></a>

#### get\_custom\_pivot\_node\_transform

```python
def get_custom_pivot_node_transform() -> Optional[Transform]
```

x.get_custom_pivot_node_transform() -> Transform or None
Get the node pivot geometric offset.

Returns:
    Transform or None: 

    attribute_value (Transform):

<a id="unreal.InterchangeSceneNode.get_custom_local_transform"></a>

#### get\_custom\_local\_transform

```python
def get_custom_local_transform() -> Optional[Transform]
```

x.get_custom_local_transform() -> Transform or None
Get the default scene node local transform.
The default transform is the local transform of the node (no bind pose, no time evaluation).

Returns:
    Transform or None: 

    attribute_value (Transform):

<a id="unreal.InterchangeSceneNode.get_custom_has_bind_pose"></a>

#### get\_custom\_has\_bind\_pose

```python
def get_custom_has_bind_pose() -> Optional[bool]
```

x.get_custom_has_bind_pose() -> bool or None
Gets if the joint has BindPose (if the setter was used, otherwise returns with false and T0 evaluation presumes bHasBindPose==true).

Returns:
    bool or None: 

    has_bind_pose (bool):

<a id="unreal.InterchangeSceneNode.get_custom_global_transform"></a>

#### get\_custom\_global\_transform

```python
def get_custom_global_transform(
        base_node_container: InterchangeBaseNodeContainer,
        global_offset_transform: Transform,
        force_recache: bool = False) -> Optional[Transform]
```

x.get_custom_global_transform(base_node_container, global_offset_transform, force_recache=False) -> Transform or None
Get the default scene node global transform. This value is computed from the local transforms of all parent scene nodes.

Args:
    base_node_container (InterchangeBaseNodeContainer): 
    global_offset_transform (Transform): 
    force_recache (bool): 

Returns:
    Transform or None: 

    attribute_value (Transform):

<a id="unreal.InterchangeSceneNode.get_custom_geometric_transform"></a>

#### get\_custom\_geometric\_transform

```python
def get_custom_geometric_transform() -> Optional[Transform]
```

x.get_custom_geometric_transform() -> Transform or None
Get the geometric offset. Any mesh attached to this scene node will be offset using this transform.

Returns:
    Transform or None: 

    attribute_value (Transform):

<a id="unreal.InterchangeSceneNode.get_custom_bind_pose_local_transform"></a>

#### get\_custom\_bind\_pose\_local\_transform

```python
def get_custom_bind_pose_local_transform() -> Optional[Transform]
```

x.get_custom_bind_pose_local_transform() -> Transform or None
Get the local transform of the bind pose scene node.

Returns:
    Transform or None: 

    attribute_value (Transform):

<a id="unreal.InterchangeSceneNode.get_custom_bind_pose_global_transform"></a>

#### get\_custom\_bind\_pose\_global\_transform

```python
def get_custom_bind_pose_global_transform(
        base_node_container: InterchangeBaseNodeContainer,
        global_offset_transform: Transform,
        force_recache: bool = False) -> Optional[Transform]
```

x.get_custom_bind_pose_global_transform(base_node_container, global_offset_transform, force_recache=False) -> Transform or None
Get the global transform of the bind pose scene node. This value is computed from the local transforms of all parent bind poses.

Args:
    base_node_container (InterchangeBaseNodeContainer): 
    global_offset_transform (Transform): 
    force_recache (bool): 

Returns:
    Transform or None: 

    attribute_value (Transform):

<a id="unreal.InterchangeSceneNode.get_custom_asset_instance_uid"></a>

#### get\_custom\_asset\_instance\_uid

```python
def get_custom_asset_instance_uid() -> Optional[str]
```

x.get_custom_asset_instance_uid() -> str or None
Get which asset, if any, a scene node is instantiating. Return false if the Attribute was not set previously.

Returns:
    str or None: 

    attribute_value (str):

<a id="unreal.InterchangeSceneNode.get_custom_animation_asset_uid_to_play"></a>

#### get\_custom\_animation\_asset\_uid\_to\_play

```python
def get_custom_animation_asset_uid_to_play() -> Optional[str]
```

x.get_custom_animation_asset_uid_to_play() -> str or None
Get the Animation Asset To Play by this Scene Node.

Returns:
    str or None: 

    attribute_value (str):

<a id="unreal.InterchangeSceneNode.add_specialized_type"></a>

#### add\_specialized\_type

```python
def add_specialized_type(specialized_type: str) -> bool
```

x.add_specialized_type(specialized_type) -> bool
Add Specialized Type

Args:
    specialized_type (str): 

Returns:
    bool:

<a id="unreal.InterchangeShaderPortsAPI"></a>