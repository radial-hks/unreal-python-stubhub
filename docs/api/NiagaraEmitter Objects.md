## NiagaraEmitter Objects

```python
class NiagaraEmitter(Object)
```

Niagara Emitters are particle spawners that can be reused for different effects by putting them into Niagara systems.
Emitters render their particles using different renderers, such as Sprite Renderers or Mesh Renderers to produce different effects.

Emitter assets cannot be spawned or used in a level directly, but need to be placed in a Niagara system. Emitters support inheritance, so that
changes to the base asset are automatically picked up by child emitter assets and emitters in system assets.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraEmitter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allocation_mode`` (ParticleAllocationMode):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'AllocationMode' is deprecated.
- ``attributes_to_preserve`` (Array[str]):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'AttributesToPreserve' is deprecated.
- ``determinism`` (bool):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'bDeterminism' is deprecated.
- ``editor_data`` (NiagaraEditorDataBase):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'EditorData' is deprecated.
- ``editor_parameters`` (NiagaraEditorParametersAdapterBase):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'EditorParameters' is deprecated.
- ``emitter_spawn_script_props`` (NiagaraEmitterScriptProperties):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'EmitterSpawnScriptProps' is deprecated.
- ``emitter_update_script_props`` (NiagaraEmitterScriptProperties):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'EmitterUpdateScriptProps' is deprecated.
- ``event_handler_script_props`` (Array[NiagaraEventScriptProperties]):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'EventHandlerScriptProps' is deprecated.
- ``gpu_compute_script`` (NiagaraScript):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'GPUComputeScript' is deprecated.
- ``graph_source`` (NiagaraScriptSourceBase):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'GraphSource' is deprecated.
- ``interpolated_spawning`` (bool):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'bInterpolatedSpawning' is deprecated.
- ``is_inheritable`` (bool):  [Read-Write] If an emitter is inheritable, new emitters based on an inheritable emitter, or Niagara Systems using an inheritable emitter, will automatically inherit changes made to the original emitter.
- ``local_space`` (bool):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'bLocalSpace' is deprecated.
- ``max_gpu_particles_spawn_per_frame`` (uint32):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'MaxGPUParticlesSpawnPerFrame' is deprecated.
- ``parent`` (NiagaraEmitter):  [Read-Write]
  deprecated: Property 'Parent' is deprecated.
- ``parent_at_last_merge`` (NiagaraEmitter):  [Read-Write]
  deprecated: Property 'ParentAtLastMerge' is deprecated.
- ``parent_scratch_pad_scripts`` (Array[NiagaraScript]):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'ParentScratchPadScripts' is deprecated.
- ``platforms`` (NiagaraPlatformSet):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'Platforms' is deprecated.
- ``pre_allocation_count`` (int32):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'PreAllocationCount' is deprecated.
- ``random_seed`` (int32):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'RandomSeed' is deprecated.
- ``renderer_bindings`` (NiagaraParameterStore):  [Read-Write]
  deprecated: Property 'RendererBindings' is deprecated.
- ``renderer_properties`` (Array[NiagaraRendererProperties]):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'RendererProperties' is deprecated.
- ``requires_persistent_i_ds`` (bool):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'bRequiresPersistentIDs' is deprecated.
- ``scalability_overrides`` (NiagaraEmitterScalabilityOverrides):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'ScalabilityOverrides' is deprecated.
- ``scratch_pad_scripts`` (Array[NiagaraScript]):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'ScratchPadScripts' is deprecated.
- ``shared_event_generator_ids`` (Array[Name]):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'SharedEventGeneratorIds' is deprecated.
- ``sim_target`` (NiagaraSimTarget):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'SimTarget' is deprecated.
- ``simulation_stages`` (Array[NiagaraSimulationStageBase]):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'SimulationStages' is deprecated.
- ``spawn_script_props`` (NiagaraEmitterScriptProperties):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'SpawnScriptProps' is deprecated.
- ``template_asset_description`` (Text):  [Read-Write]
- ``template_specification`` (NiagaraScriptTemplateSpecification):  [Read-Write]
  deprecated: Property 'TemplateSpecification' is deprecated.
- ``update_script_props`` (NiagaraEmitterScriptProperties):  [Read-Write] Use property in struct returned from GetEmitterData() instead
  deprecated: Property 'UpdateScriptProps' is deprecated.

<a id="unreal.NiagaraEmitter.local_space"></a>

#### local_space

```python
@property
def local_space() -> bool
```

(bool):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'bLocalSpace' is deprecated.

<a id="unreal.NiagaraEmitter.local_space"></a>

#### local_space

```python
@local_space.setter
def local_space(value: bool) -> None
```

