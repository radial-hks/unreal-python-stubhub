## NiagaraSystem Objects

```python
class NiagaraSystem(FXSystemAsset)
```

A Niagara System contains multiple Niagara Emitters to create various effects.
Niagara Systems can be placed in the world, unlike Emitters, and expose User Parameters to configure an effect at runtime.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraSystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_culling_for_local_players_override`` (bool):  [Read-Write] The override value for bAllowCullingForLocalPlayers from the Effect Type.
- ``allow_system_state_fast_path`` (bool):  [Read-Write] When enabled if all emitters don't require script execution and the system script is empty / constant we can invoke a faster CPU path.
- ``bake_out_rapid_iteration`` (bool):  [Read-Write] When enable constant values are baked into the scripts while editing the system, this will increase iteration times but improve performance.
- ``bake_out_rapid_iteration_on_cook`` (bool):  [Read-Write] When enabled constant values are baked into scripts to improve performance.
- ``cast_shadow`` (bool):  [Read-Write] When enabled this is the default value set on the component.
  Controls whether the primitive component should cast a shadow or not.
- ``compress_attributes`` (bool):  [Read-Write] Toggles whether or not emitters within this system will try and compress their particle attributes.
        In some cases, this precision change can lead to perceivable differences, but memory costs and or performance (especially true for GPU emitters) can improve.
- ``custom_depth_stencil_value`` (int32):  [Read-Write] When enabled this is the default value set on the component.
  Optionally write this 0-255 value to the stencil buffer in CustomDepth pass (Requires project setting or r.CustomDepth == 3)
- ``custom_depth_stencil_write_mask`` (RendererStencilMask):  [Read-Write] When enabled this is the default value set on the component.
  Mask used for stencil buffer writes.
- ``determinism`` (bool):  [Read-Write] When disabled we will generate a RandomSeed per instance on reset which is not deterministic.
  When enabled we will always use the RandomSeed from the system plus the components RandomSeedOffset, this allows for determinism but variance between components.
- ``disable_debug_switches`` (bool):  [Read-Write] When enable debug switches are disabled while editing the system.
- ``disable_debug_switches_on_cook`` (bool):  [Read-Write] When enabled debug switches are disabled when compiling the system.
- ``disable_experimental_vm`` (bool):  [Read-Write] If true, disables optimized VM, if available
- ``dump_debug_emitter_info`` (bool):  [Read-Write]
- ``dump_debug_system_info`` (bool):  [Read-Write]
- ``effect_type`` (NiagaraEffectType):  [Read-Write] An effect types defines settings shared between systems, for example scalability and validation rules.
  Things like environment fx usually have a different effect type than gameplay relevant fx such as weapon impacts.
  This way whole classes of effects can be adjusted at once.
- ``fixed_bounds`` (bool):  [Read-Write] Whether or not fixed bounds are enabled.
- ``fixed_bounds`` (Box):  [Read-Write] The fixed bounding box value for the whole system. When placed in the level and the bounding box is not visible to the camera, the effect is culled from rendering.
- ``fixed_tick_delta`` (bool):  [Read-Write]
- ``fixed_tick_delta_time`` (float):  [Read-Write] If activated, the system ticks with a fixed delta time instead of the varying game thread delta time. This leads to much more stable simulations.
  When the fixed tick delta is smaller than the game thread tick time the simulation is substepping by executing multiple ticks per frame.
  Note that activating this feature forces the system to tick on the game thread instead of an async task in parallel.

  The max number of substeps per frame can be set via fx.Niagara.SystemSimulation.MaxTickSubsteps
- ``ignore_particle_reads_for_attribute_trim`` (bool):  [Read-Write] If true ParticleReads will not absolutely prevent attribute trimming - User must ensure that the appropriate attributes are preserved on the source emitter!
- ``initial_owner_velocity_from_actor`` (bool):  [Read-Write] When enabled we use the owner actor's velocity for the first frame.
  If we do not have an owner actor, or this is disable then the first frame's velocity will be zero.
- ``max_pool_size`` (uint32):  [Read-Write] Max number of components of this system to keep resident in the world component pool.
- ``override_allow_culling_for_local_players`` (bool):  [Read-Write] Controls whether we should override the Effect Type value for bAllowCullingForLocalPlayers.
- ``override_cast_shadow`` (bool):  [Read-Write] Various optional overrides for component properties when spawning a system
- ``override_custom_depth_stencil_value`` (bool):  [Read-Write]
- ``override_custom_depth_stencil_write_mask`` (bool):  [Read-Write]
- ``override_receives_decals`` (bool):  [Read-Write]
- ``override_render_custom_depth`` (bool):  [Read-Write]
- ``override_scalability_settings`` (bool):  [Read-Write]
- ``override_translucency_sort_distance_offset`` (bool):  [Read-Write]
- ``override_translucency_sort_priority`` (bool):  [Read-Write]
- ``parameter_collection_overrides`` (Array[NiagaraParameterCollectionInstance]):  [Read-Write]
- ``platforms`` (NiagaraPlatformSet):  [Read-Write]
- ``pool_prime_size`` (uint32):  [Read-Write] How many instances we should use to initially prime the pool.
  This can amortize runtime activation cost by moving it to load time.
  Use with care as this could cause large hitches for systems loaded/unloaded during play rather than at level load.
