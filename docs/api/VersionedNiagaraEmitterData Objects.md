## VersionedNiagaraEmitterData Objects

```python
class VersionedNiagaraEmitterData(StructBase)
```

Struct containing all of the data that can be different between different emitter versions.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraEmitter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``add_emitter_default_view_state`` (NiagaraEmitterDefaultSummaryState):  [Read-Write] This determines how emitters will be added to a system by default. If summary view is setup, consider setting this to 'Summary'.
- ``allocation_mode`` (ParticleAllocationMode):  [Read-Write] The emitter needs to allocate memory for the particles each tick.
  To prevent reallocations, the emitter should allocate as much memory as is needed for the max particle count.
  This setting controls if the allocation size should be automatically determined or manually entered.
- ``attributes_to_preserve`` (Array[str]):  [Read-Write] An allow list of Particle attributes (e.g. "Particle.Position" or "Particle.Age") that will not be removed from the DataSet  even if they aren't read by the VM.
            Used in conjunction with UNiagaraSystem::bTrimAttributes
- ``calculate_bounds_mode`` (NiagaraEmitterCalculateBoundMode):  [Read-Write] How should we calculate bounds for the emitter.
  Note: If this is greyed out it means fixed bounds are enabled in the System Properties and these bounds are therefore ignored.
- ``determinism`` (bool):  [Read-Write] Toggles whether to globally make the random number generator be deterministic or non-deterministic. Any random calculation that is set to the emitter defaults will inherit this value. It is still possible to tweak individual random to be deterministic or not. In this case deterministic means that it will return the same results for the same configuration of the emitter as long as delta time is not variable. Any changes to the emitter's individual scripts will adjust the results.
- ``emitter_dependencies`` (Array[NiagaraDataInterfaceEmitterBinding]):  [Read-Write] List of emitter dependencies to use when calculating the execution order for emitter particle scripts.
  This is generally only required when you are using advanced features, such as reading / writing to a data interface in different emitters
  and need to ensure the emitters can not run concurrently with one another, either on the CPU or the GPU.
- ``fixed_bounds`` (Box):  [Read-Write] The fixed bounding box value. CalculateBoundsMode is the condition whether the fixed bounds can be edited.
  Note: If this is greyed out it means fixed bounds are enabled in the System Properties and these bounds are therefore ignored.
- ``interpolated_spawning`` (bool):  [Read-Write] When enabled, this will spawn using interpolated parameter values and perform a partial update at spawn time. This adds significant additional cost for spawning but will produce much smoother spawning for high spawn rates, erratic frame rates and fast moving emitters.
- ``local_space`` (bool):  [Read-Write] Toggles whether or not the particles within this emitter are relative to the emitter origin or in global space.
- ``max_gpu_particles_spawn_per_frame`` (int32):  [Read-Write] An override on the max number of GPU particles we expect to spawn in a single frame. A value of 0 means it'll use fx.MaxNiagaraGPUParticlesSpawnPerFrame.
- ``platforms`` (NiagaraPlatformSet):  [Read-Write]
- ``pre_allocation_count`` (int32):  [Read-Write] The emitter will allocate at least this many particles on it's first tick.
  This can aid performance by avoiding many allocations as an emitter ramps up to it's max size.
- ``random_seed`` (int32):  [Read-Write] An emitter-based seed for the deterministic random number generator.
- ``requires_persistent_i_ds`` (bool):  [Read-Write] Creates a stable Identifier (Particles.ID) which does not vary from frame to frame. This comes at a small memory and performance cost. This allows external objects to track the same particle over multiple frames. Particle arrays are tightly packed and a particle's actual index in the array may change from frame to frame. This optionally lets you use a lookup table to track a particle by index in the lookup table.
- ``scalability_overrides`` (NiagaraEmitterScalabilityOverrides):  [Read-Write]
- ``sim_stage_execution_loop_editor_data`` (Array[NiagaraSimStageExecutionLoopEditorData]):  [Read-Write]
- ``sim_target`` (NiagaraSimTarget):  [Read-Write]

<a id="unreal.VersionedNiagaraEmitterData.__init__"></a>

#### __init__

```python
def __init__(
    local_space: bool = False,
    determinism: bool = False,
    random_seed: int = 0,
    interpolated_spawning: bool = False,
    sim_target: NiagaraSimTarget = NiagaraSimTarget.CPU_SIM,
    fixed_bounds: Box = [[0.000000, 0.000000, 0.000000],
                         [0.000000, 0.000000, 0.000000], False],
    requires_persistent_i_ds: bool = False,
    max_gpu_particles_spawn_per_frame: int = 0,
    allocation_mode: ParticleAllocationMode = ParticleAllocationMode.
    AUTOMATIC_ESTIMATE
) -> None
```

<a id="unreal.VersionedNiagaraEmitterData.local_space"></a>

#### local_space

```python
@property
def local_space() -> bool
```

(bool):  [Read-Write] Toggles whether or not the particles within this emitter are relative to the emitter origin or in global space.

