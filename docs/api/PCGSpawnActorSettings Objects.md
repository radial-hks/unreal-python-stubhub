## PCGSpawnActorSettings Objects

```python
class PCGSpawnActorSettings(PCGBaseSubgraphSettings)
```

* PCG settings class that allows spawning actors with some options to perform the work more efficiently.
* Note that depending on the options, any PCG components on the spawned actors can be also generated,
* which is why this class derives from UPCGBaseSubgraphSettings - it has similar inner-workings to the subgraph node
* as far as data passing and dispatch go.
* Note that at this point in time, results from the underlying graphs being generated is not propagated back as results of this node.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSpawnActor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_template_actor_editing`` (bool):  [Read-Write]
- ``attach_options`` (PCGAttachOptions):  [Read-Write]
- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``debug`` (bool):  [Read-Write]
- ``debug_buffer_size`` (int32):  [Read-Write] Size (in number of floats) of the shader debug print buffer.
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``description`` (Text):  [Read-Write]
- ``determinism_settings`` (PCGDeterminismSettings):  [Read-Write]
- ``dump_cooked_hlsl`` (bool):  [Read-Write] Dump the cooked HLSL into the log after it is generated.
- ``dump_data_descriptions`` (bool):  [Read-Write] Dump the data descriptions of input/output pins to the log.
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``force_disable_actor_parsing`` (bool):  [Read-Write] Note that this is no longer the default value for new nodes, it is now EPCGSpawnActorOption::NoMerging.
- ``generation_trigger`` (PCGSpawnActorGenerationTrigger):  [Read-Write]
- ``inherit_actor_tags`` (bool):  [Read-Write] Warning: inheriting parent actor tags work only in non-collapsed actor hierarchies
- ``option`` (PCGSpawnActorOption):  [Read-Write]
- ``post_spawn_function_names`` (Array[Name]):  [Read-Write] Can specify a list of functions from the template class to be called on each actor spawned, in order. Need to have "CallInEditor" flag enabled
  and have either no parameters or exactly the parameters PCGPoint and PCGMetadata
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``spawn_attribute`` (Name):  [Read-Write]
- ``spawn_by_attribute`` (bool):  [Read-Write] Note that this is no longer the default value for new nodes, it is now EPCGAttachOptions::InFolder
- ``spawned_actor_property_override_descriptions`` (Array[PCGObjectPropertyOverrideDescription]):  [Read-Write]
- ``tags_to_add_on_actors`` (Array[Name]):  [Read-Write]
- ``template_actor`` (Actor):  [Read-Write]
- ``template_actor_class`` (type(Class)):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.
- ``warn_on_identical_spawn`` (bool):  [Read-Write] Adds a warning to the node on repeated spawning with identical conditions (ie. same actor at same spawn location, etc).

<a id="unreal.PCGSpawnActorSettings.post_spawn_function_names"></a>

#### post_spawn_function_names

```python
@property
def post_spawn_function_names() -> Array[Name]
```

(Array[Name]):  [Read-Write] Can specify a list of functions from the template class to be called on each actor spawned, in order. Need to have "CallInEditor" flag enabled
and have either no parameters or exactly the parameters PCGPoint and PCGMetadata

<a id="unreal.PCGSpawnActorSettings.post_spawn_function_names"></a>

#### post_spawn_function_names

```python
@post_spawn_function_names.setter
def post_spawn_function_names(value: Array[Name]) -> None
```

<a id="unreal.PCGSpawnActorSettings.option"></a>

#### option

```python
@property
def option() -> PCGSpawnActorOption
```

(PCGSpawnActorOption):  [Read-Write]

<a id="unreal.PCGSpawnActorSettings.option"></a>

#### option

```python
@option.setter
def option(value: PCGSpawnActorOption) -> None
```

<a id="unreal.PCGSpawnActorSettings.force_disable_actor_parsing"></a>

#### force_disable_actor_parsing

```python
@property
def force_disable_actor_parsing() -> bool
```

(bool):  [Read-Write] Note that this is no longer the default value for new nodes, it is now EPCGSpawnActorOption::NoMerging.

<a id="unreal.PCGSpawnActorSettings.force_disable_actor_parsing"></a>

#### force_disable_actor_parsing

```python
@force_disable_actor_parsing.setter
def force_disable_actor_parsing(value: bool) -> None
```

<a id="unreal.PCGSpawnActorSettings.generation_trigger"></a>

#### generation_trigger

```python
@property
def generation_trigger() -> PCGSpawnActorGenerationTrigger
```

(PCGSpawnActorGenerationTrigger):  [Read-Write]

<a id="unreal.PCGSpawnActorSettings.generation_trigger"></a>

