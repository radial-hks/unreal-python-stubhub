## SkyCreator Objects

```python
class SkyCreator(Actor)
```

Sky Creator

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorActor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_guid`` (Guid):  [Read-Write] The GUID for this actor; this guid will be the same for actors from instanced streaming levels.
  see: ActorInstanceGuid, FActorInstanceGuidMapper
  note: Don't use VisibleAnywhere here to avoid getting the CPF_Edit flag and get this property reset when resetting to defaults. See FActorDetails::AddActorCategory and EditorUtilities::CopySingleProperty for details.
- ``actor_instance_guid`` (Guid):  [Read-Write] The instance GUID for this actor; this guid will be unique for actors from instanced streaming levels.
  see: ActorGuid
  note: This is not guaranteed to be valid during PostLoad, but safe to access from RegisterAllComponents.
- ``aerial_pespective_view_distance_scale`` (float):  [Read-Write] Makes the aerial perspective look thicker by scaling distances from view to surfaces (opaque and translucent).
- ``allow_tick_before_begin_play`` (bool):  [Read-Write] Whether we allow this Actor to tick before it receives the BeginPlay event.
  Normally we don't tick actors until after BeginPlay; this setting allows this behavior to be overridden.
  This Actor must be able to tick for this setting to be relevant.
- ``always_relevant`` (bool):  [Read-Write] Always relevant for network (overrides bOnlyRelevantToOwner).
- ``async_physics_tick_enabled`` (bool):  [Read-Write] Whether to use use the async physics tick with this actor.
- ``atmosphere_height`` (float):  [Read-Write] Atmosphere Height defines the height of the atmosphere above the planet's surface (in kilometers).
- ``auto_destroy_when_finished`` (bool):  [Read-Write] If true then destroy self when "finished", meaning all relevant components report that they are done and no timelines or timers are in flight.
- ``auto_receive_input`` (AutoReceiveInput):  [Read-Write] Automatically registers this actor to receive input from a player.
- ``background_clouds_contrast`` (float):  [Read-Write] Background Clouds Contrast.
- ``background_clouds_reflection_scale`` (float):  [Read-Write] Affects the scale of reflection injected to sky light. When set to 0, Background Clouds are not illuminating the world.
- ``billboard`` (BillboardComponent):  [Read-Write]
- ``block_input`` (bool):  [Read-Write] If true, all input on the stack below this actor will not be considered
- ``call_pre_replication`` (bool):  [Read-Write]
- ``call_pre_replication_for_replay`` (bool):  [Read-Write]
- ``camera_location`` (Vector):  [Read-Only]
- ``camera_location_snapped`` (Vector):  [Read-Only]
- ``can_be_damaged`` (bool):  [Read-Write] Whether this actor can take damage. Must be true for damage events (e.g. ReceiveDamage()) to be called.
  see: https://www.unrealengine.com/blog/damage-in-ue4
  see: TakeDamage(), ReceiveDamage()
- ``can_be_in_cluster`` (bool):  [Read-Write] If true, this actor can be put inside of a GC Cluster to improve Garbage Collection performance
- ``cinematic_quality`` (bool):  [Read-Write] Enables cinematic quality on Volumetric Cloud Render Target.
  Disables any form of Volumetric Cloud Render Target optimizations.
- ``cloud_ambient_occlusion`` (bool):  [Read-Write] Whether the cloud should occlude sky contribution within the atmosphere (progressively fading multiple scattering out) or not.
- ``cloud_ambient_occlusion_aperture_scale`` (float):  [Read-Write] Controls the cone aperture angle over which the sky occlusion due to volumetric clouds is evaluated.
  A value of 1 means `take into account the entire hemisphere` resulting in blurry occlusion,
  while a value of 0 means `take into account a single up occlusion direction up` resulting in sharp occlusion.
- ``cloud_ambient_occlusion_extent`` (float):  [Read-Write] The world space radius of the cloud ambient occlusion map around the camera in kilometers.
- ``cloud_ambient_occlusion_map_resolution_scale`` (float):  [Read-Write] Scale the cloud ambient occlusion map resolution, base resolution is 512. The resolution is still clamped to 'r.VolumetricCloud.SkyAO.MaxResolution'.
- ``cloud_map_offset`` (Vector2D):  [Read-Write] Low Cloud Map tileable texture UV offset.
- ``cloud_map_scale`` (float):  [Read-Write] Cloud Map tileable texture scale in kilometers.
- ``cloud_noise_detail_wind_offset`` (Vector):  [Read-Only]
- ``cloud_noise_shape_wind_offset`` (Vector):  [Read-Only]
- ``cloud_wind_offset`` (Vector):  [Read-Only]
- ``cloud_wind_skew_amount`` (float):  [Read-Write] Skew clouds towards Low Cloud Wind Direction. Affected by Low Cloud Wind Speed.
- ``cloud_wind_skew_direction`` (Vector):  [Read-Only]
- ``cloud_wind_skew_force`` (float):  [Read-Only]
- ``common_mp_cs`` (Array[MaterialParameterCollection]):  [Read-Write] Common Material Parameter Collection. Essential for most of effects and settings related to materials.
- ``compass`` (StaticMeshComponent):  [Read-Write]
- ``content_bundle_guid`` (Guid):  [Read-Write] The GUID for this actor's content bundle.
- ``control_moon_direction`` (bool):  [Read-Write] Whether to control Moon direction automatically by Sky Creator.
- ``control_sun_direction`` (bool):  [Read-Write] Whether to control Sun direction automatically by Sky Creator.
- ``coverage_variation_map_scale`` (float):  [Read-Write] Coverage Variation Map tileable texture scale in kilometers.
- ``current_lightning_interval`` (float):  [Read-Only]
- ``current_volumetric_cloud_material`` (MaterialInterface):  [Read-Only]
- ``custom_time_dilation`` (float):  [Read-Write] Allow each actor to run at a different time speed. The DeltaTime for a frame is multiplied by the global TimeDilation (in WorldSettings) and this CustomTimeDilation for this actor's tick.
- ``data_layer_assets`` (Array[DataLayerAsset]):  [Read-Write] There is currently an issue where if we allow property override of DataLayerAssets and it contains Private datalayers
  then it will always serialize a diff since those are outered to the instanced level and will get remapped differently between the Override instance and Archetype instance we are comparing against
- ``data_layers`` (Array[ActorDataLayer]):  [Read-Only] DataLayers the actor belongs to.
- ``date`` (DateTime):  [Read-Only] Calculated Date.
- ``day`` (int32):  [Read-Write] Day.
- ``daylight_saving_time`` (bool):  [Read-Write] Enables Daylight Saving Time (DST).
- ``default_update_overlaps_method_during_level_streaming`` (ActorUpdateOverlapsMethod):  [Read-Only] Default value taken from config file for this class when 'UseConfigDefault' is chosen for
  'UpdateOverlapsMethodDuringLevelStreaming'. This allows a default to be chosen per class in the matching config.
  For example, for Actor it could be specified in DefaultEngine.ini as:

  [/Script/Engine.Actor]
  DefaultUpdateOverlapsMethodDuringLevelStreaming = OnlyUpdateMovable

  Another subclass could set their default to something different, such as:

  [/Script/Engine.BlockingVolume]
  DefaultUpdateOverlapsMethodDuringLevelStreaming = NeverUpdate
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``editor_independent_wind_settings`` (SkyCreatorWindSettings):  [Read-Write] Editor Independent Wind Settings.
- ``editor_time_of_day`` (float):  [Read-Write] Time of Day in Editor.
- ``editor_weather_preset`` (SkyCreatorWeatherPreset):  [Read-Write] Current Weather Preset in Editor.
- ``editor_weather_settings`` (SkyCreatorWeatherSettings):  [Read-Write] Current Weather Settings in Editor allowing to direct variable control.
- ``editor_weather_type`` (SkyCreatorEditorWeatherType):  [Read-Write] Whether to use Editor Weather Preset or Editor Weather Settings.
- ``enable_auto_lod_generation`` (bool):  [Read-Write] Whether this actor should be considered or not during HLOD generation.
- ``enable_exponential_height_fog`` (bool):  [Read-Write] Whether to enable Exponential Height Fog.
- ``enable_gpu_precipitation`` (bool):  [Read-Write] Whether to enable GPU Precipitation feature. Requires Occlusion Capture to be enabled.
  This is relatively cheap to use and improves overall precipitation particle density.
- ``enable_occlusion_capture`` (bool):  [Read-Write] Whether to enable realtime Occlusion Capture.
- ``enable_rain_ripples_solver`` (bool):  [Read-Write]
- ``enable_wind`` (bool):  [Read-Write] Whether to enable Wind. Affects Volumetric Clouds and Weather FX particles.
- ``exponential_height_fog`` (ExponentialHeightFogComponent):  [Read-Write]
- ``exponential_height_fog_mobility`` (ComponentMobility):  [Read-Write] Exponential Height Fog Mobility.
- ``exposure_bias_curve`` (CurveFloat):  [Read-Write] Exposure compensation based on the scene EV100.
  Used to calibrate the final exposure differently depending on the average scene luminance.
  0: no adjustment, -1:2x darker, -2:4x darker, 1:2x brighter, 2:4x brighter, ...
- ``exposure_high_percent`` (float):  [Read-Write] The eye adaptation will adapt to a value extracted from the luminance histogram of the scene color.
  The value is defined as having x percent below this brightness. Higher values give bright spots on the screen more priority
  but can lead to less stable results. Lower values give the medium and darker values more priority but might cause burn out of
  bright spots.
  >0, <100, good values are in the range 80 .. 95
- ``exposure_histogram_log_max`` (float):  [Read-Write] Histogram Max value. Expressed in Log2(Luminance).
- ``exposure_histogram_log_min`` (float):  [Read-Write] Histogram Min value. Expressed in Log2(Luminance).
- ``exposure_histogram_max_ev100`` (float):  [Read-Write] Histogram Max value. Expressed in EV100 when using ExtendDefaultLuminanceRange (see project settings)
- ``exposure_histogram_min_ev100`` (float):  [Read-Write] Histogram Min value. Expressed in EV100 when using ExtendDefaultLuminanceRange (see project settings)
- ``exposure_low_percent`` (float):  [Read-Write] The eye adaptation will adapt to a value extracted from the luminance histogram of the scene color.
  The value is defined as having x percent below this brightness. Higher values give bright spots on the screen more priority
  but can lead to less stable results. Lower values give the medium and darker values more priority but might cause burn out of
  bright spots.
  >0, <100, good values are in the range 70 .. 80
- ``exposure_max_brightness`` (float):  [Read-Write] Auto-Exposure maximum adaptation. Eye Adaptation is disabled if Min = Max.
  Auto-exposure is implemented by choosing an exposure value for which the average luminance generates a pixel brightness equal to the Constant Calibration value.
  The Min/Max are expressed in pixel luminance (cd/m2).
- ``exposure_max_ev100`` (float):  [Read-Write] Auto-Exposure maximum adaptation. Eye Adaptation is disabled if Min = Max.
  Auto-exposure is implemented by choosing an exposure value for which the average luminance generates a pixel brightness equal to the Constant Calibration value.
  The Min/Max are expressed in EV100 when using ExtendDefaultLuminanceRange (see project settings).
- ``exposure_meter_mask`` (Texture):  [Read-Write] Exposure metering mask. Bright spots on the mask will have high influence on auto-exposure metering
  and dark spots will have low influence.
- ``exposure_method`` (AutoExposureMethod):  [Read-Write] Luminance computation method.
- ``exposure_min_brightness`` (float):  [Read-Write] Auto-Exposure minimum adaptation. Eye Adaptation is disabled if Min = Max.
  Auto-exposure is implemented by choosing an exposure value for which the average luminance generates a pixel brightness equal to the Constant Calibration value.
  The Min/Max are expressed in pixel luminance (cd/m2).
- ``exposure_min_ev100`` (float):  [Read-Write] Auto-Exposure minimum adaptation. Eye Adaptation is disabled if Min = Max.
  Auto-exposure is implemented by choosing an exposure value for which the average luminance generates a pixel brightness equal to the Constant Calibration value.
  The Min/Max are expressed in EV100 when using ExtendDefaultLuminanceRange (see project settings).
- ``exposure_speed_down`` (float):  [Read-Write] In F-stops per second, should be >0
- ``exposure_speed_up`` (float):  [Read-Write] In F-stops per second, should be >0
- ``extend_default_luminance_range`` (bool):  [Read-Only]
- ``external_data_layer_asset`` (ExternalDataLayerAsset):  [Read-Only]
- ``find_camera_component_when_view_target`` (bool):  [Read-Write] If true, this actor should search for an owned camera component to view through when used as a view target.
- ``fog_height_offset`` (float):  [Read-Write] Fog height offset, relative to the actor position Z.
- ``generate_overlap_events_during_level_streaming`` (bool):  [Read-Write] If true, this actor will generate overlap Begin/End events when spawned as part of level streaming, which includes initial level load.
  You might enable this is in the case where a streaming level loads around an actor and you want Begin/End overlap events to trigger.
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``god_rays_resolution`` (float):  [Read-Write] This value controls Aerial Perspective LUT Width.
- ``ground_contribution`` (bool):  [Read-Write] Sample the shadowed lighting contribution from the ground onto the medium (single scattering).
  This adds some costs to the tracing when enabled.
- ``hidden`` (bool):  [Read-Write] Allows us to only see this Actor in the Editor, and not in the actual game.
  see: SetActorHiddenInGame()
- ``high_quality_aerial_perspective`` (bool):  [Read-Write] Enable/disable a second pass to trace the aerial perspective per pixel on clouds instead of using the aerial perspective texture.
  Only usable when r.VolumetricCloud.EnableAerialPerspectiveSampling = 1 and only needed for extra quality when r.VolumetricRenderTarget = 1.
- ``hlod_layer`` (HLODLayer):  [Read-Write] The UHLODLayer in which this actor should be included.
- ``ignores_origin_shifting`` (bool):  [Read-Write] Whether this actor should not be affected by world origin shifting.
- ``independent_wind_control`` (bool):  [Read-Write] If set to true, Cloud & Weather FX Wind is controlled by either static values or by separate controller.
  If set to false, Cloud & Weather FX Wind will read values from Weather Presets.
- ``initial_life_span`` (float):  [Read-Write] How long this Actor lives before dying, 0=forever. Note this is the INITIAL value and should not be modified once play has begun.
- ``input_priority`` (int32):  [Read-Write] The priority of this input component when pushed in to the stack.
- ``instigator`` (Pawn):  [Read-Write] Pawn responsible for damage and other gameplay events caused by this actor.
- ``is_editor_only_actor`` (bool):  [Read-Write] Whether this actor is editor-only. Use with care, as if this actor is referenced by anything else that reference will be NULL in cooked builds
- ``is_editor_tick_enabled`` (bool):  [Read-Write]
- ``is_main_world_only`` (bool):  [Read-Write] If checked, this Actor will only get loaded in a main world (persistent level), it will not be loaded through Level Instances.
- ``is_spatially_loaded`` (bool):  [Read-Write] Determine if this actor is spatially loaded when placed in a partitioned world.
       If true, this actor will be loaded when in the range of any streaming sources and if (1) in no data layers, or (2) one or more of its data layers are enabled.
       If false, this actor will be loaded if (1) in no data layers, or (2) one or more of its data layers are enabled.
- ``last_lightning_position`` (Vector):  [Read-Only] Desc.
- ``latitude`` (float):  [Read-Write] Latitude for calculating Real Sun & Moon positioning.
- ``layer_bottom_altitude`` (float):  [Read-Write] The altitude at which the cloud layer starts (kilometers above the ground).
- ``layer_bottom_altitude_position`` (Vector):  [Read-Only] Desc.
- ``layer_height`` (float):  [Read-Write] The altitude at which the cloud layer ends (kilometers above the ground).
- ``layer_top_altitude_position`` (Vector):  [Read-Only]
- ``layers`` (Array[Name]):  [Read-Write] Layers the actor belongs to.  This is outside of the editoronly data to allow hiding of LD-specified layers at runtime for profiling.
- ``light_transition`` (bool):  [Read-Write] Enables Light Transition feature which optimizes performance and smoothly transitions between Sun Light & Moon Light.
  Assumes that Sun Light is always the dominant light source and that both light sources are always affecting atmosphere.
- ``lightning_available_positions`` (Array[Vector]):  [Read-Only] Desc.
- ``lightning_bolt_emissive_scale`` (float):  [Read-Write] Lightning Bolt Emissive Scale.
- ``lightning_current_index`` (int32):  [Read-Only] Desc.
- ``lightning_flash_emissive_reflection_scale`` (float):  [Read-Write] Affects the scale of reflection injected to sky light. When set to 0, Lightning Flashes are not illuminating the world..
- ``lightning_flash_emissive_scale`` (float):  [Read-Write] Lightning Flash Emissive Scale.
- ``lightning_flash_fade_delta`` (float):  [Read-Only]
- ``lightning_flash_fade_speed`` (float):  [Read-Write] Lightning Flash Fade Speed.
- ``lightning_flash_fade_update_rate`` (float):  [Read-Write] Update Rate of the Lightning Flash Fade.
- ``lightning_flash_radius_scale`` (float):  [Read-Write] Lightning Flash Radius Scale.
- ``lightning_max_samples`` (int32):  [Read-Write] Number of samples to find a Lightning spawn position from Volumetric Clouds.
- ``lightning_parameters`` (Array[SkyCreatorLightningParameters]):  [Read-Only] Desc.
- ``lightning_random_degree_in_cone_max`` (float):  [Read-Write] Random Degree In Cone Max.
- ``lightning_spawn_inner_radius`` (float):  [Read-Write] Inner radius for a random Lightning spawn.
- ``lightning_spawn_outer_radius`` (float):  [Read-Write] Outer radius for a random Lightning spawn.
- ``lightnings_parameters_rt`` (TextureRenderTarget2D):  [Read-Write] Desc.
- ``longitude`` (float):  [Read-Write] Longitude for calculating Real Sun & Moon positioning.
- ``lower_hemisphere_is_solid_color`` (bool):  [Read-Write] Whether all distant lighting from the lower hemisphere should be set to LowerHemisphereColor.
  Enabling this is accurate when lighting a scene on a planet where the ground blocks the sky,
  However disabling it can be useful to approximate skylight bounce lighting (eg Movable light).
- ``material_fx_cutoff_softness`` (float):  [Read-Write] Cutoff Softness of the all Material FX.
- ``material_fx_cutoff_world_height`` (float):  [Read-Write] Cutoff World Height of the all Material FX.
- ``min_net_update_frequency`` (float):  [Read-Write]
- ``month`` (int32):  [Read-Write] Month.
- ``moon_atmosphere_disk_color_scale`` (LinearColor):  [Read-Write] A color multiplied with the moon disk luminance.
- ``moon_azimuth`` (float):  [Read-Write] Moon Azimuth angle in degrees.
- ``moon_cloud_shadow_extent`` (float):  [Read-Write] The world space radius of the cloud shadow map around the camera in kilometers.
- ``moon_cloud_shadow_map_resolution_scale`` (float):  [Read-Write] Scale the cloud shadow map resolution, base resolution is 512. The resolution is still clamped to 'r.VolumetricCloud.ShadowMap.MaxResolution'.
- ``moon_cloud_shadow_ray_sample_count_scale`` (float):  [Read-Write] Scale the shadow map tracing sample count.
  The sample count resolution is still clamped according to scalability setting to 'r.VolumetricCloud.ShadowMap.RaySampleMaxCount'.
