## AvaShapeDynamicMeshBase Objects

```python
class AvaShapeDynamicMeshBase(ActorComponent)
```

Ava Shape Dynamic Mesh Base

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheShapes
- **File**: AvaShapeDynMeshBase.h

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
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``size_type`` (SizeType):  [Read-Write] the type of size you want to handle
- ``uniform_scaled_size`` (float):  [Read-Write] Uniform scaled size of the mesh
- ``use_primary_material_everywhere`` (bool):  [Read-Write] use primary material for every slot available
- ``vertex_color`` (LinearColor):  [Read-Write]

<a id="unreal.AvaShapeDynamicMeshBase.allow_edit_size"></a>

#### allow_edit_size

```python
@property
def allow_edit_size() -> bool
```

(bool):  [Read-Only] enable mesh size property editing

<a id="unreal.AvaShapeDynamicMeshBase.size_type"></a>

#### size_type

```python
@property
def size_type() -> SizeType
```

(SizeType):  [Read-Write] the type of size you want to handle

<a id="unreal.AvaShapeDynamicMeshBase.size_type"></a>

#### size_type

```python
@size_type.setter
def size_type(value: SizeType) -> None
```

<a id="unreal.AvaShapeDynamicMeshBase.uniform_scaled_size"></a>

#### uniform_scaled_size

```python
@property
def uniform_scaled_size() -> float
```

(float):  [Read-Write] Uniform scaled size of the mesh

<a id="unreal.AvaShapeDynamicMeshBase.uniform_scaled_size"></a>

#### uniform_scaled_size

```python
@uniform_scaled_size.setter
def uniform_scaled_size(value: float) -> None
```

<a id="unreal.AvaShapeDynamicMeshBase.vertex_color"></a>

#### vertex_color

```python
@property
def vertex_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AvaShapeDynamicMeshBase.vertex_color"></a>

#### vertex_color

```python
@vertex_color.setter
def vertex_color(value: LinearColor) -> None
```

<a id="unreal.AvaShapeDynamicMeshBase.use_primary_material_everywhere"></a>

#### use_primary_material_everywhere

```python
@property
def use_primary_material_everywhere() -> bool
```

(bool):  [Read-Write] use primary material for every slot available

<a id="unreal.AvaShapeDynamicMeshBase.use_primary_material_everywhere"></a>

#### use_primary_material_everywhere

```python
@use_primary_material_everywhere.setter
def use_primary_material_everywhere(value: bool) -> None
```

<a id="unreal.AvaShapeDynamicMeshBase.mesh_datas"></a>

#### mesh_datas

```python
@property
def mesh_datas() -> Map[int, AvaShapeMeshData]
```

(Map[int32, AvaShapeMeshData]):  [Read-Only] Meshes used for the current shape sections

<a id="unreal.AvaShapeDynamicMeshBase.toggle_gizmo"></a>

#### toggle_gizmo

```python
def toggle_gizmo(gizmo_component: AvaGizmoComponent,
                 show_as_gizmo: bool = True) -> None
```

x.toggle_gizmo(gizmo_component, show_as_gizmo=True) -> None
Whether to show the callee as a gizmo or not

Args:
    gizmo_component (AvaGizmoComponent): 
    show_as_gizmo (bool):

<a id="unreal.AvaToolboxDynamicMeshBase"></a>