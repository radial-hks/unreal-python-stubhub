## ChaosDestructionListener Objects

```python
class ChaosDestructionListener(SceneComponent)
```

Object allowing for retrieving Chaos Destruction data.

**C++ Source:**

- **Module**: GeometryCollectionEngine
- **File**: ChaosBlueprint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``breaking_event_request_settings`` (ChaosBreakingEventRequestSettings):  [Read-Write] The settings to use for breaking event listening
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``chaos_solver_actors`` (Set[ChaosSolverActor]):  [Read-Write] Which chaos solver actors we're using. If empty, this listener will fallback to the "world" solver.
- ``collision_event_request_settings`` (ChaosCollisionEventRequestSettings):  [Read-Write] The settings to use for collision event listening
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``geometry_collection_actors`` (Set[GeometryCollectionActor]):  [Read-Write] Which chaos solver actors we're using. If empty, this listener will fallback to the "world" solver.
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``is_breaking_event_listening_enabled`` (bool):  [Read-Write] Whether or not collision event listening is enabled
- ``is_collision_event_listening_enabled`` (bool):  [Read-Write] Whether or not collision event listening is enabled
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``is_removal_event_listening_enabled`` (bool):  [Read-Write] Whether or not removal event listening is enabled
- ``is_trailing_event_listening_enabled`` (bool):  [Read-Write] Whether or not trailing event listening is enabled
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``on_breaking_events`` (OnChaosBreakingEvents):  [Read-Write] Called when new breaking events are available.
- ``on_collision_events`` (OnChaosCollisionEvents):  [Read-Write] Called when new collision events are available.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``on_removal_events`` (OnChaosRemovalEvents):  [Read-Write] Called when new trailing events are available.
- ``on_trailing_events`` (OnChaosTrailingEvents):  [Read-Write] Called when new trailing events are available.
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``relative_location`` (Vector):  [Read-Write] Location of the component relative to its parent
- ``relative_rotation`` (Rotator):  [Read-Write] Rotation of the component relative to its parent
- ``relative_scale3d`` (Vector):  [Read-Write] Non-uniform scaling of the component relative to its parent.
  Note that scaling is always applied in local space (no shearing etc)
- ``removal_event_request_settings`` (ChaosRemovalEventRequestSettings):  [Read-Write] The settings to use for removal event listening
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``trailing_event_request_settings`` (ChaosTrailingEventRequestSettings):  [Read-Write] The settings to use for trailing event listening
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.ChaosDestructionListener.is_collision_event_listening_enabled"></a>

#### is_collision_event_listening_enabled

```python
@property
def is_collision_event_listening_enabled() -> bool
```

(bool):  [Read-Only] Whether or not collision event listening is enabled

<a id="unreal.ChaosDestructionListener.is_breaking_event_listening_enabled"></a>

#### is_breaking_event_listening_enabled

```python
@property
def is_breaking_event_listening_enabled() -> bool
```

(bool):  [Read-Only] Whether or not collision event listening is enabled

<a id="unreal.ChaosDestructionListener.is_trailing_event_listening_enabled"></a>

#### is_trailing_event_listening_enabled

```python
@property
def is_trailing_event_listening_enabled() -> bool
```

(bool):  [Read-Only] Whether or not trailing event listening is enabled

<a id="unreal.ChaosDestructionListener.is_removal_event_listening_enabled"></a>

#### is_removal_event_listening_enabled

```python
@property
def is_removal_event_listening_enabled() -> bool
```

(bool):  [Read-Only] Whether or not removal event listening is enabled

<a id="unreal.ChaosDestructionListener.collision_event_request_settings"></a>

#### collision_event_request_settings

```python
@property
def collision_event_request_settings() -> ChaosCollisionEventRequestSettings
```

(ChaosCollisionEventRequestSettings):  [Read-Only] The settings to use for collision event listening

<a id="unreal.ChaosDestructionListener.breaking_event_request_settings"></a>

#### breaking_event_request_settings

```python
@property
def breaking_event_request_settings() -> ChaosBreakingEventRequestSettings
```

(ChaosBreakingEventRequestSettings):  [Read-Only] The settings to use for breaking event listening

<a id="unreal.ChaosDestructionListener.trailing_event_request_settings"></a>

#### trailing_event_request_settings

```python
@property
def trailing_event_request_settings() -> ChaosTrailingEventRequestSettings
```

(ChaosTrailingEventRequestSettings):  [Read-Only] The settings to use for trailing event listening

<a id="unreal.ChaosDestructionListener.removal_event_request_settings"></a>

#### removal_event_request_settings

```python
@property
def removal_event_request_settings() -> ChaosRemovalEventRequestSettings
```

(ChaosRemovalEventRequestSettings):  [Read-Only] The settings to use for removal event listening

<a id="unreal.ChaosDestructionListener.chaos_solver_actors"></a>

#### chaos_solver_actors

```python
@property
def chaos_solver_actors() -> Set[ChaosSolverActor]
```