- ``moon_constant_atmosphere_disk_color_scale`` (bool):  [Read-Write] Whether to use constant Atmosphere Disk Color Scale for Moon.
- ``moon_constant_intensity`` (bool):  [Read-Write] Whether to control Moon Intensity by a constant value or by a value from a Weather Preset.
- ``moon_current_intensity`` (float):  [Read-Only] Desc.
- ``moon_disk_size`` (float):  [Read-Write] Angle subtended by light source in degrees (also known as angular diameter).
  Realistic value is 0.5357 which is the angle for our sun.
- ``moon_elevation`` (float):  [Read-Write] Moon Elevation angle in degrees.
- ``moon_fade_in_out_time`` (float):  [Read-Write] Fade in/out time for Moon at Dawn or Dusk
- ``moon_intensity`` (float):  [Read-Write] Moon Constant Intensity.
- ``moon_light`` (DirectionalLightComponent):  [Read-Write]
- ``moon_light_mobility`` (ComponentMobility):  [Read-Write] Moon Light Mobility.
- ``moon_per_pixel_atmosphere_transmittance`` (bool):  [Read-Write] Whether to apply atmosphere transmittance per pixel on opaque meshes, instead of using the light global transmittance.
- ``moon_phase`` (float):  [Read-Write] Moon Disk Phase.
- ``moon_phase_light_intensity_max_scale`` (float):  [Read-Write] Maximum Moon Light Intensity scale of the Moon Phase.
- ``moon_phase_light_intensity_min_scale`` (float):  [Read-Write] Minimum Moon Light Intensity scale of the Moon Phase.
- ``moon_phase_light_intensity_scale`` (bool):  [Read-Write] Whether to scale Moon Light Intensity of the Moon Phase.
- ``moon_position_data`` (CelestialPositionData):  [Read-Only] Moon Position Data.
- ``moon_position_type`` (SkyCreatorMoonPositionType):  [Read-Write] Moon Position Type.
- ``moon_rotation`` (float):  [Read-Write] Moon Disk Rotation.
- ``moon_sphere`` (StaticMeshComponent):  [Read-Write]
- ``moon_surface_brightness`` (float):  [Read-Only] Current Moon Surface Brightness.
- ``moon_use_temperature`` (bool):  [Read-Write] Whether to use Color temperature for moon.
- ``moonrise_time`` (float):  [Read-Write] User-defined Moonrise Time.
- ``moonset_time`` (float):  [Read-Write] User-defined Moonset Time.
- ``multi_scattering_approximation_octave_count`` (int32):  [Read-Write] How many octave to use for the multiple-scattering approximation.
  This makes the shader more expensive so try to use only a single octave.
  0 means single scattering only.
- ``net_cull_distance_squared`` (float):  [Read-Write]
- ``net_dormancy`` (NetDormancy):  [Read-Write] Dormancy setting for actor to take itself off of the replication list without being destroyed on clients.
- ``net_load_on_client`` (bool):  [Read-Write] This actor will be loaded on network clients during map load
- ``net_priority`` (float):  [Read-Write] Priority for this actor when checking for replication in a low bandwidth or saturated situation, higher priority means it is more likely to replicate
- ``net_update_frequency`` (float):  [Read-Write]
- ``net_use_owner_relevancy`` (bool):  [Read-Write] If actor has valid Owner, call Owner's IsNetRelevantFor and GetNetPriority
- ``night_intensity_transition_end_sun_angle`` (float):  [Read-Write] The angle of the Sun to end the transition to Sky Light Night Intensity.
- ``night_intensity_transition_start_sun_angle`` (float):  [Read-Write] The angle of the Sun to start the transition to Sky Light Night Intensity.
- ``noise_detail_resolution`` (VolumetricCloudNoiseDetailResolution):  [Read-Write] Resolution of a Noise Detail 3D Texture. Can affect performance and memory consumption.
- ``noise_detail_scale`` (float):  [Read-Write] Tileable 3D Noise Detail Scale (in kilometers).
- ``noise_shape_resolution`` (VolumetricCloudNoiseShapeResolution):  [Read-Write] Resolution of a Noise Shape 3D Texture. Can affect performance and memory consumption.
- ``noise_shape_scale`` (float):  [Read-Write] Tileable 3D Noise Shape Scale (in kilometers).
- ``occlusion_bias`` (float):  [Read-Write] Occlusion Bias works similarly as known 'Shadow Bias' technique in shadow mapping. Low values can cause occlusion artifacts.
- ``occlusion_blur_distance`` (float):  [Read-Write] Blurring distance of the Occlusion Blur.
- ``occlusion_blur_samples`` (int32):  [Read-Write] Sample count of the Occlusion Blur.
- ``occlusion_capture`` (SceneCaptureComponent2D):  [Read-Write]
- ``occlusion_capture_height`` (float):  [Read-Write] Occlusion Capture camera height.
- ``occlusion_capture_realtime_update`` (bool):  [Read-Write] Occlusion Capture realtime update. Expensive, so use with caution.
- ``occlusion_capture_step_distance`` (float):  [Read-Write] Fixed distance step to update Occlusion Capture.
- ``occlusion_capture_step_size`` (float):  [Read-Only] Step Size of the Occlusion Capture. Also this will be the size of a single texel of the Occlusion Render Target in world units.
  This is done to avoid 'pixel bleeding'.
- ``occlusion_capture_width`` (float):  [Read-Write] Occlusion Capture width. Half of this value is a radius.
- ``occlusion_current_location`` (Vector):  [Read-Only]
- ``occlusion_mask_fade_hardness`` (float):  [Read-Write] Hardness of fading Occlusion radial mask.
- ``occlusion_render_target`` (TextureRenderTarget2D):  [Read-Write] Occlusion Render Target.
- ``on_actor_begin_overlap`` (ActorBeginOverlapSignature):  [Read-Write] Called when another actor begins to overlap this actor, for example a player walking into a trigger.
  For events when objects have a blocking collision, for example a player hitting a wall, see 'Hit' events.
  note: Components on both this and the other Actor must have bGenerateOverlapEvents set to true to generate overlap events.
- ``on_actor_end_overlap`` (ActorEndOverlapSignature):  [Read-Write] Called when another actor stops overlapping this actor.
  note: Components on both this and the other Actor must have bGenerateOverlapEvents set to true to generate overlap events.
- ``on_actor_hit`` (ActorHitSignature):  [Read-Write] Called when this Actor hits (or is hit by) something solid. This could happen due to things like Character movement, using Set Location with 'sweep' enabled, or physics simulation.
  For events when objects overlap (e.g. walking into a trigger) see the 'Overlap' event.
  note: For collisions during physics simulation to generate hit events, 'Simulation Generates Hit Events' must be enabled.
- ``on_begin_cursor_over`` (ActorBeginCursorOverSignature):  [Read-Write] Called when the mouse cursor is moved over this actor if mouse over events are enabled in the player controller.
- ``on_clicked`` (ActorOnClickedSignature):  [Read-Write] Called when the left mouse button is clicked while the mouse is over this actor and click events are enabled in the player controller.
- ``on_destroyed`` (ActorDestroyedSignature):  [Read-Write] Event triggered when the actor has been explicitly destroyed.
- ``on_end_cursor_over`` (ActorEndCursorOverSignature):  [Read-Write] Called when the mouse cursor is moved off this actor if mouse over events are enabled in the player controller.
- ``on_end_play`` (ActorEndPlaySignature):  [Read-Write] Event triggered when the actor is being deleted or removed from a level.
- ``on_input_touch_begin`` (ActorOnInputTouchBeginSignature):  [Read-Write] Called when a touch input is received over this actor when touch events are enabled in the player controller.
- ``on_input_touch_end`` (ActorOnInputTouchEndSignature):  [Read-Write] Called when a touch input is received over this component when touch events are enabled in the player controller.
- ``on_input_touch_enter`` (ActorBeginTouchOverSignature):  [Read-Write] Called when a finger is moved over this actor when touch over events are enabled in the player controller.
- ``on_input_touch_leave`` (ActorEndTouchOverSignature):  [Read-Write] Called when a finger is moved off this actor when touch over events are enabled in the player controller.
- ``on_lightning_strike`` (OnLightningStrike):  [Read-Write]
- ``on_released`` (ActorOnReleasedSignature):  [Read-Write] Called when the left mouse button is released while the mouse is over this actor and click events are enabled in the player controller.
- ``on_take_any_damage`` (TakeAnyDamageSignature):  [Read-Write] Called when the actor is damaged in any way.
- ``on_take_point_damage`` (TakePointDamageSignature):  [Read-Write] Called when the actor is damaged by point damage.
- ``on_take_radial_damage`` (TakeRadialDamageSignature):  [Read-Write] Called when the actor is damaged by radial damage.
- ``only_relevant_to_owner`` (bool):  [Read-Write] If true, this actor is only relevant to its owner. If this flag is changed during play, all non-owner channels would need to be explicitly closed.
- ``optimize_bp_component_data`` (bool):  [Read-Write] Whether to cook additional data to speed up spawn events at runtime for any Blueprint classes based on this Actor. This option may slightly increase memory usage in a cooked build.
- ``pause_rain_ripples_solver`` (bool):  [Read-Write]
- ``per_sample_atmospheric_light_transmittance`` (bool):  [Read-Write] Whether to apply atmosphere transmittance per sample, instead of using the light global transmittance.
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
- ``planet_radius`` (float):  [Read-Write] The planet radius (kilometers from the center to the ground level).
- ``planet_top_position`` (Vector):  [Read-Only] Desc.
- ``post_process`` (PostProcessComponent):  [Read-Write]
- ``post_process_priority`` (float):  [Read-Write] Priority of the Exposure component. It will override only Exposure settings from Post Process Volumes with lower priority,
  unless additional Post Process settings modified on this component.
- ``precipitation_camera_fade_distance`` (float):  [Read-Write] Camera Fade distance for precipitation particles.
- ``precipitation_camera_fade_offset`` (float):  [Read-Write] Camera Fade Offset distance for precipitation particles.
- ``precipitation_collision_channel`` (CollisionChannel):  [Read-Write] Collision Channel for precipitation particles to check against.
- ``precipitation_depth_fade_distance`` (float):  [Read-Write] Depth Fade distance for precipitation particles.
- ``precipitation_max_view_distance`` (float):  [Read-Write] Max distance at where precipitation particles will live.
- ``precipitation_spawn_radius`` (float):  [Read-Write] Precipitation spawn radius around the camera.
- ``precipitation_spawn_radius_gpu`` (float):  [Read-Write] GPU Precipitation spawn radius around the camera.
- ``precipitation_vertical_check_distance`` (float):  [Read-Write] Distance of vertical line trace from particle spawn point to check against occlusion.
- ``primary_actor_tick`` (ActorTickFunction):  [Read-Write] Primary Actor tick function, which calls TickActor().
  Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.
  see: https://docs.unrealengine.com/API/Runtime/Engine/Engine/FTickFunction
  see: AddTickPrerequisiteActor(), AddTickPrerequisiteComponent()
- ``puddles_mask_scale`` (float):  [Read-Write] Scale of the Puddles Mask in world units.
- ``puddles_roughness`` (float):  [Read-Write] Roughness of the Puddles effect.
- ``puddles_slope_angle`` (float):  [Read-Write] Slope Angle for the Puddles effect.
- ``puddles_slope_smoothness`` (float):  [Read-Write] Slope Smoothness for the Puddles effect.
- ``rain_camera_motion_alignment_scale`` (float):  [Read-Write] Sets the amount of Camera Motion Alignment effect.
  Set 0 to turn it off.
- ``rain_distance_scale_factor`` (float):  [Read-Write] Scale Factor by distance for rain particles (for better visibility).
- ``rain_mask_hardness`` (float):  [Read-Write] Mask Hardness for snow particles. Controls how 'soft' they look.
- ``rain_ripples_force`` (MaterialInterface):  [Read-Write]
- ``rain_ripples_max_density`` (float):  [Read-Write] Max density of Rain Ripples when the amount equals "1".
- ``rain_ripples_normal`` (MaterialInterface):  [Read-Write]
- ``rain_ripples_normal_mid`` (MaterialInstanceDynamic):  [Read-Only]
- ``rain_ripples_normal_rt`` (TextureRenderTarget2D):  [Read-Only]
- ``rain_ripples_propagation`` (MaterialInterface):  [Read-Write]
- ``rain_ripples_propagation_frame0`` (TextureRenderTarget2D):  [Read-Only]
- ``rain_ripples_propagation_frame1`` (TextureRenderTarget2D):  [Read-Only]
- ``rain_ripples_propagation_frame2`` (TextureRenderTarget2D):  [Read-Only]
- ``rain_ripples_propagation_mid`` (MaterialInstanceDynamic):  [Read-Only]
- ``rain_ripples_scale`` (float):  [Read-Write] Scale of the Rain Ripples in world units.
- ``rain_ripples_solver_delta`` (float):  [Read-Only]
- ``rain_ripples_solver_height_state`` (int32):  [Read-Only]
- ``rain_ripples_update_rate`` (float):  [Read-Write] Update Rate of the Rain Ripples Solver. Higher values increases simulation speed.
- ``rain_spawn_rate_max_cpu`` (float):  [Read-Write] Max number of rain particles to spawn per second.
  Value is multiplied by "Rain Amount" value in weather preset.
- ``rain_spawn_rate_max_gpu`` (float):  [Read-Write] Max number of rain particles to spawn per second.
  Value is multiplied by "Rain Amount" value in weather preset.
- ``rain_splash_spawn_rate_max`` (float):  [Read-Write] Max number of rain splash particles to spawn per second.
  Value is multiplied by "Rain Amount" value in weather preset.
- ``rain_splash_spawn_rate_max_gpu`` (float):  [Read-Write] Max number of rain splash particles to spawn per second.
  Value is multiplied by "Rain Amount" value in weather preset.
- ``rain_velocity_elongation_scale`` (float):  [Read-Write] Elongation (stretching) scale based on velocity of a rain particle.
- ``rainbow_depth_fade_distance`` (float):  [Read-Write] Depth Fade distance for precipitation particles.
- ``rainbow_distance`` (float):  [Read-Write] Camera Fade distance for precipitation particles.
- ``ray_march_volume_shadow`` (bool):  [Read-Write] Disable this to use the cloud shadow map instead of secondary raymarching.
  This is usually enough for clouds viewed from the ground and it result in a performance boost.
  Shadow now have infinite length but also becomes less accurate and gray scale.
- ``real_time_capture`` (bool):  [Read-Write] When enabled, the sky will be captured and convolved to achieve dynamic diffuse and specular environment lighting.
  SkyAtmosphere, VolumetricCloud Components as well as sky domes with Sky materials are taken into account.
  Should be enabled if using dynamic time of day.
- ``reflection_sample_count_scale`` (float):  [Read-Write] Scale the tracing sample count in reflection views. Quality level scalability CVARs affect the maximum range.
  The sample count resolution is still clamped according to scalability setting to 'r.VolumetricCloud.ReflectionRaySampleMaxCount'.
- ``relevant_for_level_bounds`` (bool):  [Read-Write] If true, this actor's component's bounds will be included in the level's
  bounding box unless the Actor's class has overridden IsLevelBoundsRelevant
- ``remote_role`` (NetRole):  [Read-Only] Describes how much control the remote machine has over the actor.
- ``render_mode`` (VolumetricCloudRenderTargetMode):  [Read-Write] Default: trace quarter resolution + reconstruct at half resolution + upsample
  Quality: trace half resolution + reconstruct full res + upsample
  Performance: trace at quarter resolution + reconstruct full resolution (cannot intersect with opaque meshes and forces UpsamplingMode = 2)
- ``replay_rewindable`` (bool):  [Read-Write] If true, this actor will only be destroyed during scrubbing if the replay is set to a time before the actor existed.
  Otherwise, RewindForReplay will be called if we detect the actor needs to be reset.
  Note, this Actor must not be destroyed by gamecode, and RollbackViaDeletion may not be used.
- ``replicate_movement`` (bool):  [Read-Write] If true, replicate movement/location related properties.
  Actor must also be set to replicate.
  see: SetReplicates()
  see: https://docs.unrealengine.com/InteractiveExperiences/Networking/Actors
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects and the replicated actor components list
  When false the replication system will instead call the virtual ReplicateSubobjects() function where the subobjects and actor components need to be manually replicated.
- ``replicated_movement`` (RepMovement):  [Read-Write] Used for replication of our RootComponent's position and velocity
- ``replicates`` (bool):  [Read-Write] If true, this actor will replicate to remote machines
  see: SetReplicates()
- ``role`` (NetRole):  [Read-Only] Describes how much control the local machine has over the actor.
- ``root`` (SceneComponent):  [Read-Write]
- ``root_component`` (SceneComponent):  [Read-Write] The component that defines the transform (location, rotation, scale) of this Actor in the world, all other components must be attached to this one somehow
- ``runtime_grid`` (Name):  [Read-Write] Determine in which partition grid this actor will be placed in the partition (if the world is partitioned).
  If None, the decision will be left to the partition.
- ``sample_cloud_density`` (bool):  [Read-Write] Enables sampling Volumetric Clouds to find a Lightning spawn position. Currently is a bit expensive to use.
- ``second_fog_height_offset`` (float):  [Read-Write] Second Fog height offset, relative to the actor position Z.
- ``shadow_reflection_sample_count_scale`` (float):  [Read-Write] Scale the shadow tracing sample count in reflection views, only used with Advanced Output ray marched shadows. Quality level scalability CVARs affect the maximum range.
  The sample count resolution is still clamped according to scalability setting to 'r.VolumetricCloud.Shadow.ReflectionRaySampleMaxCount'.
- ``shadow_tracing_distance`` (float):  [Read-Write] The shadow tracing distance in kilometers, only used with Advanced Output ray marched shadows.
- ``shadow_view_sample_count_scale`` (float):  [Read-Write] Scale the shadow tracing sample count in primary views, only used with Advanced Output ray marched shadows. Quality level scalability CVARs affect the maximum range.
  The sample count resolution is still clamped according to scalability setting to 'r.VolumetricCloud.Shadow.ViewRaySampleMaxCount'.
- ``show_debug_variables`` (bool):  [Read-Write] Show or Hide debug variables across all sub-categories of settings.
- ``sky_atmosphere`` (SkyAtmosphereComponent):  [Read-Write]
- ``sky_atmosphere_mobility`` (ComponentMobility):  [Read-Write] Sky Atmosphere Mobility.
- ``sky_light`` (SkyLightComponent):  [Read-Write]
- ``sky_light_capture_time_slice`` (bool):  [Read-Write] When enabled, the real-time sky light capture and convolutions will by distributed over several frames to lower the per-frame cost.
- ``sky_light_mobility`` (ComponentMobility):  [Read-Write] Sky Light Mobility.
- ``sky_sphere`` (StaticMeshComponent):  [Read-Write]
- ``sky_sphere_material`` (MaterialInterface):  [Read-Write]
- ``sky_sphere_mid`` (MaterialInstanceDynamic):  [Read-Write]
- ``sky_sphere_radius`` (float):  [Read-Write] Sky Sphere mesh radius in kilometers.
- ``snow_camera_motion_alignment_scale`` (float):  [Read-Write] Sets the amount of Camera Motion Alignment effect.
  Set 0 to turn it off.
