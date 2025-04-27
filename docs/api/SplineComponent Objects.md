## SplineComponent Objects

```python
class SplineComponent(PrimitiveComponent)
```

A spline component is a spline shape which can be used for other purposes (e.g. animating objects). It contains debug rendering capabilities.
see: https://docs.unrealengine.com/latest/INT/Resources/ContentExamples/Blueprint_Splines

**C++ Source:**

- **Module**: Engine
- **File**: SplineComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``adjust_tangents_on_snap`` (bool):  [Read-Write] Adjust tangents after snapping.
- ``affect_distance_field_lighting`` (bool):  [Read-Write] Controls whether the primitive should affect dynamic distance field lighting methods.  This flag is only used if CastShadow is true. *
- ``affect_dynamic_indirect_lighting`` (bool):  [Read-Write] Controls whether the primitive should influence indirect lighting.
- ``affect_indirect_lighting_while_hidden`` (bool):  [Read-Write] Controls whether the primitive should affect indirect lighting when hidden. This flag is only used if bAffectDynamicIndirectLighting is true.
- ``allow_cull_distance_volume`` (bool):  [Read-Write] Whether to accept cull distance volumes to modify cached cull distance.
- ``allow_discontinuous_spline`` (bool):  [Read-Write] Whether the spline's leave and arrive tangents can be different
- ``always_create_physics_state`` (bool):  [Read-Write] Indicates if we'd like to create physics state all the time (for collision and simulation).
  If you set this to false, it still will create physics state if collision or simulation activated.
  This can help performance if you'd like to avoid overhead of creating physics state when triggers
- ``apply_impulse_on_damage`` (bool):  [Read-Write] True for damage to this component to apply physics impulse, false to opt out of these impulses.
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``body_instance`` (BodyInstance):  [Read-Write] Physics scene information for this component, holds a single rigid body with multiple shapes.
- ``bounds_scale`` (float):  [Read-Write] Scales the bounds of the object.
  This is useful when using World Position Offset to animate the vertices of the object outside of its bounds.
  Warning: Increasing the bounds of an object will reduce performance and shadow quality!
  Currently only used by StaticMeshComponent and SkeletalMeshComponent.
- ``cached_max_draw_distance`` (float):  [Read-Only] The distance to cull this primitive at.
  A CachedMaxDrawDistance of 0 indicates that the primitive should not be culled by distance.
- ``can_character_step_up_on`` (CanBeCharacterBase):  [Read-Write] Determine whether a Character can step up onto this component.
  This controls whether they can try to step up on it when they bump in to it, not whether they can walk on it after landing on it.
  see: FWalkableSlopeOverride
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``cast_cinematic_shadow`` (bool):  [Read-Write] Whether this component should cast shadows from lights that have bCastShadowsFromCinematicObjectsOnly enabled.
  This is useful for characters in a cinematic with special cinematic lights, where the cost of shadowmap rendering of the environment is undesired.
- ``cast_contact_shadow`` (bool):  [Read-Write] Whether the object should cast contact shadows.
  This flag is only used if CastShadow is true.
- ``cast_dynamic_shadow`` (bool):  [Read-Write] Controls whether the primitive should cast shadows in the case of non precomputed shadowing.  This flag is only used if CastShadow is true. *
- ``cast_far_shadow`` (bool):  [Read-Write] When enabled, the component will be rendering into the far shadow cascades (only for directional lights).
- ``cast_hidden_shadow`` (bool):  [Read-Write] If true, the primitive will cast shadows even if bHidden is true.
  Controls whether the primitive should cast shadows when hidden.
  This flag is only used if CastShadow is true.
- ``cast_inset_shadow`` (bool):  [Read-Write] Whether this component should create a per-object shadow that gives higher effective shadow resolution.
  Useful for cinematic character shadowing. Assumed to be enabled if bSelfShadowOnly is enabled.
- ``cast_shadow`` (bool):  [Read-Write] Controls whether the primitive component should cast a shadow or not.
- ``cast_shadow_as_two_sided`` (bool):  [Read-Write] Whether this primitive should cast dynamic shadows as if it were a two sided material.
- ``cast_static_shadow`` (bool):  [Read-Write] Whether the object should cast a static shadow from shadow casting lights.  This flag is only used if CastShadow is true.
- ``cast_volumetric_translucent_shadow`` (bool):  [Read-Write] Whether the object should cast a volumetric translucent shadow.
  Volumetric translucent shadows are useful for primitives with smoothly changing opacity like particles representing a volume,
  But have artifacts when used on highly opaque surfaces.
- ``closed_loop`` (bool):  [Read-Write] Whether the spline is to be considered as a closed loop.
  Use SetClosedLoop() to set this property, and IsClosedLoop() to read it.
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``consider_for_actor_placement_when_hidden`` (bool):  [Read-Write] If true, this component will be considered for placement when dragging and placing items in the editor even if it is not visible, such as in the case of hidden collision meshes
- ``custom_depth_stencil_value`` (int32):  [Read-Write] Optionally write this 0-255 value to the stencil buffer in CustomDepth pass (Requires project setting or r.CustomDepth == 3)
- ``custom_depth_stencil_write_mask`` (RendererStencilMask):  [Read-Write] Mask used for stencil buffer writes.
- ``custom_primitive_data`` (CustomPrimitiveData):  [Read-Write] Optional user defined default values for the custom primitive data of this primitive
- ``default_up_vector`` (Vector):  [Read-Write] Default up vector in local space to be used when calculating transforms along the spline
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``draw_debug`` (bool):  [Read-Write] If true, the spline will be rendered if the Splines showflag is set.
- ``duration`` (float):  [Read-Write] Specifies the duration of the spline in seconds
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``editor_selected_spline_segment_color`` (LinearColor):  [Read-Write] Color of selected spline component parts in the editor
- ``editor_tangent_color`` (LinearColor):  [Read-Write] Color of spline point tangents in the editor
- ``editor_unselected_spline_segment_color`` (LinearColor):  [Read-Write] Color of unselected spline component parts in the editor
- ``emissive_light_source`` (bool):  [Read-Write] Whether the primitive will be used as an emissive light source.
- ``enable_auto_lod_generation`` (bool):  [Read-Write] Whether to include this component in HLODs or not.
- ``exclude_for_specific_hlod_levels`` (Array[int32]):  [Read-Write]
  deprecated: WARNING: This property has been deprecated, use the SetExcludedFromHLODLevel/IsExcludedFromHLODLevel functions instead
- ``exclude_from_hlod_levels`` (uint8):  [Read-Write] Which specific HLOD levels this component should be excluded from
- ``exclude_from_light_attachment_group`` (bool):  [Read-Write] If set, then it overrides any bLightAttachmentsAsGroup set in a parent.
- ``fill_collision_underneath_for_navmesh`` (bool):  [Read-Write] If set, navmesh will not be generated under the surface of the geometry
- ``first_person_primitive_type`` (FirstPersonPrimitiveType):  [Read-Write] If this is set to FirstPerson, the camera FirstPersonFieldOfView and FirstPersonScale parameters will be used on this component. These parameters can be used to render the component with a different field of view and a smaller depth range such that clipping with the scene can be avoided. This is useful for rendering first person view geometry.
- ``force_mip_streaming`` (bool):  [Read-Write] If true, forces mips for textures used by this component to be resident when this component's level is loaded.
- ``generate_overlap_events`` (bool):  [Read-Write]
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``hidden_in_scene_capture`` (bool):  [Read-Write] When true, will not be captured by Scene Capture
- ``hlod_batching_policy`` (HLODBatchingPolicy):  [Read-Write] Determines how the geometry of a component will be incorporated in proxy (simplified) HLODs.
- ``holdout`` (bool):  [Read-Write] If this is True, this primitive will render black with an alpha of 0, but all secondary effects (shadows, reflections, indirect lighting) remain. This feature requires activating the project setting(s) "Alpha Output", and "Support Primitive Alpha Holdout" if using the deferred renderer.
- ``ignore_radial_force`` (bool):  [Read-Write] Will ignore radial forces applied to this component.
- ``ignore_radial_impulse`` (bool):  [Read-Write] Will ignore radial impulses applied to this component.
- ``indirect_lighting_cache_quality`` (IndirectLightingCacheQuality):  [Read-Write] Quality of indirect lighting for Movable primitives.  This has a large effect on Indirect Lighting Cache update time.
- ``input_spline_points_to_construction_script`` (bool):  [Read-Write] Whether the spline points should be passed to the User Construction Script so they can be further manipulated by it.
  If false, they will not be visible to it, and it will not be able to influence the per-instance positions set in the editor.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``ld_max_draw_distance`` (float):  [Read-Write] Max draw distance exposed to LDs. The real max draw distance is the min (disregarding 0) of this and volumes affecting this object.
- ``light_attachments_as_group`` (bool):  [Read-Write] Whether to light this component and any attachments as a group.  This only has effect on the root component of an attachment tree.
  When enabled, attached component shadowing settings like bCastInsetShadow, bCastVolumetricTranslucentShadow, etc, will be ignored.
  This is useful for improving performance when multiple movable components are attached together.
- ``lighting_channels`` (LightingChannels):  [Read-Write] Channels that this component should be in.  Lights with matching channels will affect the component.
  These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing.
  Lighting channels are only supported on translucent materials using forward shading (i.e. when not using the translucency lighting volume).
