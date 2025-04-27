## PCGSanityCheckPointDataSettings Objects

```python
class PCGSanityCheckPointDataSettings(PCGSettings)
```

PCGSanity Check Point Data Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSanityCheckPointData.h

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
- ``max_point_count`` (int32):  [Read-Write]
- ``min_point_count`` (int32):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGSanityCheckPointDataSettings.min_point_count"></a>

#### min_point_count

```python
@property
def min_point_count() -> int
```

(int32):  [Read-Write]

<a id="unreal.PCGSanityCheckPointDataSettings.min_point_count"></a>

#### min_point_count

```python
@min_point_count.setter
def min_point_count(value: int) -> None
```

<a id="unreal.PCGSanityCheckPointDataSettings.max_point_count"></a>

#### max_point_count

```python
@property
def max_point_count() -> int
```

(int32):  [Read-Write]

<a id="unreal.PCGSanityCheckPointDataSettings.max_point_count"></a>

#### max_point_count

```python
@max_point_count.setter
def max_point_count(value: int) -> None
```

<a id="unreal.PCGDataCollectionExporter"></a>