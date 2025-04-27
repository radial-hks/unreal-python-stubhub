## PCGCreatePointsSettings Objects

```python
class PCGCreatePointsSettings(PCGSettings)
```

Creates point data from a provided list of points.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCreatePoints.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``coordinate_space`` (PCGCoordinateSpace):  [Read-Write] Sets the generation referential of the points
- ``cull_points_outside_volume`` (bool):  [Read-Write] If true, points are removed if they are outside of the volume
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
- ``points_to_create`` (Array[PCGPoint]):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGCreatePointsSettings.points_to_create"></a>

#### points_to_create

```python
@property
def points_to_create() -> Array[PCGPoint]
```

(Array[PCGPoint]):  [Read-Write]

<a id="unreal.PCGCreatePointsSettings.points_to_create"></a>

#### points_to_create

```python
@points_to_create.setter
def points_to_create(value: Array[PCGPoint]) -> None
```

<a id="unreal.PCGCreatePointsSettings.coordinate_space"></a>

#### coordinate_space

```python
@property
def coordinate_space() -> PCGCoordinateSpace
```

(PCGCoordinateSpace):  [Read-Write] Sets the generation referential of the points

<a id="unreal.PCGCreatePointsSettings.coordinate_space"></a>

#### coordinate_space

```python
@coordinate_space.setter
def coordinate_space(value: PCGCoordinateSpace) -> None
```

<a id="unreal.PCGCreatePointsSettings.cull_points_outside_volume"></a>

#### cull_points_outside_volume

```python
@property
def cull_points_outside_volume() -> bool
```

(bool):  [Read-Write] If true, points are removed if they are outside of the volume

<a id="unreal.PCGCreatePointsSettings.cull_points_outside_volume"></a>

#### cull_points_outside_volume

```python
@cull_points_outside_volume.setter
def cull_points_outside_volume(value: bool) -> None
```

<a id="unreal.PCGCreatePointsGridSettings"></a>