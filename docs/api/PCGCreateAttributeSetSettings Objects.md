## PCGCreateAttributeSetSettings Objects

```python
class PCGCreateAttributeSetSettings(PCGSettings)
```

Creates a new Attribute Set.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCreateAttribute.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attribute_types`` (PCGMetadataTypesConstantStruct):  [Read-Write]
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
- ``output_target`` (PCGAttributePropertyOutputNoSourceSelector):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGCreateAttributeSetSettings.attribute_types"></a>

#### attribute_types

```python
@property
def attribute_types() -> PCGMetadataTypesConstantStruct
```

(PCGMetadataTypesConstantStruct):  [Read-Write]

<a id="unreal.PCGCreateAttributeSetSettings.attribute_types"></a>

#### attribute_types

```python
@attribute_types.setter
def attribute_types(value: PCGMetadataTypesConstantStruct) -> None
```

<a id="unreal.PCGCreateAttributeSetSettings.output_target"></a>

#### output_target

```python
@property
def output_target() -> PCGAttributePropertyOutputNoSourceSelector
```

(PCGAttributePropertyOutputNoSourceSelector):  [Read-Write]

<a id="unreal.PCGCreateAttributeSetSettings.output_target"></a>

#### output_target

```python
@output_target.setter
def output_target(value: PCGAttributePropertyOutputNoSourceSelector) -> None
```

<a id="unreal.PCGCreateCollisionDataSettings"></a>