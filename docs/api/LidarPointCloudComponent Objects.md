## LidarPointCloudComponent Objects

```python
class LidarPointCloudComponent(MeshComponent)
```

Component that allows you to render specified point cloud section

**C++ Source:**

- **Plugin**: LidarPointCloud
- **Module**: LidarPointCloudRuntime
- **File**: LidarPointCloudComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``affect_distance_field_lighting`` (bool):  [Read-Write] Controls whether the primitive should affect dynamic distance field lighting methods.  This flag is only used if CastShadow is true. *
- ``affect_dynamic_indirect_lighting`` (bool):  [Read-Write] Controls whether the primitive should influence indirect lighting.
- ``affect_indirect_lighting_while_hidden`` (bool):  [Read-Write] Controls whether the primitive should affect indirect lighting when hidden. This flag is only used if bAffectDynamicIndirectLighting is true.
- ``allow_cull_distance_volume`` (bool):  [Read-Write] Whether to accept cull distance volumes to modify cached cull distance.
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
- ``classification_colors`` (Map[int32, LinearColor]):  [Read-Write] Used with the Classification source.
  Maps the given classification ID to a color.
- ``color_source`` (LidarPointCloudColorationMode):  [Read-Write] Specifies which source to use for point colors.
- ``color_tint`` (LinearColor):  [Read-Write] Specifies the tint to apply to the points.
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``consider_for_actor_placement_when_hidden`` (bool):  [Read-Write] If true, this component will be considered for placement when dragging and placing items in the editor even if it is not visible, such as in the case of hidden collision meshes
- ``contrast`` (Vector4):  [Read-Write]
- ``custom_depth_stencil_value`` (int32):  [Read-Write] Optionally write this 0-255 value to the stencil buffer in CustomDepth pass (Requires project setting or r.CustomDepth == 3)
- ``custom_depth_stencil_write_mask`` (RendererStencilMask):  [Read-Write] Mask used for stencil buffer writes.
- ``custom_material`` (MaterialInterface):  [Read-Write] Allows using custom-built material for the point cloud.
  Set to None to use the default one instead.
- ``custom_primitive_data`` (CustomPrimitiveData):  [Read-Write] Optional user defined default values for the custom primitive data of this primitive
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``draw_node_bounds`` (bool):  [Read-Write] Enabling this will cause the visible nodes to render their bounds.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``elevation_color_bottom`` (LinearColor):  [Read-Write] Specifies the bottom color of the elevation-based gradient.
- ``elevation_color_top`` (LinearColor):  [Read-Write] Specifies the top color of the elevation-based gradient.
- ``emissive_light_source`` (bool):  [Read-Write] Whether the primitive will be used as an emissive light source.
- ``enable_auto_lod_generation`` (bool):  [Read-Write] Whether to include this component in HLODs or not.
- ``enable_material_parameter_caching`` (bool):  [Read-Write]
- ``exclude_for_specific_hlod_levels`` (Array[int32]):  [Read-Write]
  deprecated: WARNING: This property has been deprecated, use the SetExcludedFromHLODLevel/IsExcludedFromHLODLevel functions instead
- ``exclude_from_hlod_levels`` (uint8):  [Read-Write] Which specific HLOD levels this component should be excluded from
- ``exclude_from_light_attachment_group`` (bool):  [Read-Write] If set, then it overrides any bLightAttachmentsAsGroup set in a parent.
- ``fill_collision_underneath_for_navmesh`` (bool):  [Read-Write] If set, navmesh will not be generated under the surface of the geometry
- ``first_person_primitive_type`` (FirstPersonPrimitiveType):  [Read-Write] If this is set to FirstPerson, the camera FirstPersonFieldOfView and FirstPersonScale parameters will be used on this component. These parameters can be used to render the component with a different field of view and a smaller depth range such that clipping with the scene can be avoided. This is useful for rendering first person view geometry.
- ``force_mip_streaming`` (bool):  [Read-Write] If true, forces mips for textures used by this component to be resident when this component's level is loaded.
- ``gain`` (Vector4):  [Read-Write] Affects the emissive strength of the color. Useful to create Bloom and light bleed effects.
- ``gamma`` (Vector4):  [Read-Write]
- ``gap_filling_strength`` (float):  [Read-Write] If set to > 0, it attempts to close gaps between points.
  Setting this too high may cause visual artifacts.
  This setting may interfere with AO
