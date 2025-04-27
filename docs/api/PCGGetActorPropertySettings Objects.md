## PCGGetActorPropertySettings Objects

```python
class PCGGetActorPropertySettings(PCGSettings)
```

Extract a property value from an actor/component into a ParamData.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGGetActorProperty.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_selector`` (PCGActorSelectorSettings):  [Read-Write]
- ``always_requery_actors`` (bool):  [Read-Write] If this is true, we will never put this element in cache, and will always try to re-query the actors and read the latest properties from them.
- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``component_class`` (type(Class)):  [Read-Write] If we are looking for an actor component, the class can be specified here.
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
- ``force_object_and_struct_extraction`` (bool):  [Read-Write] If the property is a struct/object supported by metadata, this option can be toggled to force extracting all (compatible) properties contained in this property. Automatically true if unsupported by metadata. For now, only supports direct child properties (and not deeper).
- ``output_actor_reference`` (bool):  [Read-Write] Controls whether an actor reference attribute will be added to the result
- ``output_attribute_name`` (Name):  [Read-Write] By default, attribute name will be None, but it can be overridden by this name. Use
  SourceName: to use the property name (only works when not extracting). Will be ignored if multiple properties are extracted at the same time.
- ``output_component_reference`` (bool):  [Read-Write] Controls whether a component reference attribute will be added to the result
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``process_all_components`` (bool):  [Read-Write] Process all Actor components. If not set, only the first component found will be processed.
- ``property_name`` (Name):  [Read-Write] Property name to extract. Can only extract properties that are compatible with metadata types. If None, extract the actor/component directly. Can be a comma-separated list, assuming they have the same cardinality.
- ``seed`` (int32):  [Read-Write]
- ``select_component`` (bool):  [Read-Write] Allow to look for an actor component instead of an actor. It will need to be attached to the found actor.
- ``track_actors_only_within_bounds`` (bool):  [Read-Write] If this is checked, found actors that are outside component bounds will not trigger a refresh. Only works for tags for now in editor.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGGetActorPropertySettings.actor_selector"></a>

#### actor_selector

```python
@property
def actor_selector() -> PCGActorSelectorSettings
```

(PCGActorSelectorSettings):  [Read-Write]

<a id="unreal.PCGGetActorPropertySettings.actor_selector"></a>

#### actor_selector

```python
@actor_selector.setter
def actor_selector(value: PCGActorSelectorSettings) -> None
```

<a id="unreal.PCGGetActorPropertySettings.select_component"></a>

#### select_component

```python
@property
def select_component() -> bool
```

(bool):  [Read-Write] Allow to look for an actor component instead of an actor. It will need to be attached to the found actor.

<a id="unreal.PCGGetActorPropertySettings.select_component"></a>

#### select_component

```python
@select_component.setter
def select_component(value: bool) -> None
```

<a id="unreal.PCGGetActorPropertySettings.component_class"></a>

#### component_class

```python
@property
def component_class() -> Class
```

(type(Class)):  [Read-Write] If we are looking for an actor component, the class can be specified here.

<a id="unreal.PCGGetActorPropertySettings.component_class"></a>

#### component_class

```python
@component_class.setter
def component_class(value: Class) -> None
```

<a id="unreal.PCGGetActorPropertySettings.process_all_components"></a>

#### process_all_components

```python
@property
def process_all_components() -> bool
```

(bool):  [Read-Write] Process all Actor components. If not set, only the first component found will be processed.

<a id="unreal.PCGGetActorPropertySettings.process_all_components"></a>

#### process_all_components

```python
@process_all_components.setter
def process_all_components(value: bool) -> None
```

<a id="unreal.PCGGetActorPropertySettings.output_component_reference"></a>

#### output_component_reference

```python
@property
def output_component_reference() -> bool
```

(bool):  [Read-Write] Controls whether a component reference attribute will be added to the result

<a id="unreal.PCGGetActorPropertySettings.output_component_reference"></a>

#### output_component_reference

```python
@output_component_reference.setter
def output_component_reference(value: bool) -> None
```

<a id="unreal.PCGGetActorPropertySettings.property_name"></a>

#### property_name

```python
@property
def property_name() -> Name
```

(Name):  [Read-Write] Property name to extract. Can only extract properties that are compatible with metadata types. If None, extract the actor/component directly. Can be a comma-separated list, assuming they have the same cardinality.

<a id="unreal.PCGGetActorPropertySettings.property_name"></a>

#### property_name

```python
@property_name.setter
def property_name(value: Name) -> None
```

<a id="unreal.PCGGetActorPropertySettings.force_object_and_struct_extraction"></a>

#### force_object_and_struct_extraction

```python
@property
def force_object_and_struct_extraction() -> bool
```

(bool):  [Read-Write] If the property is a struct/object supported by metadata, this option can be toggled to force extracting all (compatible) properties contained in this property. Automatically true if unsupported by metadata. For now, only supports direct child properties (and not deeper).

<a id="unreal.PCGGetActorPropertySettings.force_object_and_struct_extraction"></a>

#### force_object_and_struct_extraction

```python
@force_object_and_struct_extraction.setter
def force_object_and_struct_extraction(value: bool) -> None
```

<a id="unreal.PCGGetActorPropertySettings.output_attribute_name"></a>

#### output_attribute_name

```python
@property
def output_attribute_name() -> Name
```

(Name):  [Read-Write] By default, attribute name will be None, but it can be overridden by this name. Use
SourceName: to use the property name (only works when not extracting). Will be ignored if multiple properties are extracted at the same time.

<a id="unreal.PCGGetActorPropertySettings.output_attribute_name"></a>

#### output_attribute_name

```python
@output_attribute_name.setter
def output_attribute_name(value: Name) -> None
```

<a id="unreal.PCGGetActorPropertySettings.output_actor_reference"></a>

#### output_actor_reference

```python
@property
def output_actor_reference() -> bool
```

(bool):  [Read-Write] Controls whether an actor reference attribute will be added to the result

<a id="unreal.PCGGetActorPropertySettings.output_actor_reference"></a>

#### output_actor_reference

```python
@output_actor_reference.setter
def output_actor_reference(value: bool) -> None
```

<a id="unreal.PCGGetActorPropertySettings.always_requery_actors"></a>

#### always_requery_actors

```python
@property
def always_requery_actors() -> bool
```

(bool):  [Read-Write] If this is true, we will never put this element in cache, and will always try to re-query the actors and read the latest properties from them.

<a id="unreal.PCGGetActorPropertySettings.always_requery_actors"></a>

#### always_requery_actors

```python
@always_requery_actors.setter
def always_requery_actors(value: bool) -> None
```

<a id="unreal.PCGGetActorPropertySettings.track_actors_only_within_bounds"></a>

#### track_actors_only_within_bounds

```python
@property
def track_actors_only_within_bounds() -> bool
```

(bool):  [Read-Only] If this is checked, found actors that are outside component bounds will not trigger a refresh. Only works for tags for now in editor.

<a id="unreal.PCGPropertyToParamDataSettings"></a>