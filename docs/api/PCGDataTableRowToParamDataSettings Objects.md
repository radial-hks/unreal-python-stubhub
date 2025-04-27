## PCGDataTableRowToParamDataSettings Objects

```python
class PCGDataTableRowToParamDataSettings(PCGSettings)
```

PCGData Table Row to Param Data Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGDataTableRowToParamData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``data_table`` (DataTable):  [Read-Write] the data table to copy from
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
- ``row_name`` (Name):  [Read-Write] The name of the row to copy from
- ``seed`` (int32):  [Read-Write]
- ``synchronous_load`` (bool):  [Read-Write] By default, data table loading is asynchronous, can force it synchronous if needed.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGDataTableRowToParamDataSettings.row_name"></a>

#### row_name

```python
@property
def row_name() -> Name
```

(Name):  [Read-Write] The name of the row to copy from

<a id="unreal.PCGDataTableRowToParamDataSettings.row_name"></a>

#### row_name

```python
@row_name.setter
def row_name(value: Name) -> None
```

<a id="unreal.PCGDataTableRowToParamDataSettings.data_table"></a>

#### data_table

```python
@property
def data_table() -> DataTable
```

(DataTable):  [Read-Write] the data table to copy from

<a id="unreal.PCGDataTableRowToParamDataSettings.data_table"></a>

#### data_table

```python
@data_table.setter
def data_table(value: DataTable) -> None
```

<a id="unreal.PCGDataTableRowToParamDataSettings.synchronous_load"></a>

#### synchronous_load

```python
@property
def synchronous_load() -> bool
```

(bool):  [Read-Write] By default, data table loading is asynchronous, can force it synchronous if needed.

<a id="unreal.PCGDataTableRowToParamDataSettings.synchronous_load"></a>

#### synchronous_load

```python
@synchronous_load.setter
def synchronous_load(value: bool) -> None
```

<a id="unreal.PCGDebugSettings"></a>