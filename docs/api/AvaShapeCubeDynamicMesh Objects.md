## AvaShapeCubeDynamicMesh Objects

```python
class AvaShapeCubeDynamicMesh(AvaShape3DDynMeshBase)
```

Ava Shape Cube Dynamic Mesh

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheShapes
- **File**: AvaShapeCubeDynMesh.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_edit_size`` (bool):  [Read-Write] enable mesh size property editing
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``bevel_num`` (uint8):  [Read-Write] represents the bevel number of division, only valid when bevel size is greater than zero
- ``bevel_size_ratio`` (float):  [Read-Write] represents the bevel size applied on each face of the cube, 0 means no bevels
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``mesh_datas`` (Map[int32, AvaShapeMeshData]):  [Read-Write] Meshes used for the current shape sections
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``pixel_size3d`` (Vector):  [Read-Write] pixel size of the mesh, will only be available in editor
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``size3d`` (Vector):  [Read-Write] * Corresponds to the total size from 0 to mesh size
- ``size_type`` (SizeType):  [Read-Write] the type of size you want to handle
- ``uniform_scaled_size`` (float):  [Read-Write] Uniform scaled size of the mesh
- ``use_primary_material_everywhere`` (bool):  [Read-Write] use primary material for every slot available
- ``vertex_color`` (LinearColor):  [Read-Write]

<a id="unreal.AvaShapeCubeDynamicMesh.bevel_size_ratio"></a>

#### bevel_size_ratio

```python
@property
def bevel_size_ratio() -> float
```

(float):  [Read-Write] represents the bevel size applied on each face of the cube, 0 means no bevels

<a id="unreal.AvaShapeCubeDynamicMesh.bevel_size_ratio"></a>

#### bevel_size_ratio

```python
@bevel_size_ratio.setter
def bevel_size_ratio(value: float) -> None
```

<a id="unreal.AvaShapeCubeDynamicMesh.bevel_num"></a>

#### bevel_num

```python
@property
def bevel_num() -> int
```

(uint8):  [Read-Write] represents the bevel number of division, only valid when bevel size is greater than zero

<a id="unreal.AvaShapeCubeDynamicMesh.bevel_num"></a>

#### bevel_num

```python
@bevel_num.setter
def bevel_num(value: int) -> None
```

<a id="unreal.AvaToolboxCubeDynamicMesh"></a>