- ``snow_distance_scale_factor`` (float):  [Read-Write] Scale Factor by distance for snow particles (for better visibility).
- ``snow_mask_hardness`` (float):  [Read-Write] Mask Hardness for snow particles. Controls how 'soft' they look.
- ``snow_mask_scale`` (float):  [Read-Write] Scale of the Snow Mask in world units.
- ``snow_roughness`` (float):  [Read-Write] Roughness of the Snow Material.
- ``snow_scale`` (float):  [Read-Write] Scale of the Snow Material in world units.
- ``snow_slope_angle`` (float):  [Read-Write] Slope Angle for the Snow effect.
- ``snow_slope_smoothness`` (float):  [Read-Write] Slope Smoothness for the Snow effect.
- ``snow_sparkles_roughness`` (float):  [Read-Write] Roughness of the Snow Sparkles effect.
- ``snow_sparkles_scale`` (float):  [Read-Write] Scale of the Snow Sparkles effect in world units.
- ``snow_spawn_rate_max_cpu`` (float):  [Read-Write] Max number of snow particles to spawn per second.
  Value is multiplied by "Snow Amount" value in weather preset.
- ``snow_spawn_rate_max_gpu`` (float):  [Read-Write] Max number of snow particles to spawn per second.
  Value is multiplied by "Snow Amount" value in weather preset.
- ``snow_velocity_elongation_scale`` (float):  [Read-Write] Elongation (stretching) scale based on velocity of a snow particle.
- ``spawn_collision_handling_method`` (SpawnActorCollisionHandlingMethod):  [Read-Write] Controls how to handle spawning this actor in a situation where it's colliding with something else. "Default" means AlwaysSpawn here.
- ``sprite_scale`` (float):  [Read-Write] The scale to apply to any billboard components in editor builds (happens in any WITH_EDITOR build, including non-cooked games).
- ``star_map`` (StaticMeshComponent):  [Read-Write]
- ``star_map_additional_rotation`` (Vector):  [Read-Write] Star Map Additional Rotation.
- ``star_map_rotation_type`` (SkyCreatorStarMapRotationType):  [Read-Write] Star Map Rotation Type.
- ``star_map_texture`` (Texture2D):  [Read-Write] Star Map Texture.
- ``sun_atmosphere_disk_color_scale`` (LinearColor):  [Read-Write] A color multiplied with the sun disk luminance.
- ``sun_azimuth`` (float):  [Read-Write] Sun Azimuth angle in degrees.
- ``sun_cloud_shadow_extent`` (float):  [Read-Write] The world space radius of the cloud shadow map around the camera in kilometers.
- ``sun_cloud_shadow_map_resolution_scale`` (float):  [Read-Write] Scale the cloud shadow map resolution, base resolution is 512. The resolution is still clamped to 'r.VolumetricCloud.ShadowMap.MaxResolution'.
- ``sun_cloud_shadow_ray_sample_count_scale`` (float):  [Read-Write] Scale the shadow map tracing sample count.
  The sample count resolution is still clamped according to scalability setting to 'r.VolumetricCloud.ShadowMap.RaySampleMaxCount'.
- ``sun_constant_atmosphere_disk_color_scale`` (bool):  [Read-Write] Whether to use constant Atmosphere Disk Color Scale for Sun.
- ``sun_constant_intensity`` (bool):  [Read-Write] Whether to control Sun Intensity by a constant value or by a value from a Weather Preset.
- ``sun_current_elevation`` (float):  [Read-Only] Current Sun Elevation.
- ``sun_current_intensity`` (float):  [Read-Only] Desc.
- ``sun_dawn_offset_time`` (float):  [Read-Write] Sets "Sun Dawn Time" depending on "Sunrise Time"
- ``sun_dawn_time`` (float):  [Read-Only] Sun Dawn Time.
- ``sun_disk_size`` (float):  [Read-Write] Angle subtended by light source in degrees (also known as angular diameter).
  Realistic value is 0.5357 which is the angle for our sun.
- ``sun_dusk_offset_time`` (float):  [Read-Write] Sets "Sun Dusk Time" depending on "Sunset Time"
- ``sun_dusk_time`` (float):  [Read-Only] Sun Dusk Time.
- ``sun_elevation`` (float):  [Read-Write] Sun Elevation angle in degrees.
- ``sun_fade_in_out_time`` (float):  [Read-Write] Fade in/out time for Sun at Dawn or Dusk
- ``sun_intensity`` (float):  [Read-Write] Sun Constant Intensity.
- ``sun_light`` (DirectionalLightComponent):  [Read-Write]
- ``sun_light_mobility`` (ComponentMobility):  [Read-Write] Sun Light Mobility.
- ``sun_min_angle_at_dawn_dusk`` (float):  [Read-Write] Minimum Sun angle below horizon at Dawn or Dusk
- ``sun_per_pixel_atmosphere_transmittance`` (bool):  [Read-Write] Whether to apply atmosphere transmittance per pixel on opaque meshes, instead of using the light global transmittance.
- ``sun_position_data`` (CelestialPositionData):  [Read-Only] Sun Position Data.
- ``sun_position_type`` (SkyCreatorSunPositionType):  [Read-Write] Sun Position Type.
- ``sun_sphere`` (StaticMeshComponent):  [Read-Write]
- ``sun_surface_brightness`` (float):  [Read-Only] Current Sun Surface Brightness.
- ``sun_use_temperature`` (bool):  [Read-Write] Whether to use Color temperature for sun.
- ``sunrise_time`` (float):  [Read-Write] User-defined Sunrise Time.
- ``sunset_time`` (float):  [Read-Write] User-defined Sunset Time.
- ``tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing.
- ``time_of_day`` (float):  [Read-Only]
- ``time_zone`` (float):  [Read-Write] Time Zone.
- ``trace_sample_count_scale`` (float):  [Read-Write] Scale the atmosphere tracing sample count. Quality level scalability
  The sample count is still clamped according to scalability setting to 'r.SkyAtmosphere.SampleCountMax' when 'r.SkyAtmosphere.FastSkyLUT' is 0.
  The sample count is still clamped according to scalability setting to 'r.SkyAtmosphere.FastSkyLUT.SampleCountMax' when 'r.SkyAtmosphere.FastSkyLUT' is 1.
  The sample count is still clamped for aerial perspective according to  'r.SkyAtmosphere.AerialPerspectiveLUT.SampleCountMaxPerSlice'.
- ``tracing_max_distance`` (float):  [Read-Write] The maximum distance that will be traced inside the cloud layer (in kilometers).
- ``tracing_start_max_distance`` (float):  [Read-Write] The maximum distance of the volumetric surface before which we will accept to start tracing (in kilometers).
- ``transform_mode`` (SkyAtmosphereTransformMode):  [Read-Write] - Planet Top at Absolute World Position places the top ground level of the atmosphere at the world origin
  coordinates (0,0,0) in the scene. The Sky Atmosphere is not movable when this option is selected.
  - Planet Top at Component Transform places the top ground level of the atmosphere relative to the component's
  transform origin. Moving the transform of the Sky Atmosphere component, or one that it is a child of,
  moves the atmosphere within the level
  - Planet Center at Component Transform places the atmosphere centered to the component's transform origin.
  Moving the transform of the Sky Atmosphere component, or one that it is a child of, moves the atmosphere within the level.
- ``transition_end_sun_angle`` (float):  [Read-Write] The angle to end the transition.
  From this angle to "Transition Middle Sun Angle" the surface lighting of the Moon linearly fades in.
- ``transition_middle_sun_angle`` (float):  [Read-Write] The angle to switch the transition.
  At this angle the Shadow casting feature is switching between Sun & Moon as they're should not cast shadows simultaneously.
  From this angle to "Transition End Sun Angle" the surface lighting of the Moon linearly fades in.
- ``transition_start_sun_angle`` (float):  [Read-Write] The angle of the Sun to start the light transition.
  From this angle to "Transition Middle Sun Angle" the surface lighting of the Sun linearly fades out.
- ``turbulence_scale`` (float):  [Read-Write] Tileable Turbulence Scale (in kilometers).
- ``update_overlaps_method_during_level_streaming`` (ActorUpdateOverlapsMethod):  [Read-Write] Condition for calling UpdateOverlaps() to initialize overlap state when loaded in during level streaming.
  If set to 'UseConfigDefault', the default specified in ini (displayed in 'DefaultUpdateOverlapsMethodDuringLevelStreaming') will be used.
  If overlaps are not initialized, this actor and attached components will not have an initial state of what objects are touching it,
  and overlap events may only come in once one of those objects update overlaps themselves (for example when moving).
  However if an object touching it *does* initialize state, both objects will know about their touching state with each other.
  This can be a potentially large performance savings during level loading and streaming, and is safe if the object and others initially
  overlapping it do not need the overlap state because they will not trigger overlap notifications.

  Note that if 'bGenerateOverlapEventsDuringLevelStreaming' is true, overlaps are always updated in this case, but that flag
  determines whether the Begin/End overlap events are triggered.
  see: bGenerateOverlapEventsDuringLevelStreaming, DefaultUpdateOverlapsMethodDuringLevelStreaming, GetUpdateOverlapsMethodDuringLevelStreaming()
- ``use_editor_time_of_day`` (bool):  [Read-Write] Controls Time of Day by Editor.
  Disable if using a separate controller to drive Time of Day.
- ``use_editor_weather_settings`` (bool):  [Read-Write] Controls Weather Settings by Editor.
  Disable if using a separate controller to drive Weather Settings.
- ``use_exposure_settings`` (bool):  [Read-Write] Whether to use built-in Exposure Settings.
- ``view_sample_count_scale`` (float):  [Read-Write] Scale the tracing sample count in primary views. Quality level scalability CVARs affect the maximum range.
  The sample count resolution is still clamped according to scalability setting to 'r.VolumetricCloud.ViewRaySampleCountMax'.
- ``volumetric_cloud`` (VolumetricCloudComponent):  [Read-Write]
- ``volumetric_cloud_density_sample_material`` (MaterialInterface):  [Read-Only]
- ``volumetric_cloud_density_sample_mid`` (MaterialInstanceDynamic):  [Read-Only]
- ``volumetric_cloud_density_sample_rt`` (TextureRenderTarget2D):  [Read-Only]
- ``volumetric_cloud_mid`` (MaterialInstanceDynamic):  [Read-Only]
- ``volumetric_clouds_mpc`` (MaterialParameterCollection):  [Read-Write] Essential Material Parameter Collection for Volumetric Clouds.
- ``volumetric_fog`` (bool):  [Read-Write] Whether to enable Volumetric fog. Scalability settings control the resolution of the fog simulation.
- ``weather_fx`` (NiagaraComponent):  [Read-Write]
- ``weather_fx_cutoff_softness`` (float):  [Read-Write] Cutoff Softness of the all WeatherFX.
- ``weather_fx_cutoff_world_height`` (float):  [Read-Write] Cutoff World Height of the all WeatherFX.
- ``weather_settings`` (SkyCreatorWeatherSettings):  [Read-Only]
- ``wetness_slope_angle`` (float):  [Read-Write] Slope Angle for the Wetness effect.
- ``wetness_slope_smoothness`` (float):  [Read-Write] Slope Smoothness for the Wetness effect.
- ``wind_ripples_scale`` (float):  [Read-Write] Scale of the Wind Ripples in world units.
- ``year`` (int32):  [Read-Write] Year. //, ClampMin = "1990.0", ClampMax = "2100.0", ))

<a id="unreal.SkyCreator.root"></a>

#### root

```python
@property
def root() -> SceneComponent
```

(SceneComponent):  [Read-Only]

<a id="unreal.SkyCreator.billboard"></a>

#### billboard

```python
@property
def billboard() -> BillboardComponent
```

(BillboardComponent):  [Read-Only]

<a id="unreal.SkyCreator.compass"></a>

#### compass

```python
@property
def compass() -> StaticMeshComponent
```

(StaticMeshComponent):  [Read-Only]

<a id="unreal.SkyCreator.sky_atmosphere"></a>

#### sky\_atmosphere

```python
@property
def sky_atmosphere() -> SkyAtmosphereComponent
```

(SkyAtmosphereComponent):  [Read-Only]

<a id="unreal.SkyCreator.volumetric_cloud"></a>

#### volumetric\_cloud

```python
@property
def volumetric_cloud() -> VolumetricCloudComponent
```

(VolumetricCloudComponent):  [Read-Only]

<a id="unreal.SkyCreator.sky_light"></a>

#### sky\_light

```python
@property
def sky_light() -> SkyLightComponent
```

(SkyLightComponent):  [Read-Only]

<a id="unreal.SkyCreator.sun_light"></a>

#### sun\_light

```python
@property
def sun_light() -> DirectionalLightComponent
```

(DirectionalLightComponent):  [Read-Only]

<a id="unreal.SkyCreator.moon_light"></a>

#### moon\_light

```python
@property
def moon_light() -> DirectionalLightComponent
```

(DirectionalLightComponent):  [Read-Only]

<a id="unreal.SkyCreator.exponential_height_fog"></a>

#### exponential\_height\_fog

```python
@property
def exponential_height_fog() -> ExponentialHeightFogComponent
```

(ExponentialHeightFogComponent):  [Read-Only]

<a id="unreal.SkyCreator.post_process"></a>

#### post\_process

```python
@property
def post_process() -> PostProcessComponent
```

(PostProcessComponent):  [Read-Only]

<a id="unreal.SkyCreator.star_map"></a>

#### star\_map

```python
@property
def star_map() -> StaticMeshComponent
```

(StaticMeshComponent):  [Read-Only]

<a id="unreal.SkyCreator.sun_sphere"></a>

#### sun\_sphere

```python
@property
def sun_sphere() -> StaticMeshComponent
```

(StaticMeshComponent):  [Read-Only]

<a id="unreal.SkyCreator.moon_sphere"></a>

#### moon\_sphere

```python
@property
def moon_sphere() -> StaticMeshComponent
```

(StaticMeshComponent):  [Read-Only]

<a id="unreal.SkyCreator.occlusion_capture"></a>

#### occlusion\_capture

```python
@property
def occlusion_capture() -> SceneCaptureComponent2D
```

(SceneCaptureComponent2D):  [Read-Only]

<a id="unreal.SkyCreator.weather_fx"></a>

#### weather\_fx

```python
@property
def weather_fx() -> NiagaraComponent
```

(NiagaraComponent):  [Read-Only]

<a id="unreal.SkyCreator.sky_sphere"></a>

#### sky\_sphere

```python
@property
def sky_sphere() -> StaticMeshComponent
```

(StaticMeshComponent):  [Read-Only]

<a id="unreal.SkyCreator.sky_sphere_material"></a>

#### sky\_sphere\_material

