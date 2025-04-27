## PCGFilterByIndexSettings Objects

```python
class PCGFilterByIndexSettings(PCGFilterDataBaseSettings)
```

Filters a data collection based on a user defined index range expression.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGFilterByIndex.h

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
- ``invert_filter`` (bool):  [Read-Write] Will invert which indices will be included and excluded.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``selected_indices`` (str):  [Read-Write] Selected individual indices or index ranges to include or exclude. Negative end indices allowed.
  For example, on an array of size 10: '0,2,4:5,7:-1' will include indices: 0,2,4,7,8
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGFilterByIndexSettings.invert_filter"></a>

#### invert_filter

```python
@property
def invert_filter() -> bool
```

(bool):  [Read-Write] Will invert which indices will be included and excluded.

<a id="unreal.PCGFilterByIndexSettings.invert_filter"></a>

#### invert_filter

```python
@invert_filter.setter
def invert_filter(value: bool) -> None
```

<a id="unreal.PCGFilterByIndexSettings.selected_indices"></a>

#### selected_indices

```python
@property
def selected_indices() -> str
```

(str):  [Read-Write] Selected individual indices or index ranges to include or exclude. Negative end indices allowed.
For example, on an array of size 10: '0,2,4:5,7:-1' will include indices: 0,2,4,7,8

<a id="unreal.PCGFilterByIndexSettings.selected_indices"></a>

#### selected_indices

```python
@selected_indices.setter
def selected_indices(value: str) -> None
```

<a id="unreal.PCGFilterByTagSettings"></a>