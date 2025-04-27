## PCGDeleteTagsSettings Objects

```python
class PCGDeleteTagsSettings(PCGSettings)
```

Filters the tags on the input data.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGDeleteTags.h

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
- ``operation`` (PCGTagFilterOperation):  [Read-Write]
- ``operator`` (PCGStringMatchingOperator):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``selected_tags`` (str):  [Read-Write] Comma-separated list of tags to add or remove from the input data.
- ``tokenize_on_white_space`` (bool):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGDeleteTagsSettings.operation"></a>

#### operation

```python
@property
def operation() -> PCGTagFilterOperation
```

(PCGTagFilterOperation):  [Read-Write]

<a id="unreal.PCGDeleteTagsSettings.operation"></a>

#### operation

```python
@operation.setter
def operation(value: PCGTagFilterOperation) -> None
```

<a id="unreal.PCGDeleteTagsSettings.operator"></a>

#### operator

```python
@property
def operator() -> PCGStringMatchingOperator
```

(PCGStringMatchingOperator):  [Read-Write]

<a id="unreal.PCGDeleteTagsSettings.operator"></a>

#### operator

```python
@operator.setter
def operator(value: PCGStringMatchingOperator) -> None
```

<a id="unreal.PCGDeleteTagsSettings.selected_tags"></a>

#### selected_tags

```python
@property
def selected_tags() -> str
```

(str):  [Read-Write] Comma-separated list of tags to add or remove from the input data.

<a id="unreal.PCGDeleteTagsSettings.selected_tags"></a>

#### selected_tags

```python
@selected_tags.setter
def selected_tags(value: str) -> None
```

<a id="unreal.PCGDistanceSettings"></a>