```python
@property
def sky_sphere_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Only]

<a id="unreal.SkyCreator.sky_sphere_mid"></a>

#### sky\_sphere\_mid

```python
@property
def sky_sphere_mid() -> MaterialInstanceDynamic
```

(MaterialInstanceDynamic):  [Read-Only]

<a id="unreal.SkyCreator.use_editor_time_of_day"></a>

#### use\_editor\_time\_of\_day

```python
@property
def use_editor_time_of_day() -> bool
```

(bool):  [Read-Only] Controls Time of Day by Editor.
Disable if using a separate controller to drive Time of Day.

<a id="unreal.SkyCreator.editor_time_of_day"></a>

#### editor\_time\_of\_day

```python
@property
def editor_time_of_day() -> float
```

(float):  [Read-Only] Time of Day in Editor.

<a id="unreal.SkyCreator.use_editor_weather_settings"></a>

#### use\_editor\_weather\_settings

```python
@property
def use_editor_weather_settings() -> bool
```

(bool):  [Read-Only] Controls Weather Settings by Editor.
Disable if using a separate controller to drive Weather Settings.

<a id="unreal.SkyCreator.editor_weather_type"></a>

#### editor\_weather\_type

```python
@property
def editor_weather_type() -> SkyCreatorEditorWeatherType
```

(SkyCreatorEditorWeatherType):  [Read-Only] Whether to use Editor Weather Preset or Editor Weather Settings.

<a id="unreal.SkyCreator.editor_weather_preset"></a>

#### editor\_weather\_preset

```python
@property
def editor_weather_preset() -> SkyCreatorWeatherPreset
```

(SkyCreatorWeatherPreset):  [Read-Only] Current Weather Preset in Editor.

<a id="unreal.SkyCreator.editor_weather_settings"></a>

#### editor\_weather\_settings

```python
@property
def editor_weather_settings() -> SkyCreatorWeatherSettings
```

(SkyCreatorWeatherSettings):  [Read-Only] Current Weather Settings in Editor allowing to direct variable control.

<a id="unreal.SkyCreator.is_editor_tick_enabled"></a>

#### is\_editor\_tick\_enabled

```python
@property
def is_editor_tick_enabled() -> bool
```

(bool):  [Read-Only]

<a id="unreal.SkyCreator.time_of_day"></a>

#### time\_of\_day

```python
@property
def time_of_day() -> float
```

(float):  [Read-Only]

<a id="unreal.SkyCreator.weather_settings"></a>

#### weather\_settings

```python
@property
def weather_settings() -> SkyCreatorWeatherSettings
```

(SkyCreatorWeatherSettings):  [Read-Only]

<a id="unreal.SkyCreator.common_mp_cs"></a>

#### common\_mp\_cs

```python
@property
def common_mp_cs() -> Array[MaterialParameterCollection]
```

(Array[MaterialParameterCollection]):  [Read-Only] Common Material Parameter Collection. Essential for most of effects and settings related to materials.

<a id="unreal.SkyCreator.sky_sphere_radius"></a>

#### sky\_sphere\_radius

```python
@property
def sky_sphere_radius() -> float
```

(float):  [Read-Only] Sky Sphere mesh radius in kilometers.

<a id="unreal.SkyCreator.show_debug_variables"></a>

#### show\_debug\_variables

```python
@property
def show_debug_variables() -> bool
```

(bool):  [Read-Only] Show or Hide debug variables across all sub-categories of settings.

<a id="unreal.SkyCreator.sun_position_type"></a>

#### sun\_position\_type

```python
@property
def sun_position_type() -> SkyCreatorSunPositionType
```

(SkyCreatorSunPositionType):  [Read-Only] Sun Position Type.

<a id="unreal.SkyCreator.sun_position_data"></a>

#### sun\_position\_data

```python
@property
def sun_position_data() -> CelestialPositionData
```

(CelestialPositionData):  [Read-Only] Sun Position Data.

<a id="unreal.SkyCreator.moon_position_type"></a>

#### moon\_position\_type

```python
@property
def moon_position_type() -> SkyCreatorMoonPositionType
```

(SkyCreatorMoonPositionType):  [Read-Only] Moon Position Type.

<a id="unreal.SkyCreator.moon_position_data"></a>

#### moon\_position\_data

```python
@property
def moon_position_data() -> CelestialPositionData
```

(CelestialPositionData):  [Read-Only] Moon Position Data.

<a id="unreal.SkyCreator.sunrise_time"></a>

#### sunrise\_time

```python
@property
def sunrise_time() -> float
```

(float):  [Read-Only] User-defined Sunrise Time.

<a id="unreal.SkyCreator.sunset_time"></a>

#### sunset\_time

```python
@property
def sunset_time() -> float
```

(float):  [Read-Only] User-defined Sunset Time.

<a id="unreal.SkyCreator.sun_dawn_offset_time"></a>

#### sun\_dawn\_offset\_time

```python
@property
def sun_dawn_offset_time() -> float
```

(float):  [Read-Only] Sets "Sun Dawn Time" depending on "Sunrise Time"

<a id="unreal.SkyCreator.sun_dusk_offset_time"></a>

#### sun\_dusk\_offset\_time

```python
@property
def sun_dusk_offset_time() -> float
```

(float):  [Read-Only] Sets "Sun Dusk Time" depending on "Sunset Time"

<a id="unreal.SkyCreator.sun_dawn_time"></a>

#### sun\_dawn\_time

```python
@property
def sun_dawn_time() -> float
```

(float):  [Read-Only] Sun Dawn Time.

<a id="unreal.SkyCreator.sun_dusk_time"></a>

#### sun\_dusk\_time

```python
@property
def sun_dusk_time() -> float
```

(float):  [Read-Only] Sun Dusk Time.

<a id="unreal.SkyCreator.sun_elevation"></a>

#### sun\_elevation

```python
@property
def sun_elevation() -> float
```

(float):  [Read-Only] Sun Elevation angle in degrees.

<a id="unreal.SkyCreator.sun_azimuth"></a>

#### sun\_azimuth

```python
@property
def sun_azimuth() -> float
```

(float):  [Read-Only] Sun Azimuth angle in degrees.

<a id="unreal.SkyCreator.sun_min_angle_at_dawn_dusk"></a>

#### sun\_min\_angle\_at\_dawn\_dusk

```python
@property
def sun_min_angle_at_dawn_dusk() -> float
```

(float):  [Read-Only] Minimum Sun angle below horizon at Dawn or Dusk

<a id="unreal.SkyCreator.sun_fade_in_out_time"></a>

#### sun\_fade\_in\_out\_time

```python
@property
def sun_fade_in_out_time() -> float
```

(float):  [Read-Only] Fade in/out time for Sun at Dawn or Dusk

<a id="unreal.SkyCreator.moonrise_time"></a>

#### moonrise\_time

```python
@property
def moonrise_time() -> float
```

(float):  [Read-Only] User-defined Moonrise Time.

<a id="unreal.SkyCreator.moonset_time"></a>

#### moonset\_time

```python
@property
def moonset_time() -> float
```

(float):  [Read-Only] User-defined Moonset Time.

<a id="unreal.SkyCreator.moon_elevation"></a>

#### moon\_elevation

```python
@property
def moon_elevation() -> float
```

(float):  [Read-Only] Moon Elevation angle in degrees.

<a id="unreal.SkyCreator.moon_azimuth"></a>

#### moon\_azimuth

```python
@property
def moon_azimuth() -> float
```

(float):  [Read-Only] Moon Azimuth angle in degrees.

<a id="unreal.SkyCreator.moon_fade_in_out_time"></a>

#### moon\_fade\_in\_out\_time

```python
@property
def moon_fade_in_out_time() -> float
```

(float):  [Read-Only] Fade in/out time for Moon at Dawn or Dusk

<a id="unreal.SkyCreator.latitude"></a>

#### latitude

```python
@property
def latitude() -> float
```

(float):  [Read-Only] Latitude for calculating Real Sun & Moon positioning.

<a id="unreal.SkyCreator.longitude"></a>

#### longitude

```python
@property
def longitude() -> float
```

(float):  [Read-Only] Longitude for calculating Real Sun & Moon positioning.

<a id="unreal.SkyCreator.time_zone"></a>

#### time\_zone

```python
@property
def time_zone() -> float
```

(float):  [Read-Only] Time Zone.

<a id="unreal.SkyCreator.daylight_saving_time"></a>

#### daylight\_saving\_time

```python
@property
def daylight_saving_time() -> bool
```

(bool):  [Read-Only] Enables Daylight Saving Time (DST).

<a id="unreal.SkyCreator.year"></a>

#### year

```python
@property
def year() -> int
```

(int32):  [Read-Only] Year. //, ClampMin = "1990.0", ClampMax = "2100.0", ))

<a id="unreal.SkyCreator.month"></a>

#### month

```python
@property
def month() -> int
```

(int32):  [Read-Only] Month.

<a id="unreal.SkyCreator.day"></a>

#### day

```python
@property
def day() -> int
```

(int32):  [Read-Only] Day.

<a id="unreal.SkyCreator.date"></a>

#### date

```python
@property
def date() -> DateTime
```

(DateTime):  [Read-Only] Calculated Date.

<a id="unreal.SkyCreator.light_transition"></a>

#### light\_transition

```python
@property
def light_transition() -> bool
```

(bool):  [Read-Only] Enables Light Transition feature which optimizes performance and smoothly transitions between Sun Light & Moon Light.
Assumes that Sun Light is always the dominant light source and that both light sources are always affecting atmosphere.

<a id="unreal.SkyCreator.sun_surface_brightness"></a>

#### sun\_surface\_brightness

```python
@property
def sun_surface_brightness() -> float
```

(float):  [Read-Only] Current Sun Surface Brightness.

<a id="unreal.SkyCreator.moon_surface_brightness"></a>

#### moon\_surface\_brightness

```python
@property
def moon_surface_brightness() -> float
```

(float):  [Read-Only] Current Moon Surface Brightness.

<a id="unreal.SkyCreator.sun_current_elevation"></a>

#### sun\_current\_elevation

```python
@property
def sun_current_elevation() -> float
```

(float):  [Read-Only] Current Sun Elevation.

<a id="unreal.SkyCreator.transition_start_sun_angle"></a>

#### transition\_start\_sun\_angle

```python
@property
def transition_start_sun_angle() -> float
```

(float):  [Read-Only] The angle of the Sun to start the light transition.
From this angle to "Transition Middle Sun Angle" the surface lighting of the Sun linearly fades out.

<a id="unreal.SkyCreator.transition_middle_sun_angle"></a>

#### transition\_middle\_sun\_angle

```python
@property
def transition_middle_sun_angle() -> float
```

(float):  [Read-Only] The angle to switch the transition.
At this angle the Shadow casting feature is switching between Sun & Moon as they're should not cast shadows simultaneously.
From this angle to "Transition End Sun Angle" the surface lighting of the Moon linearly fades in.

<a id="unreal.SkyCreator.transition_end_sun_angle"></a>

#### transition\_end\_sun\_angle

```python
@property
def transition_end_sun_angle() -> float
```

(float):  [Read-Only] The angle to end the transition.
From this angle to "Transition Middle Sun Angle" the surface lighting of the Moon linearly fades in.

<a id="unreal.SkyCreator.night_intensity_transition_start_sun_angle"></a>

#### night\_intensity\_transition\_start\_sun\_angle

```python
@property
def night_intensity_transition_start_sun_angle() -> float
```

(float):  [Read-Only] The angle of the Sun to start the transition to Sky Light Night Intensity.

<a id="unreal.SkyCreator.night_intensity_transition_end_sun_angle"></a>

#### night\_intensity\_transition\_end\_sun\_angle

```python
@property
def night_intensity_transition_end_sun_angle() -> float
```

(float):  [Read-Only] The angle of the Sun to end the transition to Sky Light Night Intensity.

<a id="unreal.SkyCreator.sky_atmosphere_mobility"></a>

#### sky\_atmosphere\_mobility

```python
@property
def sky_atmosphere_mobility() -> ComponentMobility
```

(ComponentMobility):  [Read-Only] Sky Atmosphere Mobility.

<a id="unreal.SkyCreator.transform_mode"></a>

#### transform\_mode

```python
@property
def transform_mode() -> SkyAtmosphereTransformMode
```

(SkyAtmosphereTransformMode):  [Read-Only] - Planet Top at Absolute World Position places the top ground level of the atmosphere at the world origin
coordinates (0,0,0) in the scene. The Sky Atmosphere is not movable when this option is selected.
- Planet Top at Component Transform places the top ground level of the atmosphere relative to the component's
transform origin. Moving the transform of the Sky Atmosphere component, or one that it is a child of,
moves the atmosphere within the level
- Planet Center at Component Transform places the atmosphere centered to the component's transform origin.
Moving the transform of the Sky Atmosphere component, or one that it is a child of, moves the atmosphere within the level.

<a id="unreal.SkyCreator.planet_radius"></a>

#### planet\_radius

```python
@property
def planet_radius() -> float
```

(float):  [Read-Only] The planet radius (kilometers from the center to the ground level).

<a id="unreal.SkyCreator.atmosphere_height"></a>

#### atmosphere\_height

```python
@property
def atmosphere_height() -> float
```

(float):  [Read-Only] Atmosphere Height defines the height of the atmosphere above the planet's surface (in kilometers).

<a id="unreal.SkyCreator.aerial_pespective_view_distance_scale"></a>

#### aerial\_pespective\_view\_distance\_scale

```python
@property
def aerial_pespective_view_distance_scale() -> float
```

(float):  [Read-Only] Makes the aerial perspective look thicker by scaling distances from view to surfaces (opaque and translucent).

<a id="unreal.SkyCreator.planet_top_position"></a>

#### planet\_top\_position

```python
@property
def planet_top_position() -> Vector
```

(Vector):  [Read-Only] Desc.

<a id="unreal.SkyCreator.trace_sample_count_scale"></a>

#### trace\_sample\_count\_scale

```python
@property
def trace_sample_count_scale() -> float
```

(float):  [Read-Only] Scale the atmosphere tracing sample count. Quality level scalability
The sample count is still clamped according to scalability setting to 'r.SkyAtmosphere.SampleCountMax' when 'r.SkyAtmosphere.FastSkyLUT' is 0.
The sample count is still clamped according to scalability setting to 'r.SkyAtmosphere.FastSkyLUT.SampleCountMax' when 'r.SkyAtmosphere.FastSkyLUT' is 1.
The sample count is still clamped for aerial perspective according to  'r.SkyAtmosphere.AerialPerspectiveLUT.SampleCountMaxPerSlice'.

<a id="unreal.SkyCreator.god_rays_resolution"></a>

#### god\_rays\_resolution

```python
@property
def god_rays_resolution() -> float
```

(float):  [Read-Only] This value controls Aerial Perspective LUT Width.

<a id="unreal.SkyCreator.layer_bottom_altitude"></a>

#### layer\_bottom\_altitude

```python
@property
def layer_bottom_altitude() -> float
```

(float):  [Read-Only] The altitude at which the cloud layer starts (kilometers above the ground).

<a id="unreal.SkyCreator.layer_height"></a>

#### layer\_height

```python
@property
def layer_height() -> float
```

(float):  [Read-Only] The altitude at which the cloud layer ends (kilometers above the ground).

<a id="unreal.SkyCreator.tracing_start_max_distance"></a>

#### tracing\_start\_max\_distance

```python
@property
def tracing_start_max_distance() -> float
```

(float):  [Read-Only] The maximum distance of the volumetric surface before which we will accept to start tracing (in kilometers).

<a id="unreal.SkyCreator.tracing_max_distance"></a>

#### tracing\_max\_distance

```python
@property
def tracing_max_distance() -> float
```

(float):  [Read-Only] The maximum distance that will be traced inside the cloud layer (in kilometers).

<a id="unreal.SkyCreator.per_sample_atmospheric_light_transmittance"></a>

#### per\_sample\_atmospheric\_light\_transmittance

```python
@property
def per_sample_atmospheric_light_transmittance() -> bool
```

(bool):  [Read-Only] Whether to apply atmosphere transmittance per sample, instead of using the light global transmittance.

<a id="unreal.SkyCreator.volumetric_clouds_mpc"></a>

#### volumetric\_clouds\_mpc

```python
@property
def volumetric_clouds_mpc() -> MaterialParameterCollection
```

(MaterialParameterCollection):  [Read-Only] Essential Material Parameter Collection for Volumetric Clouds.

<a id="unreal.SkyCreator.layer_bottom_altitude_position"></a>

#### layer\_bottom\_altitude\_position

```python
@property
def layer_bottom_altitude_position() -> Vector
```

(Vector):  [Read-Only] Desc.

<a id="unreal.SkyCreator.layer_top_altitude_position"></a>

#### layer\_top\_altitude\_position

```python
@property
def layer_top_altitude_position() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.SkyCreator.current_volumetric_cloud_material"></a>

#### current\_volumetric\_cloud\_material

```python
@property
def current_volumetric_cloud_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Only]

<a id="unreal.SkyCreator.volumetric_cloud_density_sample_material"></a>

#### volumetric\_cloud\_density\_sample\_material

```python
@property
def volumetric_cloud_density_sample_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Only]

<a id="unreal.SkyCreator.volumetric_cloud_density_sample_mid"></a>

#### volumetric\_cloud\_density\_sample\_mid

```python
@property
def volumetric_cloud_density_sample_mid() -> MaterialInstanceDynamic
```

(MaterialInstanceDynamic):  [Read-Only]

<a id="unreal.SkyCreator.volumetric_cloud_density_sample_rt"></a>

#### volumetric\_cloud\_density\_sample\_rt

```python
@property
def volumetric_cloud_density_sample_rt() -> TextureRenderTarget2D
```

(TextureRenderTarget2D):  [Read-Only]

<a id="unreal.SkyCreator.cinematic_quality"></a>

#### cinematic\_quality

```python
@property
def cinematic_quality() -> bool
```

(bool):  [Read-Only] Enables cinematic quality on Volumetric Cloud Render Target.
Disables any form of Volumetric Cloud Render Target optimizations.

<a id="unreal.SkyCreator.render_mode"></a>

#### render\_mode

```python
@property
def render_mode() -> VolumetricCloudRenderTargetMode
```

(VolumetricCloudRenderTargetMode):  [Read-Only] Default: trace quarter resolution + reconstruct at half resolution + upsample
Quality: trace half resolution + reconstruct full res + upsample
Performance: trace at quarter resolution + reconstruct full resolution (cannot intersect with opaque meshes and forces UpsamplingMode = 2)

<a id="unreal.SkyCreator.high_quality_aerial_perspective"></a>

#### high\_quality\_aerial\_perspective

```python
@property
def high_quality_aerial_perspective() -> bool
```

(bool):  [Read-Only] Enable/disable a second pass to trace the aerial perspective per pixel on clouds instead of using the aerial perspective texture.
Only usable when r.VolumetricCloud.EnableAerialPerspectiveSampling = 1 and only needed for extra quality when r.VolumetricRenderTarget = 1.

<a id="unreal.SkyCreator.multi_scattering_approximation_octave_count"></a>

#### multi\_scattering\_approximation\_octave\_count

```python
@property
def multi_scattering_approximation_octave_count() -> int
```

(int32):  [Read-Only] How many octave to use for the multiple-scattering approximation.
This makes the shader more expensive so try to use only a single octave.
0 means single scattering only.

<a id="unreal.SkyCreator.ground_contribution"></a>

#### ground\_contribution

```python
@property
def ground_contribution() -> bool
```

(bool):  [Read-Only] Sample the shadowed lighting contribution from the ground onto the medium (single scattering).
This adds some costs to the tracing when enabled.

<a id="unreal.SkyCreator.ray_march_volume_shadow"></a>

#### ray\_march\_volume\_shadow

```python
@property
def ray_march_volume_shadow() -> bool
```

(bool):  [Read-Only] Disable this to use the cloud shadow map instead of secondary raymarching.
This is usually enough for clouds viewed from the ground and it result in a performance boost.
Shadow now have infinite length but also becomes less accurate and gray scale.

<a id="unreal.SkyCreator.view_sample_count_scale"></a>

#### view\_sample\_count\_scale

```python
@property
def view_sample_count_scale() -> float
```

(float):  [Read-Only] Scale the tracing sample count in primary views. Quality level scalability CVARs affect the maximum range.
The sample count resolution is still clamped according to scalability setting to 'r.VolumetricCloud.ViewRaySampleCountMax'.

<a id="unreal.SkyCreator.reflection_sample_count_scale"></a>

#### reflection\_sample\_count\_scale

```python
@property
def reflection_sample_count_scale() -> float
```

(float):  [Read-Only] Scale the tracing sample count in reflection views. Quality level scalability CVARs affect the maximum range.
The sample count resolution is still clamped according to scalability setting to 'r.VolumetricCloud.ReflectionRaySampleMaxCount'.

<a id="unreal.SkyCreator.shadow_view_sample_count_scale"></a>

#### shadow\_view\_sample\_count\_scale

```python
@property
def shadow_view_sample_count_scale() -> float
```

(float):  [Read-Only] Scale the shadow tracing sample count in primary views, only used with Advanced Output ray marched shadows. Quality level scalability CVARs affect the maximum range.
The sample count resolution is still clamped according to scalability setting to 'r.VolumetricCloud.Shadow.ViewRaySampleMaxCount'.

<a id="unreal.SkyCreator.shadow_reflection_sample_count_scale"></a>

#### shadow\_reflection\_sample\_count\_scale

```python
@property
def shadow_reflection_sample_count_scale() -> float
```

(float):  [Read-Only] Scale the shadow tracing sample count in reflection views, only used with Advanced Output ray marched shadows. Quality level scalability CVARs affect the maximum range.
The sample count resolution is still clamped according to scalability setting to 'r.VolumetricCloud.Shadow.ReflectionRaySampleMaxCount'.

<a id="unreal.SkyCreator.shadow_tracing_distance"></a>

#### shadow\_tracing\_distance

```python
@property
def shadow_tracing_distance() -> float
```

(float):  [Read-Only] The shadow tracing distance in kilometers, only used with Advanced Output ray marched shadows.

<a id="unreal.SkyCreator.cloud_map_scale"></a>

#### cloud\_map\_scale

```python
@property
def cloud_map_scale() -> float
```

(float):  [Read-Only] Cloud Map tileable texture scale in kilometers.

<a id="unreal.SkyCreator.cloud_map_offset"></a>

#### cloud\_map\_offset

```python
@property
def cloud_map_offset() -> Vector2D
```

(Vector2D):  [Read-Only] Low Cloud Map tileable texture UV offset.

<a id="unreal.SkyCreator.coverage_variation_map_scale"></a>

#### coverage\_variation\_map\_scale

```python
@property
def coverage_variation_map_scale() -> float
```

(float):  [Read-Only] Coverage Variation Map tileable texture scale in kilometers.

<a id="unreal.SkyCreator.noise_shape_resolution"></a>

#### noise\_shape\_resolution

```python
@property
def noise_shape_resolution() -> VolumetricCloudNoiseShapeResolution
```

(VolumetricCloudNoiseShapeResolution):  [Read-Only] Resolution of a Noise Shape 3D Texture. Can affect performance and memory consumption.

<a id="unreal.SkyCreator.noise_detail_resolution"></a>

#### noise\_detail\_resolution

