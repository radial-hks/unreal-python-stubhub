## PCGMetadataPartitionSettings Objects

```python
class PCGMetadataPartitionSettings(PCGSettings)
```

PCGMetadata Partition Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGMetadataPartition.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``assign_index_partition`` (bool):  [Read-Write] Assign an index partition as an extra attribute.
- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``debug`` (bool):  [Read-Write]
- ``debug_buffer_size`` (int32):  [Read-Write] Size (in number of floats) of the shader debug print buffer.
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``description`` (Text):  [Read-Write]
- ``determinism_settings`` (PCGDeterminismSettings):  [Read-Write]
- ``do_not_partition`` (bool):  [Read-Write] If we assign an index, we can also not partition (and only assign the partition index to the original data).
- ``dump_cooked_hlsl`` (bool):  [Read-Write] Dump the cooked HLSL into the log after it is generated.
- ``dump_data_descriptions`` (bool):  [Read-Write] Dump the data descriptions of input/output pins to the log.
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``partition_attribute`` (Name):  [Read-Write]
  deprecated: PartitionAttribute has been deprecated.
- ``partition_attribute_selectors`` (Array[PCGAttributePropertyInputSelector]):  [Read-Write] The data will be partitioned on these selected attributes.
- ``partition_attribute_source`` (PCGAttributePropertyInputSelector):  [Read-Write]
  deprecated: PartitionAttributeSource has been deprecated.
- ``partition_index_attribute_name`` (Name):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``tokenize_on_white_space`` (bool):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGMetadataPartitionSettings.partition_attribute_selectors"></a>

#### partition_attribute_selectors

```python
@property
def partition_attribute_selectors(
) -> Array[PCGAttributePropertyInputSelector]
```

(Array[PCGAttributePropertyInputSelector]):  [Read-Write] The data will be partitioned on these selected attributes.

<a id="unreal.PCGMetadataPartitionSettings.partition_attribute_selectors"></a>

#### partition_attribute_selectors

```python
@partition_attribute_selectors.setter
def partition_attribute_selectors(
        value: Array[PCGAttributePropertyInputSelector]) -> None
```

<a id="unreal.PCGMetadataPartitionSettings.partition_attribute"></a>

#### partition_attribute

```python
@property
def partition_attribute() -> Name
```

(Name):  [Read-Write]
deprecated: PartitionAttribute has been deprecated.

<a id="unreal.PCGMetadataPartitionSettings.partition_attribute"></a>

#### partition_attribute

```python
@partition_attribute.setter
def partition_attribute(value: Name) -> None
```

<a id="unreal.PCGMetadataPartitionSettings.partition_attribute_source"></a>

#### partition_attribute_source

```python
@property
def partition_attribute_source() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write]
deprecated: PartitionAttributeSource has been deprecated.

<a id="unreal.PCGMetadataPartitionSettings.partition_attribute_source"></a>

#### partition_attribute_source

```python
@partition_attribute_source.setter
def partition_attribute_source(
        value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGMetadataRenameSettings"></a>