## SceneCaptureComponent Objects

```python
class SceneCaptureComponent(SceneComponent)
```

-> will be exported to EngineDecalClasses.h

**C++ Source:**

- **Module**: Engine
- **File**: SceneCaptureComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``always_persist_rendering_state`` (bool):  [Read-Write] Whether to persist the rendering state even if bCaptureEveryFrame==false.  This allows velocities for Motion Blur and Temporal AA to be computed.
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``capture_every_frame`` (bool):  [Read-Write] Whether to update the capture's contents every frame.  If disabled, the component will render once on load and then only when moved.
- ``capture_gpu_next_render`` (bool):  [Read-Write] Capture a GPU frame for this scene capture, next time it renders (capture program must be connected).
- ``capture_on_movement`` (bool):  [Read-Write] Whether to update the capture's contents on movement.  Disable if you are going to capture manually from blueprint.
- ``capture_sort_priority`` (int32):  [Read-Write] Capture priority within the frame to sort scene capture on GPU to resolve interdependencies between multiple capture components. Highest come first.
- ``capture_source`` (SceneCaptureSource):  [Read-Write]
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``dump_gpu_next_render`` (bool):  [Read-Write] Run DumpGPU for this scene capture, next time it renders.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``hidden_actors`` (Array[Actor]):  [Read-Write] The actors to hide in the scene capture.
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``lod_distance_factor`` (float):  [Read-Write] Scales the distance used by LOD. Set to values greater than 1 to cause the scene capture to use lower LODs than the main view to speed up the scene capture pass.
- ``max_view_distance_override`` (float):  [Read-Write] if > 0, sets a maximum render distance override.  Can be used to cull distant objects from a reflection if the reflecting plane is in an enclosed area like a hallway or room
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``primitive_render_mode`` (SceneCapturePrimitiveRenderMode):  [Read-Write] Controls what primitives get rendered into the scene capture.
- ``profiling_event_name`` (str):  [Read-Write] Name of the profiling event.
- ``relative_location`` (Vector):  [Read-Write] Location of the component relative to its parent
- ``relative_rotation`` (Rotator):  [Read-Write] Rotation of the component relative to its parent
- ``relative_scale3d`` (Vector):  [Read-Write] Non-uniform scaling of the component relative to its parent.
  Note that scaling is always applied in local space (no shearing etc)
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``show_flag_settings`` (Array[EngineShowFlagsSetting]):  [Read-Write]
- ``show_only_actors`` (Array[Actor]):  [Read-Write] The only actors to be rendered by this scene capture, if PrimitiveRenderMode is set to UseShowOnlyList.
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``use_ray_tracing_if_enabled`` (bool):  [Read-Write] Whether to use ray tracing for this capture. Ray Tracing must be enabled in the project.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.SceneCaptureComponent.primitive_render_mode"></a>

#### primitive_render_mode

```python
@property
def primitive_render_mode() -> SceneCapturePrimitiveRenderMode
```

(SceneCapturePrimitiveRenderMode):  [Read-Write] Controls what primitives get rendered into the scene capture.

<a id="unreal.SceneCaptureComponent.primitive_render_mode"></a>

#### primitive_render_mode

```python
@primitive_render_mode.setter
def primitive_render_mode(value: SceneCapturePrimitiveRenderMode) -> None
```

<a id="unreal.SceneCaptureComponent.capture_source"></a>

#### capture_source

```python
@property
def capture_source() -> SceneCaptureSource
```

(SceneCaptureSource):  [Read-Write]

<a id="unreal.SceneCaptureComponent.capture_source"></a>

#### capture_source

```python
@capture_source.setter
def capture_source(value: SceneCaptureSource) -> None
```

<a id="unreal.SceneCaptureComponent.capture_every_frame"></a>

#### capture_every_frame

```python
@property
def capture_every_frame() -> bool
```

(bool):  [Read-Write] Whether to update the capture's contents every frame.  If disabled, the component will render once on load and then only when moved.

<a id="unreal.SceneCaptureComponent.capture_every_frame"></a>

#### capture_every_frame

```python
@capture_every_frame.setter
def capture_every_frame(value: bool) -> None
```

