## NiagaraSettings Objects

```python
class NiagaraSettings(DeveloperSettings)
```

Niagara Settings

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accurate_quat_interpolation`` (bool):  [Read-Write] If set to true, quaternion attributes will be interpolated via slerp instead of lerp in interpolated spawn scripts.
- ``additional_parameter_enums`` (Array[SoftObjectPath]):  [Read-Write]
- ``additional_parameter_types`` (Array[SoftObjectPath]):  [Read-Write]
- ``additional_payload_types`` (Array[SoftObjectPath]):  [Read-Write]
- ``allow_create_actor_from_system_with_no_effect_type`` (bool):  [Read-Write] Should we allow placing a Niagara System in the editor into a level which has no effect type assigned?
- ``byte_code_strip_option`` (NiagaraStripScriptByteCodeOption):  [Read-Write] Controls how byte code will be stripped when loading assets that have multiple sets of bytecode (i.e. optimized).
- ``compilation_mode`` (NiagaraCompilationMode):  [Read-Write]
- ``component_renderer_warnings_per_class`` (Map[str, Text]):  [Read-Write] Info texts that the component renderer shows the user depending on the selected component class.
- ``default_effect_type`` (SoftObjectPath):  [Read-Write] Default effect type to use for effects that don't define their own. Can be null.
- ``default_gpu_translucent_latency`` (NiagaraDefaultGpuTranslucentLatency):  [Read-Write] The default setting for Gpu simulation translucent draw latency.
- ``default_grid_format`` (NiagaraGpuBufferFormat):  [Read-Write] The default buffer format used by all Niagara Grid Data Interfaces unless overridden.
- ``default_light_inverse_exposure_blend`` (float):  [Read-Write] The default InverseExposureBlend used for the light renderer.
- ``default_pixel_coverage_mode`` (NiagaraDefaultRendererPixelCoverageMode):  [Read-Write] The default setting for pixel coverage mode when automatic is set on the Niagara Renderer.
- ``default_render_target_format`` (TextureRenderTargetFormat):  [Read-Write] The default render target format used by all Niagara Render Target Data Interfaces unless overridden.
- ``default_renderer_motion_vector_setting`` (NiagaraDefaultRendererMotionVectorSetting):  [Read-Write] The default setting for motion vectors in Niagara renderers
- ``default_sort_precision`` (NiagaraDefaultSortPrecision):  [Read-Write] The default setting for sorting precision when automatic is set on the Niagara Renderer.
- ``enforce_strict_stack_types`` (bool):  [Read-Write] If set to true, types like positions and vectors cannot be assigned to each other without an explicit conversion step.
  If false, type checks are loosened and some types can be implicitly converted into each other.
  It is recommended to not disable this when working with large world coordinates.
- ``experimental_vm_enabled`` (bool):  [Read-Write] True indicates that we will generate byte code for the new optimized VM.  Control over whether the new VM will
  be used when executing NiagaraScripts will also take into account the overrides on the system (bDisableExperimentalVM) and
  the cvars fx.NiagaraScript.StripByteCodeOnLoad and fx.ForceExecVMPath.
- ``invalid_namespace_write_severity`` (NiagaraCompileErrorSeverity):  [Read-Write] If the Niagara compiler sees that a script writes to a namespace that is read only (e.g. a particle script writing to a system attribute), what should it do.
- ``limit_delta_time`` (bool):  [Read-Write] Whether to limit the max tick delta time or not.
- ``max_delta_time_per_tick`` (float):  [Read-Write] Limits the delta time per tick for emitters to prevent simulation spikes due to frame lags.
- ``ndi_collision_query_async_gpu_trace_provider_order`` (Array[NDICollisionQuery_AsyncGpuTraceProvider]):  [Read-Write] Defines how traces tagged as 'Project Default' will be interpreted when using the AsyncGpuTrace data interface.
  The system will go through (starting at element 0) to find the first provider that is available.
