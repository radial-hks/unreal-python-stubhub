## PCGMetadataMakeVectorSettings Objects

```python
class PCGMetadataMakeVectorSettings(PCGMetadataSettingsBase)
```

PCGMetadata Make Vector Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGMetadataMakeVector.h

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
- ``input_source1`` (PCGAttributePropertyInputSelector):  [Read-Write]
- ``input_source2`` (PCGAttributePropertyInputSelector):  [Read-Write]
- ``input_source3`` (PCGAttributePropertyInputSelector):  [Read-Write]
- ``input_source4`` (PCGAttributePropertyInputSelector):  [Read-Write]
- ``make_vector3_op`` (PCGMetadataMakeVector3):  [Read-Write]
- ``make_vector4_op`` (PCGMetadataMakeVector4):  [Read-Write]
- ``output_data_from_pin`` (Name):  [Read-Write] By default, output is taken from first non-param pin (aka if the second pin is a point data, the output will be this point data). You can change it to any available input pin.
- ``output_target`` (PCGAttributePropertyOutputSelector):  [Read-Write]
- ``output_type`` (PCGMetadataTypes):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGMetadataMakeVectorSettings.input_source1"></a>

#### input_source1

```python
@property
def input_source1() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write]

<a id="unreal.PCGMetadataMakeVectorSettings.input_source1"></a>

#### input_source1

```python
@input_source1.setter
def input_source1(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGMetadataMakeVectorSettings.input_source2"></a>

#### input_source2

```python
@property
def input_source2() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write]

<a id="unreal.PCGMetadataMakeVectorSettings.input_source2"></a>

#### input_source2

```python
@input_source2.setter
def input_source2(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGMetadataMakeVectorSettings.input_source3"></a>

#### input_source3

```python
@property
def input_source3() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write]

<a id="unreal.PCGMetadataMakeVectorSettings.input_source3"></a>

#### input_source3

```python
@input_source3.setter
def input_source3(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGMetadataMakeVectorSettings.input_source4"></a>

#### input_source4

```python
@property
def input_source4() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write]

<a id="unreal.PCGMetadataMakeVectorSettings.input_source4"></a>

#### input_source4

```python
@input_source4.setter
def input_source4(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGMetadataMakeVectorSettings.output_type"></a>

#### output_type

```python
@property
def output_type() -> PCGMetadataTypes
```

(PCGMetadataTypes):  [Read-Write]

<a id="unreal.PCGMetadataMakeVectorSettings.output_type"></a>

#### output_type

```python
@output_type.setter
def output_type(value: PCGMetadataTypes) -> None
```

<a id="unreal.PCGMetadataMakeVectorSettings.make_vector3_op"></a>

#### make_vector3_op

```python
@property
def make_vector3_op() -> PCGMetadataMakeVector3
```

(PCGMetadataMakeVector3):  [Read-Write]

<a id="unreal.PCGMetadataMakeVectorSettings.make_vector3_op"></a>

#### make_vector3_op

```python
@make_vector3_op.setter
def make_vector3_op(value: PCGMetadataMakeVector3) -> None
```

<a id="unreal.PCGMetadataMakeVectorSettings.make_vector4_op"></a>

#### make_vector4_op

```python
@property
def make_vector4_op() -> PCGMetadataMakeVector4
```

(PCGMetadataMakeVector4):  [Read-Write]

<a id="unreal.PCGMetadataMakeVectorSettings.make_vector4_op"></a>

#### make_vector4_op

```python
@make_vector4_op.setter
def make_vector4_op(value: PCGMetadataMakeVector4) -> None
```

<a id="unreal.PCGMetadataMathsSettings"></a>