(Set[ChaosSolverActor]):  [Read-Only] Which chaos solver actors we're using. If empty, this listener will fallback to the "world" solver.

<a id="unreal.ChaosDestructionListener.geometry_collection_actors"></a>

#### geometry_collection_actors

```python
@property
def geometry_collection_actors() -> Set[GeometryCollectionActor]
```

(Set[GeometryCollectionActor]):  [Read-Only] Which chaos solver actors we're using. If empty, this listener will fallback to the "world" solver.

<a id="unreal.ChaosDestructionListener.on_collision_events"></a>

#### on_collision_events

```python
@property
def on_collision_events() -> OnChaosCollisionEvents
```

(OnChaosCollisionEvents):  [Read-Write] Called when new collision events are available.

<a id="unreal.ChaosDestructionListener.on_collision_events"></a>

#### on_collision_events

```python
@on_collision_events.setter
def on_collision_events(value: OnChaosCollisionEvents) -> None
```

<a id="unreal.ChaosDestructionListener.on_breaking_events"></a>

#### on_breaking_events

```python
@property
def on_breaking_events() -> OnChaosBreakingEvents
```

(OnChaosBreakingEvents):  [Read-Write] Called when new breaking events are available.

<a id="unreal.ChaosDestructionListener.on_breaking_events"></a>

#### on_breaking_events

```python
@on_breaking_events.setter
def on_breaking_events(value: OnChaosBreakingEvents) -> None
```

<a id="unreal.ChaosDestructionListener.on_trailing_events"></a>

#### on_trailing_events

```python
@property
def on_trailing_events() -> OnChaosTrailingEvents
```

(OnChaosTrailingEvents):  [Read-Write] Called when new trailing events are available.

<a id="unreal.ChaosDestructionListener.on_trailing_events"></a>

#### on_trailing_events

```python
@on_trailing_events.setter
def on_trailing_events(value: OnChaosTrailingEvents) -> None
```

<a id="unreal.ChaosDestructionListener.on_removal_events"></a>

#### on_removal_events

```python
@property
def on_removal_events() -> OnChaosRemovalEvents
```

(OnChaosRemovalEvents):  [Read-Write] Called when new trailing events are available.

<a id="unreal.ChaosDestructionListener.on_removal_events"></a>

#### on_removal_events

```python
@on_removal_events.setter
def on_removal_events(value: OnChaosRemovalEvents) -> None
```

<a id="unreal.ChaosDestructionListener.sort_trailing_events"></a>

#### sort_trailing_events

```python
def sort_trailing_events(
        trailing_events: Array[ChaosTrailingEventData],
        sort_method: ChaosTrailingSortMethod) -> Array[ChaosTrailingEventData]
```

x.sort_trailing_events(trailing_events, sort_method) -> Array[ChaosTrailingEventData]
Sorts trailing events according to the given sort method

Args:
    trailing_events (Array[ChaosTrailingEventData]): 
    sort_method (ChaosTrailingSortMethod): 

Returns:
    Array[ChaosTrailingEventData]: 

    trailing_events (Array[ChaosTrailingEventData]):

<a id="unreal.ChaosDestructionListener.sort_removal_events"></a>

#### sort_removal_events

```python
def sort_removal_events(
        removal_events: Array[ChaosRemovalEventData],
        sort_method: ChaosRemovalSortMethod) -> Array[ChaosRemovalEventData]
```

x.sort_removal_events(removal_events, sort_method) -> Array[ChaosRemovalEventData]
Sorts removal events according to the given sort method

Args:
    removal_events (Array[ChaosRemovalEventData]): 
    sort_method (ChaosRemovalSortMethod): 

Returns:
    Array[ChaosRemovalEventData]: 

    removal_events (Array[ChaosRemovalEventData]):

<a id="unreal.ChaosDestructionListener.sort_collision_events"></a>

#### sort_collision_events

```python
def sort_collision_events(
        collision_events: Array[ChaosCollisionEventData],
        sort_method: ChaosCollisionSortMethod
) -> Array[ChaosCollisionEventData]
```

x.sort_collision_events(collision_events, sort_method) -> Array[ChaosCollisionEventData]
Sorts collision events according to the given sort method

Args:
    collision_events (Array[ChaosCollisionEventData]): 
    sort_method (ChaosCollisionSortMethod): 

Returns:
    Array[ChaosCollisionEventData]: 

    collision_events (Array[ChaosCollisionEventData]):

<a id="unreal.ChaosDestructionListener.sort_breaking_events"></a>

#### sort_breaking_events

```python
def sort_breaking_events(
        breaking_events: Array[ChaosBreakingEventData],
        sort_method: ChaosBreakingSortMethod) -> Array[ChaosBreakingEventData]
```

x.sort_breaking_events(breaking_events, sort_method) -> Array[ChaosBreakingEventData]
Sorts breaking events according to the given sort method

Args:
    breaking_events (Array[ChaosBreakingEventData]): 
    sort_method (ChaosBreakingSortMethod): 