- ``generate_overlap_events`` (bool):  [Read-Write]
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``hidden_in_scene_capture`` (bool):  [Read-Write] When true, will not be captured by Scene Capture
- ``hlod_batching_policy`` (HLODBatchingPolicy):  [Read-Write] Determines how the geometry of a component will be incorporated in proxy (simplified) HLODs.
- ``holdout`` (bool):  [Read-Write] If this is True, this primitive will render black with an alpha of 0, but all secondary effects (shadows, reflections, indirect lighting) remain. This feature requires activating the project setting(s) "Alpha Output", and "Support Primitive Alpha Holdout" if using the deferred renderer.
- ``ignore_radial_force`` (bool):  [Read-Write] Will ignore radial forces applied to this component.
- ``ignore_radial_impulse`` (bool):  [Read-Write] Will ignore radial impulses applied to this component.
- ``indirect_lighting_cache_quality`` (IndirectLightingCacheQuality):  [Read-Write] Quality of indirect lighting for Movable primitives.  This has a large effect on Indirect Lighting Cache update time.
- ``intensity_influence`` (float):  [Read-Write] Specifies the influence of Intensity data, if available, on the overall color.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``ld_max_draw_distance`` (float):  [Read-Write] Max draw distance exposed to LDs. The real max draw distance is the min (disregarding 0) of this and volumes affecting this object.
- ``light_attachments_as_group`` (bool):  [Read-Write] Whether to light this component and any attachments as a group.  This only has effect on the root component of an attachment tree.
  When enabled, attached component shadowing settings like bCastInsetShadow, bCastVolumetricTranslucentShadow, etc, will be ignored.
  This is useful for improving performance when multiple movable components are attached together.
- ``lighting_channels`` (LightingChannels):  [Read-Write] Channels that this component should be in.  Lights with matching channels will affect the component.
  These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing.
  Lighting channels are only supported on translucent materials using forward shading (i.e. when not using the translucency lighting volume).
- ``lightmap_type`` (LightmapType):  [Read-Write]
- ``max_depth`` (int32):  [Read-Write] Maximum Depth to which the nodes should be rendered.
  -1 to disable.
- ``min_depth`` (int32):  [Read-Write] Minimum Depth from which the nodes should be rendered.
  0 to disable.
- ``min_draw_distance`` (float):  [Read-Write] The minimum distance at which the primitive should be rendered,
  measured in world space units from the center of the primitive's bounding sphere to the camera position.
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``multi_body_overlap`` (bool):  [Read-Write] If true, this component will generate individual overlaps for each overlapping physics body if it is a multi-body component. When false, this component will
  generate only one overlap, regardless of how many physics bodies it has and how many of them are overlapping another component/body. This flag has no
  influence on single body components.
- ``never_distance_cull`` (bool):  [Read-Write] When enabled this object will not be culled by distance. This is ignored if a child of a HLOD.
- ``offset`` (Vector4):  [Read-Write] Applied additively, 0 being neutral.
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
- ``overlay_material`` (MaterialInterface):  [Read-Write] Translucent material to blend on top of this mesh. Mesh will be rendered twice - once with a base material and once with overlay material
- ``overlay_material_max_draw_distance`` (float):  [Read-Write] The max draw distance for overlay material. A distance of 0 indicates that overlay will be culled using primitive max distance.
- ``override_materials`` (Array[MaterialInterface]):  [Read-Write] Material overrides.
- ``owner_no_see`` (bool):  [Read-Write] If this is True, this component won't be visible when the view actor is the component's owner, directly or indirectly.
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``point_cloud`` (LidarPointCloud):  [Read-Write]
- ``point_orientation`` (LidarPointCloudSpriteOrientation):  [Read-Write] Affects the orientation of points.
- ``point_shape`` (LidarPointCloudSpriteShape):  [Read-Write] Affects the shape of points.
  deprecated: Use GetPointShape() / SetPointShape() instead.
