## PCGCreateTargetActor Objects

```python
class PCGCreateTargetActor(PCGSettings)
```

PCGCreate Target Actor

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCreateTargetActor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_template_actor_editing`` (bool):  [Read-Write] TODO: make this InlineEditConditionToggle, not done because property changed event does not propagate correctly so we can't track accurately the need to create the target actor
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
- ``post_process_function_names`` (Array[Name]):  [Read-Write] Specify a list of functions to be called on the target actor after creation. Functions need to be parameter-less and with "CallInEditor" flag enabled.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``property_override_descriptions`` (Array[PCGObjectPropertyOverrideDescription]):  [Read-Write] Override the default property values on the created target actor. Applied before post-process functions.
- ``seed`` (int32):  [Read-Write]
- ``template_actor`` (Actor):  [Read-Write]
- ``template_actor_class`` (type(Class)):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGCreateTargetActor.template_actor"></a>

#### template_actor

```python
@property
def template_actor() -> Actor
```

(Actor):  [Read-Write]

<a id="unreal.PCGCreateTargetActor.template_actor"></a>

#### template_actor

```python
@template_actor.setter
def template_actor(value: Actor) -> None
```

<a id="unreal.PCGCreateTargetActor.attach_options"></a>

#### attach_options

```python
@property
def attach_options() -> PCGAttachOptions
```

(PCGAttachOptions):  [Read-Write]

<a id="unreal.PCGCreateTargetActor.attach_options"></a>

#### attach_options

```python
@attach_options.setter
def attach_options(value: PCGAttachOptions) -> None
```

<a id="unreal.PCGCreateTargetActor.property_override_descriptions"></a>

#### property_override_descriptions

```python
@property
def property_override_descriptions(
) -> Array[PCGObjectPropertyOverrideDescription]
```

(Array[PCGObjectPropertyOverrideDescription]):  [Read-Write] Override the default property values on the created target actor. Applied before post-process functions.

<a id="unreal.PCGCreateTargetActor.property_override_descriptions"></a>

#### property_override_descriptions

```python
@property_override_descriptions.setter
def property_override_descriptions(
        value: Array[PCGObjectPropertyOverrideDescription]) -> None
```

<a id="unreal.PCGCreateTargetActor.post_process_function_names"></a>

#### post_process_function_names

```python
@property
def post_process_function_names() -> Array[Name]
```

(Array[Name]):  [Read-Write] Specify a list of functions to be called on the target actor after creation. Functions need to be parameter-less and with "CallInEditor" flag enabled.

<a id="unreal.PCGCreateTargetActor.post_process_function_names"></a>

#### post_process_function_names

```python
@post_process_function_names.setter
def post_process_function_names(value: Array[Name]) -> None
```

<a id="unreal.PCGCreateTargetActor.template_actor_class"></a>

#### template_actor_class

```python
@property
def template_actor_class() -> Class
```

(type(Class)):  [Read-Only]

<a id="unreal.PCGCreateTargetActor.allow_template_actor_editing"></a>

#### allow_template_actor_editing

```python
@property
def allow_template_actor_editing() -> bool
```

(bool):  [Read-Write] TODO: make this InlineEditConditionToggle, not done because property changed event does not propagate correctly so we can't track accurately the need to create the target actor

<a id="unreal.PCGCreateTargetActor.allow_template_actor_editing"></a>

#### allow_template_actor_editing

```python
@allow_template_actor_editing.setter
def allow_template_actor_editing(value: bool) -> None
```

<a id="unreal.PCGDataFromActorSettings"></a>