- ``lightmap_type`` (LightmapType):  [Read-Write]
- ``loop_position`` (float):  [Read-Write]
- ``loop_position_override`` (bool):  [Read-Write]
- ``min_draw_distance`` (float):  [Read-Write] The minimum distance at which the primitive should be rendered,
  measured in world space units from the center of the primitive's bounding sphere to the camera position.
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``multi_body_overlap`` (bool):  [Read-Write] If true, this component will generate individual overlaps for each overlapping physics body if it is a multi-body component. When false, this component will
  generate only one overlap, regardless of how many physics bodies it has and how many of them are overlapping another component/body. This flag has no
  influence on single body components.
- ``never_distance_cull`` (bool):  [Read-Write] When enabled this object will not be culled by distance. This is ignored if a child of a HLOD.
- ``on_begin_cursor_over`` (ComponentBeginCursorOverSignature):  [Read-Write] Event called when the mouse cursor is moved over this component and mouse over events are enabled in the player controller
- ``on_clicked`` (ComponentOnClickedSignature):  [Read-Write] Event called when the left mouse button is clicked while the mouse is over this component and click events are enabled in the player controller
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_begin_overlap`` (ComponentBeginOverlapSignature):  [Read-Write] Event called when something starts to overlaps this component, for example a player walking into a trigger.
  For events when objects have a blocking collision, for example a player hitting a wall, see 'Hit' events.
  note: Both this component and the other one must have GetGenerateOverlapEvents() set to true to generate overlap events.
  note: When receiving an overlap from another object's movement, the directions of 'Hit.Normal' and 'Hit.ImpactNormal' will be adjusted to indicate force from the other object against this object.
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``on_component_end_overlap`` (ComponentEndOverlapSignature):  [Read-Write] Event called when something stops overlapping this component
  note: Both this component and the other one must have GetGenerateOverlapEvents() set to true to generate overlap events.
- ``on_component_hit`` (ComponentHitSignature):  [Read-Write] Event called when a component hits (or is hit by) something solid. This could happen due to things like Character movement, using Set Location with 'sweep' enabled, or physics simulation.
  For events when objects overlap (e.g. walking into a trigger) see the 'Overlap' event.
  note: For collisions during physics simulation to generate hit events, 'Simulation Generates Hit Events' must be enabled for this component.
  note: When receiving a hit from another object's movement, the directions of 'Hit.Normal' and 'Hit.ImpactNormal' will be adjusted to indicate force from the other object against this object.
  note: NormalImpulse will be filled in for physics-simulating bodies, but will be zero for swept-component blocking collisions.
- ``on_component_physics_state_changed`` (ComponentPhysicsStateChanged):  [Read-Write] Event called when physics state is created or destroyed for this component
- ``on_component_sleep`` (ComponentSleepSignature):  [Read-Write] Event called when the underlying physics objects is put to sleep
- ``on_component_wake`` (ComponentWakeSignature):  [Read-Write] Event called when the underlying physics objects is woken up
- ``on_end_cursor_over`` (ComponentEndCursorOverSignature):  [Read-Write] Event called when the mouse cursor is moved off this component and mouse over events are enabled in the player controller
- ``on_input_touch_begin`` (ComponentOnInputTouchBeginSignature):  [Read-Write] Event called when a touch input is received over this component when touch events are enabled in the player controller
- ``on_input_touch_end`` (ComponentOnInputTouchEndSignature):  [Read-Write] Event called when a touch input is released over this component when touch events are enabled in the player controller
- ``on_input_touch_enter`` (ComponentBeginTouchOverSignature):  [Read-Write] Event called when a finger is moved over this component when touch over events are enabled in the player controller
- ``on_input_touch_leave`` (ComponentEndTouchOverSignature):  [Read-Write] Event called when a finger is moved off this component when touch over events are enabled in the player controller
- ``on_released`` (ComponentOnReleasedSignature):  [Read-Write] Event called when the left mouse button is released while the mouse is over this component click events are enabled in the player controller
- ``only_owner_see`` (bool):  [Read-Write] If this is True, this component will only be visible when the view actor is the component's owner, directly or indirectly.
- ``owner_no_see`` (bool):  [Read-Write] If this is True, this component won't be visible when the view actor is the component's owner, directly or indirectly.
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``ray_tracing_group_culling_priority`` (RayTracingGroupCullingPriority):  [Read-Write] Defines how quickly it should be culled. For example buildings should have a low priority, but small dressing should have a high priority.
- ``ray_tracing_group_id`` (int32):  [Read-Write] Defines run-time groups of components. For example allows to assemble multiple parts of a building at runtime.
  -1 means that component doesn't belong to any group.
- ``receive_mobile_csm_shadows`` (bool):  [Read-Write] Mobile only:
  If disabled this component will not receive CSM shadows. (Components that do not receive CSM may have reduced shading cost)
- ``receives_decals`` (bool):  [Read-Write] Whether the primitive receives decals.
- ``relative_location`` (Vector):  [Read-Write] Location of the component relative to its parent
- ``relative_rotation`` (Rotator):  [Read-Write] Rotation of the component relative to its parent
- ``relative_scale3d`` (Vector):  [Read-Write] Non-uniform scaling of the component relative to its parent.
  Note that scaling is always applied in local space (no shearing etc)
- ``render_custom_depth`` (bool):  [Read-Write] If true, this component will be rendered in the CustomDepth pass (usually used for outlines)
- ``render_in_depth_pass`` (bool):  [Read-Write] If true, this component will be rendered in the depth pass even if it's not rendered in the main pass
- ``render_in_main_pass`` (bool):  [Read-Write] If true, this component will be rendered in the main pass (z prepass, basepass, transparency)
- ``reparam_steps_per_segment`` (int32):  [Read-Write] Number of steps per spline segment to place in the reparameterization table
- ``replicate_physics_to_autonomous_proxy`` (bool):  [Read-Write] True if physics should be replicated to autonomous proxies. This should be true for
                server-authoritative simulations, and false for client authoritative simulations.
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``return_material_on_move`` (bool):  [Read-Write] If true, component sweeps will return the material in their hit result.
  see: MoveComponent(), FHitResult
- ``runtime_virtual_textures`` (Array[RuntimeVirtualTexture]):  [Read-Write] Array of runtime virtual textures into which we draw the mesh for this actor.
  The material also needs to be set up to output to a virtual texture.
- ``scale_visualization_width`` (float):  [Read-Write] Width of spline in editor for use with scale visualization
- ``self_shadow_only`` (bool):  [Read-Write] When enabled, the component will only cast a shadow on itself and not other components in the world.
  This is especially useful for first person weapons, and forces bCastInsetShadow to be enabled.
- ``shadow_cache_invalidation_behavior`` (ShadowCacheInvalidationBehavior):  [Read-Write] Control shadow invalidation behavior, in particular with respect to Virtual Shadow Maps and material effects like World Position Offset.
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``should_visualize_scale`` (bool):  [Read-Write] Whether scale visualization should be displayed
- ``single_sample_shadow_from_stationary_lights`` (bool):  [Read-Write] Whether the whole component should be shadowed as one from stationary lights, which makes shadow receiving much cheaper.
  When enabled shadowing data comes from the volume lighting samples precomputed by Lightmass, which are very sparse.
  This is currently only used on stationary directional lights.
- ``spline_curves`` (SplineCurves):  [Read-Write]
- ``spline_has_been_edited`` (bool):  [Read-Write] Whether the spline has been edited from its default by the spline component visualizer
- ``static_when_not_moveable`` (bool):  [Read-Write] When false, the underlying physics body will contain all sim data (mass, inertia tensor, etc) even if mobility is not set to Moveable
- ``stationary_endpoints`` (bool):  [Read-Write] Whether the endpoints of the spline are considered stationary when traversing the spline at non-constant velocity.  Essentially this sets the endpoints' tangents to zero vectors.
- ``trace_complex_on_move`` (bool):  [Read-Write] If true, component sweeps with this component should trace against complex collision during movement (for example, each triangle of a mesh).
  If false, collision will be resolved against simple collision bounds instead.
  see: MoveComponent()
- ``translucency_sort_distance_offset`` (float):  [Read-Write] Modified sort distance offset for translucent objects in world units.
  A positive number will move the sort distance further and a negative number will move the distance closer.

  Ignored if the object is not translucent.
  Warning: Adjusting this value will prevent the renderer from correctly sorting based on distance.  Only modify this value if you are certain it will not cause visual artifacts.
- ``translucency_sort_priority`` (int32):  [Read-Write] Translucent objects with a lower sort priority draw behind objects with a higher priority.
  Translucent objects with the same priority are rendered from back-to-front based on their bounds origin.
  This setting is also used to sort objects being drawn into a runtime virtual texture.

  Ignored if the object is not translucent.  The default priority is zero.
  Warning: This should never be set to a non-default value unless you know what you are doing, as it will prevent the renderer from sorting correctly.
  It is especially problematic on dynamic gameplay effects.