<a id="unreal.SceneCaptureComponent.capture_on_movement"></a>

#### capture_on_movement

```python
@property
def capture_on_movement() -> bool
```

(bool):  [Read-Write] Whether to update the capture's contents on movement.  Disable if you are going to capture manually from blueprint.

<a id="unreal.SceneCaptureComponent.capture_on_movement"></a>

#### capture_on_movement

```python
@capture_on_movement.setter
def capture_on_movement(value: bool) -> None
```

<a id="unreal.SceneCaptureComponent.capture_gpu_next_render"></a>

#### capture_gpu_next_render

```python
@property
def capture_gpu_next_render() -> bool
```

(bool):  [Read-Write] Capture a GPU frame for this scene capture, next time it renders (capture program must be connected).

<a id="unreal.SceneCaptureComponent.capture_gpu_next_render"></a>

#### capture_gpu_next_render

```python
@capture_gpu_next_render.setter
def capture_gpu_next_render(value: bool) -> None
```

<a id="unreal.SceneCaptureComponent.dump_gpu_next_render"></a>

#### dump_gpu_next_render

```python
@property
def dump_gpu_next_render() -> bool
```

(bool):  [Read-Write] Run DumpGPU for this scene capture, next time it renders.

<a id="unreal.SceneCaptureComponent.dump_gpu_next_render"></a>

#### dump_gpu_next_render

```python
@dump_gpu_next_render.setter
def dump_gpu_next_render(value: bool) -> None
```

<a id="unreal.SceneCaptureComponent.always_persist_rendering_state"></a>

#### always_persist_rendering_state

```python
@property
def always_persist_rendering_state() -> bool
```

(bool):  [Read-Write] Whether to persist the rendering state even if bCaptureEveryFrame==false.  This allows velocities for Motion Blur and Temporal AA to be computed.

<a id="unreal.SceneCaptureComponent.always_persist_rendering_state"></a>

#### always_persist_rendering_state

```python
@always_persist_rendering_state.setter
def always_persist_rendering_state(value: bool) -> None
```

<a id="unreal.SceneCaptureComponent.hidden_actors"></a>

#### hidden_actors

```python
@property
def hidden_actors() -> Array[Actor]
```

(Array[Actor]):  [Read-Write] The actors to hide in the scene capture.

<a id="unreal.SceneCaptureComponent.hidden_actors"></a>

#### hidden_actors

```python
@hidden_actors.setter
def hidden_actors(value: Array[Actor]) -> None
```

<a id="unreal.SceneCaptureComponent.show_only_actors"></a>

#### show_only_actors

```python
@property
def show_only_actors() -> Array[Actor]
```

(Array[Actor]):  [Read-Write] The only actors to be rendered by this scene capture, if PrimitiveRenderMode is set to UseShowOnlyList.

<a id="unreal.SceneCaptureComponent.show_only_actors"></a>

#### show_only_actors

```python
@show_only_actors.setter
def show_only_actors(value: Array[Actor]) -> None
```

<a id="unreal.SceneCaptureComponent.max_view_distance_override"></a>

#### max_view_distance_override

```python
@property
def max_view_distance_override() -> float
```

(float):  [Read-Write] if > 0, sets a maximum render distance override.  Can be used to cull distant objects from a reflection if the reflecting plane is in an enclosed area like a hallway or room

<a id="unreal.SceneCaptureComponent.max_view_distance_override"></a>

#### max_view_distance_override

```python
@max_view_distance_override.setter
def max_view_distance_override(value: float) -> None
```

<a id="unreal.SceneCaptureComponent.capture_sort_priority"></a>

#### capture_sort_priority

```python
@property
def capture_sort_priority() -> int
```

(int32):  [Read-Only] Capture priority within the frame to sort scene capture on GPU to resolve interdependencies between multiple capture components. Highest come first.

<a id="unreal.SceneCaptureComponent.use_ray_tracing_if_enabled"></a>

#### use_ray_tracing_if_enabled

```python
@property
def use_ray_tracing_if_enabled() -> bool
```

(bool):  [Read-Write] Whether to use ray tracing for this capture. Ray Tracing must be enabled in the project.

<a id="unreal.SceneCaptureComponent.use_ray_tracing_if_enabled"></a>

