## PCGSortTagsSettings Objects

```python
class PCGSortTagsSettings(PCGSettings)
```

Sorts a data collection based on a specific tag value. This is a stable sort, but will always put entries (data) that do not have the specified tag at the end.
Note that tag values are tags of the form ("Tag:Value") and support either strings or numeric values (doubles).
Tags that do not have a value ("Tag") will behave like boolean tags and will just put the ones that have the specified tag first in the output data collection.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSortTags.h

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
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``sort_method`` (PCGSortMethod):  [Read-Write]
- ``tag`` (Name):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGSortTagsSettings.tag"></a>

#### tag

```python
@property
def tag() -> Name
```

(Name):  [Read-Write]

<a id="unreal.PCGSortTagsSettings.tag"></a>

#### tag

```python
@tag.setter
def tag(value: Name) -> None
```

<a id="unreal.PCGSortTagsSettings.sort_method"></a>

#### sort_method

```python
@property
def sort_method() -> PCGSortMethod
```

(PCGSortMethod):  [Read-Write]

<a id="unreal.PCGSortTagsSettings.sort_method"></a>

#### sort_method

```python
@sort_method.setter
def sort_method(value: PCGSortMethod) -> None
```

<a id="unreal.PCGSpawnSplineSettings"></a>