#### generation_trigger

```python
@generation_trigger.setter
def generation_trigger(value: PCGSpawnActorGenerationTrigger) -> None
```

<a id="unreal.PCGSpawnActorSettings.inherit_actor_tags"></a>

#### inherit_actor_tags

```python
@property
def inherit_actor_tags() -> bool
```

(bool):  [Read-Write] Warning: inheriting parent actor tags work only in non-collapsed actor hierarchies

<a id="unreal.PCGSpawnActorSettings.inherit_actor_tags"></a>

#### inherit_actor_tags

```python
@inherit_actor_tags.setter
def inherit_actor_tags(value: bool) -> None
```

<a id="unreal.PCGSpawnActorSettings.tags_to_add_on_actors"></a>

#### tags_to_add_on_actors

```python
@property
def tags_to_add_on_actors() -> Array[Name]
```

(Array[Name]):  [Read-Write]

<a id="unreal.PCGSpawnActorSettings.tags_to_add_on_actors"></a>

#### tags_to_add_on_actors

```python
@tags_to_add_on_actors.setter
def tags_to_add_on_actors(value: Array[Name]) -> None
```

<a id="unreal.PCGSpawnActorSettings.template_actor"></a>

#### template_actor

```python
@property
def template_actor() -> Actor
```

(Actor):  [Read-Write]

<a id="unreal.PCGSpawnActorSettings.template_actor"></a>

#### template_actor

```python
@template_actor.setter
def template_actor(value: Actor) -> None
```

<a id="unreal.PCGSpawnActorSettings.spawned_actor_property_override_descriptions"></a>

#### spawned_actor_property_override_descriptions

```python
@property
def spawned_actor_property_override_descriptions(
) -> Array[PCGObjectPropertyOverrideDescription]
```

(Array[PCGObjectPropertyOverrideDescription]):  [Read-Write]

<a id="unreal.PCGSpawnActorSettings.spawned_actor_property_override_descriptions"></a>

#### spawned_actor_property_override_descriptions

```python
@spawned_actor_property_override_descriptions.setter
def spawned_actor_property_override_descriptions(
        value: Array[PCGObjectPropertyOverrideDescription]) -> None
```

<a id="unreal.PCGSpawnActorSettings.attach_options"></a>

#### attach_options

```python
@property
def attach_options() -> PCGAttachOptions
```

(PCGAttachOptions):  [Read-Write]

<a id="unreal.PCGSpawnActorSettings.attach_options"></a>

#### attach_options

```python
@attach_options.setter
def attach_options(value: PCGAttachOptions) -> None
```

<a id="unreal.PCGSpawnActorSettings.spawn_by_attribute"></a>

#### spawn_by_attribute

```python
@property
def spawn_by_attribute() -> bool
```

(bool):  [Read-Write] Note that this is no longer the default value for new nodes, it is now EPCGAttachOptions::InFolder

<a id="unreal.PCGSpawnActorSettings.spawn_by_attribute"></a>

#### spawn_by_attribute

```python
@spawn_by_attribute.setter
def spawn_by_attribute(value: bool) -> None
```

<a id="unreal.PCGSpawnActorSettings.spawn_attribute"></a>

#### spawn_attribute

```python
@property
def spawn_attribute() -> Name
```

(Name):  [Read-Write]

<a id="unreal.PCGSpawnActorSettings.spawn_attribute"></a>

#### spawn_attribute

```python
@spawn_attribute.setter
def spawn_attribute(value: Name) -> None
```

<a id="unreal.PCGSpawnActorSettings.warn_on_identical_spawn"></a>

#### warn_on_identical_spawn

```python
@property
def warn_on_identical_spawn() -> bool
```

(bool):  [Read-Write] Adds a warning to the node on repeated spawning with identical conditions (ie. same actor at same spawn location, etc).

<a id="unreal.PCGSpawnActorSettings.warn_on_identical_spawn"></a>

#### warn_on_identical_spawn

```python
@warn_on_identical_spawn.setter
def warn_on_identical_spawn(value: bool) -> None
```

<a id="unreal.PCGSpawnActorSettings.template_actor_class"></a>

#### template_actor_class

```python
@property
def template_actor_class() -> Class
```

(type(Class)):  [Read-Only]

<a id="unreal.PCGSpawnActorSettings.allow_template_actor_editing"></a>

#### allow_template_actor_editing

```python
@property
def allow_template_actor_editing() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGSpawnActorSettings.allow_template_actor_editing"></a>

#### allow_template_actor_editing

```python
@allow_template_actor_editing.setter
def allow_template_actor_editing(value: bool) -> None
```

<a id="unreal.PCGNode"></a>