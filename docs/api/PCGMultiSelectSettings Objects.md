## PCGMultiSelectSettings Objects

```python
class PCGMultiSelectSettings(PCGSettings)
```

Selects data from any number of input pins, based on a static selection criteria (Int/String/Enum)

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGMultiSelect.h

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
- ``enum_selection`` (EnumSelector):  [Read-Write] Determines which input pin will be selected if the selection mode is Enum.
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``int_options`` (Array[int32]):  [Read-Write] Determines the available input pin selection options.
- ``integer_selection`` (int32):  [Read-Write] Determines which input will be selected if the selection mode is Integer.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``selection_mode`` (PCGControlFlowSelectionMode):  [Read-Write] Determines the type of value to be used to select an input.
- ``string_options`` (Array[str]):  [Read-Write] Determines the available input pin selection options.
- ``string_selection`` (str):  [Read-Write] Determines which input will be selected if the selection mode is String.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGMultiSelectSettings.selection_mode"></a>

#### selection_mode

```python
@property
def selection_mode() -> PCGControlFlowSelectionMode
```

(PCGControlFlowSelectionMode):  [Read-Write] Determines the type of value to be used to select an input.

<a id="unreal.PCGMultiSelectSettings.selection_mode"></a>

#### selection_mode

```python
@selection_mode.setter
def selection_mode(value: PCGControlFlowSelectionMode) -> None
```

<a id="unreal.PCGMultiSelectSettings.integer_selection"></a>

#### integer_selection

```python
@property
def integer_selection() -> int
```

(int32):  [Read-Write] Determines which input will be selected if the selection mode is Integer.

<a id="unreal.PCGMultiSelectSettings.integer_selection"></a>

#### integer_selection

```python
@integer_selection.setter
def integer_selection(value: int) -> None
```

<a id="unreal.PCGMultiSelectSettings.int_options"></a>

#### int_options

```python
@property
def int_options() -> Array[int]
```

(Array[int32]):  [Read-Write] Determines the available input pin selection options.

<a id="unreal.PCGMultiSelectSettings.int_options"></a>

#### int_options

```python
@int_options.setter
def int_options(value: Array[int]) -> None
```

<a id="unreal.PCGMultiSelectSettings.string_selection"></a>

#### string_selection

```python
@property
def string_selection() -> str
```

(str):  [Read-Write] Determines which input will be selected if the selection mode is String.

<a id="unreal.PCGMultiSelectSettings.string_selection"></a>

#### string_selection

```python
@string_selection.setter
def string_selection(value: str) -> None
```

<a id="unreal.PCGMultiSelectSettings.string_options"></a>

#### string_options

```python
@property
def string_options() -> Array[str]
```

(Array[str]):  [Read-Write] Determines the available input pin selection options.

<a id="unreal.PCGMultiSelectSettings.string_options"></a>

#### string_options

```python
@string_options.setter
def string_options(value: Array[str]) -> None
```

<a id="unreal.PCGMultiSelectSettings.enum_selection"></a>

#### enum_selection

```python
@property
def enum_selection() -> EnumSelector
```

(EnumSelector):  [Read-Write] Determines which input pin will be selected if the selection mode is Enum.

<a id="unreal.PCGMultiSelectSettings.enum_selection"></a>

#### enum_selection

```python
@enum_selection.setter
def enum_selection(value: EnumSelector) -> None
```

<a id="unreal.PCGMutateSeedSettings"></a>