- ``treat_as_background_for_occlusion`` (bool):  [Read-Write] Treat this primitive as part of the background for occlusion purposes. This can be used as an optimization to reduce the cost of rendering skyboxes, large ground planes that are part of the vista, etc.
- ``use_as_occluder`` (bool):  [Read-Write] Whether to render the primitive in the depth only pass.
  This should generally be true for all objects, and let the renderer make decisions about whether to render objects in the depth only pass.
  todo: if any rendering features rely on a complete depth only pass, this variable needs to go away.
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``virtual_texture_cull_mips`` (int8):  [Read-Write] Number of lower mips in the runtime virtual texture to skip for rendering this primitive.
  Larger values reduce the effective draw distance in the runtime virtual texture.
  This culling method doesn't take into account primitive size or virtual texture size.
- ``virtual_texture_lod_bias`` (int8):  [Read-Write] Bias to the LOD selected for rendering to runtime virtual textures.
- ``virtual_texture_min_coverage`` (int8):  [Read-Write] Set the minimum pixel coverage before culling from the runtime virtual texture.
  Larger values reduce the effective draw distance in the runtime virtual texture.
- ``virtual_texture_render_pass_type`` (RuntimeVirtualTextureMainPassType):  [Read-Write] Controls if this component draws in the main pass as well as in the virtual texture.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.
- ``visible_in_ray_tracing`` (bool):  [Read-Write] If true, this component will be visible in ray tracing effects. Turning this off will remove it from ray traced reflections, shadows, etc.
- ``visible_in_real_time_sky_captures`` (bool):  [Read-Write] If true, this component will be visible in real-time sky light reflection captures.
- ``visible_in_reflection_captures`` (bool):  [Read-Write] If true, this component will be visible in reflection captures.
- ``visible_in_scene_capture_only`` (bool):  [Read-Write] When true, will only be visible in Scene Capture

<a id="unreal.SplineComponent.duration"></a>

#### duration

```python
@property
def duration() -> float
```

(float):  [Read-Write] Specifies the duration of the spline in seconds

<a id="unreal.SplineComponent.duration"></a>

#### duration

```python
@duration.setter
def duration(value: float) -> None
```

<a id="unreal.SplineComponent.stationary_endpoints"></a>

#### stationary_endpoints

```python
@property
def stationary_endpoints() -> bool
```

(bool):  [Read-Write] Whether the endpoints of the spline are considered stationary when traversing the spline at non-constant velocity.  Essentially this sets the endpoints' tangents to zero vectors.

<a id="unreal.SplineComponent.stationary_endpoints"></a>

#### stationary_endpoints

```python
@stationary_endpoints.setter
def stationary_endpoints(value: bool) -> None
```

<a id="unreal.SplineComponent.input_spline_points_to_construction_script"></a>

#### input_spline_points_to_construction_script

```python
@property
def input_spline_points_to_construction_script() -> bool
```

(bool):  [Read-Write] Whether the spline points should be passed to the User Construction Script so they can be further manipulated by it.
If false, they will not be visible to it, and it will not be able to influence the per-instance positions set in the editor.

<a id="unreal.SplineComponent.input_spline_points_to_construction_script"></a>

#### input_spline_points_to_construction_script

```python
@input_spline_points_to_construction_script.setter
def input_spline_points_to_construction_script(value: bool) -> None
```

<a id="unreal.SplineComponent.draw_debug"></a>

#### draw_debug

```python
@property
def draw_debug() -> bool
```

(bool):  [Read-Write] If true, the spline will be rendered if the Splines showflag is set.

<a id="unreal.SplineComponent.draw_debug"></a>

#### draw_debug

```python
@draw_debug.setter
def draw_debug(value: bool) -> None
```

<a id="unreal.SplineComponent.b_always_render_in_editor"></a>

#### b_always_render_in_editor

```python
@property
def b_always_render_in_editor() -> bool
```

deprecated: 'b_always_render_in_editor' was renamed to 'draw_debug'.

<a id="unreal.SplineComponent.b_always_render_in_editor"></a>

#### b_always_render_in_editor

```python
@b_always_render_in_editor.setter
def b_always_render_in_editor(value: bool) -> None
```

<a id="unreal.SplineComponent.default_up_vector"></a>

#### default_up_vector

```python
@property
def default_up_vector() -> Vector
```

(Vector):  [Read-Write] Default up vector in local space to be used when calculating transforms along the spline

<a id="unreal.SplineComponent.default_up_vector"></a>

#### default_up_vector

```python
@default_up_vector.setter
def default_up_vector(value: Vector) -> None
```

<a id="unreal.SplineComponent.update_spline"></a>

#### update_spline

```python
def update_spline() -> None
```

x.update_spline() -> None
Update the spline tangents and SplineReparamTable

<a id="unreal.SplineComponent.set_world_location_at_spline_point"></a>

#### set_world_location_at_spline_point

```python
def set_world_location_at_spline_point(point_index: int,
                                       location: Vector) -> None
```

x.set_world_location_at_spline_point(point_index, location) -> None
Move an existing point to a new world location
deprecated: Please use SetLocationAtSplinePoint, specifying SplineCoordinateSpace::World

Args:
    point_index (int32): 
    location (Vector):

<a id="unreal.SplineComponent.set_up_vector_at_spline_point"></a>

#### set_up_vector_at_spline_point

```python
def set_up_vector_at_spline_point(point_index: int,
                                  up_vector: Vector,
                                  coordinate_space: SplineCoordinateSpace,
                                  update_spline: bool = True) -> None
```

x.set_up_vector_at_spline_point(point_index, up_vector, coordinate_space, update_spline=True) -> None
Specify the up vector at a given spline point

Args:
    point_index (int32): 
    up_vector (Vector): 
    coordinate_space (SplineCoordinateSpace): 
    update_spline (bool):

<a id="unreal.SplineComponent.set_unselected_spline_segment_color"></a>

#### set_unselected_spline_segment_color

```python
def set_unselected_spline_segment_color(segment_color: LinearColor) -> None
```

x.set_unselected_spline_segment_color(segment_color) -> None
Specify unselected spline component segment color in the editor

Args:
    segment_color (LinearColor):

<a id="unreal.SplineComponent.set_tangents_at_spline_point"></a>

#### set_tangents_at_spline_point

```python
def set_tangents_at_spline_point(point_index: int,
                                 arrive_tangent: Vector,
                                 leave_tangent: Vector,
                                 coordinate_space: SplineCoordinateSpace,
                                 update_spline: bool = True) -> None
```

x.set_tangents_at_spline_point(point_index, arrive_tangent, leave_tangent, coordinate_space, update_spline=True) -> None
Specify the tangents at a given spline point

Args:
    point_index (int32): 
    arrive_tangent (Vector): 
    leave_tangent (Vector): 
    coordinate_space (SplineCoordinateSpace): 
    update_spline (bool):

<a id="unreal.SplineComponent.set_tangent_color"></a>

#### set_tangent_color

```python
def set_tangent_color(tangent_color: LinearColor) -> None
```

x.set_tangent_color(tangent_color) -> None
Specify selected spline component segment color in the editor

Args:
    tangent_color (LinearColor):

<a id="unreal.SplineComponent.set_tangent_at_spline_point"></a>

#### set_tangent_at_spline_point

```python
def set_tangent_at_spline_point(point_index: int,
                                tangent: Vector,
                                coordinate_space: SplineCoordinateSpace,
                                update_spline: bool = True) -> None
```

x.set_tangent_at_spline_point(point_index, tangent, coordinate_space, update_spline=True) -> None
Specify the tangent at a given spline point

Args:
    point_index (int32): 
    tangent (Vector): 
    coordinate_space (SplineCoordinateSpace): 
    update_spline (bool):

<a id="unreal.SplineComponent.set_spline_world_points"></a>

#### set_spline_world_points

```python
def set_spline_world_points(points: Array[Vector]) -> None
```

x.set_spline_world_points(points) -> None
Sets the spline to an array of world space points
deprecated: Please use SetSplinePoints, specifying SplineCoordinateSpace::World

Args:
    points (Array[Vector]):

<a id="unreal.SplineComponent.set_spline_point_type"></a>

#### set_spline_point_type

```python
def set_spline_point_type(point_index: int,
                          type: SplinePointType,
                          update_spline: bool = True) -> None
```

x.set_spline_point_type(point_index, type, update_spline=True) -> None
Specify the type of a spline point

Args:
    point_index (int32): 
    type (SplinePointType): 
    update_spline (bool):

<a id="unreal.SplineComponent.set_spline_points"></a>

#### set_spline_points

```python
def set_spline_points(points: Array[Vector],
                      coordinate_space: SplineCoordinateSpace,
                      update_spline: bool = True) -> None
```

x.set_spline_points(points, coordinate_space, update_spline=True) -> None
Sets the spline to an array of points

Args:
    points (Array[Vector]): 
    coordinate_space (SplineCoordinateSpace): 
    update_spline (bool):

<a id="unreal.SplineComponent.set_spline_local_points"></a>

#### set_spline_local_points

```python
def set_spline_local_points(points: Array[Vector]) -> None
```

x.set_spline_local_points(points) -> None
Sets the spline to an array of local space points
deprecated: Please use SetSplinePoints, specifying SplineCoordinateSpace::Local

Args:
    points (Array[Vector]):

<a id="unreal.SplineComponent.set_selected_spline_segment_color"></a>

#### set_selected_spline_segment_color

```python
def set_selected_spline_segment_color(segment_color: LinearColor) -> None
```

x.set_selected_spline_segment_color(segment_color) -> None
Specify selected spline component segment color in the editor

