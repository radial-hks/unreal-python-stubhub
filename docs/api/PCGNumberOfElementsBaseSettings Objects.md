## PCGNumberOfElementsBaseSettings Objects

```python
class PCGNumberOfElementsBaseSettings(PCGSettings)
```

Elements for getting the number of elements in a point data or a param data. Since the whole logic is identical
except for getting the number of elements, it is factorized in a base class.
// Base class for common elements

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGNumberOfElements.h

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
- ``output_attribute_name`` (Name):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGNumberOfElementsBaseSettings.output_attribute_name"></a>

#### output_attribute_name

```python
@property
def output_attribute_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.PCGNumberOfElementsBaseSettings.output_attribute_name"></a>

#### output_attribute_name

```python
@output_attribute_name.setter
def output_attribute_name(value: Name) -> None
```

<a id="unreal.PCGNumberOfPointsSettings"></a>