- ``ndi_skel_mesh_adjacency_triangle_index_format`` (NDISkelMesh_AdjacencyTriangleIndexFormat):  [Read-Write] Controls the format used for specifying triangle indexes in adjacency buffers.  Changing this setting requires restarting the editor.
- ``ndi_skel_mesh_gpu_max_influences`` (NDISkelMesh_GpuMaxInfluences):  [Read-Write] Controls the maximum number of influences we allow the Skeletal Mesh Data Interface to use on the GPU.  Changing this setting requires restarting the editor.
- ``ndi_skel_mesh_gpu_uniform_sampling_format`` (NDISkelMesh_GpuUniformSamplingFormat):  [Read-Write] Controls the format used for uniform sampling on the GPU.  Changing this setting requires restarting the editor.
- ``ndi_skel_mesh_support16_bit_index_weight`` (bool):  [Read-Write] Enabled support for 16 bit bone index & bone weight, optional to reduce shader complexity.  Changing this setting requires restarting the editor.
- ``ndi_skel_mesh_support_reading_deformed_geometry`` (bool):  [Read-Write] When enabled we will read deformed geometry if available, i.e. data from the deformed graph / skin cache
  When disable we will only read from the default vertex data which does not include morph targets, skin, etc.
  Changing this setting requires restarting the editor.
  Note: Enabling this does add additional branches to the skel mesh data reading.
- ``ndi_static_mesh_allow_distance_fields`` (bool):  [Read-Write] When enabled the static mesh data interface is allowed to sample from the distance field data (if present) on the GPU.
  Enabling this feature will move all systems that contain static mesh samples into PostRenderOpaque tick group regardless of the features used.
  Changing this setting requires restarting the editor.
- ``platform_set_redirects`` (Array[NiagaraPlatformSetRedirect]):  [Read-Write]
- ``position_pin_type_color`` (LinearColor):  [Read-Write] Position pin type color. The other pin colors are defined in the general editor settings.
- ``quality_levels`` (Array[Text]):  [Read-Write] The quality levels Niagara uses.
- ``quick_sim_cache_capture_frame_count`` (int32):  [Read-Write] The number of frames to capture when capturing a Sim Cache from the Niagara Component Details Panel. *
- ``show_convertible_inputs_in_stack`` (bool):  [Read-Write] If true then the "link input" menu will also show variables of different types, as long as there is a conversion script for them.
- ``sim_cache_auxiliary_file_base_path`` (str):  [Read-Write] Base path for auxiliary files written out during the generation of a Niagara Sim Cache (ie: volume files).
- ``sim_cache_max_cpu_memory_volumetrics`` (int64):  [Read-Write] Max memory in megabytes for total CPU memory for cached volumetric data
- ``system_viewport_in_orbit_mode`` (bool):  [Read-Write] Sets the default navigation behavior for the system preview viewport.
- ``systems_support_large_world_coordinates`` (bool):  [Read-Write] If true then active effects rebase the simulation positions to not lose precision. Can be turned off if not needed to skip unnecessary rebasing calculations.

<a id="unreal.NiagaraSettings.limit_delta_time"></a>

#### limit_delta_time

```python
@property
def limit_delta_time() -> bool
```

(bool):  [Read-Write] Whether to limit the max tick delta time or not.

<a id="unreal.NiagaraSettings.limit_delta_time"></a>

#### limit_delta_time

```python
@limit_delta_time.setter
def limit_delta_time(value: bool) -> None
```

<a id="unreal.NiagaraSettings.max_delta_time_per_tick"></a>

#### max_delta_time_per_tick

```python
@property
def max_delta_time_per_tick() -> float
```

(float):  [Read-Write] Limits the delta time per tick for emitters to prevent simulation spikes due to frame lags.

<a id="unreal.NiagaraSettings.max_delta_time_per_tick"></a>

#### max_delta_time_per_tick

```python
@max_delta_time_per_tick.setter
def max_delta_time_per_tick(value: float) -> None
```

<a id="unreal.NiagaraValidationRuleSet"></a>