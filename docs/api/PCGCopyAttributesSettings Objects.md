## PCGCopyAttributesSettings Objects

```python
class PCGCopyAttributesSettings(PCGSettings)
```

PCGCopy Attributes Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCopyAttributes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``copy_all_attributes`` (bool):  [Read-Write]
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
- ``input_source`` (PCGAttributePropertyInputSelector):  [Read-Write]
- ``operation`` (PCGCopyAttributesOperation):  [Read-Write]
- ``output_target`` (PCGAttributePropertyOutputSelector):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGCopyAttributesSettings.operation"></a>

#### operation

```python
@property
def operation() -> PCGCopyAttributesOperation
```

(PCGCopyAttributesOperation):  [Read-Write]

<a id="unreal.PCGCopyAttributesSettings.operation"></a>

#### operation

```python
@operation.setter
def operation(value: PCGCopyAttributesOperation) -> None
```

<a id="unreal.PCGCopyAttributesSettings.copy_all_attributes"></a>

#### copy_all_attributes

```python
@property
def copy_all_attributes() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGCopyAttributesSettings.copy_all_attributes"></a>

#### copy_all_attributes

```python
@copy_all_attributes.setter
def copy_all_attributes(value: bool) -> None
```

<a id="unreal.PCGCopyAttributesSettings.input_source"></a>

#### input_source

```python
@property
def input_source() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write]

<a id="unreal.PCGCopyAttributesSettings.input_source"></a>

#### input_source

```python
@input_source.setter
def input_source(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGCopyAttributesSettings.output_target"></a>

#### output_target

```python
@property
def output_target() -> PCGAttributePropertyOutputSelector
```

(PCGAttributePropertyOutputSelector):  [Read-Write]

<a id="unreal.PCGCopyAttributesSettings.output_target"></a>

#### output_target

```python
@output_target.setter
def output_target(value: PCGAttributePropertyOutputSelector) -> None
```

<a id="unreal.PCGAttributeTransferSettings"></a>