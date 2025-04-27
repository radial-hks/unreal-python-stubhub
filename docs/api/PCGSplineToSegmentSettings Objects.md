## PCGSplineToSegmentSettings Objects

```python
class PCGSplineToSegmentSettings(PCGSettings)
```

Take a spline as input and create a point data, with each point being a segment defined by 2 connected control points.
The point position will be in the middle of those 2 control points, and the extents of the point will be half the difference between those 2 control points.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSplineToSegment.h

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
- ``extract_angles`` (bool):  [Read-Write] Can extract the angle with previous tangent and next tangent. Will be 0 at the extremity for non-closed splines.
- ``extract_clockwise_info`` (bool):  [Read-Write] Can output a global attribute to know if the spline points order is clockwise or counterclockwise. (Only for closed loops).
- ``extract_connectivity_info`` (bool):  [Read-Write] Can set the index of the previous and next segment (to keep information on connectivity).
- ``extract_tangents`` (bool):  [Read-Write] Can extract the tangents with previous segment and next segment.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGSplineToSegmentSettings.extract_tangents"></a>

#### extract_tangents

```python
@property
def extract_tangents() -> bool
```

(bool):  [Read-Write] Can extract the tangents with previous segment and next segment.

<a id="unreal.PCGSplineToSegmentSettings.extract_tangents"></a>

#### extract_tangents

```python
@extract_tangents.setter
def extract_tangents(value: bool) -> None
```

<a id="unreal.PCGSplineToSegmentSettings.extract_angles"></a>

#### extract_angles

```python
@property
def extract_angles() -> bool
```

(bool):  [Read-Write] Can extract the angle with previous tangent and next tangent. Will be 0 at the extremity for non-closed splines.

<a id="unreal.PCGSplineToSegmentSettings.extract_angles"></a>

#### extract_angles

```python
@extract_angles.setter
def extract_angles(value: bool) -> None
```

<a id="unreal.PCGSplineToSegmentSettings.extract_connectivity_info"></a>

#### extract_connectivity_info

```python
@property
def extract_connectivity_info() -> bool
```

(bool):  [Read-Write] Can set the index of the previous and next segment (to keep information on connectivity).

<a id="unreal.PCGSplineToSegmentSettings.extract_connectivity_info"></a>

#### extract_connectivity_info

```python
@extract_connectivity_info.setter
def extract_connectivity_info(value: bool) -> None
```

<a id="unreal.PCGSplineToSegmentSettings.extract_clockwise_info"></a>

#### extract_clockwise_info

```python
@property
def extract_clockwise_info() -> bool
```

(bool):  [Read-Write] Can output a global attribute to know if the spline points order is clockwise or counterclockwise. (Only for closed loops).

<a id="unreal.PCGSplineToSegmentSettings.extract_clockwise_info"></a>

#### extract_clockwise_info

```python
@extract_clockwise_info.setter
def extract_clockwise_info(value: bool) -> None
```

<a id="unreal.PCGSplitPointsSettings"></a>