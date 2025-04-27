## AvaShapeSphereDynamicMesh Objects

```python
class AvaShapeSphereDynamicMesh(AvaShape3DDynMeshBase)
```

Ava Shape Sphere Dynamic Mesh

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheShapes
- **File**: AvaShapeSphereDynMesh.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_edit_size`` (bool):  [Read-Write] enable mesh size property editing
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``end_longitude`` (float):  [Read-Write] represents the longitude (Z) angle in degree for the sphere at the end
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``latitude_degree`` (float):  [Read-Write] represents the total latitude (Y) angle in degree for the sphere
- ``mesh_datas`` (Map[int32, AvaShapeMeshData]):  [Read-Write] Meshes used for the current shape sections
- ``num_sides`` (uint8):  [Read-Write] represents the precision of the sphere mesh
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``pixel_size3d`` (Vector):  [Read-Write] pixel size of the mesh, will only be available in editor
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``size3d`` (Vector):  [Read-Write] * Corresponds to the total size from 0 to mesh size
- ``size_type`` (SizeType):  [Read-Write] the type of size you want to handle
- ``start_latitude`` (float):  [Read-Write] represents the latitude (Y) angle in degree for the sphere at the start
- ``start_longitude`` (float):  [Read-Write] represents the longitude (Z) angle in degree for the sphere at the start
- ``uniform_scaled_size`` (float):  [Read-Write] Uniform scaled size of the mesh
- ``use_primary_material_everywhere`` (bool):  [Read-Write] use primary material for every slot available
- ``vertex_color`` (LinearColor):  [Read-Write]

<a id="unreal.AvaShapeSphereDynamicMesh.start_longitude"></a>

#### start_longitude

```python
@property
def start_longitude() -> float
```

(float):  [Read-Write] represents the longitude (Z) angle in degree for the sphere at the start

<a id="unreal.AvaShapeSphereDynamicMesh.start_longitude"></a>

#### start_longitude

```python
@start_longitude.setter
def start_longitude(value: float) -> None
```

<a id="unreal.AvaShapeSphereDynamicMesh.end_longitude"></a>

#### end_longitude

```python
@property
def end_longitude() -> float
```

(float):  [Read-Write] represents the longitude (Z) angle in degree for the sphere at the end

<a id="unreal.AvaShapeSphereDynamicMesh.end_longitude"></a>

#### end_longitude

```python
@end_longitude.setter
def end_longitude(value: float) -> None
```

<a id="unreal.AvaShapeSphereDynamicMesh.start_latitude"></a>

#### start_latitude

```python
@property
def start_latitude() -> float
```

(float):  [Read-Write] represents the latitude (Y) angle in degree for the sphere at the start

<a id="unreal.AvaShapeSphereDynamicMesh.start_latitude"></a>

#### start_latitude

```python
@start_latitude.setter
def start_latitude(value: float) -> None
```

<a id="unreal.AvaShapeSphereDynamicMesh.latitude_degree"></a>

#### latitude_degree

```python
@property
def latitude_degree() -> float
```

(float):  [Read-Write] represents the total latitude (Y) angle in degree for the sphere

<a id="unreal.AvaShapeSphereDynamicMesh.latitude_degree"></a>

#### latitude_degree

```python
@latitude_degree.setter
def latitude_degree(value: float) -> None
```

<a id="unreal.AvaShapeSphereDynamicMesh.num_sides"></a>

#### num_sides

```python
@property
def num_sides() -> int
```

(uint8):  [Read-Write] represents the precision of the sphere mesh

<a id="unreal.AvaShapeSphereDynamicMesh.num_sides"></a>

#### num_sides

```python
@num_sides.setter
def num_sides(value: int) -> None
```

<a id="unreal.AvaToolboxSphereDynamicMesh"></a>