Args:
    segment_color (LinearColor):

<a id="unreal.SplineComponent.set_scale_at_spline_point"></a>

#### set_scale_at_spline_point

```python
def set_scale_at_spline_point(point_index: int,
                              scale_vector: Vector,
                              update_spline: bool = True) -> None
```

x.set_scale_at_spline_point(point_index, scale_vector, update_spline=True) -> None
Set the scale at a given spline point

Args:
    point_index (int32): 
    scale_vector (Vector): 
    update_spline (bool):

<a id="unreal.SplineComponent.set_rotation_at_spline_point"></a>

#### set_rotation_at_spline_point

```python
def set_rotation_at_spline_point(point_index: int,
                                 rotation: Rotator,
                                 coordinate_space: SplineCoordinateSpace,
                                 update_spline: bool = True) -> None
```

x.set_rotation_at_spline_point(point_index, rotation, coordinate_space, update_spline=True) -> None
Set the rotation of an existing spline point

Args:
    point_index (int32): 
    rotation (Rotator): 
    coordinate_space (SplineCoordinateSpace): 
    update_spline (bool):

<a id="unreal.SplineComponent.set_override_construction_script"></a>

#### set_override_construction_script

```python
def set_override_construction_script(override: bool) -> None
```

x.set_override_construction_script(override) -> None
Set the spline to be edited outside of the construction script

Args:
    override (bool):

<a id="unreal.SplineComponent.set_location_at_spline_point"></a>

#### set_location_at_spline_point

```python
def set_location_at_spline_point(point_index: int,
                                 location: Vector,
                                 coordinate_space: SplineCoordinateSpace,
                                 update_spline: bool = True) -> None
```

x.set_location_at_spline_point(point_index, location, coordinate_space, update_spline=True) -> None
Move an existing point to a new location

Args:
    point_index (int32): 
    location (Vector): 
    coordinate_space (SplineCoordinateSpace): 
    update_spline (bool):

<a id="unreal.SplineComponent.set_draw_debug"></a>

#### set_draw_debug

```python
def set_draw_debug(show: bool) -> None
```

x.set_draw_debug(show) -> None
Specify whether this spline should be rendered when the Editor/Game spline show flag is set

Args:
    show (bool):

<a id="unreal.SplineComponent.set_default_up_vector"></a>

#### set_default_up_vector

```python
def set_default_up_vector(up_vector: Vector,
                          coordinate_space: SplineCoordinateSpace) -> None
```

x.set_default_up_vector(up_vector, coordinate_space) -> None
Sets the default up vector used by this spline

Args:
    up_vector (Vector): 
    coordinate_space (SplineCoordinateSpace):

<a id="unreal.SplineComponent.set_closed_loop_at_position"></a>

#### set_closed_loop_at_position

```python
def set_closed_loop_at_position(closed_loop: bool,
                                key: float,
                                update_spline: bool = True) -> None
```

x.set_closed_loop_at_position(closed_loop, key, update_spline=True) -> None
Specify whether the spline is a closed loop or not, and if so, the input key corresponding to the loop point

Args:
    closed_loop (bool): 
    key (float): 
    update_spline (bool):

<a id="unreal.SplineComponent.set_closed_loop"></a>

#### set_closed_loop

```python
def set_closed_loop(closed_loop: bool, update_spline: bool = True) -> None
```

x.set_closed_loop(closed_loop, update_spline=True) -> None
Specify whether the spline is a closed loop or not. The loop position will be at 1.0 after the last point's input key

Args:
    closed_loop (bool): 
    update_spline (bool):

<a id="unreal.SplineComponent.remove_spline_point"></a>

#### remove_spline_point

```python
def remove_spline_point(index: int, update_spline: bool = True) -> None
```

x.remove_spline_point(index, update_spline=True) -> None
Removes point at specified index from the spline

Args:
    index (int32): 
    update_spline (bool):

<a id="unreal.SplineComponent.is_closed_loop"></a>

#### is_closed_loop

```python
def is_closed_loop() -> bool
```

x.is_closed_loop() -> bool
Check whether the spline is a closed loop or not

Returns:
    bool:

<a id="unreal.SplineComponent.get_world_tangent_at_distance_along_spline"></a>

#### get_world_tangent_at_distance_along_spline

```python
def get_world_tangent_at_distance_along_spline(distance: float) -> Vector
```

x.get_world_tangent_at_distance_along_spline(distance) -> Vector
Given a distance along the length of this spline, return the tangent vector of the spline there, in world space.
deprecated: Please use GetTangentAtDistanceAlongSpline, specifying SplineCoordinateSpace::World

Args:
    distance (float): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_world_rotation_at_time"></a>

#### get_world_rotation_at_time

```python
def get_world_rotation_at_time(time: float,
                               use_constant_velocity: bool = False) -> Rotator
```

x.get_world_rotation_at_time(time, use_constant_velocity=False) -> Rotator
Given a time from 0 to the spline duration, return a rotation corresponding to the spline's position and direction there, in world space.
deprecated: Please use GetRotationAtTime, specifying SplineCoordinateSpace::World

Args:
    time (float): 
    use_constant_velocity (bool): 

Returns:
    Rotator:

<a id="unreal.SplineComponent.get_world_rotation_at_distance_along_spline"></a>

#### get_world_rotation_at_distance_along_spline

```python
def get_world_rotation_at_distance_along_spline(distance: float) -> Rotator
```

x.get_world_rotation_at_distance_along_spline(distance) -> Rotator
Given a distance along the length of this spline, return a rotation corresponding to the spline's rotation there, in world space.
deprecated: Please use GetRotationAtDistanceAlongSpline, specifying SplineCoordinateSpace::World

Args:
    distance (float): 

Returns:
    Rotator:

<a id="unreal.SplineComponent.get_world_location_at_time"></a>

#### get_world_location_at_time

```python
def get_world_location_at_time(time: float,
                               use_constant_velocity: bool = False) -> Vector
```

x.get_world_location_at_time(time, use_constant_velocity=False) -> Vector
Given a time from 0 to the spline duration, return the point in space where this puts you
deprecated: Please use GetLocationAtTime, specifying SplineCoordinateSpace::World

Args:
    time (float): 
    use_constant_velocity (bool): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_world_location_at_spline_point"></a>

#### get_world_location_at_spline_point

```python
def get_world_location_at_spline_point(point_index: int) -> Vector
```

x.get_world_location_at_spline_point(point_index) -> Vector
Get the world location at spline point
deprecated: Please use GetLocationAtSplinePoint, specifying SplineCoordinateSpace::World

Args:
    point_index (int32): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_world_location_at_distance_along_spline"></a>

#### get_world_location_at_distance_along_spline

```python
def get_world_location_at_distance_along_spline(distance: float) -> Vector
```

x.get_world_location_at_distance_along_spline(distance) -> Vector
Given a distance along the length of this spline, return the point in world space where this puts you
deprecated: Please use GetLocationAtDistanceAlongSpline, specifying SplineCoordinateSpace::World

Args:
    distance (float): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_world_direction_at_time"></a>

#### get_world_direction_at_time

```python
def get_world_direction_at_time(time: float,
                                use_constant_velocity: bool = False) -> Vector
```

x.get_world_direction_at_time(time, use_constant_velocity=False) -> Vector
Given a time from 0 to the spline duration, return a unit direction vector of the spline tangent there.
deprecated: Please use GetDirectionAtTime, specifying SplineCoordinateSpace::World

Args:
    time (float): 
    use_constant_velocity (bool): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_world_direction_at_distance_along_spline"></a>

#### get_world_direction_at_distance_along_spline

```python
def get_world_direction_at_distance_along_spline(distance: float) -> Vector
```

x.get_world_direction_at_distance_along_spline(distance) -> Vector
Given a distance along the length of this spline, return a unit direction vector of the spline tangent there, in world space.
deprecated: Please use GetDirectionAtDistanceAlongSpline, specifying SplineCoordinateSpace::World

Args:
    distance (float): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_vector_property_at_spline_point"></a>

#### get_vector_property_at_spline_point

```python
def get_vector_property_at_spline_point(index: int,
                                        property_name: Name) -> Vector
```

x.get_vector_property_at_spline_point(index, property_name) -> Vector
Get a metadata property vector value along the spline at spline point

Args:
    index (int32): 
    property_name (Name): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_vector_property_at_spline_input_key"></a>

#### get_vector_property_at_spline_input_key

```python
def get_vector_property_at_spline_input_key(key: float,
                                            property_name: Name) -> Vector
```

x.get_vector_property_at_spline_input_key(key, property_name) -> Vector
Get a metadata property vector value along the spline at spline input key

Args:
    key (float): 
    property_name (Name): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_up_vector_at_time"></a>

#### get_up_vector_at_time

```python
def get_up_vector_at_time(time: float,
                          coordinate_space: SplineCoordinateSpace,
                          use_constant_velocity: bool = False) -> Vector
```

x.get_up_vector_at_time(time, coordinate_space, use_constant_velocity=False) -> Vector
Given a time from 0 to the spline duration, return the spline's up vector there.

Args:
    time (float): 
    coordinate_space (SplineCoordinateSpace): 
    use_constant_velocity (bool): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_up_vector_at_spline_point"></a>

#### get_up_vector_at_spline_point

```python
def get_up_vector_at_spline_point(
        point_index: int, coordinate_space: SplineCoordinateSpace) -> Vector
```