<a id="unreal.NiagaraEmitter.determinism"></a>

#### determinism

```python
@property
def determinism() -> bool
```

(bool):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'bDeterminism' is deprecated.

<a id="unreal.NiagaraEmitter.determinism"></a>

#### determinism

```python
@determinism.setter
def determinism(value: bool) -> None
```

<a id="unreal.NiagaraEmitter.random_seed"></a>

#### random_seed

```python
@property
def random_seed() -> int
```

(int32):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'RandomSeed' is deprecated.

<a id="unreal.NiagaraEmitter.random_seed"></a>

#### random_seed

```python
@random_seed.setter
def random_seed(value: int) -> None
```

<a id="unreal.NiagaraEmitter.allocation_mode"></a>

#### allocation_mode

```python
@property
def allocation_mode() -> ParticleAllocationMode
```

(ParticleAllocationMode):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'AllocationMode' is deprecated.

<a id="unreal.NiagaraEmitter.allocation_mode"></a>

#### allocation_mode

```python
@allocation_mode.setter
def allocation_mode(value: ParticleAllocationMode) -> None
```

<a id="unreal.NiagaraEmitter.pre_allocation_count"></a>

#### pre_allocation_count

```python
@property
def pre_allocation_count() -> int
```

(int32):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'PreAllocationCount' is deprecated.

<a id="unreal.NiagaraEmitter.pre_allocation_count"></a>

#### pre_allocation_count

```python
@pre_allocation_count.setter
def pre_allocation_count(value: int) -> None
```

<a id="unreal.NiagaraEmitter.update_script_props"></a>

#### update_script_props

```python
@property
def update_script_props() -> NiagaraEmitterScriptProperties
```

(NiagaraEmitterScriptProperties):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'UpdateScriptProps' is deprecated.

<a id="unreal.NiagaraEmitter.update_script_props"></a>

#### update_script_props

```python
@update_script_props.setter
def update_script_props(value: NiagaraEmitterScriptProperties) -> None
```

<a id="unreal.NiagaraEmitter.spawn_script_props"></a>

#### spawn_script_props

```python
@property
def spawn_script_props() -> NiagaraEmitterScriptProperties
```

(NiagaraEmitterScriptProperties):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'SpawnScriptProps' is deprecated.

<a id="unreal.NiagaraEmitter.spawn_script_props"></a>

#### spawn_script_props

```python
@spawn_script_props.setter
def spawn_script_props(value: NiagaraEmitterScriptProperties) -> None
```

<a id="unreal.NiagaraEmitter.template_specification"></a>

#### template_specification

```python
@property
def template_specification() -> NiagaraScriptTemplateSpecification
```

(NiagaraScriptTemplateSpecification):  [Read-Write]
deprecated: Property 'TemplateSpecification' is deprecated.

<a id="unreal.NiagaraEmitter.template_specification"></a>

#### template_specification

```python
@template_specification.setter
def template_specification(value: NiagaraScriptTemplateSpecification) -> None
```

<a id="unreal.NiagaraEmitter.emitter_spawn_script_props"></a>

#### emitter_spawn_script_props

```python
@property
def emitter_spawn_script_props() -> NiagaraEmitterScriptProperties
```

(NiagaraEmitterScriptProperties):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'EmitterSpawnScriptProps' is deprecated.

<a id="unreal.NiagaraEmitter.emitter_spawn_script_props"></a>

#### emitter_spawn_script_props

```python
@emitter_spawn_script_props.setter
def emitter_spawn_script_props(value: NiagaraEmitterScriptProperties) -> None
```

<a id="unreal.NiagaraEmitter.emitter_update_script_props"></a>

#### emitter_update_script_props

```python
@property
def emitter_update_script_props() -> NiagaraEmitterScriptProperties
```

(NiagaraEmitterScriptProperties):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'EmitterUpdateScriptProps' is deprecated.

<a id="unreal.NiagaraEmitter.emitter_update_script_props"></a>

#### emitter_update_script_props

```python
@emitter_update_script_props.setter
def emitter_update_script_props(value: NiagaraEmitterScriptProperties) -> None
```

<a id="unreal.NiagaraEmitter.attributes_to_preserve"></a>

#### attributes_to_preserve

```python
@property
def attributes_to_preserve() -> Array[str]
```

(Array[str]):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'AttributesToPreserve' is deprecated.

<a id="unreal.NiagaraEmitter.attributes_to_preserve"></a>

#### attributes_to_preserve

```python
@attributes_to_preserve.setter
def attributes_to_preserve(value: Array[str]) -> None
```

