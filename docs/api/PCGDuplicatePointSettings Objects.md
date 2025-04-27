## PCGDuplicatePointSettings Objects

```python
class PCGDuplicatePointSettings(PCGSettings)
```

Creates duplicates of each point with optional transform offsets.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGDuplicatePoint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``debug`` (bool):  [Read-Write]
- ``debug_buffer_size`` (int32):  [Read-Write] Size (in number of floats) of the shader debug print buffer.
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``description`` (Text):  [Read-Write]
- ``determinism_settings`` (PCGDeterminismSettings):  [Read-Write]
- ``direction`` (Vector):  [Read-Write] Direction to stack point duplicates.
- ``direction_applied_in_relative_space`` (bool):  [Read-Write] Controls whether the axis displacement will be made in relative space or not
- ``dump_cooked_hlsl`` (bool):  [Read-Write] Dump the cooked HLSL into the log after it is generated.
- ``dump_data_descriptions`` (bool):  [Read-Write] Dump the data descriptions of input/output pins to the log.
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``iterations`` (int32):  [Read-Write] Number of duplicates to produce.
- ``output_source_point`` (bool):  [Read-Write] Include the source point.
- ``point_transform`` (Transform):  [Read-Write] Transform offset for each point duplicate
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGDuplicatePointSettings.iterations"></a>

#### iterations

```python
@property
def iterations() -> int
```

(int32):  [Read-Write] Number of duplicates to produce.

<a id="unreal.PCGDuplicatePointSettings.iterations"></a>

#### iterations

```python
@iterations.setter
def iterations(value: int) -> None
```

<a id="unreal.PCGDuplicatePointSettings.direction"></a>

#### direction

```python
@property
def direction() -> Vector
```

(Vector):  [Read-Write] Direction to stack point duplicates.

<a id="unreal.PCGDuplicatePointSettings.direction"></a>

#### direction

```python
@direction.setter
def direction(value: Vector) -> None
```

<a id="unreal.PCGDuplicatePointSettings.direction_applied_in_relative_space"></a>

#### direction_applied_in_relative_space

```python
@property
def direction_applied_in_relative_space() -> bool
```

(bool):  [Read-Write] Controls whether the axis displacement will be made in relative space or not

<a id="unreal.PCGDuplicatePointSettings.direction_applied_in_relative_space"></a>

#### direction_applied_in_relative_space

```python
@direction_applied_in_relative_space.setter
def direction_applied_in_relative_space(value: bool) -> None
```

<a id="unreal.PCGDuplicatePointSettings.output_source_point"></a>

#### output_source_point

```python
@property
def output_source_point() -> bool
```

(bool):  [Read-Write] Include the source point.

<a id="unreal.PCGDuplicatePointSettings.output_source_point"></a>

#### output_source_point

```python
@output_source_point.setter
def output_source_point(value: bool) -> None
```

<a id="unreal.PCGDuplicatePointSettings.point_transform"></a>

#### point_transform

```python
@property
def point_transform() -> Transform
```

(Transform):  [Read-Write] Transform offset for each point duplicate

<a id="unreal.PCGDuplicatePointSettings.point_transform"></a>

#### point_transform

```python
@point_transform.setter
def point_transform(value: Transform) -> None
```

<a id="unreal.PCGBadOutputsNodeSettings"></a>