x.get_up_vector_at_spline_point(point_index, coordinate_space) -> Vector
Get the up vector at spline point

Args:
    point_index (int32): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_up_vector_at_spline_input_key"></a>

#### get_up_vector_at_spline_input_key

```python
def get_up_vector_at_spline_input_key(
        key: float, coordinate_space: SplineCoordinateSpace) -> Vector
```

x.get_up_vector_at_spline_input_key(key, coordinate_space) -> Vector
Get up vector at the provided input key value

Args:
    key (float): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_up_vector_at_distance_along_spline"></a>

#### get_up_vector_at_distance_along_spline

```python
def get_up_vector_at_distance_along_spline(
        distance: float, coordinate_space: SplineCoordinateSpace) -> Vector
```

x.get_up_vector_at_distance_along_spline(distance, coordinate_space) -> Vector
Given a distance along the length of this spline, return a unit direction vector corresponding to the spline's up vector there.

Args:
    distance (float): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_transform_at_time"></a>

#### get_transform_at_time

```python
def get_transform_at_time(time: float,
                          coordinate_space: SplineCoordinateSpace,
                          use_constant_velocity: bool = False,
                          use_scale: bool = False) -> Transform
```

x.get_transform_at_time(time, coordinate_space, use_constant_velocity=False, use_scale=False) -> Transform
Given a time from 0 to the spline duration, return the spline's transform at the corresponding position.

Args:
    time (float): 
    coordinate_space (SplineCoordinateSpace): 
    use_constant_velocity (bool): 
    use_scale (bool): 

Returns:
    Transform:

<a id="unreal.SplineComponent.get_transform_at_spline_point"></a>

#### get_transform_at_spline_point

```python
def get_transform_at_spline_point(point_index: int,
                                  coordinate_space: SplineCoordinateSpace,
                                  use_scale: bool = False) -> Transform
```

x.get_transform_at_spline_point(point_index, coordinate_space, use_scale=False) -> Transform
Get the transform at spline point

Args:
    point_index (int32): 
    coordinate_space (SplineCoordinateSpace): 
    use_scale (bool): 

Returns:
    Transform:

<a id="unreal.SplineComponent.get_transform_at_spline_input_key"></a>

#### get_transform_at_spline_input_key

```python
def get_transform_at_spline_input_key(key: float,
                                      coordinate_space: SplineCoordinateSpace,
                                      use_scale: bool = False) -> Transform
```

x.get_transform_at_spline_input_key(key, coordinate_space, use_scale=False) -> Transform
Get transform at the provided input key value

Args:
    key (float): 
    coordinate_space (SplineCoordinateSpace): 
    use_scale (bool): 

Returns:
    Transform:

<a id="unreal.SplineComponent.get_transform_at_distance_along_spline"></a>

#### get_transform_at_distance_along_spline

```python
def get_transform_at_distance_along_spline(
        distance: float,
        coordinate_space: SplineCoordinateSpace,
        use_scale: bool = False) -> Transform
```

x.get_transform_at_distance_along_spline(distance, coordinate_space, use_scale=False) -> Transform
Given a distance along the length of this spline, return an FTransform corresponding to that point on the spline.

Args:
    distance (float): 
    coordinate_space (SplineCoordinateSpace): 
    use_scale (bool): 

Returns:
    Transform:

<a id="unreal.SplineComponent.get_time_at_distance_along_spline"></a>

#### get_time_at_distance_along_spline

```python
def get_time_at_distance_along_spline(distance: float) -> float
```

x.get_time_at_distance_along_spline(distance) -> float
Given a distance along the length of this spline, return the corresponding time at that point

Args:
    distance (float): 

Returns:
    float:

<a id="unreal.SplineComponent.get_tangent_at_time"></a>

#### get_tangent_at_time

```python
def get_tangent_at_time(time: float,
                        coordinate_space: SplineCoordinateSpace,
                        use_constant_velocity: bool = False) -> Vector
```

x.get_tangent_at_time(time, coordinate_space, use_constant_velocity=False) -> Vector
Given a time from 0 to the spline duration, return the spline's tangent there.

Args:
    time (float): 
    coordinate_space (SplineCoordinateSpace): 
    use_constant_velocity (bool): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_tangent_at_spline_point"></a>

#### get_tangent_at_spline_point

```python
def get_tangent_at_spline_point(
        point_index: int, coordinate_space: SplineCoordinateSpace) -> Vector
```

x.get_tangent_at_spline_point(point_index, coordinate_space) -> Vector
Get the tangent at spline point. This fetches the Leave tangent of the point.

Args:
    point_index (int32): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_tangent_at_spline_input_key"></a>

#### get_tangent_at_spline_input_key

```python
def get_tangent_at_spline_input_key(
        key: float, coordinate_space: SplineCoordinateSpace) -> Vector
```

x.get_tangent_at_spline_input_key(key, coordinate_space) -> Vector
Get tangent along spline at the provided input key value

Args:
    key (float): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_tangent_at_distance_along_spline"></a>

#### get_tangent_at_distance_along_spline

```python
def get_tangent_at_distance_along_spline(
        distance: float, coordinate_space: SplineCoordinateSpace) -> Vector
```

x.get_tangent_at_distance_along_spline(distance, coordinate_space) -> Vector
Given a distance along the length of this spline, return the tangent vector of the spline there.

Args:
    distance (float): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_spline_point_type"></a>

#### get_spline_point_type

```python
def get_spline_point_type(point_index: int) -> SplinePointType
```

x.get_spline_point_type(point_index) -> SplinePointType
Get the type of a spline point

Args:
    point_index (int32): 

Returns:
    SplinePointType:

<a id="unreal.SplineComponent.get_spline_point_at"></a>

#### get_spline_point_at

```python
def get_spline_point_at(
        point_index: int,
        coordinate_space: SplineCoordinateSpace) -> SplinePoint
```

x.get_spline_point_at(point_index, coordinate_space) -> SplinePoint
Gets the spline point of the spline at the specified index

Args:
    point_index (int32): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    SplinePoint:

<a id="unreal.SplineComponent.get_spline_length"></a>

#### get_spline_length

```python
def get_spline_length() -> float
```

x.get_spline_length() -> float
Returns total length along this spline

Returns:
    float:

<a id="unreal.SplineComponent.get_scale_at_time"></a>

#### get_scale_at_time

```python
def get_scale_at_time(time: float,
                      use_constant_velocity: bool = False) -> Vector
```

x.get_scale_at_time(time, use_constant_velocity=False) -> Vector
Given a time from 0 to the spline duration, return the spline's scale there.

Args:
    time (float): 
    use_constant_velocity (bool): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_scale_at_spline_point"></a>

#### get_scale_at_spline_point

```python
def get_scale_at_spline_point(point_index: int) -> Vector
```

x.get_scale_at_spline_point(point_index) -> Vector
Get the scale at spline point

Args:
    point_index (int32): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_scale_at_spline_input_key"></a>

#### get_scale_at_spline_input_key

```python
def get_scale_at_spline_input_key(key: float) -> Vector
```

x.get_scale_at_spline_input_key(key) -> Vector
Get scale at the provided input key value

Args:
    key (float): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_scale_at_distance_along_spline"></a>

#### get_scale_at_distance_along_spline

```python
def get_scale_at_distance_along_spline(distance: float) -> Vector
```

x.get_scale_at_distance_along_spline(distance) -> Vector
Given a distance along the length of this spline, return the spline's scale there.

Args:
    distance (float): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_rotation_at_time"></a>

#### get_rotation_at_time

```python
def get_rotation_at_time(time: float,
                         coordinate_space: SplineCoordinateSpace,
                         use_constant_velocity: bool = False) -> Rotator
```

x.get_rotation_at_time(time, coordinate_space, use_constant_velocity=False) -> Rotator
Given a time from 0 to the spline duration, return a rotation corresponding to the spline's position and direction there.

Args:
    time (float): 
    coordinate_space (SplineCoordinateSpace): 
    use_constant_velocity (bool): 

Returns:
    Rotator:

<a id="unreal.SplineComponent.get_rotation_at_spline_point"></a>

#### get_rotation_at_spline_point

```python
def get_rotation_at_spline_point(
        point_index: int, coordinate_space: SplineCoordinateSpace) -> Rotator
```

x.get_rotation_at_spline_point(point_index, coordinate_space) -> Rotator
Get the rotation at spline point as a rotator

Args:
    point_index (int32): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Rotator:

<a id="unreal.SplineComponent.get_rotation_at_spline_input_key"></a>

#### get_rotation_at_spline_input_key

```python
def get_rotation_at_spline_input_key(
        key: float, coordinate_space: SplineCoordinateSpace) -> Rotator
```

x.get_rotation_at_spline_input_key(key, coordinate_space) -> Rotator
Get rotator corresponding to rotation along spline at the provided input key value

Args:
    key (float): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Rotator:

<a id="unreal.SplineComponent.get_rotation_at_distance_along_spline"></a>

#### get_rotation_at_distance_along_spline

```python
def get_rotation_at_distance_along_spline(
        distance: float, coordinate_space: SplineCoordinateSpace) -> Rotator
```

x.get_rotation_at_distance_along_spline(distance, coordinate_space) -> Rotator
Given a distance along the length of this spline, return a rotation corresponding to the spline's rotation there.

