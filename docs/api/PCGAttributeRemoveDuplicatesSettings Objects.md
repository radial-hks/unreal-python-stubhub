## PCGAttributeRemoveDuplicatesSettings Objects

```python
class PCGAttributeRemoveDuplicatesSettings(PCGSettings)
```

Remove duplicates for given attributes

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGAttributeRemoveDuplicates.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attribute_selectors`` (Array[PCGAttributePropertyInputSelector]):  [Read-Write] The data will be partitioned on these selected attributes, and we will only keep the first entry for each partition.
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
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGAttributeRemoveDuplicatesSettings.attribute_selectors"></a>

#### attribute_selectors

```python
@property
def attribute_selectors() -> Array[PCGAttributePropertyInputSelector]
```

(Array[PCGAttributePropertyInputSelector]):  [Read-Write] The data will be partitioned on these selected attributes, and we will only keep the first entry for each partition.

<a id="unreal.PCGAttributeRemoveDuplicatesSettings.attribute_selectors"></a>

#### attribute_selectors

```python
@attribute_selectors.setter
def attribute_selectors(
        value: Array[PCGAttributePropertyInputSelector]) -> None
```

<a id="unreal.PCGCopyAttributesSettings"></a>