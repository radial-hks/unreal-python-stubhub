## PCGRandomChoiceSettings Objects

```python
class PCGRandomChoiceSettings(PCGSettings)
```

Chooses entries randomly through ratio or a fixed number of entries.
Chosen/Discarded entries will be in the same order than they appear in the input data.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGRandomChoice.h

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
- ``fixed_mode`` (bool):  [Read-Write] Either choose a fixed number of entries, or a ratio of entries.
- ``fixed_number`` (int32):  [Read-Write] Defines the number of entries to keep.
- ``output_discarded_entries`` (bool):  [Read-Write] By default, we output discarded entries. If you don't need them, disable this option.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``ratio`` (float):  [Read-Write] Defines the ratio of entries to keep.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGRandomChoiceSettings.fixed_mode"></a>

#### fixed_mode

```python
@property
def fixed_mode() -> bool
```

(bool):  [Read-Write] Either choose a fixed number of entries, or a ratio of entries.

<a id="unreal.PCGRandomChoiceSettings.fixed_mode"></a>

#### fixed_mode

```python
@fixed_mode.setter
def fixed_mode(value: bool) -> None
```

<a id="unreal.PCGRandomChoiceSettings.fixed_number"></a>

#### fixed_number

```python
@property
def fixed_number() -> int
```

(int32):  [Read-Write] Defines the number of entries to keep.

<a id="unreal.PCGRandomChoiceSettings.fixed_number"></a>

#### fixed_number

```python
@fixed_number.setter
def fixed_number(value: int) -> None
```

<a id="unreal.PCGRandomChoiceSettings.ratio"></a>

#### ratio

```python
@property
def ratio() -> float
```

(float):  [Read-Write] Defines the ratio of entries to keep.

<a id="unreal.PCGRandomChoiceSettings.ratio"></a>

#### ratio

```python
@ratio.setter
def ratio(value: float) -> None
```

<a id="unreal.PCGRandomChoiceSettings.output_discarded_entries"></a>

#### output_discarded_entries

```python
@property
def output_discarded_entries() -> bool
```

(bool):  [Read-Write] By default, we output discarded entries. If you don't need them, disable this option.

<a id="unreal.PCGRandomChoiceSettings.output_discarded_entries"></a>

#### output_discarded_entries

```python
@output_discarded_entries.setter
def output_discarded_entries(value: bool) -> None
```

<a id="unreal.PCGRandomChoiceSettings.b_output_discarded_points"></a>

#### b_output_discarded_points

```python
@property
def b_output_discarded_points() -> bool
```

deprecated: 'b_output_discarded_points' was renamed to 'output_discarded_entries'.

<a id="unreal.PCGRandomChoiceSettings.b_output_discarded_points"></a>

#### b_output_discarded_points

```python
@b_output_discarded_points.setter
def b_output_discarded_points(value: bool) -> None
```

<a id="unreal.PCGReplaceTagsSettings"></a>