Args:
    distance (float): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Rotator:

<a id="unreal.SplineComponent.get_roll_at_time"></a>

#### get_roll_at_time

```python
def get_roll_at_time(time: float,
                     coordinate_space: SplineCoordinateSpace,
                     use_constant_velocity: bool = False) -> float
```

x.get_roll_at_time(time, coordinate_space, use_constant_velocity=False) -> float
Given a time from 0 to the spline duration, return the spline's roll there, in degrees.

Args:
    time (float): 
    coordinate_space (SplineCoordinateSpace): 
    use_constant_velocity (bool): 

Returns:
    float:

<a id="unreal.SplineComponent.get_roll_at_spline_point"></a>

#### get_roll_at_spline_point

```python
def get_roll_at_spline_point(point_index: int,
                             coordinate_space: SplineCoordinateSpace) -> float
```

x.get_roll_at_spline_point(point_index, coordinate_space) -> float
Get the amount of roll at spline point, in degrees

Args:
    point_index (int32): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    float:

<a id="unreal.SplineComponent.get_roll_at_spline_input_key"></a>

#### get_roll_at_spline_input_key

```python
def get_roll_at_spline_input_key(
        key: float, coordinate_space: SplineCoordinateSpace) -> float
```

x.get_roll_at_spline_input_key(key, coordinate_space) -> float
Get roll in degrees at the provided input key value

Args:
    key (float): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    float:

<a id="unreal.SplineComponent.get_roll_at_distance_along_spline"></a>

#### get_roll_at_distance_along_spline

```python
def get_roll_at_distance_along_spline(
        distance: float, coordinate_space: SplineCoordinateSpace) -> float
```

x.get_roll_at_distance_along_spline(distance, coordinate_space) -> float
Given a distance along the length of this spline, return the spline's roll there, in degrees.

Args:
    distance (float): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    float:

<a id="unreal.SplineComponent.get_right_vector_at_time"></a>

#### get_right_vector_at_time

```python
def get_right_vector_at_time(time: float,
                             coordinate_space: SplineCoordinateSpace,
                             use_constant_velocity: bool = False) -> Vector
```

x.get_right_vector_at_time(time, coordinate_space, use_constant_velocity=False) -> Vector
Given a time from 0 to the spline duration, return the spline's right vector there.

Args:
    time (float): 
    coordinate_space (SplineCoordinateSpace): 
    use_constant_velocity (bool): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_right_vector_at_spline_point"></a>

#### get_right_vector_at_spline_point

```python
def get_right_vector_at_spline_point(
        point_index: int, coordinate_space: SplineCoordinateSpace) -> Vector
```

x.get_right_vector_at_spline_point(point_index, coordinate_space) -> Vector
Get the right vector at spline point

Args:
    point_index (int32): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_right_vector_at_spline_input_key"></a>

#### get_right_vector_at_spline_input_key

```python
def get_right_vector_at_spline_input_key(
        key: float, coordinate_space: SplineCoordinateSpace) -> Vector
```

x.get_right_vector_at_spline_input_key(key, coordinate_space) -> Vector
Get right vector at the provided input key value

Args:
    key (float): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_right_vector_at_distance_along_spline"></a>

#### get_right_vector_at_distance_along_spline

```python
def get_right_vector_at_distance_along_spline(
        distance: float, coordinate_space: SplineCoordinateSpace) -> Vector
```

x.get_right_vector_at_distance_along_spline(distance, coordinate_space) -> Vector
Given a distance along the length of this spline, return a unit direction vector corresponding to the spline's right vector there.

Args:
    distance (float): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_number_of_spline_segments"></a>

#### get_number_of_spline_segments

```python
def get_number_of_spline_segments() -> int
```

x.get_number_of_spline_segments() -> int32
Get the number of segments that make up this spline

Returns:
    int32:

<a id="unreal.SplineComponent.get_number_of_spline_points"></a>

#### get_number_of_spline_points

```python
def get_number_of_spline_points() -> int
```

x.get_number_of_spline_points() -> int32
Get the number of points that make up this spline

Returns:
    int32:

<a id="unreal.SplineComponent.get_num_spline_points"></a>

#### get_num_spline_points

```python
def get_num_spline_points() -> int
```

deprecated: 'get_num_spline_points' was renamed to 'get_number_of_spline_points'.

<a id="unreal.SplineComponent.get_location_at_time"></a>

#### get_location_at_time

```python
def get_location_at_time(time: float,
                         coordinate_space: SplineCoordinateSpace,
                         use_constant_velocity: bool = False) -> Vector
```

x.get_location_at_time(time, coordinate_space, use_constant_velocity=False) -> Vector
Given a time from 0 to the spline duration, return the point in space where this puts you

Args:
    time (float): 
    coordinate_space (SplineCoordinateSpace): 
    use_constant_velocity (bool): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_location_at_spline_point"></a>

#### get_location_at_spline_point

```python
def get_location_at_spline_point(
        point_index: int, coordinate_space: SplineCoordinateSpace) -> Vector
```

x.get_location_at_spline_point(point_index, coordinate_space) -> Vector
Get the location at spline point

Args:
    point_index (int32): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_location_at_spline_input_key"></a>

#### get_location_at_spline_input_key

```python
def get_location_at_spline_input_key(
        key: float, coordinate_space: SplineCoordinateSpace) -> Vector
```

x.get_location_at_spline_input_key(key, coordinate_space) -> Vector
Get location along spline at the provided input key value

Args:
    key (float): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_location_at_distance_along_spline"></a>

#### get_location_at_distance_along_spline

```python
def get_location_at_distance_along_spline(
        distance: float, coordinate_space: SplineCoordinateSpace) -> Vector
```

x.get_location_at_distance_along_spline(distance, coordinate_space) -> Vector
Given a distance along the length of this spline, return the point in space where this puts you

Args:
    distance (float): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_location_and_tangent_at_spline_point"></a>

#### get_location_and_tangent_at_spline_point

```python
def get_location_and_tangent_at_spline_point(
        point_index: int,
        coordinate_space: SplineCoordinateSpace) -> Tuple[Vector, Vector]
```

x.get_location_and_tangent_at_spline_point(point_index, coordinate_space) -> (location=Vector, tangent=Vector)
Get location and tangent at a spline point

Args:
    point_index (int32): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    tuple: 

    location (Vector): 

    tangent (Vector):

<a id="unreal.SplineComponent.get_local_location_and_tangent_at_spline_point"></a>

#### get_local_location_and_tangent_at_spline_point

```python
def get_local_location_and_tangent_at_spline_point(
        point_index: int) -> Tuple[Vector, Vector]
```

x.get_local_location_and_tangent_at_spline_point(point_index) -> (local_location=Vector, local_tangent=Vector)
Get local location and tangent at a spline point
deprecated: Please use GetLocationAndTangentAtSplinePoint, specifying SplineCoordinateSpace::Local

Args:
    point_index (int32): 

Returns:
    tuple: 

    local_location (Vector): 

    local_tangent (Vector):

<a id="unreal.SplineComponent.get_leave_tangent_at_spline_point"></a>

#### get_leave_tangent_at_spline_point

```python
def get_leave_tangent_at_spline_point(
        point_index: int, coordinate_space: SplineCoordinateSpace) -> Vector
```

x.get_leave_tangent_at_spline_point(point_index, coordinate_space) -> Vector
Get the leave tangent at spline point

Args:
    point_index (int32): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_input_key_value_at_spline_point"></a>

#### get_input_key_value_at_spline_point

```python
def get_input_key_value_at_spline_point(point_index: int) -> float
```

x.get_input_key_value_at_spline_point(point_index) -> float
Get the input key (e.g. the time) of the control point of the spline at the specified index.

Args:
    point_index (int32): 

Returns:
    float:

<a id="unreal.SplineComponent.get_input_key_value_at_distance_along_spline"></a>

#### get_input_key_value_at_distance_along_spline

```python
def get_input_key_value_at_distance_along_spline(distance: float) -> float
```

x.get_input_key_value_at_distance_along_spline(distance) -> float
Given a distance along the length of this spline, return the corresponding input key at that point
with a fractional component between the current input key and the next as a percentage.

Args:
    distance (float): 

Returns:
    float:

<a id="unreal.SplineComponent.get_input_key_at_distance_along_spline"></a>

#### get_input_key_at_distance_along_spline

```python
def get_input_key_at_distance_along_spline(distance: float) -> float
```

x.get_input_key_at_distance_along_spline(distance) -> float
This method has been deprecated because it was incorrectly returning the input key at time. To maintain the same behavior,
replace it with GetTimeAtDistanceAlongSpline. To actually get the input key, instead call GetInputKeyValueAtDistanceAlongSpline.
deprecated: Please use GetInputKeyValueAtDistanceAlongSpline to get input key at distance or GetTimeAtDistanceAlongSpline to get time value (normalized to duration) at distance (same logic as deprecated function).

Args:
    distance (float): 

Returns:
    float:

<a id="unreal.SplineComponent.get_float_property_at_spline_point"></a>

#### get_float_property_at_spline_point

```python
def get_float_property_at_spline_point(index: int,
                                       property_name: Name) -> float
```

x.get_float_property_at_spline_point(index, property_name) -> float
Get a metadata property float value along the spline at spline point