<a id="unreal.NiagaraEmitter.parent_scratch_pad_scripts"></a>

#### parent_scratch_pad_scripts

```python
@property
def parent_scratch_pad_scripts() -> Array[NiagaraScript]
```

(Array[NiagaraScript]):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'ParentScratchPadScripts' is deprecated.

<a id="unreal.NiagaraEmitter.parent_scratch_pad_scripts"></a>

#### parent_scratch_pad_scripts

```python
@parent_scratch_pad_scripts.setter
def parent_scratch_pad_scripts(value: Array[NiagaraScript]) -> None
```

<a id="unreal.NiagaraEmitter.sim_target"></a>

#### sim_target

```python
@property
def sim_target() -> NiagaraSimTarget
```

(NiagaraSimTarget):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'SimTarget' is deprecated.

<a id="unreal.NiagaraEmitter.sim_target"></a>

#### sim_target

```python
@sim_target.setter
def sim_target(value: NiagaraSimTarget) -> None
```

<a id="unreal.NiagaraEmitter.platforms"></a>

#### platforms

```python
@property
def platforms() -> NiagaraPlatformSet
```

(NiagaraPlatformSet):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'Platforms' is deprecated.

<a id="unreal.NiagaraEmitter.platforms"></a>

#### platforms

```python
@platforms.setter
def platforms(value: NiagaraPlatformSet) -> None
```

<a id="unreal.NiagaraEmitter.scalability_overrides"></a>

#### scalability_overrides

```python
@property
def scalability_overrides() -> NiagaraEmitterScalabilityOverrides
```

(NiagaraEmitterScalabilityOverrides):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'ScalabilityOverrides' is deprecated.

<a id="unreal.NiagaraEmitter.scalability_overrides"></a>

#### scalability_overrides

```python
@scalability_overrides.setter
def scalability_overrides(value: NiagaraEmitterScalabilityOverrides) -> None
```

<a id="unreal.NiagaraEmitter.interpolated_spawning"></a>

#### interpolated_spawning

```python
@property
def interpolated_spawning() -> bool
```

(bool):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'bInterpolatedSpawning' is deprecated.

<a id="unreal.NiagaraEmitter.interpolated_spawning"></a>

#### interpolated_spawning

```python
@interpolated_spawning.setter
def interpolated_spawning(value: bool) -> None
```

<a id="unreal.NiagaraEmitter.renderer_bindings"></a>

#### renderer_bindings

```python
@property
def renderer_bindings() -> NiagaraParameterStore
```

(NiagaraParameterStore):  [Read-Write]
deprecated: Property 'RendererBindings' is deprecated.

<a id="unreal.NiagaraEmitter.renderer_bindings"></a>

#### renderer_bindings

```python
@renderer_bindings.setter
def renderer_bindings(value: NiagaraParameterStore) -> None
```

<a id="unreal.NiagaraEmitter.requires_persistent_i_ds"></a>

#### requires_persistent_i_ds

```python
@property
def requires_persistent_i_ds() -> bool
```

(bool):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'bRequiresPersistentIDs' is deprecated.

<a id="unreal.NiagaraEmitter.requires_persistent_i_ds"></a>

#### requires_persistent_i_ds

```python
@requires_persistent_i_ds.setter
def requires_persistent_i_ds(value: bool) -> None
```

<a id="unreal.NiagaraEmitter.max_gpu_particles_spawn_per_frame"></a>

#### max_gpu_particles_spawn_per_frame

```python
@property
def max_gpu_particles_spawn_per_frame() -> int
```

(uint32):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'MaxGPUParticlesSpawnPerFrame' is deprecated.

<a id="unreal.NiagaraEmitter.max_gpu_particles_spawn_per_frame"></a>

#### max_gpu_particles_spawn_per_frame

```python
@max_gpu_particles_spawn_per_frame.setter
def max_gpu_particles_spawn_per_frame(value: int) -> None
```

<a id="unreal.NiagaraEmitter.graph_source"></a>

#### graph_source

```python
@property
def graph_source() -> NiagaraScriptSourceBase
```

(NiagaraScriptSourceBase):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'GraphSource' is deprecated.

<a id="unreal.NiagaraEmitter.graph_source"></a>

#### graph_source

```python
@graph_source.setter
def graph_source(value: NiagaraScriptSourceBase) -> None
```

<a id="unreal.NiagaraEmitter.scratch_pad_scripts"></a>

#### scratch_pad_scripts

```python
@property
def scratch_pad_scripts() -> Array[NiagaraScript]
```

(Array[NiagaraScript]):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'ScratchPadScripts' is deprecated.

<a id="unreal.NiagaraEmitter.scratch_pad_scripts"></a>

