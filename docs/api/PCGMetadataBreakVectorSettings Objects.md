## PCGMetadataBreakVectorSettings Objects

```python
class PCGMetadataBreakVectorSettings(PCGMetadataSettingsBase)
```

PCGMetadata Break Vector Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGMetadataBreakVector.h

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
- ``output_data_from_pin`` (Name):  [Read-Write] By default, output is taken from first non-param pin (aka if the second pin is a point data, the output will be this point data). You can change it to any available input pin.
- ``output_target`` (PCGAttributePropertyOutputSelector):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGMetadataBreakVectorSettings.input_source"></a>

#### input_source

```python
@property
def input_source() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write]

<a id="unreal.PCGMetadataBreakVectorSettings.input_source"></a>

#### input_source

```python
@input_source.setter
def input_source(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGMetadataCompareSettings"></a>