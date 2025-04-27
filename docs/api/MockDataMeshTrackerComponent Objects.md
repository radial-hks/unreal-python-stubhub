## MockDataMeshTrackerComponent Objects

```python
class MockDataMeshTrackerComponent(SceneComponent)
```

The MeshTrackerComponent class manages requests for environmental mesh data, processes the results and provides
them to the calling system. The calling system is able request environmental mesh data within a specified area.
Various other search criteria can be set via this class's public properties.  Mesh data requests are processed
on a separate thread.  Once a mesh data request has been processed the calling system will be notified via an
FOnMeshTrackerUpdated broadcast.

**C++ Source:**

- **Module**: MRMesh
- **File**: MockDataMeshTrackerComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``block_vertex_colors`` (Array[Color]):  [Read-Write] Colors through which we cycle when setting vertex color by block.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``on_mesh_tracker_updated`` (OnMockDataMeshTrackerUpdated):  [Read-Write] Activated whenever new information about this mesh tracker is detected.
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``relative_location`` (Vector):  [Read-Write] Location of the component relative to its parent
- ``relative_rotation`` (Rotator):  [Read-Write] Rotation of the component relative to its parent
- ``relative_scale3d`` (Vector):  [Read-Write] Non-uniform scaling of the component relative to its parent.
  Note that scaling is always applied in local space (no shearing etc)
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``request_normals`` (bool):  [Read-Write] If true, the system will generate normals for the triangle vertices.
- ``request_vertex_confidence`` (bool):  [Read-Write] If true, the system will generate the mesh confidence values for the triangle vertices.
  These confidence values can be used to determine if the user needs to scan more.
- ``scan_world`` (bool):  [Read-Write] Set to true to start scanning the world for meshes.
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``update_interval`` (float):  [Read-Write] Update Interval in Seconds.
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``vertex_color_from_confidence_one`` (LinearColor):  [Read-Write] Color mapped to confidence value of one.
- ``vertex_color_from_confidence_zero`` (LinearColor):  [Read-Write] Color mapped to confidence value of zero.
- ``vertex_color_mode`` (MeshTrackerVertexColorMode):  [Read-Write] Vertex Colors can be unused, or filled with several types of information.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.MockDataMeshTrackerComponent.on_mesh_tracker_updated"></a>

#### on_mesh_tracker_updated

```python
@property
def on_mesh_tracker_updated() -> OnMockDataMeshTrackerUpdated
```

(OnMockDataMeshTrackerUpdated):  [Read-Write] Activated whenever new information about this mesh tracker is detected.

<a id="unreal.MockDataMeshTrackerComponent.on_mesh_tracker_updated"></a>

#### on_mesh_tracker_updated

```python
@on_mesh_tracker_updated.setter
def on_mesh_tracker_updated(value: OnMockDataMeshTrackerUpdated) -> None
```

<a id="unreal.MockDataMeshTrackerComponent.scan_world"></a>

#### scan_world

```python
@property
def scan_world() -> bool
```

(bool):  [Read-Write] Set to true to start scanning the world for meshes.

<a id="unreal.MockDataMeshTrackerComponent.scan_world"></a>

#### scan_world

```python
@scan_world.setter
def scan_world(value: bool) -> None
```

<a id="unreal.MockDataMeshTrackerComponent.request_normals"></a>

#### request_normals

```python
@property
def request_normals() -> bool
```

(bool):  [Read-Write] If true, the system will generate normals for the triangle vertices.

<a id="unreal.MockDataMeshTrackerComponent.request_normals"></a>

#### request_normals

```python
@request_normals.setter
def request_normals(value: bool) -> None
```

<a id="unreal.MockDataMeshTrackerComponent.request_vertex_confidence"></a>

#### request_vertex_confidence

```python
@property
def request_vertex_confidence() -> bool
```

