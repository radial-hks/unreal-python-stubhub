## PCGAttributeGetFromPointIndexSettings Objects

```python
class PCGAttributeGetFromPointIndexSettings(PCGSettings)
```

Get the attribute/property of a point given its index. The result will be in a ParamData.
There is also a second output that will output the selected point. This point will be output
even if the property/attribute doesn't exist.

The Index can be overridden by a second Params input.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGAttributeGetFromPointIndexElement.h

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
- ``index`` (int32):  [Read-Write]
- ``input_source`` (PCGAttributePropertyInputSelector):  [Read-Write]
- ``output_attribute_name`` (Name):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGAttributeGetFromPointIndexSettings.input_source"></a>

#### input_source

```python
@property
def input_source() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write]

<a id="unreal.PCGAttributeGetFromPointIndexSettings.input_source"></a>

#### input_source

```python
@input_source.setter
def input_source(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGAttributeGetFromPointIndexSettings.index"></a>

#### index

```python
@property
def index() -> int
```

(int32):  [Read-Write]

<a id="unreal.PCGAttributeGetFromPointIndexSettings.index"></a>

#### index

```python
@index.setter
def index(value: int) -> None
```

<a id="unreal.PCGAttributeGetFromPointIndexSettings.output_attribute_name"></a>

#### output_attribute_name

```python
@property
def output_attribute_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.PCGAttributeGetFromPointIndexSettings.output_attribute_name"></a>

#### output_attribute_name

```python
@output_attribute_name.setter
def output_attribute_name(value: Name) -> None
```

<a id="unreal.PCGAttributeNoiseSettings"></a>