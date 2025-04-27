## PlanarReflectionComponent Objects

```python
class PlanarReflectionComponent(SceneCaptureComponent)
```

UPlanarReflectionComponent

**C++ Source:**

- **Module**: Engine
- **File**: PlanarReflectionComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``always_persist_rendering_state`` (bool):  [Read-Write] Whether to persist the rendering state even if bCaptureEveryFrame==false.  This allows velocities for Motion Blur and Temporal AA to be computed.
- ``angle_from_plane_fade_end`` (float):  [Read-Write] Receiving pixels whose normal is at this angle from the reflection plane will have completely faded out the planar reflection.
- ``angle_from_plane_fade_start`` (float):  [Read-Write] Receiving pixels whose normal is at this angle from the reflection plane will begin to fade out the planar reflection.
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
- ``distance_from_plane_fadeout_end`` (float):  [Read-Write] Receiving pixels at this distance from the reflection plane will have completely faded out the planar reflection.
- ``distance_from_plane_fadeout_start`` (float):  [Read-Write] Receiving pixels at this distance from the reflection plane will begin to fade out the planar reflection.
- ``dump_gpu_next_render`` (bool):  [Read-Write] Run DumpGPU for this scene capture, next time it renders.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``extra_fov`` (float):  [Read-Write] Additional FOV used when rendering to the reflection texture.
  This is useful when normal distortion is causing reads outside the reflection texture.
  Larger values increase rendering thread and GPU cost, as more objects and triangles have to be rendered into the planar reflection.
- ``hidden_actors`` (Array[Actor]):  [Read-Write] The actors to hide in the scene capture.
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``lod_distance_factor`` (float):  [Read-Write] Scales the distance used by LOD. Set to values greater than 1 to cause the scene capture to use lower LODs than the main view to speed up the scene capture pass.
- ``max_view_distance_override`` (float):  [Read-Write] if > 0, sets a maximum render distance override.  Can be used to cull distant objects from a reflection if the reflecting plane is in an enclosed area like a hallway or room
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``normal_distortion_strength`` (float):  [Read-Write] Controls the strength of normals when distorting the planar reflection.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``prefilter_roughness`` (float):  [Read-Write] The roughness value to prefilter the planar reflection texture with, useful for hiding low resolution.  Larger values have larger GPU cost.
- ``prefilter_roughness_distance`` (float):  [Read-Write] The distance at which the prefilter roughness value will be achieved.
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``primitive_render_mode`` (SceneCapturePrimitiveRenderMode):  [Read-Write] Controls what primitives get rendered into the scene capture.
- ``profiling_event_name`` (str):  [Read-Write] Name of the profiling event.
- ``relative_location`` (Vector):  [Read-Write] Location of the component relative to its parent
- ``relative_rotation`` (Rotator):  [Read-Write] Rotation of the component relative to its parent
- ``relative_scale3d`` (Vector):  [Read-Write] Non-uniform scaling of the component relative to its parent.
  Note that scaling is always applied in local space (no shearing etc)
- ``render_scene_two_sided`` (bool):  [Read-Write] Whether to render the scene as two-sided, which can be useful to hide artifacts where normal distortion would read 'under' an object that has been clipped by the reflection plane.
  With this setting enabled, the backfaces of a mesh would be displayed in the clipped region instead of the background which is potentially a bright sky.
  Be sure to add the water plane to HiddenActors if enabling this, as the water plane will now block the reflection.
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``screen_percentage`` (int32):  [Read-Write] Downsample percent, can be used to reduce GPU time rendering the planar reflection.
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``show_flag_settings`` (Array[EngineShowFlagsSetting]):  [Read-Write]
- ``show_only_actors`` (Array[Actor]):  [Read-Write] The only actors to be rendered by this scene capture, if PrimitiveRenderMode is set to UseShowOnlyList.
- ``show_preview_plane`` (bool):  [Read-Write]
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``use_ray_tracing_if_enabled`` (bool):  [Read-Write] Whether to use ray tracing for this capture. Ray Tracing must be enabled in the project.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.PlaneReflectionCapture"></a>