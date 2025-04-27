## PCGLoadAlembicSettings Objects

```python
class PCGLoadAlembicSettings(PCGExternalDataSettings)
```

PCGLoad Alembic Settings

**C++ Source:**

- **Plugin**: PCGExternalDataInterop
- **Module**: PCGExternalDataInterop
- **File**: PCGLoadAlembicElement.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alembic_file_path`` (FilePath):  [Read-Write]
- ``attribute_mapping`` (Map[str, PCGAttributePropertyInputSelector]):  [Read-Write]
- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``conversion_flip_handedness`` (bool):  [Read-Write] Flips rotation direction (W), useful together with swizzling
- ``conversion_rotation`` (Vector):  [Read-Write] Rotation in Euler angles applied during import. For Max, use (90, 0, 0).
- ``conversion_scale`` (Vector):  [Read-Write] Scale to apply during import. Note that for both Max/Maya presets the value flips the Y axis.
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
- ``setup`` (PCGLoadAlembicStandardSetup):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGLoadAlembicSettings.alembic_file_path"></a>

#### alembic_file_path

```python
@property
def alembic_file_path() -> FilePath
```

(FilePath):  [Read-Write]

<a id="unreal.PCGLoadAlembicSettings.alembic_file_path"></a>

#### alembic_file_path

```python
@alembic_file_path.setter
def alembic_file_path(value: FilePath) -> None
```

<a id="unreal.PCGLoadAlembicSettings.conversion_scale"></a>

#### conversion_scale

```python
@property
def conversion_scale() -> Vector
```

(Vector):  [Read-Write] Scale to apply during import. Note that for both Max/Maya presets the value flips the Y axis.

<a id="unreal.PCGLoadAlembicSettings.conversion_scale"></a>

#### conversion_scale

```python
@conversion_scale.setter
def conversion_scale(value: Vector) -> None
```

<a id="unreal.PCGLoadAlembicSettings.conversion_rotation"></a>

#### conversion_rotation

```python
@property
def conversion_rotation() -> Vector
```

(Vector):  [Read-Write] Rotation in Euler angles applied during import. For Max, use (90, 0, 0).

<a id="unreal.PCGLoadAlembicSettings.conversion_rotation"></a>

#### conversion_rotation

```python
@conversion_rotation.setter
def conversion_rotation(value: Vector) -> None
```

<a id="unreal.PCGLoadAlembicSettings.conversion_flip_handedness"></a>

#### conversion_flip_handedness

```python
@property
def conversion_flip_handedness() -> bool
```

(bool):  [Read-Write] Flips rotation direction (W), useful together with swizzling

<a id="unreal.PCGLoadAlembicSettings.conversion_flip_handedness"></a>

#### conversion_flip_handedness

```python
@conversion_flip_handedness.setter
def conversion_flip_handedness(value: bool) -> None
```

<a id="unreal.PCGLoadAlembicSettings.setup_from_standard"></a>

#### setup_from_standard

```python
def setup_from_standard(setup: PCGLoadAlembicStandardSetup) -> None
```

x.setup_from_standard(setup) -> None
Setup from Standard

Args:
    setup (PCGLoadAlembicStandardSetup):

<a id="unreal.PCGAlembicToPCGAssetExporter"></a>