- ``random_seed`` (int32):  [Read-Write] Seed used for system script random number generator.
- ``receives_decals`` (bool):  [Read-Write] When enabled this is the default value set on the component.
  Whether the primitive receives decals.
- ``render_custom_depth`` (bool):  [Read-Write] When enabled this is the default value set on the component.
  This primitive has bRenderCustomDepth enabled.
- ``require_current_frame_data`` (bool):  [Read-Write] When enabled, we follow the settings on the UNiagaraComponent for tick order. When this option is disabled, we ignore any dependencies from data interfaces or other variables and instead fire off the simulation as early in the frame as possible. This greatly
        reduces overhead and allows the game thread to run faster, but comes at a tradeoff if the dependencies might leave gaps or other visual artifacts.
- ``support_large_world_coordinates`` (bool):  [Read-Write] If true then position type values will be rebased on system activation to fit into a float precision vector. This needs to be turned off when using a custom data interface or renderer that does not support the rebasing.
- ``system_scalability_overrides`` (NiagaraSystemScalabilityOverrides):  [Read-Write]
- ``template_asset_description`` (Text):  [Read-Write]
- ``translucency_sort_distance_offset`` (float):  [Read-Write] When enabled this is the default value set on the component.
  Modifies the sort distance for translucent objects, see PrimitiveComponent description for more details.
- ``translucency_sort_priority`` (int32):  [Read-Write] When enabled this is the default value set on the component.
  Adjusts the translucent object sorting priority, see PrimitiveComponent description for more details.
- ``trim_attributes`` (bool):  [Read-Write] When enabled we trim particle attributes while editing the system.
- ``trim_attributes_on_cook`` (bool):  [Read-Write] If true Particle attributes will be removed from the DataSet if they are unnecessary (are never read by ParameterMap)
- ``warmup_tick_count`` (int32):  [Read-Write] Number of ticks to process for warmup. You can set by this or by time via WarmupTime.
- ``warmup_tick_delta`` (float):  [Read-Write] Delta time to use for warmup ticks.
- ``warmup_time`` (float):  [Read-Write] Warm up time in seconds. Used to calculate WarmupTickCount. Rounds down to the nearest multiple of WarmupTickDelta.

<a id="unreal.NiagaraSystem.cast_shadow"></a>

#### cast_shadow

```python
@property
def cast_shadow() -> bool
```

(bool):  [Read-Only] When enabled this is the default value set on the component.
Controls whether the primitive component should cast a shadow or not.

<a id="unreal.NiagaraSystem.receives_decals"></a>

#### receives_decals

```python
@property
def receives_decals() -> bool
```

(bool):  [Read-Only] When enabled this is the default value set on the component.
Whether the primitive receives decals.

<a id="unreal.NiagaraSystem.render_custom_depth"></a>

#### render_custom_depth

```python
@property
def render_custom_depth() -> bool
```

(bool):  [Read-Only] When enabled this is the default value set on the component.
This primitive has bRenderCustomDepth enabled.

<a id="unreal.NiagaraSystem.custom_depth_stencil_write_mask"></a>

#### custom_depth_stencil_write_mask

```python
@property
def custom_depth_stencil_write_mask() -> RendererStencilMask
```

(RendererStencilMask):  [Read-Only] When enabled this is the default value set on the component.
Mask used for stencil buffer writes.

<a id="unreal.NiagaraSystem.custom_depth_stencil_value"></a>

#### custom_depth_stencil_value

```python
@property
def custom_depth_stencil_value() -> int
```

(int32):  [Read-Only] When enabled this is the default value set on the component.
Optionally write this 0-255 value to the stencil buffer in CustomDepth pass (Requires project setting or r.CustomDepth == 3)

<a id="unreal.NiagaraSystem.translucency_sort_priority"></a>

#### translucency_sort_priority

```python
@property
def translucency_sort_priority() -> int
```

(int32):  [Read-Only] When enabled this is the default value set on the component.
Adjusts the translucent object sorting priority, see PrimitiveComponent description for more details.

<a id="unreal.NiagaraSystem.translucency_sort_distance_offset"></a>

#### translucency_sort_distance_offset

```python
@property
def translucency_sort_distance_offset() -> float
```

(float):  [Read-Only] When enabled this is the default value set on the component.
Modifies the sort distance for translucent objects, see PrimitiveComponent description for more details.

<a id="unreal.NiagaraEffect"></a>