- ``point_size`` (float):  [Read-Write] Use to tweak the size of the points.
  Set to 0 to switch to 1 pixel points.
- ``point_size_bias`` (float):  [Read-Write] Larger values will help mask LOD transition areas, but too large values will lead to loss of detail.
  Values in range 0.035 - 0.05 seem to produce best overall results.
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
- ``replicate_physics_to_autonomous_proxy`` (bool):  [Read-Write] True if physics should be replicated to autonomous proxies. This should be true for
                server-authoritative simulations, and false for client authoritative simulations.
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``return_material_on_move`` (bool):  [Read-Write] If true, component sweeps will return the material in their hit result.
  see: MoveComponent(), FHitResult
- ``runtime_virtual_textures`` (Array[RuntimeVirtualTexture]):  [Read-Write] Array of runtime virtual textures into which we draw the mesh for this actor.
  The material also needs to be set up to output to a virtual texture.
- ``saturation`` (Vector4):  [Read-Write]
- ``scaling_method`` (LidarPointCloudScalingMethod):  [Read-Write] Determines how the points will be scaled
- ``self_shadow_only`` (bool):  [Read-Write] When enabled, the component will only cast a shadow on itself and not other components in the world.
  This is especially useful for first person weapons, and forces bCastInsetShadow to be enabled.
- ``shadow_cache_invalidation_behavior`` (ShadowCacheInvalidationBehavior):  [Read-Write] Control shadow invalidation behavior, in particular with respect to Virtual Shadow Maps and material effects like World Position Offset.
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``single_sample_shadow_from_stationary_lights`` (bool):  [Read-Write] Whether the whole component should be shadowed as one from stationary lights, which makes shadow receiving much cheaper.
  When enabled shadowing data comes from the volume lighting samples precomputed by Lightmass, which are very sparse.
  This is currently only used on stationary directional lights.
- ``static_when_not_moveable`` (bool):  [Read-Write] When false, the underlying physics body will contain all sim data (mass, inertia tensor, etc) even if mobility is not set to Moveable
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
- ``use_frustum_culling`` (bool):  [Read-Write] If enabled, points outside of the visible frustum will not be rendered.
  While most project should leave this enabled, disabling it may help
  with the data streaming lag when shooting cinematics.
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

<a id="unreal.LidarPointCloudComponent.point_cloud"></a>

#### point_cloud

```python
@property
def point_cloud() -> LidarPointCloud
```

(LidarPointCloud):  [Read-Only]

<a id="unreal.LidarPointCloudComponent.custom_material"></a>

#### custom_material

