## AvaShapeTorusDynamicMesh Objects

```python
class AvaShapeTorusDynamicMesh(AvaShape3DDynMeshBase)
```

Ava Shape Torus Dynamic Mesh

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheShapes
- **File**: AvaShapeTorusDynMesh.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_edit_size`` (bool):  [Read-Write] enable mesh size property editing
- ``angle_degree`` (float):  [Read-Write] represents the tube angle in degree for the torus
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``inner_size`` (float):  [Read-Write] represents the size ratio available inside the torus
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``mesh_datas`` (Map[int32, AvaShapeMeshData]):  [Read-Write] Meshes used for the current shape sections
- ``num_sides`` (uint8):  [Read-Write] represents the precision of each circle composing a slice
- ``num_slices`` (uint8):  [Read-Write] represents the number of slices composing the tube
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``pixel_size3d`` (Vector):  [Read-Write] pixel size of the mesh, will only be available in editor
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``size3d`` (Vector):  [Read-Write] * Corresponds to the total size from 0 to mesh size
- ``size_type`` (SizeType):  [Read-Write] the type of size you want to handle
- ``start_degree`` (float):  [Read-Write] represents the starting angle in degree for the torus
- ``uniform_scaled_size`` (float):  [Read-Write] Uniform scaled size of the mesh
- ``use_primary_material_everywhere`` (bool):  [Read-Write] use primary material for every slot available
- ``vertex_color`` (LinearColor):  [Read-Write]

<a id="unreal.AvaShapeTorusDynamicMesh.num_slices"></a>

#### num_slices

```python
@property
def num_slices() -> int
```

(uint8):  [Read-Write] represents the number of slices composing the tube

<a id="unreal.AvaShapeTorusDynamicMesh.num_slices"></a>

#### num_slices

```python
@num_slices.setter
def num_slices(value: int) -> None
```

<a id="unreal.AvaShapeTorusDynamicMesh.num_sides"></a>

#### num_sides

```python
@property
def num_sides() -> int
```

(uint8):  [Read-Write] represents the precision of each circle composing a slice

<a id="unreal.AvaShapeTorusDynamicMesh.num_sides"></a>

#### num_sides

```python
@num_sides.setter
def num_sides(value: int) -> None
```

<a id="unreal.AvaShapeTorusDynamicMesh.inner_size"></a>

#### inner_size

```python
@property
def inner_size() -> float
```

(float):  [Read-Write] represents the size ratio available inside the torus

<a id="unreal.AvaShapeTorusDynamicMesh.inner_size"></a>

#### inner_size

```python
@inner_size.setter
def inner_size(value: float) -> None
```

<a id="unreal.AvaShapeTorusDynamicMesh.angle_degree"></a>

#### angle_degree

```python
@property
def angle_degree() -> float
```

(float):  [Read-Write] represents the tube angle in degree for the torus

<a id="unreal.AvaShapeTorusDynamicMesh.angle_degree"></a>

#### angle_degree

```python
@angle_degree.setter
def angle_degree(value: float) -> None
```

<a id="unreal.AvaShapeTorusDynamicMesh.start_degree"></a>

#### start_degree

```python
@property
def start_degree() -> float
```

(float):  [Read-Write] represents the starting angle in degree for the torus

<a id="unreal.AvaShapeTorusDynamicMesh.start_degree"></a>

#### start_degree

```python
@start_degree.setter
def start_degree(value: float) -> None
```

<a id="unreal.AvaToolboxTorusDynamicMesh"></a>