#### scratch_pad_scripts

```python
@scratch_pad_scripts.setter
def scratch_pad_scripts(value: Array[NiagaraScript]) -> None
```

<a id="unreal.NiagaraEmitter.editor_data"></a>

#### editor_data

```python
@property
def editor_data() -> NiagaraEditorDataBase
```

(NiagaraEditorDataBase):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'EditorData' is deprecated.

<a id="unreal.NiagaraEmitter.editor_data"></a>

#### editor_data

```python
@editor_data.setter
def editor_data(value: NiagaraEditorDataBase) -> None
```

<a id="unreal.NiagaraEmitter.editor_parameters"></a>

#### editor_parameters

```python
@property
def editor_parameters() -> NiagaraEditorParametersAdapterBase
```

(NiagaraEditorParametersAdapterBase):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'EditorParameters' is deprecated.

<a id="unreal.NiagaraEmitter.editor_parameters"></a>

#### editor_parameters

```python
@editor_parameters.setter
def editor_parameters(value: NiagaraEditorParametersAdapterBase) -> None
```

<a id="unreal.NiagaraEmitter.renderer_properties"></a>

#### renderer_properties

```python
@property
def renderer_properties() -> Array[NiagaraRendererProperties]
```

(Array[NiagaraRendererProperties]):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'RendererProperties' is deprecated.

<a id="unreal.NiagaraEmitter.renderer_properties"></a>

#### renderer_properties

```python
@renderer_properties.setter
def renderer_properties(value: Array[NiagaraRendererProperties]) -> None
```

<a id="unreal.NiagaraEmitter.event_handler_script_props"></a>

#### event_handler_script_props

```python
@property
def event_handler_script_props() -> Array[NiagaraEventScriptProperties]
```

(Array[NiagaraEventScriptProperties]):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'EventHandlerScriptProps' is deprecated.

<a id="unreal.NiagaraEmitter.event_handler_script_props"></a>

#### event_handler_script_props

```python
@event_handler_script_props.setter
def event_handler_script_props(
        value: Array[NiagaraEventScriptProperties]) -> None
```

<a id="unreal.NiagaraEmitter.simulation_stages"></a>

#### simulation_stages

```python
@property
def simulation_stages() -> Array[NiagaraSimulationStageBase]
```

(Array[NiagaraSimulationStageBase]):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'SimulationStages' is deprecated.

<a id="unreal.NiagaraEmitter.simulation_stages"></a>

#### simulation_stages

```python
@simulation_stages.setter
def simulation_stages(value: Array[NiagaraSimulationStageBase]) -> None
```

<a id="unreal.NiagaraEmitter.gpu_compute_script"></a>

#### gpu_compute_script

```python
@property
def gpu_compute_script() -> NiagaraScript
```

(NiagaraScript):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'GPUComputeScript' is deprecated.

<a id="unreal.NiagaraEmitter.gpu_compute_script"></a>

#### gpu_compute_script

```python
@gpu_compute_script.setter
def gpu_compute_script(value: NiagaraScript) -> None
```

<a id="unreal.NiagaraEmitter.shared_event_generator_ids"></a>

#### shared_event_generator_ids

```python
@property
def shared_event_generator_ids() -> Array[Name]
```

(Array[Name]):  [Read-Write] Use property in struct returned from GetEmitterData() instead
deprecated: Property 'SharedEventGeneratorIds' is deprecated.

<a id="unreal.NiagaraEmitter.shared_event_generator_ids"></a>

#### shared_event_generator_ids

```python
@shared_event_generator_ids.setter
def shared_event_generator_ids(value: Array[Name]) -> None
```

<a id="unreal.NiagaraEmitter.parent"></a>

#### parent

```python
@property
def parent() -> NiagaraEmitter
```

(NiagaraEmitter):  [Read-Write]
deprecated: Property 'Parent' is deprecated.

<a id="unreal.NiagaraEmitter.parent"></a>

#### parent

```python
@parent.setter
def parent(value: NiagaraEmitter) -> None
```

<a id="unreal.NiagaraEmitter.parent_at_last_merge"></a>

#### parent_at_last_merge

```python
@property
def parent_at_last_merge() -> NiagaraEmitter
```

(NiagaraEmitter):  [Read-Write]
deprecated: Property 'ParentAtLastMerge' is deprecated.

<a id="unreal.NiagaraEmitter.parent_at_last_merge"></a>

#### parent_at_last_merge

```python
@parent_at_last_merge.setter
def parent_at_last_merge(value: NiagaraEmitter) -> None
```

<a id="unreal.NiagaraEmitterProperties"></a>