```python
@property
def custom_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Only] Allows using custom-built material for the point cloud.
Set to None to use the default one instead.

<a id="unreal.LidarPointCloudComponent.point_size"></a>

#### point_size

```python
@property
def point_size() -> float
```

(float):  [Read-Write] Use to tweak the size of the points.
Set to 0 to switch to 1 pixel points.

<a id="unreal.LidarPointCloudComponent.point_size"></a>

#### point_size

```python
@point_size.setter
def point_size(value: float) -> None
```

<a id="unreal.LidarPointCloudComponent.scaling_method"></a>

#### scaling_method

```python
@property
def scaling_method() -> LidarPointCloudScalingMethod
```

(LidarPointCloudScalingMethod):  [Read-Write] Determines how the points will be scaled

<a id="unreal.LidarPointCloudComponent.scaling_method"></a>

#### scaling_method

```python
@scaling_method.setter
def scaling_method(value: LidarPointCloudScalingMethod) -> None
```

<a id="unreal.LidarPointCloudComponent.gap_filling_strength"></a>

#### gap_filling_strength

```python
@property
def gap_filling_strength() -> float
```

(float):  [Read-Write] If set to > 0, it attempts to close gaps between points.
Setting this too high may cause visual artifacts.
This setting may interfere with AO

<a id="unreal.LidarPointCloudComponent.gap_filling_strength"></a>

#### gap_filling_strength

```python
@gap_filling_strength.setter
def gap_filling_strength(value: float) -> None
```

<a id="unreal.LidarPointCloudComponent.color_source"></a>

#### color_source

```python
@property
def color_source() -> LidarPointCloudColorationMode
```

(LidarPointCloudColorationMode):  [Read-Write] Specifies which source to use for point colors.

<a id="unreal.LidarPointCloudComponent.color_source"></a>

#### color_source

```python
@color_source.setter
def color_source(value: LidarPointCloudColorationMode) -> None
```

<a id="unreal.LidarPointCloudComponent.point_shape"></a>

#### point_shape

```python
@property
def point_shape() -> LidarPointCloudSpriteShape
```

(LidarPointCloudSpriteShape):  [Read-Write] Affects the shape of points.
deprecated: Use GetPointShape() / SetPointShape() instead.

<a id="unreal.LidarPointCloudComponent.point_shape"></a>

#### point_shape

```python
@point_shape.setter
def point_shape(value: LidarPointCloudSpriteShape) -> None
```

<a id="unreal.LidarPointCloudComponent.point_orientation"></a>

#### point_orientation

```python
@property
def point_orientation() -> LidarPointCloudSpriteOrientation
```

(LidarPointCloudSpriteOrientation):  [Read-Write] Affects the orientation of points.

<a id="unreal.LidarPointCloudComponent.point_orientation"></a>

#### point_orientation

```python
@point_orientation.setter
def point_orientation(value: LidarPointCloudSpriteOrientation) -> None
```

<a id="unreal.LidarPointCloudComponent.classification_colors"></a>

#### classification_colors

```python
@property
def classification_colors() -> Map[int, LinearColor]
```

(Map[int32, LinearColor]):  [Read-Write] Used with the Classification source.
Maps the given classification ID to a color.

<a id="unreal.LidarPointCloudComponent.classification_colors"></a>

#### classification_colors

```python
@classification_colors.setter
def classification_colors(value: Map[int, LinearColor]) -> None
```

<a id="unreal.LidarPointCloudComponent.elevation_color_bottom"></a>

#### elevation_color_bottom

```python
@property
def elevation_color_bottom() -> LinearColor
```

(LinearColor):  [Read-Write] Specifies the bottom color of the elevation-based gradient.

<a id="unreal.LidarPointCloudComponent.elevation_color_bottom"></a>

#### elevation_color_bottom

```python
@elevation_color_bottom.setter
def elevation_color_bottom(value: LinearColor) -> None
```

<a id="unreal.LidarPointCloudComponent.elevation_color_top"></a>

#### elevation_color_top

```python
@property
def elevation_color_top() -> LinearColor
```

(LinearColor):  [Read-Write] Specifies the top color of the elevation-based gradient.

<a id="unreal.LidarPointCloudComponent.elevation_color_top"></a>

#### elevation_color_top

```python
@elevation_color_top.setter
def elevation_color_top(value: LinearColor) -> None
```

<a id="unreal.LidarPointCloudComponent.point_size_bias"></a>

#### point_size_bias

```python
@property
def point_size_bias() -> float
```

(float):  [Read-Write] Larger values will help mask LOD transition areas, but too large values will lead to loss of detail.
Values in range 0.035 - 0.05 seem to produce best overall results.

<a id="unreal.LidarPointCloudComponent.point_size_bias"></a>

#### point_size_bias

```python
@point_size_bias.setter
def point_size_bias(value: float) -> None
```

<a id="unreal.LidarPointCloudComponent.saturation"></a>

#### saturation

```python
@property
def saturation() -> Vector4
```

(Vector4):  [Read-Write]

<a id="unreal.LidarPointCloudComponent.saturation"></a>

#### saturation

```python
@saturation.setter
def saturation(value: Vector4) -> None
```

<a id="unreal.LidarPointCloudComponent.contrast"></a>

#### contrast

```python
@property
def contrast() -> Vector4
```

(Vector4):  [Read-Write]

<a id="unreal.LidarPointCloudComponent.contrast"></a>

#### contrast

```python
@contrast.setter
def contrast(value: Vector4) -> None
```

<a id="unreal.LidarPointCloudComponent.gamma"></a>

#### gamma

```python
@property
def gamma() -> Vector4
```

(Vector4):  [Read-Write]

<a id="unreal.LidarPointCloudComponent.gamma"></a>

#### gamma

```python
@gamma.setter
def gamma(value: Vector4) -> None
```

<a id="unreal.LidarPointCloudComponent.gain"></a>

#### gain

```python
@property
def gain() -> Vector4
```

(Vector4):  [Read-Write] Affects the emissive strength of the color. Useful to create Bloom and light bleed effects.

<a id="unreal.LidarPointCloudComponent.gain"></a>

#### gain

```python
@gain.setter
def gain(value: Vector4) -> None
```

<a id="unreal.LidarPointCloudComponent.offset"></a>

#### offset

```python
@property
def offset() -> Vector4
```

(Vector4):  [Read-Write] Applied additively, 0 being neutral.

<a id="unreal.LidarPointCloudComponent.offset"></a>

#### offset

```python
@offset.setter
def offset(value: Vector4) -> None
```

<a id="unreal.LidarPointCloudComponent.color_tint"></a>

#### color_tint

```python
@property
def color_tint() -> LinearColor
```

(LinearColor):  [Read-Write] Specifies the tint to apply to the points.

<a id="unreal.LidarPointCloudComponent.color_tint"></a>

#### color_tint

```python
@color_tint.setter
def color_tint(value: LinearColor) -> None
```

<a id="unreal.LidarPointCloudComponent.intensity_influence"></a>

#### intensity_influence

```python
@property
def intensity_influence() -> float
```

(float):  [Read-Write] Specifies the influence of Intensity data, if available, on the overall color.

<a id="unreal.LidarPointCloudComponent.intensity_influence"></a>

#### intensity_influence

```python
@intensity_influence.setter
def intensity_influence(value: float) -> None
```

<a id="unreal.LidarPointCloudComponent.use_frustum_culling"></a>

#### use_frustum_culling

```python
@property
def use_frustum_culling() -> bool
```

(bool):  [Read-Write] If enabled, points outside of the visible frustum will not be rendered.
While most project should leave this enabled, disabling it may help
with the data streaming lag when shooting cinematics.

<a id="unreal.LidarPointCloudComponent.use_frustum_culling"></a>

#### use_frustum_culling

```python
@use_frustum_culling.setter
def use_frustum_culling(value: bool) -> None
```

<a id="unreal.LidarPointCloudComponent.min_depth"></a>

#### min_depth

```python
@property
def min_depth() -> int
```

(int32):  [Read-Write] Minimum Depth from which the nodes should be rendered.
0 to disable.

<a id="unreal.LidarPointCloudComponent.min_depth"></a>

#### min_depth

```python
@min_depth.setter
def min_depth(value: int) -> None
```

<a id="unreal.LidarPointCloudComponent.max_depth"></a>

#### max_depth

```python
@property
def max_depth() -> int
```

(int32):  [Read-Write] Maximum Depth to which the nodes should be rendered.
-1 to disable.

<a id="unreal.LidarPointCloudComponent.max_depth"></a>

#### max_depth

```python
@max_depth.setter
def max_depth(value: int) -> None
```

<a id="unreal.LidarPointCloudComponent.draw_node_bounds"></a>

#### draw_node_bounds

```python
@property
def draw_node_bounds() -> bool
```

(bool):  [Read-Write] Enabling this will cause the visible nodes to render their bounds.

<a id="unreal.LidarPointCloudComponent.draw_node_bounds"></a>

#### draw_node_bounds

```python
@draw_node_bounds.setter
def draw_node_bounds(value: bool) -> None
```

<a id="unreal.LidarPointCloudComponent.set_visibility_of_points_in_sphere"></a>

#### set_visibility_of_points_in_sphere

```python
def set_visibility_of_points_in_sphere(new_visibility: bool, center: Vector,
                                       radius: float) -> None
