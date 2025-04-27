## PCGApplyOnActorSettings Objects

```python
class PCGApplyOnActorSettings(PCGSettings)
```

Apply property overrides and executes functions on a target actor.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGApplyOnActor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

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
- ``object_reference_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] If something is connected in the In pin, will look for this attribute values to load, representing the object reference.
- ``post_process_function_names`` (Array[Name]):  [Read-Write] Specify a list of functions to be called on the target actor. Functions need to be parameter-less and with "CallInEditor" flag enabled.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``property_override_descriptions`` (Array[PCGObjectPropertyOverrideDescription]):  [Read-Write] Override the default property values on the target actor. Applied before post-process functions.
- ``seed`` (int32):  [Read-Write]
- ``silence_error_on_empty_object_path`` (bool):  [Read-Write] Opt-in option to silence errors when the path is Empty or nothing to extract.
- ``synchronous_load`` (bool):  [Read-Write] By default, object loading is asynchronous, can force it synchronous if needed.
- ``target_actor`` (Actor):  [Read-Write]
  deprecated: TargetActor has been deprecated; pass data directly to the 'In' pin instead.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGApplyOnActorSettings.object_reference_attribute"></a>

#### object_reference_attribute

```python
@property
def object_reference_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] If something is connected in the In pin, will look for this attribute values to load, representing the object reference.

<a id="unreal.PCGApplyOnActorSettings.object_reference_attribute"></a>

#### object_reference_attribute

```python
@object_reference_attribute.setter
def object_reference_attribute(
        value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGApplyOnActorSettings.target_actor"></a>

#### target_actor

```python
@property
def target_actor() -> Actor
```

(Actor):  [Read-Write]
deprecated: TargetActor has been deprecated; pass data directly to the 'In' pin instead.

<a id="unreal.PCGApplyOnActorSettings.target_actor"></a>

#### target_actor

```python
@target_actor.setter
def target_actor(value: Actor) -> None
```

<a id="unreal.PCGApplyOnActorSettings.property_override_descriptions"></a>

#### property_override_descriptions

```python
@property
def property_override_descriptions(
) -> Array[PCGObjectPropertyOverrideDescription]
```

(Array[PCGObjectPropertyOverrideDescription]):  [Read-Write] Override the default property values on the target actor. Applied before post-process functions.

<a id="unreal.PCGApplyOnActorSettings.property_override_descriptions"></a>

#### property_override_descriptions

```python
@property_override_descriptions.setter
def property_override_descriptions(
        value: Array[PCGObjectPropertyOverrideDescription]) -> None
```

<a id="unreal.PCGApplyOnActorSettings.post_process_function_names"></a>

#### post_process_function_names

```python
@property
def post_process_function_names() -> Array[Name]
```

(Array[Name]):  [Read-Write] Specify a list of functions to be called on the target actor. Functions need to be parameter-less and with "CallInEditor" flag enabled.

<a id="unreal.PCGApplyOnActorSettings.post_process_function_names"></a>

#### post_process_function_names

```python
@post_process_function_names.setter
def post_process_function_names(value: Array[Name]) -> None
```

<a id="unreal.PCGApplyOnActorSettings.silence_error_on_empty_object_path"></a>

#### silence_error_on_empty_object_path

```python
@property
def silence_error_on_empty_object_path() -> bool
```

(bool):  [Read-Write] Opt-in option to silence errors when the path is Empty or nothing to extract.

<a id="unreal.PCGApplyOnActorSettings.silence_error_on_empty_object_path"></a>

#### silence_error_on_empty_object_path

```python
@silence_error_on_empty_object_path.setter
def silence_error_on_empty_object_path(value: bool) -> None
```

<a id="unreal.PCGApplyOnActorSettings.synchronous_load"></a>

#### synchronous_load

```python
@property
def synchronous_load() -> bool
```

(bool):  [Read-Write] By default, object loading is asynchronous, can force it synchronous if needed.

<a id="unreal.PCGApplyOnActorSettings.synchronous_load"></a>

#### synchronous_load

```python
@synchronous_load.setter
def synchronous_load(value: bool) -> None
```

<a id="unreal.PCGApplyScaleToBoundsSettings"></a>