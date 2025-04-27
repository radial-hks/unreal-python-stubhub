## PCGGenericUserParameterGetSettings Objects

```python
class PCGGenericUserParameterGetSettings(PCGSettings)
```

Generic getter for user parameter defined in the PCG Graph, by the user.
Will pick up the value from the graph instance.
This getter allows to set manually the user parameter they want to get, and add extractor, the same way than GetActorProperty or GetPropertyFromObjectPath

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGUserParameterGet.h

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
- ``force_object_and_struct_extraction`` (bool):  [Read-Write] If the property is a struct/object supported by metadata, this option can be toggled to force extracting all (compatible) properties contained in this property. Automatically true if unsupported by metadata. For now, only supports direct child properties (and not deeper).
- ``output_attribute_name`` (Name):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``property_path`` (str):  [Read-Write]
- ``quiet`` (bool):  [Read-Write]
- ``seed`` (int32):  [Read-Write]
- ``source`` (PCGUserParameterSource):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGGenericUserParameterGetSettings.property_path"></a>

#### property_path

```python
@property
def property_path() -> str
```

(str):  [Read-Write]

<a id="unreal.PCGGenericUserParameterGetSettings.property_path"></a>

#### property_path

```python
@property_path.setter
def property_path(value: str) -> None
```

<a id="unreal.PCGGenericUserParameterGetSettings.force_object_and_struct_extraction"></a>

#### force_object_and_struct_extraction

```python
@property
def force_object_and_struct_extraction() -> bool
```

(bool):  [Read-Write] If the property is a struct/object supported by metadata, this option can be toggled to force extracting all (compatible) properties contained in this property. Automatically true if unsupported by metadata. For now, only supports direct child properties (and not deeper).

<a id="unreal.PCGGenericUserParameterGetSettings.force_object_and_struct_extraction"></a>

#### force_object_and_struct_extraction

```python
@force_object_and_struct_extraction.setter
def force_object_and_struct_extraction(value: bool) -> None
```

<a id="unreal.PCGGenericUserParameterGetSettings.output_attribute_name"></a>

#### output_attribute_name

```python
@property
def output_attribute_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.PCGGenericUserParameterGetSettings.output_attribute_name"></a>

#### output_attribute_name

```python
@output_attribute_name.setter
def output_attribute_name(value: Name) -> None
```

<a id="unreal.PCGGenericUserParameterGetSettings.source"></a>

#### source

```python
@property
def source() -> PCGUserParameterSource
```

(PCGUserParameterSource):  [Read-Write]

<a id="unreal.PCGGenericUserParameterGetSettings.source"></a>

#### source

```python
@source.setter
def source(value: PCGUserParameterSource) -> None
```

<a id="unreal.PCGGenericUserParameterGetSettings.quiet"></a>

#### quiet

```python
@property
def quiet() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGGenericUserParameterGetSettings.quiet"></a>

#### quiet

```python
@quiet.setter
def quiet(value: bool) -> None
```

<a id="unreal.PCGUserParametersData"></a>