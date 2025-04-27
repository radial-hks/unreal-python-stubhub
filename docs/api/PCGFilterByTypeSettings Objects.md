## PCGFilterByTypeSettings Objects

```python
class PCGFilterByTypeSettings(PCGFilterDataBaseSettings)
```

Filters an input collection based on data type.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGFilterByType.h

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
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``show_outside_filter`` (bool):  [Read-Write]
- ``target_type`` (PCGDataType):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGFilterByTypeSettings.target_type"></a>

#### target_type

```python
@property
def target_type() -> PCGDataType
```

(PCGDataType):  [Read-Write]

<a id="unreal.PCGFilterByTypeSettings.target_type"></a>

#### target_type

```python
@target_type.setter
def target_type(value: PCGDataType) -> None
```

<a id="unreal.PCGFilterByTypeSettings.show_outside_filter"></a>

#### show_outside_filter

```python
@property
def show_outside_filter() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGFilterByTypeSettings.show_outside_filter"></a>

#### show_outside_filter

```python
@show_outside_filter.setter
def show_outside_filter(value: bool) -> None
```

<a id="unreal.PCGGetTagsSettings"></a>