#### use_ray_tracing_if_enabled

```python
@use_ray_tracing_if_enabled.setter
def use_ray_tracing_if_enabled(value: bool) -> None
```

<a id="unreal.SceneCaptureComponent.show_flag_settings"></a>

#### show_flag_settings

```python
@property
def show_flag_settings() -> Array[EngineShowFlagsSetting]
```

(Array[EngineShowFlagsSetting]):  [Read-Write]

<a id="unreal.SceneCaptureComponent.show_flag_settings"></a>

#### show_flag_settings

```python
@show_flag_settings.setter
def show_flag_settings(value: Array[EngineShowFlagsSetting]) -> None
```

<a id="unreal.SceneCaptureComponent.profiling_event_name"></a>

#### profiling_event_name

```python
@property
def profiling_event_name() -> str
```

(str):  [Read-Write] Name of the profiling event.

<a id="unreal.SceneCaptureComponent.profiling_event_name"></a>

#### profiling_event_name

```python
@profiling_event_name.setter
def profiling_event_name(value: str) -> None
```

<a id="unreal.SceneCaptureComponent.show_only_component"></a>

#### show_only_component

```python
def show_only_component(component: PrimitiveComponent) -> None
```

x.show_only_component(component) -> None
Adds the component to our list of show-only components.

Args:
    component (PrimitiveComponent):

<a id="unreal.SceneCaptureComponent.show_only_actor_components"></a>

#### show_only_actor_components

```python
def show_only_actor_components(actor: Actor,
                               include_from_child_actors: bool = False
                               ) -> None
```

x.show_only_actor_components(actor, include_from_child_actors=False) -> None
Adds all primitive components in the actor to our list of show-only components.

Args:
    actor (Actor): 
    include_from_child_actors (bool): Whether to include the components from child actors

<a id="unreal.SceneCaptureComponent.set_capture_sort_priority"></a>

#### set_capture_sort_priority

```python
def set_capture_sort_priority(new_capture_sort_priority: int) -> None
```

x.set_capture_sort_priority(new_capture_sort_priority) -> None
Changes the value of TranslucentSortPriority.

Args:
    new_capture_sort_priority (int32):

<a id="unreal.SceneCaptureComponent.remove_show_only_component"></a>

#### remove_show_only_component

```python
def remove_show_only_component(component: PrimitiveComponent) -> None
```

x.remove_show_only_component(component) -> None
Removes a component from the Show Only list.

Args:
    component (PrimitiveComponent):

<a id="unreal.SceneCaptureComponent.remove_show_only_actor_components"></a>

#### remove_show_only_actor_components

```python
def remove_show_only_actor_components(actor: Actor,
                                      include_from_child_actors: bool = False
                                      ) -> None
```

x.remove_show_only_actor_components(actor, include_from_child_actors=False) -> None
Removes an actor's components from the Show Only list.

Args:
    actor (Actor): 
    include_from_child_actors (bool): Whether to remove the components from child actors

<a id="unreal.SceneCaptureComponent.hide_component"></a>

#### hide_component

```python
def hide_component(component: PrimitiveComponent) -> None
```

x.hide_component(component) -> None
Adds the component to our list of hidden components.

Args:
    component (PrimitiveComponent):

<a id="unreal.SceneCaptureComponent.hide_actor_components"></a>

#### hide_actor_components

```python
def hide_actor_components(actor: Actor,
                          include_from_child_actors: bool = False) -> None
```

x.hide_actor_components(actor, include_from_child_actors=False) -> None
Adds all primitive components in the actor to our list of hidden components.

Args:
    actor (Actor): 
    include_from_child_actors (bool): Whether to include the components from child actors

<a id="unreal.SceneCaptureComponent.clear_show_only_components"></a>

#### clear_show_only_components

```python
def clear_show_only_components() -> None
```

x.clear_show_only_components() -> None
Clears the Show Only list.

<a id="unreal.SceneCaptureComponent.clear_hidden_components"></a>

#### clear_hidden_components

```python
def clear_hidden_components() -> None
```

x.clear_hidden_components() -> None
Clears the hidden list.

<a id="unreal.PlanarReflectionComponent"></a>