```python
@property
def noise_detail_resolution() -> VolumetricCloudNoiseDetailResolution
```

(VolumetricCloudNoiseDetailResolution):  [Read-Only] Resolution of a Noise Detail 3D Texture. Can affect performance and memory consumption.

<a id="unreal.SkyCreator.noise_shape_scale"></a>

#### noise\_shape\_scale

```python
@property
def noise_shape_scale() -> float
```

(float):  [Read-Only] Tileable 3D Noise Shape Scale (in kilometers).

<a id="unreal.SkyCreator.noise_detail_scale"></a>

#### noise\_detail\_scale

```python
@property
def noise_detail_scale() -> float
```

(float):  [Read-Only] Tileable 3D Noise Detail Scale (in kilometers).

<a id="unreal.SkyCreator.turbulence_scale"></a>

#### turbulence\_scale

```python
@property
def turbulence_scale() -> float
```

(float):  [Read-Only] Tileable Turbulence Scale (in kilometers).

<a id="unreal.SkyCreator.background_clouds_contrast"></a>

#### background\_clouds\_contrast

```python
@property
def background_clouds_contrast() -> float
```

(float):  [Read-Only] Background Clouds Contrast.

<a id="unreal.SkyCreator.background_clouds_reflection_scale"></a>

#### background\_clouds\_reflection\_scale

```python
@property
def background_clouds_reflection_scale() -> float
```

(float):  [Read-Only] Affects the scale of reflection injected to sky light. When set to 0, Background Clouds are not illuminating the world.

<a id="unreal.SkyCreator.sky_light_mobility"></a>

#### sky\_light\_mobility

```python
@property
def sky_light_mobility() -> ComponentMobility
```

(ComponentMobility):  [Read-Only] Sky Light Mobility.

<a id="unreal.SkyCreator.real_time_capture"></a>

#### real\_time\_capture

```python
@property
def real_time_capture() -> bool
```

(bool):  [Read-Only] When enabled, the sky will be captured and convolved to achieve dynamic diffuse and specular environment lighting.
SkyAtmosphere, VolumetricCloud Components as well as sky domes with Sky materials are taken into account.
Should be enabled if using dynamic time of day.

<a id="unreal.SkyCreator.sky_light_capture_time_slice"></a>

#### sky\_light\_capture\_time\_slice

```python
@property
def sky_light_capture_time_slice() -> bool
```

(bool):  [Read-Only] When enabled, the real-time sky light capture and convolutions will by distributed over several frames to lower the per-frame cost.

<a id="unreal.SkyCreator.lower_hemisphere_is_solid_color"></a>

#### lower\_hemisphere\_is\_solid\_color

```python
@property
def lower_hemisphere_is_solid_color() -> bool
```

(bool):  [Read-Only] Whether all distant lighting from the lower hemisphere should be set to LowerHemisphereColor.
Enabling this is accurate when lighting a scene on a planet where the ground blocks the sky,
However disabling it can be useful to approximate skylight bounce lighting (eg Movable light).

<a id="unreal.SkyCreator.cloud_ambient_occlusion"></a>

#### cloud\_ambient\_occlusion

```python
@property
def cloud_ambient_occlusion() -> bool
```

(bool):  [Read-Only] Whether the cloud should occlude sky contribution within the atmosphere (progressively fading multiple scattering out) or not.

<a id="unreal.SkyCreator.cloud_ambient_occlusion_extent"></a>

#### cloud\_ambient\_occlusion\_extent

```python
@property
def cloud_ambient_occlusion_extent() -> float
```

(float):  [Read-Only] The world space radius of the cloud ambient occlusion map around the camera in kilometers.

<a id="unreal.SkyCreator.cloud_ambient_occlusion_map_resolution_scale"></a>

#### cloud\_ambient\_occlusion\_map\_resolution\_scale

```python
@property
def cloud_ambient_occlusion_map_resolution_scale() -> float
```

(float):  [Read-Only] Scale the cloud ambient occlusion map resolution, base resolution is 512. The resolution is still clamped to 'r.VolumetricCloud.SkyAO.MaxResolution'.

<a id="unreal.SkyCreator.cloud_ambient_occlusion_aperture_scale"></a>

#### cloud\_ambient\_occlusion\_aperture\_scale

```python
@property
def cloud_ambient_occlusion_aperture_scale() -> float
```

(float):  [Read-Only] Controls the cone aperture angle over which the sky occlusion due to volumetric clouds is evaluated.
A value of 1 means `take into account the entire hemisphere` resulting in blurry occlusion,
while a value of 0 means `take into account a single up occlusion direction up` resulting in sharp occlusion.

<a id="unreal.SkyCreator.sun_light_mobility"></a>

#### sun\_light\_mobility

```python
@property
def sun_light_mobility() -> ComponentMobility
```

(ComponentMobility):  [Read-Only] Sun Light Mobility.

<a id="unreal.SkyCreator.control_sun_direction"></a>

#### control\_sun\_direction

```python
@property
def control_sun_direction() -> bool
```

(bool):  [Read-Only] Whether to control Sun direction automatically by Sky Creator.

<a id="unreal.SkyCreator.sun_constant_intensity"></a>

#### sun\_constant\_intensity

```python
@property
def sun_constant_intensity() -> bool
```

(bool):  [Read-Only] Whether to control Sun Intensity by a constant value or by a value from a Weather Preset.

<a id="unreal.SkyCreator.sun_intensity"></a>

#### sun\_intensity

```python
@property
def sun_intensity() -> float
```

(float):  [Read-Only] Sun Constant Intensity.

<a id="unreal.SkyCreator.sun_current_intensity"></a>

#### sun\_current\_intensity

```python
@property
def sun_current_intensity() -> float
```

(float):  [Read-Only] Desc.

<a id="unreal.SkyCreator.sun_use_temperature"></a>

#### sun\_use\_temperature

```python
@property
def sun_use_temperature() -> bool
```

(bool):  [Read-Only] Whether to use Color temperature for sun.

<a id="unreal.SkyCreator.sun_disk_size"></a>

#### sun\_disk\_size

```python
@property
def sun_disk_size() -> float
```

(float):  [Read-Only] Angle subtended by light source in degrees (also known as angular diameter).
Realistic value is 0.5357 which is the angle for our sun.

<a id="unreal.SkyCreator.sun_constant_atmosphere_disk_color_scale"></a>

#### sun\_constant\_atmosphere\_disk\_color\_scale

```python
@property
def sun_constant_atmosphere_disk_color_scale() -> bool
```

(bool):  [Read-Only] Whether to use constant Atmosphere Disk Color Scale for Sun.

<a id="unreal.SkyCreator.sun_atmosphere_disk_color_scale"></a>

#### sun\_atmosphere\_disk\_color\_scale

```python
@property
def sun_atmosphere_disk_color_scale() -> LinearColor
```

(LinearColor):  [Read-Only] A color multiplied with the sun disk luminance.

<a id="unreal.SkyCreator.sun_per_pixel_atmosphere_transmittance"></a>

#### sun\_per\_pixel\_atmosphere\_transmittance

```python
@property
def sun_per_pixel_atmosphere_transmittance() -> bool
```

(bool):  [Read-Only] Whether to apply atmosphere transmittance per pixel on opaque meshes, instead of using the light global transmittance.

<a id="unreal.SkyCreator.sun_cloud_shadow_extent"></a>

#### sun\_cloud\_shadow\_extent

```python
@property
def sun_cloud_shadow_extent() -> float
```

(float):  [Read-Only] The world space radius of the cloud shadow map around the camera in kilometers.

<a id="unreal.SkyCreator.sun_cloud_shadow_map_resolution_scale"></a>

#### sun\_cloud\_shadow\_map\_resolution\_scale

```python
@property
def sun_cloud_shadow_map_resolution_scale() -> float
```

(float):  [Read-Only] Scale the cloud shadow map resolution, base resolution is 512. The resolution is still clamped to 'r.VolumetricCloud.ShadowMap.MaxResolution'.

<a id="unreal.SkyCreator.sun_cloud_shadow_ray_sample_count_scale"></a>

#### sun\_cloud\_shadow\_ray\_sample\_count\_scale

```python
@property
def sun_cloud_shadow_ray_sample_count_scale() -> float
```

(float):  [Read-Only] Scale the shadow map tracing sample count.
The sample count resolution is still clamped according to scalability setting to 'r.VolumetricCloud.ShadowMap.RaySampleMaxCount'.

<a id="unreal.SkyCreator.moon_light_mobility"></a>

#### moon\_light\_mobility

```python
@property
def moon_light_mobility() -> ComponentMobility
```

(ComponentMobility):  [Read-Only] Moon Light Mobility.

<a id="unreal.SkyCreator.control_moon_direction"></a>

#### control\_moon\_direction

```python
@property
def control_moon_direction() -> bool
```

(bool):  [Read-Only] Whether to control Moon direction automatically by Sky Creator.

<a id="unreal.SkyCreator.moon_constant_intensity"></a>

#### moon\_constant\_intensity

```python
@property
def moon_constant_intensity() -> bool
```

(bool):  [Read-Only] Whether to control Moon Intensity by a constant value or by a value from a Weather Preset.

<a id="unreal.SkyCreator.moon_intensity"></a>

#### moon\_intensity

```python
@property
def moon_intensity() -> float
```

(float):  [Read-Only] Moon Constant Intensity.

<a id="unreal.SkyCreator.moon_current_intensity"></a>

#### moon\_current\_intensity

```python
@property
def moon_current_intensity() -> float
```

(float):  [Read-Only] Desc.

<a id="unreal.SkyCreator.moon_use_temperature"></a>

#### moon\_use\_temperature

```python
@property
def moon_use_temperature() -> bool
```

(bool):  [Read-Only] Whether to use Color temperature for moon.

<a id="unreal.SkyCreator.moon_disk_size"></a>

#### moon\_disk\_size

```python
@property
def moon_disk_size() -> float
```

(float):  [Read-Write] Angle subtended by light source in degrees (also known as angular diameter).
Realistic value is 0.5357 which is the angle for our sun.

<a id="unreal.SkyCreator.moon_disk_size"></a>

#### moon\_disk\_size

```python
@moon_disk_size.setter
def moon_disk_size(value: float) -> None
```

<a id="unreal.SkyCreator.moon_rotation"></a>

#### moon\_rotation

```python
@property
def moon_rotation() -> float
```

(float):  [Read-Write] Moon Disk Rotation.

<a id="unreal.SkyCreator.moon_rotation"></a>

#### moon\_rotation

```python
@moon_rotation.setter
def moon_rotation(value: float) -> None
```

<a id="unreal.SkyCreator.moon_phase"></a>

#### moon\_phase

```python
@property
def moon_phase() -> float
```

(float):  [Read-Write] Moon Disk Phase.

<a id="unreal.SkyCreator.moon_phase"></a>

#### moon\_phase

```python
@moon_phase.setter
def moon_phase(value: float) -> None
```

<a id="unreal.SkyCreator.moon_phase_light_intensity_scale"></a>

#### moon\_phase\_light\_intensity\_scale

```python
@property
def moon_phase_light_intensity_scale() -> bool
```

(bool):  [Read-Only] Whether to scale Moon Light Intensity of the Moon Phase.

<a id="unreal.SkyCreator.moon_phase_light_intensity_min_scale"></a>

#### moon\_phase\_light\_intensity\_min\_scale

```python
@property
def moon_phase_light_intensity_min_scale() -> float
```

(float):  [Read-Only] Minimum Moon Light Intensity scale of the Moon Phase.

<a id="unreal.SkyCreator.moon_phase_light_intensity_max_scale"></a>

#### moon\_phase\_light\_intensity\_max\_scale

```python
@property
def moon_phase_light_intensity_max_scale() -> float
```

(float):  [Read-Only] Maximum Moon Light Intensity scale of the Moon Phase.

<a id="unreal.SkyCreator.moon_constant_atmosphere_disk_color_scale"></a>

#### moon\_constant\_atmosphere\_disk\_color\_scale

```python
@property
def moon_constant_atmosphere_disk_color_scale() -> bool
```

(bool):  [Read-Only] Whether to use constant Atmosphere Disk Color Scale for Moon.

<a id="unreal.SkyCreator.moon_atmosphere_disk_color_scale"></a>

#### moon\_atmosphere\_disk\_color\_scale

```python
@property
def moon_atmosphere_disk_color_scale() -> LinearColor
```

(LinearColor):  [Read-Only] A color multiplied with the moon disk luminance.

<a id="unreal.SkyCreator.moon_per_pixel_atmosphere_transmittance"></a>

#### moon\_per\_pixel\_atmosphere\_transmittance

```python
@property
def moon_per_pixel_atmosphere_transmittance() -> bool
```

(bool):  [Read-Only] Whether to apply atmosphere transmittance per pixel on opaque meshes, instead of using the light global transmittance.

<a id="unreal.SkyCreator.moon_cloud_shadow_extent"></a>

#### moon\_cloud\_shadow\_extent

```python
@property
def moon_cloud_shadow_extent() -> float
```

(float):  [Read-Only] The world space radius of the cloud shadow map around the camera in kilometers.

<a id="unreal.SkyCreator.moon_cloud_shadow_map_resolution_scale"></a>

#### moon\_cloud\_shadow\_map\_resolution\_scale

```python
@property
def moon_cloud_shadow_map_resolution_scale() -> float
```

(float):  [Read-Only] Scale the cloud shadow map resolution, base resolution is 512. The resolution is still clamped to 'r.VolumetricCloud.ShadowMap.MaxResolution'.

<a id="unreal.SkyCreator.moon_cloud_shadow_ray_sample_count_scale"></a>

#### moon\_cloud\_shadow\_ray\_sample\_count\_scale

```python
@property
def moon_cloud_shadow_ray_sample_count_scale() -> float
```

(float):  [Read-Only] Scale the shadow map tracing sample count.
The sample count resolution is still clamped according to scalability setting to 'r.VolumetricCloud.ShadowMap.RaySampleMaxCount'.

<a id="unreal.SkyCreator.exponential_height_fog_mobility"></a>

#### exponential\_height\_fog\_mobility

```python
@property
def exponential_height_fog_mobility() -> ComponentMobility
```

(ComponentMobility):  [Read-Only] Exponential Height Fog Mobility.

<a id="unreal.SkyCreator.enable_exponential_height_fog"></a>

#### enable\_exponential\_height\_fog

```python
@property
def enable_exponential_height_fog() -> bool
```

(bool):  [Read-Only] Whether to enable Exponential Height Fog.

<a id="unreal.SkyCreator.volumetric_fog"></a>

#### volumetric\_fog

```python
@property
def volumetric_fog() -> bool
```

(bool):  [Read-Only] Whether to enable Volumetric fog. Scalability settings control the resolution of the fog simulation.

<a id="unreal.SkyCreator.fog_height_offset"></a>

#### fog\_height\_offset

```python
@property
def fog_height_offset() -> float
```

(float):  [Read-Only] Fog height offset, relative to the actor position Z.

<a id="unreal.SkyCreator.second_fog_height_offset"></a>

#### second\_fog\_height\_offset

```python
@property
def second_fog_height_offset() -> float
```

(float):  [Read-Only] Second Fog height offset, relative to the actor position Z.

<a id="unreal.SkyCreator.star_map_texture"></a>

#### star\_map\_texture

```python
@property
def star_map_texture() -> Texture2D
```

(Texture2D):  [Read-Only] Star Map Texture.

<a id="unreal.SkyCreator.star_map_rotation_type"></a>

#### star\_map\_rotation\_type

```python
@property
def star_map_rotation_type() -> SkyCreatorStarMapRotationType
```

(SkyCreatorStarMapRotationType):  [Read-Only] Star Map Rotation Type.

<a id="unreal.SkyCreator.star_map_additional_rotation"></a>

#### star\_map\_additional\_rotation

```python
@property
def star_map_additional_rotation() -> Vector
```

(Vector):  [Read-Only] Star Map Additional Rotation.

<a id="unreal.SkyCreator.enable_occlusion_capture"></a>

#### enable\_occlusion\_capture

```python
@property
def enable_occlusion_capture() -> bool
```

(bool):  [Read-Only] Whether to enable realtime Occlusion Capture.

<a id="unreal.SkyCreator.occlusion_render_target"></a>

#### occlusion\_render\_target

```python
@property
def occlusion_render_target() -> TextureRenderTarget2D
```

(TextureRenderTarget2D):  [Read-Only] Occlusion Render Target.

<a id="unreal.SkyCreator.occlusion_capture_width"></a>

#### occlusion\_capture\_width

```python
@property
def occlusion_capture_width() -> float
```

(float):  [Read-Only] Occlusion Capture width. Half of this value is a radius.

<a id="unreal.SkyCreator.occlusion_capture_height"></a>

#### occlusion\_capture\_height

```python
@property
def occlusion_capture_height() -> float
```

(float):  [Read-Only] Occlusion Capture camera height.

<a id="unreal.SkyCreator.occlusion_capture_realtime_update"></a>

#### occlusion\_capture\_realtime\_update

```python
@property
def occlusion_capture_realtime_update() -> bool
```

(bool):  [Read-Only] Occlusion Capture realtime update. Expensive, so use with caution.

<a id="unreal.SkyCreator.occlusion_capture_step_distance"></a>

#### occlusion\_capture\_step\_distance

```python
@property
def occlusion_capture_step_distance() -> float
```

(float):  [Read-Only] Fixed distance step to update Occlusion Capture.

<a id="unreal.SkyCreator.occlusion_capture_step_size"></a>

#### occlusion\_capture\_step\_size

```python
@property
def occlusion_capture_step_size() -> float
```

(float):  [Read-Only] Step Size of the Occlusion Capture. Also this will be the size of a single texel of the Occlusion Render Target in world units.
This is done to avoid 'pixel bleeding'.

<a id="unreal.SkyCreator.occlusion_bias"></a>

#### occlusion\_bias

```python
@property
def occlusion_bias() -> float
```

(float):  [Read-Only] Occlusion Bias works similarly as known 'Shadow Bias' technique in shadow mapping. Low values can cause occlusion artifacts.

<a id="unreal.SkyCreator.occlusion_blur_samples"></a>

#### occlusion\_blur\_samples

```python
@property
def occlusion_blur_samples() -> int
```

(int32):  [Read-Only] Sample count of the Occlusion Blur.

<a id="unreal.SkyCreator.occlusion_blur_distance"></a>

#### occlusion\_blur\_distance

```python
@property
def occlusion_blur_distance() -> float
```

(float):  [Read-Only] Blurring distance of the Occlusion Blur.

<a id="unreal.SkyCreator.occlusion_mask_fade_hardness"></a>

#### occlusion\_mask\_fade\_hardness

```python
@property
def occlusion_mask_fade_hardness() -> float
```

(float):  [Read-Only] Hardness of fading Occlusion radial mask.

<a id="unreal.SkyCreator.camera_location"></a>

#### camera\_location

```python
@property
def camera_location() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.SkyCreator.camera_location_snapped"></a>

#### camera\_location\_snapped

```python
@property
def camera_location_snapped() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.SkyCreator.occlusion_current_location"></a>

#### occlusion\_current\_location