Returns:
    Array[ChaosBreakingEventData]: 

    breaking_events (Array[ChaosBreakingEventData]):

<a id="unreal.ChaosDestructionListener.set_trailing_event_request_settings"></a>

#### set_trailing_event_request_settings

```python
def set_trailing_event_request_settings(
        settings: ChaosTrailingEventRequestSettings) -> None
```

x.set_trailing_event_request_settings(settings) -> None
Sets trailing event request settings dynamically

Args:
    settings (ChaosTrailingEventRequestSettings):

<a id="unreal.ChaosDestructionListener.set_trailing_event_enabled"></a>

#### set_trailing_event_enabled

```python
def set_trailing_event_enabled(is_enabled: bool) -> None
```

x.set_trailing_event_enabled(is_enabled) -> None
Enables or disables trailing event listening

Args:
    is_enabled (bool):

<a id="unreal.ChaosDestructionListener.set_removal_event_request_settings"></a>

#### set_removal_event_request_settings

```python
def set_removal_event_request_settings(
        settings: ChaosRemovalEventRequestSettings) -> None
```

x.set_removal_event_request_settings(settings) -> None
Sets removal event request settings dynamically

Args:
    settings (ChaosRemovalEventRequestSettings):

<a id="unreal.ChaosDestructionListener.set_removal_event_enabled"></a>

#### set_removal_event_enabled

```python
def set_removal_event_enabled(is_enabled: bool) -> None
```

x.set_removal_event_enabled(is_enabled) -> None
Enables or disables removal event listening

Args:
    is_enabled (bool):

<a id="unreal.ChaosDestructionListener.set_collision_event_request_settings"></a>

#### set_collision_event_request_settings

```python
def set_collision_event_request_settings(
        settings: ChaosCollisionEventRequestSettings) -> None
```

x.set_collision_event_request_settings(settings) -> None
Sets collision event request settings dynamically

Args:
    settings (ChaosCollisionEventRequestSettings):

<a id="unreal.ChaosDestructionListener.set_collision_event_enabled"></a>

#### set_collision_event_enabled

```python
def set_collision_event_enabled(is_enabled: bool) -> None
```

x.set_collision_event_enabled(is_enabled) -> None
Enables or disables collision event listening

Args:
    is_enabled (bool):

<a id="unreal.ChaosDestructionListener.set_breaking_event_request_settings"></a>

#### set_breaking_event_request_settings

```python
def set_breaking_event_request_settings(
        settings: ChaosBreakingEventRequestSettings) -> None
```

x.set_breaking_event_request_settings(settings) -> None
Sets breaking event request settings dynamically

Args:
    settings (ChaosBreakingEventRequestSettings):

<a id="unreal.ChaosDestructionListener.set_breaking_event_enabled"></a>

#### set_breaking_event_enabled

```python
def set_breaking_event_enabled(is_enabled: bool) -> None
```

x.set_breaking_event_enabled(is_enabled) -> None
Enables or disables breaking event listening

Args:
    is_enabled (bool):

<a id="unreal.ChaosDestructionListener.remove_geometry_collection_actor"></a>

#### remove_geometry_collection_actor

```python
def remove_geometry_collection_actor(
        geometry_collection_actor: GeometryCollectionActor) -> None
```

x.remove_geometry_collection_actor(geometry_collection_actor) -> None
Dynamically removes a chaos solver from the listener

Args:
    geometry_collection_actor (GeometryCollectionActor):

<a id="unreal.ChaosDestructionListener.remove_chaos_solver_actor"></a>

#### remove_chaos_solver_actor

```python
def remove_chaos_solver_actor(chaos_solver_actor: ChaosSolverActor) -> None
```

x.remove_chaos_solver_actor(chaos_solver_actor) -> None
Dynamically removes a chaos solver from the listener

Args:
    chaos_solver_actor (ChaosSolverActor):

<a id="unreal.ChaosDestructionListener.is_event_listening"></a>

#### is_event_listening

```python
def is_event_listening() -> bool
```

x.is_event_listening() -> bool
Returns if the destruction listener is listening to any events

Returns:
    bool:

<a id="unreal.ChaosDestructionListener.add_geometry_collection_actor"></a>

#### add_geometry_collection_actor

```python
def add_geometry_collection_actor(
        geometry_collection_actor: GeometryCollectionActor) -> None
```

x.add_geometry_collection_actor(geometry_collection_actor) -> None
Dynamically adds a chaos solver to the listener

Args:
    geometry_collection_actor (GeometryCollectionActor):

<a id="unreal.ChaosDestructionListener.add_chaos_solver_actor"></a>

#### add_chaos_solver_actor

```python
def add_chaos_solver_actor(chaos_solver_actor: ChaosSolverActor) -> None
```

x.add_chaos_solver_actor(chaos_solver_actor) -> None
Dynamically adds a chaos solver to the listener

Args:
    chaos_solver_actor (ChaosSolverActor):

<a id="unreal.GeometryCollectionActor"></a>