Args:
    index (int32): 
    property_name (Name): 

Returns:
    float:

<a id="unreal.SplineComponent.get_float_property_at_spline_input_key"></a>

#### get_float_property_at_spline_input_key

```python
def get_float_property_at_spline_input_key(key: float,
                                           property_name: Name) -> float
```

x.get_float_property_at_spline_input_key(key, property_name) -> float
Get a metadata property float value along the spline at spline input key

Args:
    key (float): 
    property_name (Name): 

Returns:
    float:

<a id="unreal.SplineComponent.get_distance_along_spline_at_spline_point"></a>

#### get_distance_along_spline_at_spline_point

```python
def get_distance_along_spline_at_spline_point(point_index: int) -> float
```

x.get_distance_along_spline_at_spline_point(point_index) -> float
Get the distance along the spline at the spline point

Args:
    point_index (int32): 

Returns:
    float:

<a id="unreal.SplineComponent.get_distance_along_spline_at_spline_input_key"></a>

#### get_distance_along_spline_at_spline_input_key

```python
def get_distance_along_spline_at_spline_input_key(key: float) -> float
```

x.get_distance_along_spline_at_spline_input_key(key) -> float
Get distance along the spline at the provided input key value

Args:
    key (float): 

Returns:
    float:

<a id="unreal.SplineComponent.get_distance_along_spline_at_location"></a>

#### get_distance_along_spline_at_location

```python
def get_distance_along_spline_at_location(
        location: Vector, coordinate_space: SplineCoordinateSpace) -> float
```

x.get_distance_along_spline_at_location(location, coordinate_space) -> float
Get distance along the spline at closest point of the provided input location

Args:
    location (Vector): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    float:

<a id="unreal.SplineComponent.get_direction_at_time"></a>

#### get_direction_at_time

```python
def get_direction_at_time(time: float,
                          coordinate_space: SplineCoordinateSpace,
                          use_constant_velocity: bool = False) -> Vector
```

x.get_direction_at_time(time, coordinate_space, use_constant_velocity=False) -> Vector
Given a time from 0 to the spline duration, return a unit direction vector of the spline tangent there.

Args:
    time (float): 
    coordinate_space (SplineCoordinateSpace): 
    use_constant_velocity (bool): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_direction_at_spline_point"></a>

#### get_direction_at_spline_point

```python
def get_direction_at_spline_point(
        point_index: int, coordinate_space: SplineCoordinateSpace) -> Vector
```

x.get_direction_at_spline_point(point_index, coordinate_space) -> Vector
Get the direction at spline point

Args:
    point_index (int32): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_direction_at_spline_input_key"></a>

#### get_direction_at_spline_input_key

```python
def get_direction_at_spline_input_key(
        key: float, coordinate_space: SplineCoordinateSpace) -> Vector
```

x.get_direction_at_spline_input_key(key, coordinate_space) -> Vector
Get unit direction along spline at the provided input key value

Args:
    key (float): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_direction_at_distance_along_spline"></a>

#### get_direction_at_distance_along_spline

```python
def get_direction_at_distance_along_spline(
        distance: float, coordinate_space: SplineCoordinateSpace) -> Vector
```

x.get_direction_at_distance_along_spline(distance, coordinate_space) -> Vector
Given a distance along the length of this spline, return a unit direction vector of the spline tangent there.

Args:
    distance (float): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_default_up_vector"></a>

#### get_default_up_vector

```python
def get_default_up_vector(coordinate_space: SplineCoordinateSpace) -> Vector
```

x.get_default_up_vector(coordinate_space) -> Vector
Gets the default up vector used by this spline

Args:
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Vector:

<a id="unreal.SplineComponent.get_arrive_tangent_at_spline_point"></a>

#### get_arrive_tangent_at_spline_point

```python
def get_arrive_tangent_at_spline_point(
        point_index: int, coordinate_space: SplineCoordinateSpace) -> Vector
```

x.get_arrive_tangent_at_spline_point(point_index, coordinate_space) -> Vector
Get the arrive tangent at spline point

Args:
    point_index (int32): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Vector:

<a id="unreal.SplineComponent.find_up_vector_closest_to_world_location"></a>

#### find_up_vector_closest_to_world_location

```python
def find_up_vector_closest_to_world_location(
        world_location: Vector,
        coordinate_space: SplineCoordinateSpace) -> Vector
```

x.find_up_vector_closest_to_world_location(world_location, coordinate_space) -> Vector
Given a location, in world space, return a unit direction vector corresponding to the spline's up vector closest to the location.

Args:
    world_location (Vector): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Vector:

<a id="unreal.SplineComponent.find_transform_closest_to_world_location"></a>

#### find_transform_closest_to_world_location

```python
def find_transform_closest_to_world_location(
        world_location: Vector,
        coordinate_space: SplineCoordinateSpace,
        use_scale: bool = False) -> Transform
```

x.find_transform_closest_to_world_location(world_location, coordinate_space, use_scale=False) -> Transform
Given a location, in world space, return an FTransform closest to that location.

Args:
    world_location (Vector): 
    coordinate_space (SplineCoordinateSpace): 
    use_scale (bool): 

Returns:
    Transform:

<a id="unreal.SplineComponent.find_tangent_closest_to_world_location"></a>

#### find_tangent_closest_to_world_location

```python
def find_tangent_closest_to_world_location(
        world_location: Vector,
        coordinate_space: SplineCoordinateSpace) -> Vector
```

x.find_tangent_closest_to_world_location(world_location, coordinate_space) -> Vector
Given a location, in world space, return the tangent vector of the spline closest to the location.

Args:
    world_location (Vector): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Vector:

<a id="unreal.SplineComponent.find_scale_closest_to_world_location"></a>

#### find_scale_closest_to_world_location

```python
def find_scale_closest_to_world_location(world_location: Vector) -> Vector
```

x.find_scale_closest_to_world_location(world_location) -> Vector
Given a location, in world space, return the spline's scale closest to the location.

Args:
    world_location (Vector): 

Returns:
    Vector:

<a id="unreal.SplineComponent.find_rotation_closest_to_world_location"></a>

#### find_rotation_closest_to_world_location

```python
def find_rotation_closest_to_world_location(
        world_location: Vector,
        coordinate_space: SplineCoordinateSpace) -> Rotator
```

x.find_rotation_closest_to_world_location(world_location, coordinate_space) -> Rotator
Given a location, in world space, return rotation corresponding to the spline's rotation closest to the location.

Args:
    world_location (Vector): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Rotator:

<a id="unreal.SplineComponent.find_roll_closest_to_world_location"></a>

#### find_roll_closest_to_world_location

```python
def find_roll_closest_to_world_location(
        world_location: Vector,
        coordinate_space: SplineCoordinateSpace) -> float
```

x.find_roll_closest_to_world_location(world_location, coordinate_space) -> float
Given a location, in world space, return the spline's roll closest to the location, in degrees.

Args:
    world_location (Vector): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    float:

<a id="unreal.SplineComponent.find_right_vector_closest_to_world_location"></a>

#### find_right_vector_closest_to_world_location

```python
def find_right_vector_closest_to_world_location(
        world_location: Vector,
        coordinate_space: SplineCoordinateSpace) -> Vector
```

x.find_right_vector_closest_to_world_location(world_location, coordinate_space) -> Vector
Given a location, in world space, return a unit direction vector corresponding to the spline's right vector closest to the location.

Args:
    world_location (Vector): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Vector:

<a id="unreal.SplineComponent.find_location_closest_to_world_location"></a>

#### find_location_closest_to_world_location

```python
def find_location_closest_to_world_location(
        world_location: Vector,
        coordinate_space: SplineCoordinateSpace) -> Vector
```

x.find_location_closest_to_world_location(world_location, coordinate_space) -> Vector
Given a location, in world space, return the point on the curve that is closest to the location.

Args:
    world_location (Vector): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Vector:

<a id="unreal.SplineComponent.find_input_key_closest_to_world_location"></a>

#### find_input_key_closest_to_world_location

```python
def find_input_key_closest_to_world_location(world_location: Vector) -> float
```

x.find_input_key_closest_to_world_location(world_location) -> float
Given a location, in world space, return the input key closest to that location.

Args:
    world_location (Vector): 

Returns:
    float:

<a id="unreal.SplineComponent.find_direction_closest_to_world_location"></a>

#### find_direction_closest_to_world_location

```python
def find_direction_closest_to_world_location(
        world_location: Vector,
        coordinate_space: SplineCoordinateSpace) -> Vector
```

x.find_direction_closest_to_world_location(world_location, coordinate_space) -> Vector
Given a location, in world space, return a unit direction vector of the spline tangent closest to the location.

Args:
    world_location (Vector): 
    coordinate_space (SplineCoordinateSpace): 

Returns:
    Vector:

<a id="unreal.SplineComponent.divide_spline_into_polyline_recursive_with_distances"></a>

#### divide_spline_into_polyline_recursive_with_distances

```python
def divide_spline_into_polyline_recursive_with_distances(
    start_distance_along_spline: float, end_distance_along_spline: float,
    coordinate_space: SplineCoordinateSpace,
    max_square_distance_from_spline: float
) -> Optional[Tuple[Array[Vector], Array[float]]]
```