```

x.set_visibility_of_points_in_sphere(new_visibility, center, radius) -> None
Sets visibility of points within the given sphere.

Args:
    new_visibility (bool): 
    center (Vector): 
    radius (float):

<a id="unreal.LidarPointCloudComponent.set_visibility_of_points_in_box"></a>

#### set_visibility_of_points_in_box

```python
def set_visibility_of_points_in_box(new_visibility: bool, center: Vector,
                                    extent: Vector) -> None
```

x.set_visibility_of_points_in_box(new_visibility, center, extent) -> None
Sets visibility of points within the given box.

Args:
    new_visibility (bool): 
    center (Vector): 
    extent (Vector):

<a id="unreal.LidarPointCloudComponent.set_visibility_of_points_by_ray"></a>

#### set_visibility_of_points_by_ray

```python
def set_visibility_of_points_by_ray(new_visibility: bool, origin: Vector,
                                    direction: Vector, radius: float) -> None
```

x.set_visibility_of_points_by_ray(new_visibility, origin, direction, radius) -> None
Sets visibility of points hit by the given ray.

Args:
    new_visibility (bool): 
    origin (Vector): 
    direction (Vector): 
    radius (float):

<a id="unreal.LidarPointCloudComponent.set_visibility_of_first_point_by_ray"></a>

#### set_visibility_of_first_point_by_ray

```python
def set_visibility_of_first_point_by_ray(new_visibility: bool, origin: Vector,
                                         direction: Vector,
                                         radius: float) -> None
