## PCGCopyPointsSettings Objects

```python
class PCGCopyPointsSettings(PCGSettings)
```

PCGCopy Points Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCopyPoints.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attribute_inheritance`` (PCGCopyPointsMetadataInheritanceMode):  [Read-Write] The method used to determine output data attributes
- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``color_inheritance`` (PCGCopyPointsInheritanceMode):  [Read-Write] The method used to determine output point color
- ``copy_each_source_on_every_target`` (bool):  [Read-Write] If this option is set, each source point data will be copied to every target point data (cartesian product), producing N * M point data. Otherwise, will do a N:N (or N:1 or 1:N) operation, producing N point data.
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
- ``rotation_inheritance`` (PCGCopyPointsInheritanceMode):  [Read-Write] The method used to determine output point rotation
- ``scale_inheritance`` (PCGCopyPointsInheritanceMode):  [Read-Write] The method used to determine output point scale
- ``seed`` (int32):  [Read-Write]
- ``seed_inheritance`` (PCGCopyPointsInheritanceMode):  [Read-Write] The method used to determine output seed values. Relative recomputes the seed from the new location.
- ``tag_inheritance`` (PCGCopyPointsTagInheritanceMode):  [Read-Write] The method used to determine the output data tags
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGCopyPointsSettings.rotation_inheritance"></a>

#### rotation_inheritance

```python
@property
def rotation_inheritance() -> PCGCopyPointsInheritanceMode
```

(PCGCopyPointsInheritanceMode):  [Read-Write] The method used to determine output point rotation

<a id="unreal.PCGCopyPointsSettings.rotation_inheritance"></a>

#### rotation_inheritance

```python
@rotation_inheritance.setter
def rotation_inheritance(value: PCGCopyPointsInheritanceMode) -> None
```

<a id="unreal.PCGCopyPointsSettings.scale_inheritance"></a>

#### scale_inheritance

```python
@property
def scale_inheritance() -> PCGCopyPointsInheritanceMode
```

(PCGCopyPointsInheritanceMode):  [Read-Write] The method used to determine output point scale

<a id="unreal.PCGCopyPointsSettings.scale_inheritance"></a>

#### scale_inheritance

```python
@scale_inheritance.setter
def scale_inheritance(value: PCGCopyPointsInheritanceMode) -> None
```

<a id="unreal.PCGCopyPointsSettings.color_inheritance"></a>

#### color_inheritance

```python
@property
def color_inheritance() -> PCGCopyPointsInheritanceMode
```

(PCGCopyPointsInheritanceMode):  [Read-Write] The method used to determine output point color

<a id="unreal.PCGCopyPointsSettings.color_inheritance"></a>

#### color_inheritance

```python
@color_inheritance.setter
def color_inheritance(value: PCGCopyPointsInheritanceMode) -> None
```

<a id="unreal.PCGCopyPointsSettings.seed_inheritance"></a>

#### seed_inheritance

```python
@property
def seed_inheritance() -> PCGCopyPointsInheritanceMode
```

(PCGCopyPointsInheritanceMode):  [Read-Write] The method used to determine output seed values. Relative recomputes the seed from the new location.

<a id="unreal.PCGCopyPointsSettings.seed_inheritance"></a>

#### seed_inheritance

```python
@seed_inheritance.setter
def seed_inheritance(value: PCGCopyPointsInheritanceMode) -> None
```

<a id="unreal.PCGCopyPointsSettings.attribute_inheritance"></a>

#### attribute_inheritance

```python
@property
def attribute_inheritance() -> PCGCopyPointsMetadataInheritanceMode
```

(PCGCopyPointsMetadataInheritanceMode):  [Read-Write] The method used to determine output data attributes

<a id="unreal.PCGCopyPointsSettings.attribute_inheritance"></a>

#### attribute_inheritance

```python
@attribute_inheritance.setter
def attribute_inheritance(value: PCGCopyPointsMetadataInheritanceMode) -> None
```

<a id="unreal.PCGCopyPointsSettings.tag_inheritance"></a>

#### tag_inheritance

```python
@property
def tag_inheritance() -> PCGCopyPointsTagInheritanceMode
```

(PCGCopyPointsTagInheritanceMode):  [Read-Write] The method used to determine the output data tags

<a id="unreal.PCGCopyPointsSettings.tag_inheritance"></a>

#### tag_inheritance

```python
@tag_inheritance.setter
def tag_inheritance(value: PCGCopyPointsTagInheritanceMode) -> None
```

<a id="unreal.PCGCopyPointsSettings.copy_each_source_on_every_target"></a>

#### copy_each_source_on_every_target

```python
@property
def copy_each_source_on_every_target() -> bool
```

(bool):  [Read-Write] If this option is set, each source point data will be copied to every target point data (cartesian product), producing N * M point data. Otherwise, will do a N:N (or N:1 or 1:N) operation, producing N point data.

<a id="unreal.PCGCopyPointsSettings.copy_each_source_on_every_target"></a>

#### copy_each_source_on_every_target

```python
@copy_each_source_on_every_target.setter
def copy_each_source_on_every_target(value: bool) -> None
```

<a id="unreal.PCGAddAttributeSettings"></a>