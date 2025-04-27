## PCGFilterByAttributeSettings Objects

```python
class PCGFilterByAttributeSettings(PCGFilterDataBaseSettings)
```

Separates data on whether they have a specific metadata attribute (not by value)

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGFilterByAttribute.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attribute`` (Name):  [Read-Write] Comma-separated list of attributes to look for
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
- ``ignore_properties`` (bool):  [Read-Write] Controls whether properties (denoted by $) will be considered in the filter or not.
- ``operator`` (PCGStringMatchingOperator):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGFilterByAttributeSettings.attribute"></a>

#### attribute

```python
@property
def attribute() -> Name
```

(Name):  [Read-Write] Comma-separated list of attributes to look for

<a id="unreal.PCGFilterByAttributeSettings.attribute"></a>

#### attribute

```python
@attribute.setter
def attribute(value: Name) -> None
```

<a id="unreal.PCGFilterByAttributeSettings.operator"></a>

#### operator

```python
@property
def operator() -> PCGStringMatchingOperator
```

(PCGStringMatchingOperator):  [Read-Write]

<a id="unreal.PCGFilterByAttributeSettings.operator"></a>

#### operator

```python
@operator.setter
def operator(value: PCGStringMatchingOperator) -> None
```

<a id="unreal.PCGFilterByAttributeSettings.ignore_properties"></a>

#### ignore_properties

```python
@property
def ignore_properties() -> bool
```

(bool):  [Read-Write] Controls whether properties (denoted by $) will be considered in the filter or not.

<a id="unreal.PCGFilterByAttributeSettings.ignore_properties"></a>

#### ignore_properties

```python
@ignore_properties.setter
def ignore_properties(value: bool) -> None
```

<a id="unreal.PCGFilterElementsByIndexSettings"></a>