x.divide_spline_into_polyline_recursive_with_distances(start_distance_along_spline, end_distance_along_spline, coordinate_space, max_square_distance_from_spline) -> (out_points=Array[Vector], out_distances_along_spline=Array[double]) or None
Given a threshold, recursively sub-divides the spline section until the list of segments (polyline) matches the spline shape. Note: Prefer ConvertSplineToPolyline_InDistanceRange

Args:
    start_distance_along_spline (float): 
    end_distance_along_spline (float): 
    coordinate_space (SplineCoordinateSpace): 
    max_square_distance_from_spline (float): 

Returns:
    tuple or None: 

    out_points (Array[Vector]): 

    out_distances_along_spline (Array[double]):

<a id="unreal.SplineComponent.divide_spline_into_polyline_recursive"></a>

#### divide_spline_into_polyline_recursive

```python
def divide_spline_into_polyline_recursive(
        start_distance_along_spline: float, end_distance_along_spline: float,
        coordinate_space: SplineCoordinateSpace,
        max_square_distance_from_spline: float) -> Optional[Array[Vector]]
```

x.divide_spline_into_polyline_recursive(start_distance_along_spline, end_distance_along_spline, coordinate_space, max_square_distance_from_spline) -> Array[Vector] or None
Given a threshold, recursively sub-divides the spline section until the list of segments (polyline) matches the spline shape. Note: Prefer ConvertSplineToPolyline_InDistanceRange

Args:
    start_distance_along_spline (float): 
    end_distance_along_spline (float): 
    coordinate_space (SplineCoordinateSpace): 
    max_square_distance_from_spline (float): 

Returns:
    Array[Vector] or None: 

    out_points (Array[Vector]):

<a id="unreal.SplineComponent.convert_spline_to_poly_line_with_distances"></a>

#### convert_spline_to_poly_line_with_distances

```python
def convert_spline_to_poly_line_with_distances(
    coordinate_space: SplineCoordinateSpace,
    max_square_distance_from_spline: float
) -> Optional[Tuple[Array[Vector], Array[float]]]
```

x.convert_spline_to_poly_line_with_distances(coordinate_space, max_square_distance_from_spline) -> (out_points=Array[Vector], out_distances_along_spline=Array[double]) or None
Given a threshold, returns a list of vertices along the spline that, treated as a list of segments (polyline), matches the spline shape. Also fills a list of corresponding distances along the spline for each point.

Args:
    coordinate_space (SplineCoordinateSpace): 
    max_square_distance_from_spline (float): 

Returns:
    tuple or None: 

    out_points (Array[Vector]): 

    out_distances_along_spline (Array[double]):

<a id="unreal.SplineComponent.convert_spline_to_polyline_in_time_range"></a>

#### convert_spline_to_polyline_in_time_range

```python
def convert_spline_to_polyline_in_time_range(
    coordinate_space: SplineCoordinateSpace,
    max_square_distance_from_spline: float,
    start_time_along_spline: float,
    end_time_along_spline: float,
    use_constant_velocity: bool,
    allow_wrapping_if_closed: bool = True
) -> Optional[Tuple[Array[Vector], Array[float]]]
```

x.convert_spline_to_polyline_in_time_range(coordinate_space, max_square_distance_from_spline, start_time_along_spline, end_time_along_spline, use_constant_velocity, allow_wrapping_if_closed=True) -> (out_points=Array[Vector], out_distances_along_spline=Array[double]) or None
Given a threshold and start and end time range, returns a list of vertices along the spline that, treated as a list of segments (polyline), matches the spline shape in that range. Also fills a list of corresponding distances along the spline for each point.

Args:
    coordinate_space (SplineCoordinateSpace): 
    max_square_distance_from_spline (float): 
    start_time_along_spline (float): 
    end_time_along_spline (float): 
    use_constant_velocity (bool): 
    allow_wrapping_if_closed (bool): 

Returns:
    tuple or None: 

    out_points (Array[Vector]): 

    out_distances_along_spline (Array[double]):

<a id="unreal.SplineComponent.convert_spline_to_polyline_in_distance_range"></a>

#### convert_spline_to_polyline_in_distance_range

```python
def convert_spline_to_polyline_in_distance_range(
    coordinate_space: SplineCoordinateSpace,
    max_square_distance_from_spline: float,
    start_dist_along_spline: float,
    end_dist_along_spline: float,
    allow_wrapping_if_closed: bool = True
) -> Optional[Tuple[Array[Vector], Array[float]]]
```

x.convert_spline_to_polyline_in_distance_range(coordinate_space, max_square_distance_from_spline, start_dist_along_spline, end_dist_along_spline, allow_wrapping_if_closed=True) -> (out_points=Array[Vector], out_distances_along_spline=Array[double]) or None
Given a threshold and a start and end distance range, returns a list of vertices along the spline that, treated as a list of segments (polyline), matches the spline shape in that range. Also fills a list of corresponding distances along the spline for each point.

Args:
    coordinate_space (SplineCoordinateSpace): 
    max_square_distance_from_spline (float): 
    start_dist_along_spline (float): 
    end_dist_along_spline (float): 
    allow_wrapping_if_closed (bool): 

Returns:
    tuple or None: 

    out_points (Array[Vector]): 

    out_distances_along_spline (Array[double]):

<a id="unreal.SplineComponent.convert_spline_to_poly_line"></a>

#### convert_spline_to_poly_line

```python
def convert_spline_to_poly_line(
        coordinate_space: SplineCoordinateSpace,
        max_square_distance_from_spline: float) -> Optional[Array[Vector]]
```

x.convert_spline_to_poly_line(coordinate_space, max_square_distance_from_spline) -> Array[Vector] or None
Given a threshold, returns a list of vertices along the spline that, treated as a list of segments (polyline), matches the spline shape.

Args:
    coordinate_space (SplineCoordinateSpace): 
    max_square_distance_from_spline (float): 

Returns:
    Array[Vector] or None: 

    out_points (Array[Vector]):

<a id="unreal.SplineComponent.convert_spline_segment_to_poly_line"></a>

#### convert_spline_segment_to_poly_line

```python
def convert_spline_segment_to_poly_line(
        spline_point_start_index: int, coordinate_space: SplineCoordinateSpace,
        max_square_distance_from_spline: float) -> Optional[Array[Vector]]
```

x.convert_spline_segment_to_poly_line(spline_point_start_index, coordinate_space, max_square_distance_from_spline) -> Array[Vector] or None
Given a threshold, returns a list of vertices along the spline segment that, treated as a list of segments (polyline), matches the spline shape.

Args:
    spline_point_start_index (int32): 
    coordinate_space (SplineCoordinateSpace): 
    max_square_distance_from_spline (float): 

Returns:
    Array[Vector] or None: 

    out_points (Array[Vector]):

<a id="unreal.SplineComponent.clear_spline_points"></a>

#### clear_spline_points

```python
def clear_spline_points(update_spline: bool = True) -> None
```

x.clear_spline_points(update_spline=True) -> None
Clears all the points in the spline

Args:
    update_spline (bool):

<a id="unreal.SplineComponent.add_spline_world_point"></a>

#### add_spline_world_point

```python
def add_spline_world_point(position: Vector) -> None
```

x.add_spline_world_point(position) -> None
Adds a world space point to the spline
deprecated: Please use AddSplinePoint, specifying SplineCoordinateSpace::World

Args:
    position (Vector):

<a id="unreal.SplineComponent.add_spline_point_at_index"></a>

#### add_spline_point_at_index

```python
def add_spline_point_at_index(position: Vector,
                              index: int,
                              coordinate_space: SplineCoordinateSpace,
                              update_spline: bool = True) -> None
```

x.add_spline_point_at_index(position, index, coordinate_space, update_spline=True) -> None
Adds a point to the spline at the specified index

Args:
    position (Vector): 
    index (int32): 
    coordinate_space (SplineCoordinateSpace): 
    update_spline (bool):

<a id="unreal.SplineComponent.add_spline_point"></a>

#### add_spline_point

```python
def add_spline_point(position: Vector,
                     coordinate_space: SplineCoordinateSpace,
                     update_spline: bool = True) -> None
```

x.add_spline_point(position, coordinate_space, update_spline=True) -> None
Adds a point to the spline

Args:
    position (Vector): 
    coordinate_space (SplineCoordinateSpace): 
    update_spline (bool):

<a id="unreal.SplineComponent.add_spline_local_point"></a>

#### add_spline_local_point

```python
def add_spline_local_point(position: Vector) -> None
```

x.add_spline_local_point(position) -> None
Adds a local space point to the spline
deprecated: Please use AddSplinePoint, specifying SplineCoordinateSpace::Local

Args:
    position (Vector):

<a id="unreal.SplineComponent.add_points"></a>

#### add_points

```python
def add_points(points: Array[SplinePoint], update_spline: bool = True) -> None
```

x.add_points(points, update_spline=True) -> None
Adds an array of FSplinePoints to the spline.

Args:
    points (Array[SplinePoint]): 
    update_spline (bool):

<a id="unreal.SplineComponent.add_point"></a>

#### add_point

```python
def add_point(point: SplinePoint, update_spline: bool = True) -> None
```

x.add_point(point, update_spline=True) -> None
Adds an FSplinePoint to the spline. This contains its input key, position, tangent, rotation and scale.

Args:
    point (SplinePoint): 
    update_spline (bool):

<a id="unreal.SplineMeshComponent"></a>