## PCGFilterElementsByIndexSettings Objects

```python
class PCGFilterElementsByIndexSettings(PCGSettings)
```

Filters points or the elements of an attribute set based on a second input of points, attribute sets, or a user-defined index range expression.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGFilterElementsByIndex.h

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
- ``index_selection_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] The attribute which will define the indices to filter.
- ``invert_filter`` (bool):  [Read-Write] Will invert which indices will be included and excluded.
- ``output_discarded_elements`` (bool):  [Read-Write] An additional output for discarded elements.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``select_indices_by_input`` (bool):  [Read-Write] A second input will define the indices to filter.
- ``selected_indices`` (str):  [Read-Write] Selected individual indices or index ranges to include or exclude. Negative end indices allowed.
  For example, on an array of size 10: '0,2,4:5,7:-1' will include indices: 0,2,4,7,8.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGFilterElementsByIndexSettings.select_indices_by_input"></a>

#### select_indices_by_input

```python
@property
def select_indices_by_input() -> bool
```

(bool):  [Read-Write] A second input will define the indices to filter.

<a id="unreal.PCGFilterElementsByIndexSettings.select_indices_by_input"></a>

#### select_indices_by_input

```python
@select_indices_by_input.setter
def select_indices_by_input(value: bool) -> None
```

<a id="unreal.PCGFilterElementsByIndexSettings.index_selection_attribute"></a>

#### index_selection_attribute

```python
@property
def index_selection_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] The attribute which will define the indices to filter.

<a id="unreal.PCGFilterElementsByIndexSettings.index_selection_attribute"></a>

#### index_selection_attribute

```python
@index_selection_attribute.setter
def index_selection_attribute(
        value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGFilterElementsByIndexSettings.selected_indices"></a>

#### selected_indices

```python
@property
def selected_indices() -> str
```

(str):  [Read-Write] Selected individual indices or index ranges to include or exclude. Negative end indices allowed.
For example, on an array of size 10: '0,2,4:5,7:-1' will include indices: 0,2,4,7,8.

<a id="unreal.PCGFilterElementsByIndexSettings.selected_indices"></a>

#### selected_indices

```python
@selected_indices.setter
def selected_indices(value: str) -> None
```

<a id="unreal.PCGFilterElementsByIndexSettings.output_discarded_elements"></a>

#### output_discarded_elements

```python
@property
def output_discarded_elements() -> bool
```

(bool):  [Read-Write] An additional output for discarded elements.

<a id="unreal.PCGFilterElementsByIndexSettings.output_discarded_elements"></a>

#### output_discarded_elements

```python
@output_discarded_elements.setter
def output_discarded_elements(value: bool) -> None
```

<a id="unreal.PCGFilterElementsByIndexSettings.invert_filter"></a>

#### invert_filter

```python
@property
def invert_filter() -> bool
```

(bool):  [Read-Write] Will invert which indices will be included and excluded.

<a id="unreal.PCGFilterElementsByIndexSettings.invert_filter"></a>

#### invert_filter

```python
@invert_filter.setter
def invert_filter(value: bool) -> None
```

<a id="unreal.PCGGatherSettings"></a>