```

x.set_visibility_of_first_point_by_ray(new_visibility, origin, direction, radius) -> None
Sets visibility of the first point hit by the given ray.

Args:
    new_visibility (bool): 
    origin (Vector): 
    direction (Vector): 
    radius (float):

<a id="unreal.LidarPointCloudComponent.set_point_shape"></a>

#### set_point_shape

```python
def set_point_shape(new_point_shape: LidarPointCloudSpriteShape) -> None
```

x.set_point_shape(new_point_shape) -> None
Sets new Point Shape

Args:
    new_point_shape (LidarPointCloudSpriteShape):

<a id="unreal.LidarPointCloudComponent.set_point_cloud"></a>

#### set_point_cloud

```python
def set_point_cloud(point_cloud: LidarPointCloud) -> None
```

x.set_point_cloud(point_cloud) -> None
Set Point Cloud

Args:
    point_cloud (LidarPointCloud):

<a id="unreal.LidarPointCloudComponent.remove_points_in_sphere"></a>

#### remove_points_in_sphere

```python
def remove_points_in_sphere(center: Vector, radius: float,
                            visible_only: bool) -> None
```

x.remove_points_in_sphere(center, radius, visible_only) -> None
Removes all points within the given sphere

Args:
    center (Vector): 
    radius (float): 
    visible_only (bool):

<a id="unreal.LidarPointCloudComponent.remove_points_in_box"></a>

#### remove_points_in_box

```python
def remove_points_in_box(center: Vector, extent: Vector,
                         visible_only: bool) -> None
```

x.remove_points_in_box(center, extent, visible_only) -> None
Removes all points within the given box

Args:
    center (Vector): 
    extent (Vector): 
    visible_only (bool):

<a id="unreal.LidarPointCloudComponent.remove_points_by_ray"></a>

#### remove_points_by_ray

```python
def remove_points_by_ray(origin: Vector, direction: Vector, radius: float,
                         visible_only: bool) -> None
```

x.remove_points_by_ray(origin, direction, radius, visible_only) -> None
Removes all points hit by the given ray

Args:
    origin (Vector): 
    direction (Vector): 
    radius (float): 
    visible_only (bool):

<a id="unreal.LidarPointCloudComponent.remove_first_point_by_ray"></a>

#### remove_first_point_by_ray

```python
def remove_first_point_by_ray(origin: Vector, direction: Vector, radius: float,
                              visible_only: bool) -> None
