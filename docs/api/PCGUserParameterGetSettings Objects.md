## PCGUserParameterGetSettings Objects

```python
class PCGUserParameterGetSettings(PCGSettings)
```

Getter for user parameters defined in PCGGraph, by the user.
Will pick up the value from the graph instance.

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
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGUserParameterGetSettings.force_object_and_struct_extraction"></a>

#### force_object_and_struct_extraction

```python
@property
def force_object_and_struct_extraction() -> bool
```

(bool):  [Read-Write] If the property is a struct/object supported by metadata, this option can be toggled to force extracting all (compatible) properties contained in this property. Automatically true if unsupported by metadata. For now, only supports direct child properties (and not deeper).

<a id="unreal.PCGUserParameterGetSettings.force_object_and_struct_extraction"></a>

#### force_object_and_struct_extraction

```python
@force_object_and_struct_extraction.setter
def force_object_and_struct_extraction(value: bool) -> None
```

<a id="unreal.PCGGenericUserParameterGetSettings"></a>