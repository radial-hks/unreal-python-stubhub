## DisplayClusterStageGeometryComponent Objects

```python
class DisplayClusterStageGeometryComponent(ActorComponent)
```

A component that stores the generated geometry map of the stage actor, which is used for placing stage actors (light cards, CCWs, etc) flush to the stage's walls and ceiling

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayCluster
- **File**: DisplayClusterStageGeometryComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.DisplayClusterStageGeometryComponent.is_geometry_map_valid"></a>

#### is_geometry_map_valid

```python
def is_geometry_map_valid() -> bool
```

x.is_geometry_map_valid() -> bool
Gets whether the stage geometry map is valid and usable

Returns:
    bool:

<a id="unreal.DisplayClusterStageGeometryComponent.invalidate"></a>

#### invalidate

```python
def invalidate(force_immediate_redraw: bool = False) -> None
```

x.invalidate(force_immediate_redraw=False) -> None
Invalidates and regenerates the cached stage geometry map

Args:
    force_immediate_redraw (bool): Indicates whether the geometry map is regenerated immediately or is queued to redraw on the next tick

<a id="unreal.DisplayClusterStageGeometryComponent.get_stage_distance_and_normal"></a>

#### get_stage_distance_and_normal

```python
def get_stage_distance_and_normal(
        direction: Vector) -> Optional[Tuple[float, Vector]]
```

x.get_stage_distance_and_normal(direction) -> (out_distance=float, out_normal=Vector) or None
Gets the distance and normal vector (in radial space) of the stage's geometry in the specified world direction

Args:
    direction (Vector): The direction in world coordinates to query the stage geometry map

Returns:
    tuple or None: true if the stage geometry map was successfully queried, otherwise false

    out_distance (float): The distance from the stage's default view point to the nearest stage geometry in the specified direction

    out_normal (Vector): The normal vector in radial space (with x axis pointing in the direction of the stage's default view point) of the nearest stage geometry in the specified direction

<a id="unreal.DisplayClusterStageIsosphereComponent"></a>