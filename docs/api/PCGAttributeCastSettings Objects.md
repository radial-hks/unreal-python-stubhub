## PCGAttributeCastSettings Objects

```python
class PCGAttributeCastSettings(PCGSettings)
```

Cast an attribute to another type. Support broadcastable cast (like double -> FVector) and constructible cast (like double -> float)

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGAttributeCast.h

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
- ``input_source`` (PCGAttributePropertyInputSelector):  [Read-Write]
- ``output_target`` (PCGAttributePropertyOutputSelector):  [Read-Write]
- ``output_type`` (PCGMetadataTypes):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGAttributeCastSettings.input_source"></a>

#### input_source

```python
@property
def input_source() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write]

<a id="unreal.PCGAttributeCastSettings.input_source"></a>

#### input_source

```python
@input_source.setter
def input_source(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGAttributeCastSettings.output_type"></a>

#### output_type

```python
@property
def output_type() -> PCGMetadataTypes
```

(PCGMetadataTypes):  [Read-Write]

<a id="unreal.PCGAttributeCastSettings.output_type"></a>

#### output_type

```python
@output_type.setter
def output_type(value: PCGMetadataTypes) -> None
```

<a id="unreal.PCGAttributeCastSettings.output_target"></a>

#### output_target

```python
@property
def output_target() -> PCGAttributePropertyOutputSelector
```

(PCGAttributePropertyOutputSelector):  [Read-Write]

<a id="unreal.PCGAttributeCastSettings.output_target"></a>

#### output_target

```python
@output_target.setter
def output_target(value: PCGAttributePropertyOutputSelector) -> None
```

<a id="unreal.PCGAttributeFilteringSettings"></a>