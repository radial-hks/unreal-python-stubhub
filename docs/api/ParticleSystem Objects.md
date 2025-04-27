## ParticleSystem Objects

```python
class ParticleSystem(FXSystemAsset)
```

A ParticleSystem is a complete particle effect that contains any number of ParticleEmitters. By allowing multiple emitters
in a system, the designer can create elaborate particle effects that are held in a single system. Once created using
Cascade, a ParticleSystem can then be inserted into a level or created in script.

**C++ Source:**

- **Module**: Engine
- **File**: ParticleSystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_managed_ticking`` (bool):  [Read-Write] Whether or not to allow instances of this system to have their ticks managed.
- ``auto_deactivate`` (bool):  [Read-Write] Auto-deactivate system if all emitters are determined to not spawn particles again, regardless of lifetime.
- ``custom_occlusion_bounds`` (Box):  [Read-Write] The occlusion bounds to use if OcclusionBoundsMethod is set to EPSOBM_CustomBounds
- ``delay`` (float):  [Read-Write] How long this Particle system should delay when ActivateSystem is called on it.
- ``delay_low`` (float):  [Read-Write] The low end of the emitter delay if using a range.
- ``fixed_relative_bounding_box`` (Box):  [Read-Write] Fixed relative bounding box for particle system.
- ``insignificance_delay`` (float):  [Read-Write] Time delay between all emitters becoming insignificant and the systems insignificant reaction.
- ``insignificant_reaction`` (ParticleSystemInsignificanceReaction):  [Read-Write] The reaction this system takes when all emitters are insignificant.
- ``lod_distance_check_time`` (float):  [Read-Write] How often (in seconds) the system should perform the LOD distance check.
- ``lod_distances`` (Array[float]):  [Read-Write] The array of distances for each LOD level in the system.
  Used when LODMethod is set to PARTICLESYSTEMLODMETHOD_Automatic.

  Example: System with 3 LOD levels
          LODDistances(0) = 0.0
          LODDistances(1) = 2500.0
          LODDistances(2) = 5000.0

          In this case, when the system is [   0.0 ..   2499.9] from the camera, LOD level 0 will be used.
                                                                           [2500.0 ..   4999.9] from the camera, LOD level 1 will be used.
                                                                           [5000.0 .. INFINITY] from the camera, LOD level 2 will be used.
- ``lod_method`` (ParticleSystemLODMethod):  [Read-Write] The method of LOD level determination to utilize for this particle system
    PARTICLESYSTEMLODMETHOD_Automatic - Automatically set the LOD level, checking every LODDistanceCheckTime seconds.
  PARTICLESYSTEMLODMETHOD_DirectSet - LOD level is directly set by the game code.
  PARTICLESYSTEMLODMETHOD_ActivateAutomatic - LOD level is determined at Activation time, then left alone unless directly set by game code.
- ``lod_settings`` (Array[ParticleSystemLOD]):  [Read-Write]
- ``macro_uv_position`` (Vector):  [Read-Write] Local space position that UVs generated with the ParticleMacroUV material node will be centered on.
- ``macro_uv_radius`` (float):  [Read-Write] World space radius that UVs generated with the ParticleMacroUV material node will tile based on.
- ``max_pool_size`` (uint32):  [Read-Write] Max number of components of this system to keep resident in the world component pool.
- ``max_significance_level`` (ParticleSignificanceLevel):  [Read-Write] The maximum level of significance for emitters in this system. Any emitters with a higher significance will be capped at this significance level.
- ``min_time_between_ticks`` (uint32):  [Read-Write] Minimum duration between ticks; 33=tick at max. 30FPS, 16=60FPS, 8=120FPS
- ``named_material_slots`` (Array[NamedEmitterMaterial]):  [Read-Write] Array of named material slots for use by emitters of this system.
  Emitters can use these instead of their own materials by providing the name to the NamedMaterialOverrides property of their required module.
  These materials can be overridden using CreateNamedDynamicMaterialInstance() on a ParticleSystemComponent.
- ``occlusion_bounds_method`` (ParticleSystemOcclusionBoundsMethod):  [Read-Write] Which occlusion bounds method to use for this particle system.
  EPSOBM_None - Don't determine occlusion for this system.
  EPSOBM_ParticleBounds - Use the bounds of the component when determining occlusion.
- ``orient_z_axis_toward_camera`` (bool):  [Read-Write] If true, the system's Z axis will be oriented toward the camera
- ``pool_prime_size`` (uint32):  [Read-Write] How many instances we should use to initially prime the pool.
  This can amortize runtime activation cost by moving it to load time.
  Use with care as this could cause large hitches for systems loaded/unloaded during play rather than at level load.
- ``seconds_before_inactive`` (float):  [Read-Write] Number of seconds of emitter not being rendered that need to pass before it
  no longer gets ticked/ becomes inactive.
- ``system_update_mode`` (ParticleSystemUpdateMode):  [Read-Write]
- ``thumbnail_warmup`` (float):  [Read-Write] The time to warm-up the system for the thumbnail image
- ``update_time_fps`` (float):  [Read-Write] UpdateTime_FPS - the frame per second to update at in FixedTime mode
- ``use_delay_range`` (bool):  [Read-Write] If true, select the emitter delay from the range
          [DelayLow..Delay]
- ``use_fixed_relative_bounding_box`` (bool):  [Read-Write] Whether to use the fixed relative bounding box or calculate it every frame.
- ``use_realtime_thumbnail`` (bool):  [Read-Write] Inidicates the old 'real-time' thumbnail rendering should be used
- ``warmup_tick_rate`` (float):  [Read-Write] WarmupTickRate - the time step for each tick during warm up.
         Increasing this improves performance. Decreasing, improves accuracy.
         Set to 0 to use the default tick time.
- ``warmup_time`` (float):  [Read-Write] WarmupTime - the time to warm-up the particle system when first rendered
  Warning: WarmupTime is implemented by simulating the particle system for the time requested upon activation.
  This is extremely prone to cause hitches, especially with large particle counts - use with caution.

<a id="unreal.ParticleSystem.contains_emitter_type"></a>

#### contains_emitter_type

```python
def contains_emitter_type(type_data: Class) -> bool
```

x.contains_emitter_type(type_data) -> bool
Returns true if this system contains an emitter of the pasesd type.

Args:
    type_data (type(Class)): The emitter type to check for. Must be a child class of UParticleModuleTypeDataBase

Returns:
    bool:

<a id="unreal.ParticleModule"></a>