## PCGAddTagSettings Objects

```python
class PCGAddTagSettings(PCGSettings)
```

Applies the specified tags on the output data.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGAddTag.h

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
- ``ignore_tag_value_parsing`` (bool):  [Read-Write] Controls whether tags are not considered to be key-value pairs, e.g. that the prefix/suffix will be added before the ':' (if any) or not.
- ``prefix`` (str):  [Read-Write] Common prefix to add to all tags, can be left empty.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``suffix`` (str):  [Read-Write] Common suffix to add to all tags, can be left empty.
- ``tags_to_add`` (str):  [Read-Write] Comma-separated list of tags to apply to the node.
- ``tokenize_on_white_space`` (bool):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGAddTagSettings.tags_to_add"></a>

#### tags_to_add

```python
@property
def tags_to_add() -> str
```

(str):  [Read-Write] Comma-separated list of tags to apply to the node.

<a id="unreal.PCGAddTagSettings.tags_to_add"></a>

#### tags_to_add

```python
@tags_to_add.setter
def tags_to_add(value: str) -> None
```

<a id="unreal.PCGAddTagSettings.prefix"></a>

#### prefix

```python
@property
def prefix() -> str
```

(str):  [Read-Write] Common prefix to add to all tags, can be left empty.

<a id="unreal.PCGAddTagSettings.prefix"></a>

#### prefix

```python
@prefix.setter
def prefix(value: str) -> None
```

<a id="unreal.PCGAddTagSettings.suffix"></a>

#### suffix

```python
@property
def suffix() -> str
```

(str):  [Read-Write] Common suffix to add to all tags, can be left empty.

<a id="unreal.PCGAddTagSettings.suffix"></a>

#### suffix

```python
@suffix.setter
def suffix(value: str) -> None
```

<a id="unreal.PCGAddTagSettings.ignore_tag_value_parsing"></a>

#### ignore_tag_value_parsing

```python
@property
def ignore_tag_value_parsing() -> bool
```

(bool):  [Read-Write] Controls whether tags are not considered to be key-value pairs, e.g. that the prefix/suffix will be added before the ':' (if any) or not.

<a id="unreal.PCGAddTagSettings.ignore_tag_value_parsing"></a>

#### ignore_tag_value_parsing

```python
@ignore_tag_value_parsing.setter
def ignore_tag_value_parsing(value: bool) -> None
```

<a id="unreal.PCGApplyOnActorSettings"></a>