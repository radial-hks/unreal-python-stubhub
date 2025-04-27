## PCGMetadataSettingsBase Objects

```python
class PCGMetadataSettingsBase(PCGSettings)
```

Base class for all Metadata operations.
Metadata operation can work with attributes or properties. For example you could compute the addition between all points density and a constant from
a param data.
The output will be the duplication of the first spatial input (by default - can be overridden by OutputDataFromPin),
with the same metadata + the result of the operation (either in an attribute or a property).

The new attribute can collide with one of the attributes in the incoming metadata. In this case, the attribute value will be overridden by the result
of the operation. It will also override the type of the attribute if it doesn't match the original.

We only support operations between points and between spatial data. They all need to match (or be a param data)
For example, if input 0 is a point data and input 1 is a spatial data, we fail.

You can specify the name of the attribute for each input and for the output.
If the input name is None, it will take the lastest attribute in the input metadata.
If the output name is None, it will take the input name.

Each operation has some requirements for the input types, and can broadcast some values into others (example Vector + Float -> Vector).
For example, if the op only accept booleans, all other value types will throw an error.

If there are multiple values for an attribute, the operation will be done on all values. If one input has N elements and the second has 1 element,
the second will be repeated for each element of the first for the operation. We only support N-N operations and N-1 operation (ie. The number of values
needs to be all the same or 1)

If the node doesn't provide an output, check the logs to know why it failed.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGMetadataOpElementBase.h

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
- ``output_data_from_pin`` (Name):  [Read-Write] By default, output is taken from first non-param pin (aka if the second pin is a point data, the output will be this point data). You can change it to any available input pin.
- ``output_target`` (PCGAttributePropertyOutputSelector):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGMetadataSettingsBase.output_target"></a>

#### output_target

```python
@property
def output_target() -> PCGAttributePropertyOutputSelector
```

(PCGAttributePropertyOutputSelector):  [Read-Write]

<a id="unreal.PCGMetadataSettingsBase.output_target"></a>

#### output_target

```python
@output_target.setter
def output_target(value: PCGAttributePropertyOutputSelector) -> None
```

<a id="unreal.PCGMetadataSettingsBase.output_data_from_pin"></a>

#### output_data_from_pin

```python
@property
def output_data_from_pin() -> Name
```

(Name):  [Read-Write] By default, output is taken from first non-param pin (aka if the second pin is a point data, the output will be this point data). You can change it to any available input pin.

<a id="unreal.PCGMetadataSettingsBase.output_data_from_pin"></a>

#### output_data_from_pin

```python
@output_data_from_pin.setter
def output_data_from_pin(value: Name) -> None
```

<a id="unreal.PCGAttributeRemapSettings"></a>