(bool):  [Read-Write] If true, the system will generate the mesh confidence values for the triangle vertices.
These confidence values can be used to determine if the user needs to scan more.

<a id="unreal.MockDataMeshTrackerComponent.request_vertex_confidence"></a>

#### request_vertex_confidence

```python
@request_vertex_confidence.setter
def request_vertex_confidence(value: bool) -> None
```

<a id="unreal.MockDataMeshTrackerComponent.vertex_color_mode"></a>

#### vertex_color_mode

```python
@property
def vertex_color_mode() -> MeshTrackerVertexColorMode
```

(MeshTrackerVertexColorMode):  [Read-Write] Vertex Colors can be unused, or filled with several types of information.

<a id="unreal.MockDataMeshTrackerComponent.vertex_color_mode"></a>

#### vertex_color_mode

```python
@vertex_color_mode.setter
def vertex_color_mode(value: MeshTrackerVertexColorMode) -> None
```

<a id="unreal.MockDataMeshTrackerComponent.block_vertex_colors"></a>

#### block_vertex_colors

```python
@property
def block_vertex_colors() -> Array[Color]
```

(Array[Color]):  [Read-Write] Colors through which we cycle when setting vertex color by block.

<a id="unreal.MockDataMeshTrackerComponent.block_vertex_colors"></a>

#### block_vertex_colors

```python
@block_vertex_colors.setter
def block_vertex_colors(value: Array[Color]) -> None
```

<a id="unreal.MockDataMeshTrackerComponent.vertex_color_from_confidence_zero"></a>

#### vertex_color_from_confidence_zero

```python
@property
def vertex_color_from_confidence_zero() -> LinearColor
```

(LinearColor):  [Read-Write] Color mapped to confidence value of zero.

<a id="unreal.MockDataMeshTrackerComponent.vertex_color_from_confidence_zero"></a>

#### vertex_color_from_confidence_zero

```python
@vertex_color_from_confidence_zero.setter
def vertex_color_from_confidence_zero(value: LinearColor) -> None
```

<a id="unreal.MockDataMeshTrackerComponent.vertex_color_from_confidence_one"></a>

#### vertex_color_from_confidence_one

```python
@property
def vertex_color_from_confidence_one() -> LinearColor
```

(LinearColor):  [Read-Write] Color mapped to confidence value of one.

<a id="unreal.MockDataMeshTrackerComponent.vertex_color_from_confidence_one"></a>

#### vertex_color_from_confidence_one

```python
@vertex_color_from_confidence_one.setter
def vertex_color_from_confidence_one(value: LinearColor) -> None
```

<a id="unreal.MockDataMeshTrackerComponent.update_interval"></a>

#### update_interval

```python
@property
def update_interval() -> float
```

(float):  [Read-Write] Update Interval in Seconds.

<a id="unreal.MockDataMeshTrackerComponent.update_interval"></a>

#### update_interval

```python
@update_interval.setter
def update_interval(value: float) -> None
```

<a id="unreal.MockDataMeshTrackerComponent.disconnect_mr_mesh"></a>

#### disconnect_mr_mesh

```python
def disconnect_mr_mesh(mr_mesh_ptr: MRMeshComponent) -> None
```

x.disconnect_mr_mesh(mr_mesh_ptr) -> None
Unlinks the current procedural mesh component from the mesh tracking system.

Args:
    mr_mesh_ptr (MRMeshComponent): The procedural mesh component to unlink from the mesh tracking system.

<a id="unreal.MockDataMeshTrackerComponent.connect_mr_mesh"></a>

#### connect_mr_mesh

```python
def connect_mr_mesh(mr_mesh_ptr: MRMeshComponent) -> None
```

x.connect_mr_mesh(mr_mesh_ptr) -> None
Sets the procedural mesh component that will store and display the environmental mesh results.

Args:
    mr_mesh_ptr (MRMeshComponent): The procedural mesh component to store the query result in.

<a id="unreal.MRMeshComponent"></a>