```python
@property
def occlusion_current_location() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.SkyCreator.weather_fx_cutoff_world_height"></a>

#### weather\_fx\_cutoff\_world\_height

```python
@property
def weather_fx_cutoff_world_height() -> float
```

(float):  [Read-Only] Cutoff World Height of the all WeatherFX.

<a id="unreal.SkyCreator.weather_fx_cutoff_softness"></a>

#### weather\_fx\_cutoff\_softness

```python
@property
def weather_fx_cutoff_softness() -> float
```

(float):  [Read-Only] Cutoff Softness of the all WeatherFX.

<a id="unreal.SkyCreator.precipitation_spawn_radius"></a>

#### precipitation\_spawn\_radius

```python
@property
def precipitation_spawn_radius() -> float
```

(float):  [Read-Only] Precipitation spawn radius around the camera.

<a id="unreal.SkyCreator.enable_gpu_precipitation"></a>

#### enable\_gpu\_precipitation

```python
@property
def enable_gpu_precipitation() -> bool
```

(bool):  [Read-Only] Whether to enable GPU Precipitation feature. Requires Occlusion Capture to be enabled.
This is relatively cheap to use and improves overall precipitation particle density.

<a id="unreal.SkyCreator.precipitation_spawn_radius_gpu"></a>

#### precipitation\_spawn\_radius\_gpu

```python
@property
def precipitation_spawn_radius_gpu() -> float
```

(float):  [Read-Only] GPU Precipitation spawn radius around the camera.

<a id="unreal.SkyCreator.precipitation_max_view_distance"></a>

#### precipitation\_max\_view\_distance

```python
@property
def precipitation_max_view_distance() -> float
```

(float):  [Read-Only] Max distance at where precipitation particles will live.

<a id="unreal.SkyCreator.precipitation_vertical_check_distance"></a>

#### precipitation\_vertical\_check\_distance

```python
@property
def precipitation_vertical_check_distance() -> float
```

(float):  [Read-Only] Distance of vertical line trace from particle spawn point to check against occlusion.

<a id="unreal.SkyCreator.precipitation_collision_channel"></a>

#### precipitation\_collision\_channel

```python
@property
def precipitation_collision_channel() -> CollisionChannel
```

(CollisionChannel):  [Read-Only] Collision Channel for precipitation particles to check against.

<a id="unreal.SkyCreator.precipitation_depth_fade_distance"></a>

#### precipitation\_depth\_fade\_distance

```python
@property
def precipitation_depth_fade_distance() -> float
```

(float):  [Read-Only] Depth Fade distance for precipitation particles.

<a id="unreal.SkyCreator.precipitation_camera_fade_distance"></a>

#### precipitation\_camera\_fade\_distance

```python
@property
def precipitation_camera_fade_distance() -> float
```

(float):  [Read-Only] Camera Fade distance for precipitation particles.

<a id="unreal.SkyCreator.precipitation_camera_fade_offset"></a>

#### precipitation\_camera\_fade\_offset

```python
@property
def precipitation_camera_fade_offset() -> float
```

(float):  [Read-Only] Camera Fade Offset distance for precipitation particles.

<a id="unreal.SkyCreator.rain_spawn_rate_max_cpu"></a>

#### rain\_spawn\_rate\_max\_cpu

```python
@property
def rain_spawn_rate_max_cpu() -> float
```

(float):  [Read-Only] Max number of rain particles to spawn per second.
Value is multiplied by "Rain Amount" value in weather preset.

<a id="unreal.SkyCreator.rain_spawn_rate_max_gpu"></a>

#### rain\_spawn\_rate\_max\_gpu

```python
@property
def rain_spawn_rate_max_gpu() -> float
```

(float):  [Read-Only] Max number of rain particles to spawn per second.
Value is multiplied by "Rain Amount" value in weather preset.

<a id="unreal.SkyCreator.rain_distance_scale_factor"></a>

#### rain\_distance\_scale\_factor

```python
@property
def rain_distance_scale_factor() -> float
```

(float):  [Read-Only] Scale Factor by distance for rain particles (for better visibility).

<a id="unreal.SkyCreator.rain_camera_motion_alignment_scale"></a>

#### rain\_camera\_motion\_alignment\_scale

```python
@property
def rain_camera_motion_alignment_scale() -> float
```

(float):  [Read-Only] Sets the amount of Camera Motion Alignment effect.
Set 0 to turn it off.

<a id="unreal.SkyCreator.rain_velocity_elongation_scale"></a>

#### rain\_velocity\_elongation\_scale

```python
@property
def rain_velocity_elongation_scale() -> float
```

(float):  [Read-Only] Elongation (stretching) scale based on velocity of a rain particle.

<a id="unreal.SkyCreator.rain_mask_hardness"></a>

#### rain\_mask\_hardness

```python
@property
def rain_mask_hardness() -> float
```

(float):  [Read-Only] Mask Hardness for snow particles. Controls how 'soft' they look.

<a id="unreal.SkyCreator.rain_splash_spawn_rate_max"></a>

#### rain\_splash\_spawn\_rate\_max

```python
@property
def rain_splash_spawn_rate_max() -> float
```

(float):  [Read-Only] Max number of rain splash particles to spawn per second.
Value is multiplied by "Rain Amount" value in weather preset.

<a id="unreal.SkyCreator.rain_splash_spawn_rate_max_gpu"></a>

#### rain\_splash\_spawn\_rate\_max\_gpu

```python
@property
def rain_splash_spawn_rate_max_gpu() -> float
```

(float):  [Read-Only] Max number of rain splash particles to spawn per second.
Value is multiplied by "Rain Amount" value in weather preset.

<a id="unreal.SkyCreator.snow_spawn_rate_max_cpu"></a>

#### snow\_spawn\_rate\_max\_cpu

```python
@property
def snow_spawn_rate_max_cpu() -> float
```

(float):  [Read-Only] Max number of snow particles to spawn per second.
Value is multiplied by "Snow Amount" value in weather preset.

<a id="unreal.SkyCreator.snow_spawn_rate_max_gpu"></a>

#### snow\_spawn\_rate\_max\_gpu

```python
@property
def snow_spawn_rate_max_gpu() -> float
```

(float):  [Read-Only] Max number of snow particles to spawn per second.
Value is multiplied by "Snow Amount" value in weather preset.

<a id="unreal.SkyCreator.snow_distance_scale_factor"></a>

#### snow\_distance\_scale\_factor

```python
@property
def snow_distance_scale_factor() -> float
```

(float):  [Read-Only] Scale Factor by distance for snow particles (for better visibility).

<a id="unreal.SkyCreator.snow_camera_motion_alignment_scale"></a>

#### snow\_camera\_motion\_alignment\_scale

```python
@property
def snow_camera_motion_alignment_scale() -> float
```

(float):  [Read-Only] Sets the amount of Camera Motion Alignment effect.
Set 0 to turn it off.

<a id="unreal.SkyCreator.snow_velocity_elongation_scale"></a>

#### snow\_velocity\_elongation\_scale

```python
@property
def snow_velocity_elongation_scale() -> float
```

(float):  [Read-Only] Elongation (stretching) scale based on velocity of a snow particle.

<a id="unreal.SkyCreator.snow_mask_hardness"></a>

#### snow\_mask\_hardness

```python
@property
def snow_mask_hardness() -> float
```

(float):  [Read-Only] Mask Hardness for snow particles. Controls how 'soft' they look.

<a id="unreal.SkyCreator.lightnings_parameters_rt"></a>

#### lightnings\_parameters\_rt

```python
@property
def lightnings_parameters_rt() -> TextureRenderTarget2D
```

(TextureRenderTarget2D):  [Read-Only] Desc.

<a id="unreal.SkyCreator.lightning_parameters"></a>

#### lightning\_parameters

```python
@property
def lightning_parameters() -> Array[SkyCreatorLightningParameters]
```

(Array[SkyCreatorLightningParameters]):  [Read-Only] Desc.

<a id="unreal.SkyCreator.current_lightning_interval"></a>

#### current\_lightning\_interval

```python
@property
def current_lightning_interval() -> float
```

(float):  [Read-Only]

<a id="unreal.SkyCreator.last_lightning_position"></a>

#### last\_lightning\_position

```python
@property
def last_lightning_position() -> Vector
```

(Vector):  [Read-Only] Desc.

<a id="unreal.SkyCreator.lightning_available_positions"></a>

#### lightning\_available\_positions

```python
@property
def lightning_available_positions() -> Array[Vector]
```

(Array[Vector]):  [Read-Only] Desc.

<a id="unreal.SkyCreator.lightning_current_index"></a>

#### lightning\_current\_index

```python
@property
def lightning_current_index() -> int
```

(int32):  [Read-Only] Desc.

<a id="unreal.SkyCreator.sample_cloud_density"></a>

#### sample\_cloud\_density

```python
@property
def sample_cloud_density() -> bool
```

(bool):  [Read-Only] Enables sampling Volumetric Clouds to find a Lightning spawn position. Currently is a bit expensive to use.

<a id="unreal.SkyCreator.lightning_max_samples"></a>

#### lightning\_max\_samples

```python
@property
def lightning_max_samples() -> int
```

(int32):  [Read-Only] Number of samples to find a Lightning spawn position from Volumetric Clouds.

<a id="unreal.SkyCreator.lightning_spawn_inner_radius"></a>

#### lightning\_spawn\_inner\_radius

```python
@property
def lightning_spawn_inner_radius() -> float
```

(float):  [Read-Only] Inner radius for a random Lightning spawn.

<a id="unreal.SkyCreator.lightning_spawn_outer_radius"></a>

#### lightning\_spawn\_outer\_radius

```python
@property
def lightning_spawn_outer_radius() -> float
```

(float):  [Read-Only] Outer radius for a random Lightning spawn.

<a id="unreal.SkyCreator.lightning_random_degree_in_cone_max"></a>

#### lightning\_random\_degree\_in\_cone\_max

```python
@property
def lightning_random_degree_in_cone_max() -> float
```

(float):  [Read-Only] Random Degree In Cone Max.

<a id="unreal.SkyCreator.lightning_bolt_emissive_scale"></a>

#### lightning\_bolt\_emissive\_scale

```python
@property
def lightning_bolt_emissive_scale() -> float
```

(float):  [Read-Only] Lightning Bolt Emissive Scale.

<a id="unreal.SkyCreator.lightning_flash_fade_update_rate"></a>

#### lightning\_flash\_fade\_update\_rate

```python
@property
def lightning_flash_fade_update_rate() -> float
```

(float):  [Read-Only] Update Rate of the Lightning Flash Fade.

<a id="unreal.SkyCreator.lightning_flash_fade_delta"></a>

#### lightning\_flash\_fade\_delta

```python
@property
def lightning_flash_fade_delta() -> float
```

(float):  [Read-Only]

<a id="unreal.SkyCreator.lightning_flash_emissive_scale"></a>

#### lightning\_flash\_emissive\_scale

```python
@property
def lightning_flash_emissive_scale() -> float
```

(float):  [Read-Only] Lightning Flash Emissive Scale.

<a id="unreal.SkyCreator.lightning_flash_emissive_reflection_scale"></a>

#### lightning\_flash\_emissive\_reflection\_scale

```python
@property
def lightning_flash_emissive_reflection_scale() -> float
```

(float):  [Read-Only] Affects the scale of reflection injected to sky light. When set to 0, Lightning Flashes are not illuminating the world..

<a id="unreal.SkyCreator.lightning_flash_radius_scale"></a>

#### lightning\_flash\_radius\_scale

```python
@property
def lightning_flash_radius_scale() -> float
```

(float):  [Read-Only] Lightning Flash Radius Scale.

<a id="unreal.SkyCreator.lightning_flash_fade_speed"></a>

#### lightning\_flash\_fade\_speed

```python
@property
def lightning_flash_fade_speed() -> float
```

(float):  [Read-Only] Lightning Flash Fade Speed.

<a id="unreal.SkyCreator.rainbow_distance"></a>

#### rainbow\_distance

```python
@property
def rainbow_distance() -> float
```

(float):  [Read-Only] Camera Fade distance for precipitation particles.

<a id="unreal.SkyCreator.rainbow_depth_fade_distance"></a>

#### rainbow\_depth\_fade\_distance

```python
@property
def rainbow_depth_fade_distance() -> float
```

(float):  [Read-Only] Depth Fade distance for precipitation particles.

<a id="unreal.SkyCreator.material_fx_cutoff_world_height"></a>

#### material\_fx\_cutoff\_world\_height

```python
@property
def material_fx_cutoff_world_height() -> float
```

(float):  [Read-Only] Cutoff World Height of the all Material FX.

<a id="unreal.SkyCreator.material_fx_cutoff_softness"></a>

#### material\_fx\_cutoff\_softness

```python
@property
def material_fx_cutoff_softness() -> float
```

(float):  [Read-Only] Cutoff Softness of the all Material FX.

<a id="unreal.SkyCreator.wetness_slope_angle"></a>

#### wetness\_slope\_angle

```python
@property
def wetness_slope_angle() -> float
```

(float):  [Read-Only] Slope Angle for the Wetness effect.

<a id="unreal.SkyCreator.wetness_slope_smoothness"></a>

#### wetness\_slope\_smoothness

```python
@property
def wetness_slope_smoothness() -> float
```

(float):  [Read-Only] Slope Smoothness for the Wetness effect.

<a id="unreal.SkyCreator.puddles_mask_scale"></a>

#### puddles\_mask\_scale

```python
@property
def puddles_mask_scale() -> float
```

(float):  [Read-Only] Scale of the Puddles Mask in world units.

<a id="unreal.SkyCreator.puddles_roughness"></a>

#### puddles\_roughness

```python
@property
def puddles_roughness() -> float
```

(float):  [Read-Only] Roughness of the Puddles effect.

<a id="unreal.SkyCreator.puddles_slope_angle"></a>

#### puddles\_slope\_angle

```python
@property
def puddles_slope_angle() -> float
```

(float):  [Read-Only] Slope Angle for the Puddles effect.

<a id="unreal.SkyCreator.puddles_slope_smoothness"></a>

#### puddles\_slope\_smoothness

```python
@property
def puddles_slope_smoothness() -> float
```

(float):  [Read-Only] Slope Smoothness for the Puddles effect.

<a id="unreal.SkyCreator.enable_rain_ripples_solver"></a>

#### enable\_rain\_ripples\_solver

```python
@property
def enable_rain_ripples_solver() -> bool
```

(bool):  [Read-Only]

<a id="unreal.SkyCreator.pause_rain_ripples_solver"></a>

#### pause\_rain\_ripples\_solver

```python
@property
def pause_rain_ripples_solver() -> bool
```

(bool):  [Read-Only]

<a id="unreal.SkyCreator.rain_ripples_update_rate"></a>

#### rain\_ripples\_update\_rate

```python
@property
def rain_ripples_update_rate() -> float
```

(float):  [Read-Only] Update Rate of the Rain Ripples Solver. Higher values increases simulation speed.

<a id="unreal.SkyCreator.rain_ripples_scale"></a>

#### rain\_ripples\_scale

```python
@property
def rain_ripples_scale() -> float
```

(float):  [Read-Only] Scale of the Rain Ripples in world units.

<a id="unreal.SkyCreator.rain_ripples_max_density"></a>

#### rain\_ripples\_max\_density

```python
@property
def rain_ripples_max_density() -> float
```

(float):  [Read-Only] Max density of Rain Ripples when the amount equals "1".

<a id="unreal.SkyCreator.wind_ripples_scale"></a>

#### wind\_ripples\_scale

```python
@property
def wind_ripples_scale() -> float
```

(float):  [Read-Only] Scale of the Wind Ripples in world units.

<a id="unreal.SkyCreator.rain_ripples_solver_delta"></a>

#### rain\_ripples\_solver\_delta

```python
@property
def rain_ripples_solver_delta() -> float
```

(float):  [Read-Only]

<a id="unreal.SkyCreator.rain_ripples_solver_height_state"></a>

#### rain\_ripples\_solver\_height\_state

```python
@property
def rain_ripples_solver_height_state() -> int
```

(int32):  [Read-Only]

<a id="unreal.SkyCreator.rain_ripples_propagation"></a>

#### rain\_ripples\_propagation

```python
@property
def rain_ripples_propagation() -> MaterialInterface
```

(MaterialInterface):  [Read-Only]

<a id="unreal.SkyCreator.rain_ripples_propagation_mid"></a>

#### rain\_ripples\_propagation\_mid

```python
@property
def rain_ripples_propagation_mid() -> MaterialInstanceDynamic
```

(MaterialInstanceDynamic):  [Read-Only]

<a id="unreal.SkyCreator.rain_ripples_force"></a>

#### rain\_ripples\_force

```python
@property
def rain_ripples_force() -> MaterialInterface
```

(MaterialInterface):  [Read-Only]

<a id="unreal.SkyCreator.rain_ripples_normal"></a>

#### rain\_ripples\_normal

```python
@property
def rain_ripples_normal() -> MaterialInterface
```

(MaterialInterface):  [Read-Only]

<a id="unreal.SkyCreator.rain_ripples_normal_mid"></a>

#### rain\_ripples\_normal\_mid

```python
@property
def rain_ripples_normal_mid() -> MaterialInstanceDynamic
```

(MaterialInstanceDynamic):  [Read-Only]

<a id="unreal.SkyCreator.rain_ripples_propagation_frame0"></a>

#### rain\_ripples\_propagation\_frame0

```python
@property
def rain_ripples_propagation_frame0() -> TextureRenderTarget2D
```

(TextureRenderTarget2D):  [Read-Only]

<a id="unreal.SkyCreator.rain_ripples_propagation_frame1"></a>

#### rain\_ripples\_propagation\_frame1

```python
@property
def rain_ripples_propagation_frame1() -> TextureRenderTarget2D
```

(TextureRenderTarget2D):  [Read-Only]

<a id="unreal.SkyCreator.rain_ripples_propagation_frame2"></a>

#### rain\_ripples\_propagation\_frame2

```python
@property
def rain_ripples_propagation_frame2() -> TextureRenderTarget2D
```

(TextureRenderTarget2D):  [Read-Only]

<a id="unreal.SkyCreator.rain_ripples_normal_rt"></a>

#### rain\_ripples\_normal\_rt

```python
@property
def rain_ripples_normal_rt() -> TextureRenderTarget2D
```

(TextureRenderTarget2D):  [Read-Only]

<a id="unreal.SkyCreator.snow_mask_scale"></a>

#### snow\_mask\_scale

```python
@property
def snow_mask_scale() -> float
```

(float):  [Read-Only] Scale of the Snow Mask in world units.

<a id="unreal.SkyCreator.snow_scale"></a>

#### snow\_scale

```python
@property
def snow_scale() -> float
```

(float):  [Read-Only] Scale of the Snow Material in world units.

<a id="unreal.SkyCreator.snow_roughness"></a>

#### snow\_roughness

```python
@property
def snow_roughness() -> float
```

(float):  [Read-Only] Roughness of the Snow Material.

<a id="unreal.SkyCreator.snow_sparkles_scale"></a>

#### snow\_sparkles\_scale

```python
@property
def snow_sparkles_scale() -> float
```

(float):  [Read-Only] Scale of the Snow Sparkles effect in world units.

<a id="unreal.SkyCreator.snow_sparkles_roughness"></a>

#### snow\_sparkles\_roughness

```python
@property
def snow_sparkles_roughness() -> float
```

(float):  [Read-Only] Roughness of the Snow Sparkles effect.

<a id="unreal.SkyCreator.snow_slope_angle"></a>

#### snow\_slope\_angle

```python
@property
def snow_slope_angle() -> float
```

(float):  [Read-Only] Slope Angle for the Snow effect.

<a id="unreal.SkyCreator.snow_slope_smoothness"></a>

#### snow\_slope\_smoothness

```python
@property
def snow_slope_smoothness() -> float
```

(float):  [Read-Only] Slope Smoothness for the Snow effect.

<a id="unreal.SkyCreator.enable_wind"></a>

#### enable\_wind

```python
@property
def enable_wind() -> bool
```

(bool):  [Read-Only] Whether to enable Wind. Affects Volumetric Clouds and Weather FX particles.

<a id="unreal.SkyCreator.independent_wind_control"></a>

#### independent\_wind\_control

```python
@property
def independent_wind_control() -> bool
```

(bool):  [Read-Only] If set to true, Cloud & Weather FX Wind is controlled by either static values or by separate controller.
If set to false, Cloud & Weather FX Wind will read values from Weather Presets.

<a id="unreal.SkyCreator.editor_independent_wind_settings"></a>

#### editor\_independent\_wind\_settings

```python
@property
def editor_independent_wind_settings() -> SkyCreatorWindSettings
```

(SkyCreatorWindSettings):  [Read-Only] Editor Independent Wind Settings.

<a id="unreal.SkyCreator.cloud_wind_skew_amount"></a>

#### cloud\_wind\_skew\_amount

```python
@property
def cloud_wind_skew_amount() -> float
```

(float):  [Read-Write] Skew clouds towards Low Cloud Wind Direction. Affected by Low Cloud Wind Speed.

<a id="unreal.SkyCreator.cloud_wind_skew_amount"></a>

#### cloud\_wind\_skew\_amount

```python
@cloud_wind_skew_amount.setter
def cloud_wind_skew_amount(value: float) -> None
```

<a id="unreal.SkyCreator.cloud_wind_offset"></a>

#### cloud\_wind\_offset

```python
@property
def cloud_wind_offset() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.SkyCreator.cloud_wind_skew_direction"></a>

