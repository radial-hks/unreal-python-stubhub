## PCGGetPropertyFromObjectPathSettings Objects

```python
class PCGGetPropertyFromObjectPathSettings(PCGSettings)
```

Extract property from a list of soft object paths.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGGetPropertyFromObjectPath.h

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
- ``input_source`` (PCGAttributePropertyInputSelector):  [Read-Write] If something is connected in the In pin, will look for this attribute values to load.
- ``object_paths_to_extract`` (Array[SoftObjectPath]):  [Read-Write] If nothing is connected in the In pin, will use those static paths to load.
- ``output_attribute_name`` (Name):  [Read-Write] By default, attribute name will be None, but it can be overridden by this name. Use
  SourceName: to use the property name (only works when not extracting). In the case of multiple properties being extracted, will be ignored.
- ``persist_all_data`` (bool):  [Read-Write] Opt-in option to create empty data when there is nothing to extract or property is not found, to have the same number of inputs than outputs.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``property_name`` (Name):  [Read-Write] Property name to extract. Can only extract properties that are compatible with metadata types. If None, extract the object.
- ``seed`` (int32):  [Read-Write]
- ``silence_error_on_empty_object_path`` (bool):  [Read-Write] Opt-in option to silence errors when the path is Empty or nothing to extract.
- ``synchronous_load`` (bool):  [Read-Write] By default, object loading is asynchronous, can force it synchronous if needed.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGGetPropertyFromObjectPathSettings.object_paths_to_extract"></a>

#### object_paths_to_extract

```python
@property
def object_paths_to_extract() -> Array[SoftObjectPath]
```

(Array[SoftObjectPath]):  [Read-Write] If nothing is connected in the In pin, will use those static paths to load.

<a id="unreal.PCGGetPropertyFromObjectPathSettings.object_paths_to_extract"></a>

#### object_paths_to_extract

```python
@object_paths_to_extract.setter
def object_paths_to_extract(value: Array[SoftObjectPath]) -> None
```

<a id="unreal.PCGGetPropertyFromObjectPathSettings.input_source"></a>

#### input_source

```python
@property
def input_source() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] If something is connected in the In pin, will look for this attribute values to load.

<a id="unreal.PCGGetPropertyFromObjectPathSettings.input_source"></a>

#### input_source

```python
@input_source.setter
def input_source(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGGetPropertyFromObjectPathSettings.property_name"></a>

#### property_name

```python
@property
def property_name() -> Name
```

(Name):  [Read-Write] Property name to extract. Can only extract properties that are compatible with metadata types. If None, extract the object.

<a id="unreal.PCGGetPropertyFromObjectPathSettings.property_name"></a>

#### property_name

```python
@property_name.setter
def property_name(value: Name) -> None
```

<a id="unreal.PCGGetPropertyFromObjectPathSettings.force_object_and_struct_extraction"></a>

#### force_object_and_struct_extraction

```python
@property
def force_object_and_struct_extraction() -> bool
```

(bool):  [Read-Write] If the property is a struct/object supported by metadata, this option can be toggled to force extracting all (compatible) properties contained in this property. Automatically true if unsupported by metadata. For now, only supports direct child properties (and not deeper).

<a id="unreal.PCGGetPropertyFromObjectPathSettings.force_object_and_struct_extraction"></a>

#### force_object_and_struct_extraction

```python
@force_object_and_struct_extraction.setter
def force_object_and_struct_extraction(value: bool) -> None
```

<a id="unreal.PCGGetPropertyFromObjectPathSettings.output_attribute_name"></a>

#### output_attribute_name

```python
@property
def output_attribute_name() -> Name
```

(Name):  [Read-Write] By default, attribute name will be None, but it can be overridden by this name. Use
SourceName: to use the property name (only works when not extracting). In the case of multiple properties being extracted, will be ignored.

<a id="unreal.PCGGetPropertyFromObjectPathSettings.output_attribute_name"></a>

#### output_attribute_name

```python
@output_attribute_name.setter
def output_attribute_name(value: Name) -> None
```

<a id="unreal.PCGGetPropertyFromObjectPathSettings.synchronous_load"></a>

#### synchronous_load

```python
@property
def synchronous_load() -> bool
```

(bool):  [Read-Write] By default, object loading is asynchronous, can force it synchronous if needed.

<a id="unreal.PCGGetPropertyFromObjectPathSettings.synchronous_load"></a>

#### synchronous_load

```python
@synchronous_load.setter
def synchronous_load(value: bool) -> None
```

<a id="unreal.PCGGetPropertyFromObjectPathSettings.persist_all_data"></a>

#### persist_all_data

```python
@property
def persist_all_data() -> bool
```

(bool):  [Read-Write] Opt-in option to create empty data when there is nothing to extract or property is not found, to have the same number of inputs than outputs.

<a id="unreal.PCGGetPropertyFromObjectPathSettings.persist_all_data"></a>

#### persist_all_data

```python
@persist_all_data.setter
def persist_all_data(value: bool) -> None
```

<a id="unreal.PCGGetPropertyFromObjectPathSettings.silence_error_on_empty_object_path"></a>

#### silence_error_on_empty_object_path

```python
@property
def silence_error_on_empty_object_path() -> bool
```

(bool):  [Read-Write] Opt-in option to silence errors when the path is Empty or nothing to extract.

<a id="unreal.PCGGetPropertyFromObjectPathSettings.silence_error_on_empty_object_path"></a>

#### silence_error_on_empty_object_path

```python
@silence_error_on_empty_object_path.setter
def silence_error_on_empty_object_path(value: bool) -> None
```

<a id="unreal.PCGGraphAuthoringTestHelperSettings"></a>