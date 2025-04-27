## AvaShape3DDynMeshBase Objects

```python
class AvaShape3DDynMeshBase(AvaShapeDynamicMeshBase)
```

Ava Shape 3DDyn Mesh Base

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheShapes
- **File**: AvaShape3DDynMeshBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_edit_size`` (bool):  [Read-Write] enable mesh size property editing
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
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

<a id="unreal.AvaShape3DDynMeshBase.pixel_size3d"></a>

#### pixel_size3d

```python
@property
def pixel_size3d() -> Vector
```

(Vector):  [Read-Write] pixel size of the mesh, will only be available in editor

<a id="unreal.AvaShape3DDynMeshBase.pixel_size3d"></a>

#### pixel_size3d

```python
@pixel_size3d.setter
def pixel_size3d(value: Vector) -> None
```

<a id="unreal.AvaShape3DDynMeshBase.size3d"></a>

#### size3d

```python
@property
def size3d() -> Vector
```

(Vector):  [Read-Write] * Corresponds to the total size from 0 to mesh size

<a id="unreal.AvaShape3DDynMeshBase.size3d"></a>

#### size3d

```python
@size3d.setter
def size3d(value: Vector) -> None
```

<a id="unreal.AvaToolbox3DDynMeshBase"></a>