#### cloud\_wind\_skew\_direction

```python
@property
def cloud_wind_skew_direction() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.SkyCreator.cloud_wind_skew_force"></a>

#### cloud\_wind\_skew\_force

```python
@property
def cloud_wind_skew_force() -> float
```

(float):  [Read-Only]

<a id="unreal.SkyCreator.cloud_noise_shape_wind_offset"></a>

#### cloud\_noise\_shape\_wind\_offset

```python
@property
def cloud_noise_shape_wind_offset() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.SkyCreator.cloud_noise_detail_wind_offset"></a>

#### cloud\_noise\_detail\_wind\_offset

```python
@property
def cloud_noise_detail_wind_offset() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.SkyCreator.use_exposure_settings"></a>

#### use\_exposure\_settings

```python
@property
def use_exposure_settings() -> bool
```

(bool):  [Read-Only] Whether to use built-in Exposure Settings.

<a id="unreal.SkyCreator.extend_default_luminance_range"></a>

#### extend\_default\_luminance\_range

```python
@property
def extend_default_luminance_range() -> bool
```

(bool):  [Read-Only]

<a id="unreal.SkyCreator.post_process_priority"></a>

#### post\_process\_priority

```python
@property
def post_process_priority() -> float
```

(float):  [Read-Write] Priority of the Exposure component. It will override only Exposure settings from Post Process Volumes with lower priority,
unless additional Post Process settings modified on this component.

<a id="unreal.SkyCreator.post_process_priority"></a>

#### post\_process\_priority

```python
@post_process_priority.setter
def post_process_priority(value: float) -> None
```

<a id="unreal.SkyCreator.exposure_method"></a>

#### exposure\_method

```python
@property
def exposure_method() -> AutoExposureMethod
```

(AutoExposureMethod):  [Read-Write] Luminance computation method.

<a id="unreal.SkyCreator.exposure_method"></a>

#### exposure\_method

```python
@exposure_method.setter
def exposure_method(value: AutoExposureMethod) -> None
```

<a id="unreal.SkyCreator.exposure_bias_curve"></a>

#### exposure\_bias\_curve

```python
@property
def exposure_bias_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] Exposure compensation based on the scene EV100.
Used to calibrate the final exposure differently depending on the average scene luminance.
0: no adjustment, -1:2x darker, -2:4x darker, 1:2x brighter, 2:4x brighter, ...

<a id="unreal.SkyCreator.exposure_bias_curve"></a>

#### exposure\_bias\_curve

```python
@exposure_bias_curve.setter
def exposure_bias_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreator.exposure_meter_mask"></a>

#### exposure\_meter\_mask

```python
@property
def exposure_meter_mask() -> Texture
```

(Texture):  [Read-Write] Exposure metering mask. Bright spots on the mask will have high influence on auto-exposure metering
and dark spots will have low influence.

<a id="unreal.SkyCreator.exposure_meter_mask"></a>

#### exposure\_meter\_mask

```python
@exposure_meter_mask.setter
def exposure_meter_mask(value: Texture) -> None
```

<a id="unreal.SkyCreator.exposure_min_brightness"></a>

#### exposure\_min\_brightness

```python
@property
def exposure_min_brightness() -> float
```

(float):  [Read-Write] Auto-Exposure minimum adaptation. Eye Adaptation is disabled if Min = Max.
Auto-exposure is implemented by choosing an exposure value for which the average luminance generates a pixel brightness equal to the Constant Calibration value.
The Min/Max are expressed in pixel luminance (cd/m2).

<a id="unreal.SkyCreator.exposure_min_brightness"></a>

#### exposure\_min\_brightness

```python
@exposure_min_brightness.setter
def exposure_min_brightness(value: float) -> None
```

<a id="unreal.SkyCreator.exposure_max_brightness"></a>

#### exposure\_max\_brightness

```python
@property
def exposure_max_brightness() -> float
```

(float):  [Read-Write] Auto-Exposure maximum adaptation. Eye Adaptation is disabled if Min = Max.
Auto-exposure is implemented by choosing an exposure value for which the average luminance generates a pixel brightness equal to the Constant Calibration value.
The Min/Max are expressed in pixel luminance (cd/m2).

<a id="unreal.SkyCreator.exposure_max_brightness"></a>

#### exposure\_max\_brightness

```python
@exposure_max_brightness.setter
def exposure_max_brightness(value: float) -> None
```

<a id="unreal.SkyCreator.exposure_min_ev100"></a>

#### exposure\_min\_ev100

```python
@property
def exposure_min_ev100() -> float
```

(float):  [Read-Write] Auto-Exposure minimum adaptation. Eye Adaptation is disabled if Min = Max.
Auto-exposure is implemented by choosing an exposure value for which the average luminance generates a pixel brightness equal to the Constant Calibration value.
The Min/Max are expressed in EV100 when using ExtendDefaultLuminanceRange (see project settings).

<a id="unreal.SkyCreator.exposure_min_ev100"></a>

#### exposure\_min\_ev100

```python
@exposure_min_ev100.setter
def exposure_min_ev100(value: float) -> None
```

<a id="unreal.SkyCreator.exposure_max_ev100"></a>

#### exposure\_max\_ev100

```python
@property
def exposure_max_ev100() -> float
```

(float):  [Read-Write] Auto-Exposure maximum adaptation. Eye Adaptation is disabled if Min = Max.
Auto-exposure is implemented by choosing an exposure value for which the average luminance generates a pixel brightness equal to the Constant Calibration value.
The Min/Max are expressed in EV100 when using ExtendDefaultLuminanceRange (see project settings).

<a id="unreal.SkyCreator.exposure_max_ev100"></a>

#### exposure\_max\_ev100

```python
@exposure_max_ev100.setter
def exposure_max_ev100(value: float) -> None
```

<a id="unreal.SkyCreator.exposure_speed_up"></a>

#### exposure\_speed\_up

```python
@property
def exposure_speed_up() -> float
```

(float):  [Read-Write] In F-stops per second, should be >0

<a id="unreal.SkyCreator.exposure_speed_up"></a>

#### exposure\_speed\_up

```python
@exposure_speed_up.setter
def exposure_speed_up(value: float) -> None
```

<a id="unreal.SkyCreator.exposure_speed_down"></a>

#### exposure\_speed\_down

```python
@property
def exposure_speed_down() -> float
```

(float):  [Read-Write] In F-stops per second, should be >0

<a id="unreal.SkyCreator.exposure_speed_down"></a>

#### exposure\_speed\_down

```python
@exposure_speed_down.setter
def exposure_speed_down(value: float) -> None
```

<a id="unreal.SkyCreator.exposure_low_percent"></a>

#### exposure\_low\_percent

```python
@property
def exposure_low_percent() -> float
```

(float):  [Read-Write] The eye adaptation will adapt to a value extracted from the luminance histogram of the scene color.
The value is defined as having x percent below this brightness. Higher values give bright spots on the screen more priority
but can lead to less stable results. Lower values give the medium and darker values more priority but might cause burn out of
bright spots.
>0, <100, good values are in the range 70 .. 80

<a id="unreal.SkyCreator.exposure_low_percent"></a>

#### exposure\_low\_percent

```python
@exposure_low_percent.setter
def exposure_low_percent(value: float) -> None
```

<a id="unreal.SkyCreator.exposure_high_percent"></a>

#### exposure\_high\_percent

```python
@property
def exposure_high_percent() -> float
```

(float):  [Read-Write] The eye adaptation will adapt to a value extracted from the luminance histogram of the scene color.
The value is defined as having x percent below this brightness. Higher values give bright spots on the screen more priority
but can lead to less stable results. Lower values give the medium and darker values more priority but might cause burn out of
bright spots.
>0, <100, good values are in the range 80 .. 95

<a id="unreal.SkyCreator.exposure_high_percent"></a>

#### exposure\_high\_percent

```python
@exposure_high_percent.setter
def exposure_high_percent(value: float) -> None
```

<a id="unreal.SkyCreator.exposure_histogram_log_min"></a>

#### exposure\_histogram\_log\_min

```python
@property
def exposure_histogram_log_min() -> float
```

(float):  [Read-Write] Histogram Min value. Expressed in Log2(Luminance).

<a id="unreal.SkyCreator.exposure_histogram_log_min"></a>

#### exposure\_histogram\_log\_min

```python
@exposure_histogram_log_min.setter
def exposure_histogram_log_min(value: float) -> None
```

<a id="unreal.SkyCreator.exposure_histogram_log_max"></a>

#### exposure\_histogram\_log\_max

```python
@property
def exposure_histogram_log_max() -> float
```

(float):  [Read-Write] Histogram Max value. Expressed in Log2(Luminance).

<a id="unreal.SkyCreator.exposure_histogram_log_max"></a>

#### exposure\_histogram\_log\_max

```python
@exposure_histogram_log_max.setter
def exposure_histogram_log_max(value: float) -> None
```

<a id="unreal.SkyCreator.exposure_histogram_min_ev100"></a>

#### exposure\_histogram\_min\_ev100

```python
@property
def exposure_histogram_min_ev100() -> float
```

(float):  [Read-Write] Histogram Min value. Expressed in EV100 when using ExtendDefaultLuminanceRange (see project settings)

<a id="unreal.SkyCreator.exposure_histogram_min_ev100"></a>

#### exposure\_histogram\_min\_ev100

```python
@exposure_histogram_min_ev100.setter
def exposure_histogram_min_ev100(value: float) -> None
```

<a id="unreal.SkyCreator.exposure_histogram_max_ev100"></a>

#### exposure\_histogram\_max\_ev100

```python
@property
def exposure_histogram_max_ev100() -> float
```

(float):  [Read-Write] Histogram Max value. Expressed in EV100 when using ExtendDefaultLuminanceRange (see project settings)

<a id="unreal.SkyCreator.exposure_histogram_max_ev100"></a>

#### exposure\_histogram\_max\_ev100

```python
@exposure_histogram_max_ev100.setter
def exposure_histogram_max_ev100(value: float) -> None
```

<a id="unreal.SkyCreator.on_lightning_strike"></a>

#### on\_lightning\_strike

```python
@property
def on_lightning_strike() -> OnLightningStrike
```

(OnLightningStrike):  [Read-Write]

<a id="unreal.SkyCreator.on_lightning_strike"></a>

#### on\_lightning\_strike

```python
@on_lightning_strike.setter
def on_lightning_strike(value: OnLightningStrike) -> None
```

<a id="unreal.SkyCreator.spawn_lightning_strike"></a>

#### spawn\_lightning\_strike

```python
def spawn_lightning_strike(lightning_position: Vector) -> None
```

x.spawn_lightning_strike(lightning_position) -> None
Spawn Lightning Strike

Args:
    lightning_position (Vector):

<a id="unreal.SkyCreator.set_wind_settings"></a>

#### set\_wind\_settings

```python
def set_wind_settings(wind_settings: SkyCreatorWindSettings) -> None
```

x.set_wind_settings(wind_settings) -> None
Set Wind Settings

Args:
    wind_settings (SkyCreatorWindSettings):

<a id="unreal.SkyCreator.set_wind_independent_settings"></a>

#### set\_wind\_independent\_settings

```python
def set_wind_independent_settings(
        wind_settings: SkyCreatorWindSettings) -> None
```

x.set_wind_independent_settings(wind_settings) -> None
Set Wind Independent Settings

Args:
    wind_settings (SkyCreatorWindSettings):

<a id="unreal.SkyCreator.set_weather_settings"></a>

#### set\_weather\_settings

```python
def set_weather_settings(weather_settings: SkyCreatorWeatherSettings) -> None
```

x.set_weather_settings(weather_settings) -> None
Set Weather Settings

Args:
    weather_settings (SkyCreatorWeatherSettings):

<a id="unreal.SkyCreator.set_weather_material_fx_settings"></a>

#### set\_weather\_material\_fx\_settings

```python
def set_weather_material_fx_settings(
        weather_material_fx_settings: SkyCreatorWeatherMaterialFXSettings
) -> None
```

x.set_weather_material_fx_settings(weather_material_fx_settings) -> None
Set Weather Material FXSettings

Args:
    weather_material_fx_settings (SkyCreatorWeatherMaterialFXSettings):

<a id="unreal.SkyCreator.set_weather_fx_settings"></a>

#### set\_weather\_fx\_settings

```python
def set_weather_fx_settings(
        weather_fx_settings: SkyCreatorWeatherFXSettings) -> None
```

x.set_weather_fx_settings(weather_fx_settings) -> None
Set Weather FXSettings

Args:
    weather_fx_settings (SkyCreatorWeatherFXSettings):

<a id="unreal.SkyCreator.set_volumetric_cloud_settings"></a>

#### set\_volumetric\_cloud\_settings

```python
def set_volumetric_cloud_settings(
        volumetric_cloud_settings: SkyCreatorVolumetricCloudSettings) -> None
```

x.set_volumetric_cloud_settings(volumetric_cloud_settings) -> None
Set Volumetric Cloud Settings

Args:
    volumetric_cloud_settings (SkyCreatorVolumetricCloudSettings):

<a id="unreal.SkyCreator.set_time"></a>

#### set\_time

```python
def set_time(time: float) -> None
```

x.set_time(time) -> None
Set Time

Args:
    time (float):

<a id="unreal.SkyCreator.set_sun_simple_position_settings"></a>

#### set\_sun\_simple\_position\_settings

```python
def set_sun_simple_position_settings(sunrise_time: float = 6.500000,
                                     sunset_time: float = 19.500000,
                                     sun_elevation: float = 55.000000,
                                     sun_azimuth: float = 270.000000) -> None
```

x.set_sun_simple_position_settings(sunrise_time=6.500000, sunset_time=19.500000, sun_elevation=55.000000, sun_azimuth=270.000000) -> None
Set Sun Simple Position Settings

Args:
    sunrise_time (float): 
    sunset_time (float): 
    sun_elevation (float): 
    sun_azimuth (float):

<a id="unreal.SkyCreator.set_sun_light_settings"></a>

#### set\_sun\_light\_settings

```python
def set_sun_light_settings(
        sun_light_settings: SkyCreatorSunLightSettings) -> None
```

x.set_sun_light_settings(sun_light_settings) -> None
Set Sun Light Settings

Args:
    sun_light_settings (SkyCreatorSunLightSettings):

<a id="unreal.SkyCreator.set_star_map_settings"></a>

#### set\_star\_map\_settings

```python
def set_star_map_settings(
        star_map_settings: SkyCreatorStarMapSettings) -> None
```

x.set_star_map_settings(star_map_settings) -> None
Set Star Map Settings

Args:
    star_map_settings (SkyCreatorStarMapSettings):

<a id="unreal.SkyCreator.set_sky_light_settings"></a>

#### set\_sky\_light\_settings

```python
def set_sky_light_settings(
        sky_light_settings: SkyCreatorSkyLightSettings) -> None
```

x.set_sky_light_settings(sky_light_settings) -> None
Set Sky Light Settings

Args:
    sky_light_settings (SkyCreatorSkyLightSettings):

<a id="unreal.SkyCreator.set_sky_atmosphere_settings"></a>

#### set\_sky\_atmosphere\_settings

```python
def set_sky_atmosphere_settings(
        sky_atmosphere_settings: SkyCreatorSkyAtmosphereSettings) -> None
```

x.set_sky_atmosphere_settings(sky_atmosphere_settings) -> None
Set Sky Atmosphere Settings

Args:
    sky_atmosphere_settings (SkyCreatorSkyAtmosphereSettings):

<a id="unreal.SkyCreator.set_real_position_settings"></a>

#### set\_real\_position\_settings

```python
def set_real_position_settings(latitude: float = 51.509865,
                               longitude: float = -0.118092,
                               time_zone: float = 0.000000,
                               inb_daylight_saving_time: bool = False,
                               year: int = 2022,
                               month: int = 5,
                               day: int = 10) -> None
```

x.set_real_position_settings(latitude=51.509865, longitude=-0.118092, time_zone=0.000000, inb_daylight_saving_time=False, year=2022, month=5, day=10) -> None
Set Real Position Settings

Args:
    latitude (float): 
    longitude (float): 
    time_zone (float): 
    inb_daylight_saving_time (bool): 
    year (int32): 
    month (int32): 
    day (int32):

<a id="unreal.SkyCreator.set_post_process_settings"></a>

#### set\_post\_process\_settings

```python
def set_post_process_settings(
        post_process_settings: SkyCreatorPostProcessSettings) -> None
```

x.set_post_process_settings(post_process_settings) -> None
Set Post Process Settings

Args:
    post_process_settings (SkyCreatorPostProcessSettings):

<a id="unreal.SkyCreator.set_moon_simple_position_settings"></a>

#### set\_moon\_simple\_position\_settings

```python
def set_moon_simple_position_settings(
        moonrise_time: float = 18.000000,
        moonset_time: float = 8.000000,
        moon_elevation: float = 45.000000,
        moon_azimuth: float = 270.000000) -> None