<a id="unreal.VersionedNiagaraEmitterData.local_space"></a>

#### local_space

```python
@local_space.setter
def local_space(value: bool) -> None
```

<a id="unreal.VersionedNiagaraEmitterData.determinism"></a>

#### determinism

```python
@property
def determinism() -> bool
```

(bool):  [Read-Write] Toggles whether to globally make the random number generator be deterministic or non-deterministic. Any random calculation that is set to the emitter defaults will inherit this value. It is still possible to tweak individual random to be deterministic or not. In this case deterministic means that it will return the same results for the same configuration of the emitter as long as delta time is not variable. Any changes to the emitter's individual scripts will adjust the results.

<a id="unreal.VersionedNiagaraEmitterData.determinism"></a>

#### determinism

```python
@determinism.setter
def determinism(value: bool) -> None
```

<a id="unreal.VersionedNiagaraEmitterData.random_seed"></a>

#### random_seed

```python
@property
def random_seed() -> int
```

(int32):  [Read-Write] An emitter-based seed for the deterministic random number generator.

<a id="unreal.VersionedNiagaraEmitterData.random_seed"></a>

#### random_seed

```python
@random_seed.setter
def random_seed(value: int) -> None
```

<a id="unreal.VersionedNiagaraEmitterData.interpolated_spawning"></a>

#### interpolated_spawning

```python
@property
def interpolated_spawning() -> bool
```

(bool):  [Read-Write] When enabled, this will spawn using interpolated parameter values and perform a partial update at spawn time. This adds significant additional cost for spawning but will produce much smoother spawning for high spawn rates, erratic frame rates and fast moving emitters.

<a id="unreal.VersionedNiagaraEmitterData.interpolated_spawning"></a>

#### interpolated_spawning

```python
@interpolated_spawning.setter
def interpolated_spawning(value: bool) -> None
```

<a id="unreal.VersionedNiagaraEmitterData.sim_target"></a>

#### sim_target

```python
@property
def sim_target() -> NiagaraSimTarget
```

(NiagaraSimTarget):  [Read-Write]

<a id="unreal.VersionedNiagaraEmitterData.sim_target"></a>

#### sim_target

```python
@sim_target.setter
def sim_target(value: NiagaraSimTarget) -> None
```

<a id="unreal.VersionedNiagaraEmitterData.fixed_bounds"></a>

#### fixed_bounds

```python
@property
def fixed_bounds() -> Box
```

(Box):  [Read-Write] The fixed bounding box value. CalculateBoundsMode is the condition whether the fixed bounds can be edited.
Note: If this is greyed out it means fixed bounds are enabled in the System Properties and these bounds are therefore ignored.

<a id="unreal.VersionedNiagaraEmitterData.fixed_bounds"></a>

#### fixed_bounds

```python
@fixed_bounds.setter
def fixed_bounds(value: Box) -> None
```

<a id="unreal.VersionedNiagaraEmitterData.requires_persistent_i_ds"></a>

#### requires_persistent_i_ds

```python
@property
def requires_persistent_i_ds() -> bool
```

(bool):  [Read-Write] Creates a stable Identifier (Particles.ID) which does not vary from frame to frame. This comes at a small memory and performance cost. This allows external objects to track the same particle over multiple frames. Particle arrays are tightly packed and a particle's actual index in the array may change from frame to frame. This optionally lets you use a lookup table to track a particle by index in the lookup table.

<a id="unreal.VersionedNiagaraEmitterData.requires_persistent_i_ds"></a>

#### requires_persistent_i_ds

```python
@requires_persistent_i_ds.setter
def requires_persistent_i_ds(value: bool) -> None
```

<a id="unreal.VersionedNiagaraEmitterData.max_gpu_particles_spawn_per_frame"></a>

#### max_gpu_particles_spawn_per_frame

```python
@property
def max_gpu_particles_spawn_per_frame() -> int
```

(int32):  [Read-Write] An override on the max number of GPU particles we expect to spawn in a single frame. A value of 0 means it'll use fx.MaxNiagaraGPUParticlesSpawnPerFrame.

<a id="unreal.VersionedNiagaraEmitterData.max_gpu_particles_spawn_per_frame"></a>

#### max_gpu_particles_spawn_per_frame

```python
@max_gpu_particles_spawn_per_frame.setter
def max_gpu_particles_spawn_per_frame(value: int) -> None
```

<a id="unreal.VersionedNiagaraEmitterData.allocation_mode"></a>

#### allocation_mode

```python
@property
def allocation_mode() -> ParticleAllocationMode
```

(ParticleAllocationMode):  [Read-Write] The emitter needs to allocate memory for the particles each tick.
To prevent reallocations, the emitter should allocate as much memory as is needed for the max particle count.
This setting controls if the allocation size should be automatically determined or manually entered.

<a id="unreal.VersionedNiagaraEmitterData.allocation_mode"></a>

#### allocation_mode

```python
@allocation_mode.setter
def allocation_mode(value: ParticleAllocationMode) -> None
```

<a id="unreal.NiagaraPerfBaselineStats"></a>