```

x.remove_first_point_by_ray(origin, direction, radius, visible_only) -> None
Removes the first point hit by the given ray

Args:
    origin (Vector): 
    direction (Vector): 
    radius (float): 
    visible_only (bool):

<a id="unreal.LidarPointCloudComponent.line_trace_single"></a>

#### line_trace_single

```python
def line_trace_single(origin: Vector, direction: Vector, radius: float,
                      visible_only: bool) -> Optional[LidarPointCloudPoint]
```

x.line_trace_single(origin, direction, radius, visible_only) -> LidarPointCloudPoint or None
Performs a raycast test against the point cloud. Returns the pointer if hit or nullptr otherwise.

Args:
    origin (Vector): 
    direction (Vector): 
    radius (float): 
    visible_only (bool): 

Returns:
    LidarPointCloudPoint or None: 

    point_hit (LidarPointCloudPoint):

<a id="unreal.LidarPointCloudComponent.line_trace_multi"></a>

#### line_trace_multi

```python
def line_trace_multi(
        origin: Vector, direction: Vector, radius: float, visible_only: bool,
        return_world_space: bool) -> Optional[Array[LidarPointCloudPoint]]
```

x.line_trace_multi(origin, direction, radius, visible_only, return_world_space) -> Array[LidarPointCloudPoint] or None
Performs a raycast test against the point cloud.
Populates OutHits array with the results.
If ReturnWorldSpace is selected, the points' locations will be converted into absolute value, otherwise they will be relative to the center of the cloud.
Returns true it anything has been hit.

Args:
    origin (Vector): 
    direction (Vector): 
    radius (float): 
    visible_only (bool): 
    return_world_space (bool): 

Returns:
    Array[LidarPointCloudPoint] or None: 

    out_hits (Array[LidarPointCloudPoint]):

<a id="unreal.LidarPointCloudComponent.has_points_in_sphere"></a>

#### has_points_in_sphere

```python
def has_points_in_sphere(center: Vector, radius: float,
                         visible_only: bool) -> bool
```

x.has_points_in_sphere(center, radius, visible_only) -> bool
Returns true if there are any points within the given sphere.

Args:
    center (Vector): 
    radius (float): 
    visible_only (bool): 

Returns:
    bool:

<a id="unreal.LidarPointCloudComponent.has_points_in_box"></a>

#### has_points_in_box

```python
def has_points_in_box(center: Vector, extent: Vector,
                      visible_only: bool) -> bool
```

x.has_points_in_box(center, extent, visible_only) -> bool
Returns true if there are any points within the given box.

Args:
    center (Vector): 
    extent (Vector): 
    visible_only (bool): 

Returns:
    bool:

<a id="unreal.LidarPointCloudComponent.has_points_by_ray"></a>

#### has_points_by_ray

```python
def has_points_by_ray(origin: Vector, direction: Vector, radius: float,
                      visible_only: bool) -> bool
```

x.has_points_by_ray(origin, direction, radius, visible_only) -> bool
Returns true if there are any points hit by the given ray.

Args:
    origin (Vector): 
    direction (Vector): 
    radius (float): 
    visible_only (bool): 

Returns:
    bool:

<a id="unreal.LidarPointCloudComponent.get_points_in_sphere_as_copies"></a>

#### get_points_in_sphere_as_copies

```python
def get_points_in_sphere_as_copies(
        center: Vector, radius: float, visible_only: bool,
        return_world_space: bool) -> Array[LidarPointCloudPoint]