```

x.set_moon_simple_position_settings(moonrise_time=18.000000, moonset_time=8.000000, moon_elevation=45.000000, moon_azimuth=270.000000) -> None
Set Moon Simple Position Settings

Args:
    moonrise_time (float): 
    moonset_time (float): 
    moon_elevation (float): 
    moon_azimuth (float):

<a id="unreal.SkyCreator.set_moon_phase"></a>

#### set\_moon\_phase

```python
def set_moon_phase(new_value: float) -> None
```

x.set_moon_phase(new_value) -> None
Set Moon Phase

Args:
    new_value (float):

<a id="unreal.SkyCreator.set_moon_light_settings"></a>

#### set\_moon\_light\_settings

```python
def set_moon_light_settings(
        moon_light_settings: SkyCreatorMoonLightSettings) -> None
```

x.set_moon_light_settings(moon_light_settings) -> None
Set Moon Light Settings

Args:
    moon_light_settings (SkyCreatorMoonLightSettings):

<a id="unreal.SkyCreator.set_exponential_height_fog_settings"></a>

#### set\_exponential\_height\_fog\_settings

```python
def set_exponential_height_fog_settings(
    exponential_height_fog_settings: SkyCreatorExponentialHeightFogSettings
) -> None
```

x.set_exponential_height_fog_settings(exponential_height_fog_settings) -> None
Set Exponential Height Fog Settings

Args:
    exponential_height_fog_settings (SkyCreatorExponentialHeightFogSettings):

<a id="unreal.SkyCreator.set_background_cloud_settings"></a>

#### set\_background\_cloud\_settings

```python
def set_background_cloud_settings(
        background_cloud_settings: SkyCreatorBackgroundCloudSettings) -> None
```

x.set_background_cloud_settings(background_cloud_settings) -> None
Set Background Cloud Settings

Args:
    background_cloud_settings (SkyCreatorBackgroundCloudSettings):

<a id="unreal.SkyCreator.realtime_time_of_day"></a>

#### realtime\_time\_of\_day

```python
def realtime_time_of_day(delta_seconds: float,
                         day_cycle_duration: float) -> None
```

x.realtime_time_of_day(delta_seconds, day_cycle_duration) -> None
Realtime Time Of Day

Args:
    delta_seconds (float): 
    day_cycle_duration (float):

<a id="unreal.SkyCreator.lerp_wind_settings"></a>

#### lerp\_wind\_settings

```python
def lerp_wind_settings(wind_settings_a: SkyCreatorWindSettings,
                       wind_settings_b: SkyCreatorWindSettings,
                       alpha: float) -> None
```

x.lerp_wind_settings(wind_settings_a, wind_settings_b, alpha) -> None
Lerp Wind Settings

Args:
    wind_settings_a (SkyCreatorWindSettings): 
    wind_settings_b (SkyCreatorWindSettings): 
    alpha (float):

<a id="unreal.SkyCreator.lerp_wind_independent_settings"></a>

#### lerp\_wind\_independent\_settings

```python
def lerp_wind_independent_settings(wind_settings_a: SkyCreatorWindSettings,
                                   wind_settings_b: SkyCreatorWindSettings,
                                   alpha: float) -> None
```

x.lerp_wind_independent_settings(wind_settings_a, wind_settings_b, alpha) -> None
Lerp Wind Independent Settings

Args:
    wind_settings_a (SkyCreatorWindSettings): 
    wind_settings_b (SkyCreatorWindSettings): 
    alpha (float):

<a id="unreal.SkyCreator.lerp_wetness_amount"></a>

#### lerp\_wetness\_amount

```python
def lerp_wetness_amount(wetness_amount_a: float, wetness_amount_b: float,
                        alpha: float) -> None
```

x.lerp_wetness_amount(wetness_amount_a, wetness_amount_b, alpha) -> None
Lerp Wetness Amount

Args:
    wetness_amount_a (float): 
    wetness_amount_b (float): 
    alpha (float):

<a id="unreal.SkyCreator.lerp_weather_settings"></a>

#### lerp\_weather\_settings

```python
def lerp_weather_settings(weather_settings_a: SkyCreatorWeatherSettings,
                          weather_settings_b: SkyCreatorWeatherSettings,
                          alpha: float) -> None
```

x.lerp_weather_settings(weather_settings_a, weather_settings_b, alpha) -> None
Lerp Weather Settings

Args:
    weather_settings_a (SkyCreatorWeatherSettings): 
    weather_settings_b (SkyCreatorWeatherSettings): 
    alpha (float):

<a id="unreal.SkyCreator.lerp_weather_material_fx_settings"></a>

#### lerp\_weather\_material\_fx\_settings

```python
def lerp_weather_material_fx_settings(
        weather_material_fx_settings_a: SkyCreatorWeatherMaterialFXSettings,
        weather_material_fx_settings_b: SkyCreatorWeatherMaterialFXSettings,
        alpha: float) -> None
```

x.lerp_weather_material_fx_settings(weather_material_fx_settings_a, weather_material_fx_settings_b, alpha) -> None
Lerp Weather Material FXSettings

Args:
    weather_material_fx_settings_a (SkyCreatorWeatherMaterialFXSettings): 
    weather_material_fx_settings_b (SkyCreatorWeatherMaterialFXSettings): 
    alpha (float):

<a id="unreal.SkyCreator.lerp_weather_fx_settings"></a>

#### lerp\_weather\_fx\_settings

```python
def lerp_weather_fx_settings(
        weather_fx_settings_a: SkyCreatorWeatherFXSettings,
        weather_fx_settings_b: SkyCreatorWeatherFXSettings,
        alpha: float) -> None
```

x.lerp_weather_fx_settings(weather_fx_settings_a, weather_fx_settings_b, alpha) -> None
Lerp Weather FXSettings

Args:
    weather_fx_settings_a (SkyCreatorWeatherFXSettings): 
    weather_fx_settings_b (SkyCreatorWeatherFXSettings): 
    alpha (float):

<a id="unreal.SkyCreator.lerp_volumetric_cloud_settings"></a>

#### lerp\_volumetric\_cloud\_settings

```python
def lerp_volumetric_cloud_settings(
        volumetric_cloud_settings_a: SkyCreatorVolumetricCloudSettings,
        volumetric_cloud_settings_b: SkyCreatorVolumetricCloudSettings,
        alpha: float) -> None
```

x.lerp_volumetric_cloud_settings(volumetric_cloud_settings_a, volumetric_cloud_settings_b, alpha) -> None
Lerp Volumetric Cloud Settings

Args:
    volumetric_cloud_settings_a (SkyCreatorVolumetricCloudSettings): 
    volumetric_cloud_settings_b (SkyCreatorVolumetricCloudSettings): 
    alpha (float):

<a id="unreal.SkyCreator.lerp_sun_light_settings"></a>

#### lerp\_sun\_light\_settings

```python
def lerp_sun_light_settings(sun_light_settings_a: SkyCreatorSunLightSettings,
                            sun_light_settings_b: SkyCreatorSunLightSettings,
                            alpha: float) -> None
```

x.lerp_sun_light_settings(sun_light_settings_a, sun_light_settings_b, alpha) -> None
Lerp Sun Light Settings

Args:
    sun_light_settings_a (SkyCreatorSunLightSettings): 
    sun_light_settings_b (SkyCreatorSunLightSettings): 
    alpha (float):

<a id="unreal.SkyCreator.lerp_star_map_settings"></a>

#### lerp\_star\_map\_settings

```python
def lerp_star_map_settings(star_map_settings_a: SkyCreatorStarMapSettings,
                           star_map_settings_b: SkyCreatorStarMapSettings,
                           alpha: float) -> None
```

x.lerp_star_map_settings(star_map_settings_a, star_map_settings_b, alpha) -> None
Lerp Star Map Settings

Args:
    star_map_settings_a (SkyCreatorStarMapSettings): 
    star_map_settings_b (SkyCreatorStarMapSettings): 
    alpha (float):

<a id="unreal.SkyCreator.lerp_snow_amount"></a>

#### lerp\_snow\_amount

```python
def lerp_snow_amount(snow_amount_a: float, snow_amount_b: float,
                     alpha: float) -> None
```

x.lerp_snow_amount(snow_amount_a, snow_amount_b, alpha) -> None
Lerp Snow Amount

Args:
    snow_amount_a (float): 
    snow_amount_b (float): 
    alpha (float):

<a id="unreal.SkyCreator.lerp_sky_light_settings"></a>

#### lerp\_sky\_light\_settings

```python
def lerp_sky_light_settings(sky_light_settings_a: SkyCreatorSkyLightSettings,
                            sky_light_settings_b: SkyCreatorSkyLightSettings,
                            alpha: float) -> None
```

x.lerp_sky_light_settings(sky_light_settings_a, sky_light_settings_b, alpha) -> None
Lerp Sky Light Settings

Args:
    sky_light_settings_a (SkyCreatorSkyLightSettings): 
    sky_light_settings_b (SkyCreatorSkyLightSettings): 
    alpha (float):

<a id="unreal.SkyCreator.lerp_sky_atmosphere_settings"></a>

#### lerp\_sky\_atmosphere\_settings

```python
def lerp_sky_atmosphere_settings(
        sky_atmosphere_settings_a: SkyCreatorSkyAtmosphereSettings,
        sky_atmosphere_settings_b: SkyCreatorSkyAtmosphereSettings,
        alpha: float) -> None
```

x.lerp_sky_atmosphere_settings(sky_atmosphere_settings_a, sky_atmosphere_settings_b, alpha) -> None
Lerp Sky Atmosphere Settings

Args:
    sky_atmosphere_settings_a (SkyCreatorSkyAtmosphereSettings): 
    sky_atmosphere_settings_b (SkyCreatorSkyAtmosphereSettings): 
    alpha (float):

<a id="unreal.SkyCreator.lerp_puddles_amount"></a>

#### lerp\_puddles\_amount

```python
def lerp_puddles_amount(puddles_amount_a: float, puddles_amount_b: float,
                        alpha: float) -> None
```

x.lerp_puddles_amount(puddles_amount_a, puddles_amount_b, alpha) -> None
Lerp Puddles Amount

Args:
    puddles_amount_a (float): 
    puddles_amount_b (float): 
    alpha (float):

<a id="unreal.SkyCreator.lerp_post_process_settings"></a>

#### lerp\_post\_process\_settings

```python
def lerp_post_process_settings(
        post_process_settings_a: SkyCreatorPostProcessSettings,
        post_process_settings_b: SkyCreatorPostProcessSettings,
        alpha: float) -> None
```

x.lerp_post_process_settings(post_process_settings_a, post_process_settings_b, alpha) -> None
Lerp Post Process Settings

Args:
    post_process_settings_a (SkyCreatorPostProcessSettings): 
    post_process_settings_b (SkyCreatorPostProcessSettings): 
    alpha (float):

<a id="unreal.SkyCreator.lerp_moon_light_settings"></a>

#### lerp\_moon\_light\_settings

```python
def lerp_moon_light_settings(
        moon_light_settings_a: SkyCreatorMoonLightSettings,
        moon_light_settings_b: SkyCreatorMoonLightSettings,
        alpha: float) -> None
```

x.lerp_moon_light_settings(moon_light_settings_a, moon_light_settings_b, alpha) -> None
Lerp Moon Light Settings

Args:
    moon_light_settings_a (SkyCreatorMoonLightSettings): 
    moon_light_settings_b (SkyCreatorMoonLightSettings): 
    alpha (float):

<a id="unreal.SkyCreator.lerp_exponential_height_fog_settings"></a>

#### lerp\_exponential\_height\_fog\_settings

```python
def lerp_exponential_height_fog_settings(
        exponential_height_fog_settings_a:
    SkyCreatorExponentialHeightFogSettings, exponential_height_fog_settings_b:
    SkyCreatorExponentialHeightFogSettings, alpha: float) -> None
```

x.lerp_exponential_height_fog_settings(exponential_height_fog_settings_a, exponential_height_fog_settings_b, alpha) -> None
Lerp Exponential Height Fog Settings

Args:
    exponential_height_fog_settings_a (SkyCreatorExponentialHeightFogSettings): 
    exponential_height_fog_settings_b (SkyCreatorExponentialHeightFogSettings): 
    alpha (float):

<a id="unreal.SkyCreator.lerp_background_cloud_settings"></a>

#### lerp\_background\_cloud\_settings

```python
def lerp_background_cloud_settings(
        background_cloud_settings_a: SkyCreatorBackgroundCloudSettings,
        background_cloud_settings_b: SkyCreatorBackgroundCloudSettings,
        alpha: float) -> None
```

x.lerp_background_cloud_settings(background_cloud_settings_a, background_cloud_settings_b, alpha) -> None
Lerp Background Cloud Settings

Args:
    background_cloud_settings_a (SkyCreatorBackgroundCloudSettings): 
    background_cloud_settings_b (SkyCreatorBackgroundCloudSettings): 
    alpha (float):

<a id="unreal.SkyCreator.get_wind_settings"></a>

#### get\_wind\_settings

```python
def get_wind_settings() -> SkyCreatorWindSettings
```

x.get_wind_settings() -> SkyCreatorWindSettings
Get Wind Settings

Returns:
    SkyCreatorWindSettings:

<a id="unreal.SkyCreator.get_weather_settings"></a>

#### get\_weather\_settings

```python
def get_weather_settings() -> SkyCreatorWeatherSettings
```

x.get_weather_settings() -> SkyCreatorWeatherSettings
Get Weather Settings

Returns:
    SkyCreatorWeatherSettings:

<a id="unreal.SkyCreator.get_weather_material_fx_settings"></a>

#### get\_weather\_material\_fx\_settings

```python
def get_weather_material_fx_settings() -> SkyCreatorWeatherMaterialFXSettings
```

x.get_weather_material_fx_settings() -> SkyCreatorWeatherMaterialFXSettings
Get Weather Material FXSettings

Returns:
    SkyCreatorWeatherMaterialFXSettings:

<a id="unreal.SkyCreator.get_weather_fx_settings"></a>

#### get\_weather\_fx\_settings

```python
def get_weather_fx_settings() -> SkyCreatorWeatherFXSettings
```

x.get_weather_fx_settings() -> SkyCreatorWeatherFXSettings
Get Weather FXSettings

Returns:
    SkyCreatorWeatherFXSettings:

<a id="unreal.SkyCreator.get_volumetric_cloud_settings"></a>

#### get\_volumetric\_cloud\_settings

```python
def get_volumetric_cloud_settings() -> SkyCreatorVolumetricCloudSettings
```

x.get_volumetric_cloud_settings() -> SkyCreatorVolumetricCloudSettings
Get Volumetric Cloud Settings

Returns:
    SkyCreatorVolumetricCloudSettings:

<a id="unreal.SkyCreator.get_time"></a>

#### get\_time

```python
def get_time() -> float
```

x.get_time() -> float
Get Time

Returns:
    float:

<a id="unreal.SkyCreator.get_sun_light_settings"></a>

#### get\_sun\_light\_settings

```python
def get_sun_light_settings() -> SkyCreatorSunLightSettings
```

x.get_sun_light_settings() -> SkyCreatorSunLightSettings
Get Sun Light Settings

Returns:
    SkyCreatorSunLightSettings:

<a id="unreal.SkyCreator.get_star_map_settings"></a>

#### get\_star\_map\_settings

```python
def get_star_map_settings() -> SkyCreatorStarMapSettings
```

x.get_star_map_settings() -> SkyCreatorStarMapSettings
Get Star Map Settings

Returns:
    SkyCreatorStarMapSettings:

<a id="unreal.SkyCreator.get_sky_light_settings"></a>

#### get\_sky\_light\_settings

```python
def get_sky_light_settings() -> SkyCreatorSkyLightSettings
```

x.get_sky_light_settings() -> SkyCreatorSkyLightSettings
Get Sky Light Settings

Returns:
    SkyCreatorSkyLightSettings:

<a id="unreal.SkyCreator.get_sky_atmosphere_settings"></a>

#### get\_sky\_atmosphere\_settings

```python
def get_sky_atmosphere_settings() -> SkyCreatorSkyAtmosphereSettings
```

x.get_sky_atmosphere_settings() -> SkyCreatorSkyAtmosphereSettings
Get Sky Atmosphere Settings

Returns:
    SkyCreatorSkyAtmosphereSettings:

<a id="unreal.SkyCreator.get_post_process_settings"></a>

#### get\_post\_process\_settings

```python
def get_post_process_settings() -> SkyCreatorPostProcessSettings
```

x.get_post_process_settings() -> SkyCreatorPostProcessSettings
Get Post Process Settings

Returns:
    SkyCreatorPostProcessSettings:

<a id="unreal.SkyCreator.get_moon_phase"></a>

#### get\_moon\_phase

```python
def get_moon_phase() -> float
```

x.get_moon_phase() -> float
UFUNCTION(BlueprintCallable, Category = "Sky Creator|Moon")
void SetMoonPhase(float InMoonPhase);

Returns:
    float:

<a id="unreal.SkyCreator.get_moon_light_settings"></a>

#### get\_moon\_light\_settings

```python
def get_moon_light_settings() -> SkyCreatorMoonLightSettings
```

x.get_moon_light_settings() -> SkyCreatorMoonLightSettings
Get Moon Light Settings

Returns:
    SkyCreatorMoonLightSettings:

<a id="unreal.SkyCreator.get_last_lightning_position"></a>

#### get\_last\_lightning\_position

```python
def get_last_lightning_position() -> Vector
```

x.get_last_lightning_position() -> Vector
Get Last Lightning Position

Returns:
    Vector:

<a id="unreal.SkyCreator.get_exponential_height_fog_settings"></a>

#### get\_exponential\_height\_fog\_settings

```python
def get_exponential_height_fog_settings(
) -> SkyCreatorExponentialHeightFogSettings
```

x.get_exponential_height_fog_settings() -> SkyCreatorExponentialHeightFogSettings
Get Exponential Height Fog Settings

Returns:
    SkyCreatorExponentialHeightFogSettings:

<a id="unreal.SkyCreator.get_cloud_density_at_position"></a>

#### get\_cloud\_density\_at\_position

```python
def get_cloud_density_at_position(position: Vector) -> float
```

x.get_cloud_density_at_position(position) -> float
Get Cloud Density at Position

Args:
    position (Vector): 

Returns:
    float:

<a id="unreal.SkyCreator.get_background_cloud_settings"></a>

#### get\_background\_cloud\_settings

```python
def get_background_cloud_settings() -> SkyCreatorBackgroundCloudSettings
```

x.get_background_cloud_settings() -> SkyCreatorBackgroundCloudSettings
Get Background Cloud Settings

Returns:
    SkyCreatorBackgroundCloudSettings:

<a id="unreal.SkyCreator.find_lightning_position"></a>

#### find\_lightning\_position

```python
def find_lightning_position(position: Vector) -> Optional[Vector]
```

x.find_lightning_position(position) -> Vector or None
Find Lightning Position

Args:
    position (Vector): 

Returns:
    Vector or None: 

    out_position (Vector):

<a id="unreal.SkyCreator.editor_tick"></a>

#### editor\_tick

```python
def editor_tick(delta_time: float) -> None
```

x.editor_tick(delta_time) -> None
Editor Tick

Args:
    delta_time (float):

<a id="unreal.SkyCreatorFunctionLibrary"></a>