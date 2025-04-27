## PCGAddComponentSettings Objects

```python
class PCGAddComponentSettings(PCGSettings)
```

Creates components and adds them to specified actors.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGAddComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_reference_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] Specifies what attribute is used to derive actor reference
- ``allow_template_component_editing`` (bool):  [Read-Write]
- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``class_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] Specifies component class selection
- ``component_reference_attribute`` (PCGAttributePropertyOutputNoSourceSelector):  [Read-Write] Specifies what attribute to write the component reference to.
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
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``template_component`` (ActorComponent):  [Read-Write]
- ``template_component_class`` (type(Class)):  [Read-Write]
- ``use_class_attribute`` (bool):  [Read-Write] Controls whether component class selection will be done by attribute or from a constant defined in this node.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGAddComponentSettings.use_class_attribute"></a>

#### use_class_attribute

```python
@property
def use_class_attribute() -> bool
```

(bool):  [Read-Write] Controls whether component class selection will be done by attribute or from a constant defined in this node.

<a id="unreal.PCGAddComponentSettings.use_class_attribute"></a>

#### use_class_attribute

```python
@use_class_attribute.setter
def use_class_attribute(value: bool) -> None
```

<a id="unreal.PCGAddComponentSettings.class_attribute"></a>

#### class_attribute

```python
@property
def class_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] Specifies component class selection

<a id="unreal.PCGAddComponentSettings.class_attribute"></a>

#### class_attribute

```python
@class_attribute.setter
def class_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGAddComponentSettings.template_component_class"></a>

#### template_component_class

```python
@property
def template_component_class() -> Class
```

(type(Class)):  [Read-Only]

<a id="unreal.PCGAddComponentSettings.allow_template_component_editing"></a>

#### allow_template_component_editing

```python
@property
def allow_template_component_editing() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGAddComponentSettings.allow_template_component_editing"></a>

#### allow_template_component_editing

```python
@allow_template_component_editing.setter
def allow_template_component_editing(value: bool) -> None
```

<a id="unreal.PCGAddComponentSettings.template_component"></a>

#### template_component

```python
@property
def template_component() -> ActorComponent
```

(ActorComponent):  [Read-Write]

<a id="unreal.PCGAddComponentSettings.template_component"></a>

#### template_component

```python
@template_component.setter
def template_component(value: ActorComponent) -> None
```

<a id="unreal.PCGAddComponentSettings.actor_reference_attribute"></a>

#### actor_reference_attribute

```python
@property
def actor_reference_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] Specifies what attribute is used to derive actor reference

<a id="unreal.PCGAddComponentSettings.actor_reference_attribute"></a>

#### actor_reference_attribute

```python
@actor_reference_attribute.setter
def actor_reference_attribute(
        value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGAddComponentSettings.component_reference_attribute"></a>

#### component_reference_attribute

```python
@property
def component_reference_attribute(
) -> PCGAttributePropertyOutputNoSourceSelector
```

(PCGAttributePropertyOutputNoSourceSelector):  [Read-Write] Specifies what attribute to write the component reference to.

<a id="unreal.PCGAddComponentSettings.component_reference_attribute"></a>

#### component_reference_attribute

```python
@component_reference_attribute.setter
def component_reference_attribute(
        value: PCGAttributePropertyOutputNoSourceSelector) -> None
```

<a id="unreal.PCGAddTagSettings"></a>