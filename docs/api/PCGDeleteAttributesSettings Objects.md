## PCGDeleteAttributesSettings Objects

```python
class PCGDeleteAttributesSettings(PCGSettings)
```

Removes attributes from a given input metadata.
Either removes specifically named attributes or remove all attributes not in a given list.

The output will be the original data with the updated metadata.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGDeleteAttributesElement.h

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
- ``operation`` (PCGAttributeFilterOperation):  [Read-Write] Implementation note: the default has been changed to DeleteSelected for new objects
- ``operator`` (PCGStringMatchingOperator):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``selected_attributes`` (str):  [Read-Write] Comma-separated list of attributes to keep or remove from the input data.
- ``tokenize_on_white_space`` (bool):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGDeleteAttributesSettings.operation"></a>

#### operation

```python
@property
def operation() -> PCGAttributeFilterOperation
```

(PCGAttributeFilterOperation):  [Read-Write] Implementation note: the default has been changed to DeleteSelected for new objects

<a id="unreal.PCGDeleteAttributesSettings.operation"></a>

#### operation

```python
@operation.setter
def operation(value: PCGAttributeFilterOperation) -> None
```

<a id="unreal.PCGDeleteAttributesSettings.operator"></a>

#### operator

```python
@property
def operator() -> PCGStringMatchingOperator
```

(PCGStringMatchingOperator):  [Read-Write]

<a id="unreal.PCGDeleteAttributesSettings.operator"></a>

#### operator

```python
@operator.setter
def operator(value: PCGStringMatchingOperator) -> None
```

<a id="unreal.PCGDeleteAttributesSettings.selected_attributes"></a>

#### selected_attributes

```python
@property
def selected_attributes() -> str
```

(str):  [Read-Write] Comma-separated list of attributes to keep or remove from the input data.

<a id="unreal.PCGDeleteAttributesSettings.selected_attributes"></a>

#### selected_attributes

```python
@selected_attributes.setter
def selected_attributes(value: str) -> None
```

<a id="unreal.PCGAttributeFilterSettings"></a>