```

x.get_points_in_sphere_as_copies(center, radius, visible_only, return_world_space) -> Array[LidarPointCloudPoint]
Populates the array with copies of points within the given sphere.
If ReturnWorldSpace is selected, the points' locations will be converted into absolute value, otherwise they will be relative to the center of the cloud.

Args:
    center (Vector): 
    radius (float): 
    visible_only (bool): 
    return_world_space (bool): 

Returns:
    Array[LidarPointCloudPoint]:

<a id="unreal.LidarPointCloudComponent.get_points_in_box_as_copies"></a>

#### get_points_in_box_as_copies

```python
def get_points_in_box_as_copies(
        center: Vector, extent: Vector, visible_only: bool,
        return_world_space: bool) -> Array[LidarPointCloudPoint]
```

x.get_points_in_box_as_copies(center, extent, visible_only, return_world_space) -> Array[LidarPointCloudPoint]
Populates the array with copies of points within the given box.
If ReturnWorldSpace is selected, the points' locations will be converted into absolute value, otherwise they will be relative to the center of the cloud.

Args:
    center (Vector): 
    extent (Vector): 
    visible_only (bool): 
    return_world_space (bool): 

Returns:
    Array[LidarPointCloudPoint]:

<a id="unreal.LidarPointCloudComponent.get_point_shape"></a>

#### get_point_shape

```python
def get_point_shape() -> LidarPointCloudSpriteShape
```

x.get_point_shape() -> LidarPointCloudSpriteShape
Returns the current Point Shape

Returns:
    LidarPointCloudSpriteShape:

<a id="unreal.LidarPointCloudComponent.get_point_cloud"></a>

#### get_point_cloud

```python
def get_point_cloud() -> LidarPointCloud
```

x.get_point_cloud() -> LidarPointCloud
Get Point Cloud

Returns:
    LidarPointCloud:

<a id="unreal.LidarPointCloudComponent.apply_rendering_parameters"></a>

#### apply_rendering_parameters

```python
def apply_rendering_parameters() -> None
```

x.apply_rendering_parameters() -> None
Applies specified rendering parameters (Brightness, Saturation, etc) to the selected material

<a id="unreal.LidarPointCloudComponent.apply_color_to_points_in_sphere"></a>

#### apply_color_to_points_in_sphere

```python
def apply_color_to_points_in_sphere(new_color: Color, center: Vector,
                                    radius: float, visible_only: bool) -> None
```

x.apply_color_to_points_in_sphere(new_color, center, radius, visible_only) -> None
Applies the given color to all points within the sphere

Args:
    new_color (Color): 
    center (Vector): 
    radius (float): 
    visible_only (bool):

<a id="unreal.LidarPointCloudComponent.apply_color_to_points_in_box"></a>

#### apply_color_to_points_in_box

```python
def apply_color_to_points_in_box(new_color: Color, center: Vector,
                                 extent: Vector, visible_only: bool) -> None
```

x.apply_color_to_points_in_box(new_color, center, extent, visible_only) -> None
Applies the given color to all points within the box

Args:
    new_color (Color): 
    center (Vector): 
    extent (Vector): 
    visible_only (bool):

<a id="unreal.LidarPointCloudComponent.apply_color_to_points_by_ray"></a>

#### apply_color_to_points_by_ray

```python
def apply_color_to_points_by_ray(new_color: Color, origin: Vector,
                                 direction: Vector, radius: float,
                                 visible_only: bool) -> None
```

x.apply_color_to_points_by_ray(new_color, origin, direction, radius, visible_only) -> None
Applies the given color to all points hit by the given ray

Args:
    new_color (Color): 
    origin (Vector): 
    direction (Vector): 
    radius (float): 
    visible_only (bool):

<a id="unreal.LidarPointCloudComponent.apply_color_to_first_point_by_ray"></a>

#### apply_color_to_first_point_by_ray

```python
def apply_color_to_first_point_by_ray(new_color: Color, origin: Vector,
                                      direction: Vector, radius: float,
                                      visible_only: bool) -> None
```

x.apply_color_to_first_point_by_ray(new_color, origin, direction, radius, visible_only) -> None
Applies the given color to the first point hit by the given ray

Args:
    new_color (Color): 
    origin (Vector): 
    direction (Vector): 
    radius (float): 
    visible_only (bool):

<a id="unreal.LidarPointCloudFileIO"></a>