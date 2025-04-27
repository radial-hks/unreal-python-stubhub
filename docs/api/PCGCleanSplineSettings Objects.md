## PCGCleanSplineSettings Objects

```python
class PCGCleanSplineSettings(PCGSettings)
```

Remove superfluous control points along the spline, such as those that are co-located or collinear.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCleanSpline.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``collinear_angle_threshold`` (double):  [Read-Write] A control point will be considered collinear if it is within this angle from the segment between its previous and next control points.
- ``colocation_distance_threshold`` (double):  [Read-Write] Control points will be considered co-located if they are within this distance from one another.
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
- ``fuse_colocated_control_points`` (bool):  [Read-Write] Fuse control points that share the same location in world space, within a distance threshold. Colocated points are inherently collinear, so this will automatically be applied when removing collinear points.
- ``fuse_mode`` (PCGControlPointFuseMode):  [Read-Write] Controls how two co-located points will be fused together.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``remove_collinear_control_points`` (bool):  [Read-Write] Remove control points on linear sections of the spline that would otherwise have no effect on the final spline calculation.
- ``seed`` (int32):  [Read-Write]
- ``use_radians`` (bool):  [Read-Write] Use radians directly, instead of degrees. The current 'CollinearAngleThreshold' value will be automatically converted when toggled.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.
- ``use_spline_local_space`` (bool):  [Read-Write] Use spline local space for the distance calculation, rather than world space.

<a id="unreal.PCGCleanSplineSettings.fuse_colocated_control_points"></a>

#### fuse_colocated_control_points

```python
@property
def fuse_colocated_control_points() -> bool
```

(bool):  [Read-Write] Fuse control points that share the same location in world space, within a distance threshold. Colocated points are inherently collinear, so this will automatically be applied when removing collinear points.

<a id="unreal.PCGCleanSplineSettings.fuse_colocated_control_points"></a>

#### fuse_colocated_control_points

```python
@fuse_colocated_control_points.setter
def fuse_colocated_control_points(value: bool) -> None
```

<a id="unreal.PCGCleanSplineSettings.colocation_distance_threshold"></a>

#### colocation_distance_threshold

```python
@property
def colocation_distance_threshold() -> float
```

(double):  [Read-Write] Control points will be considered co-located if they are within this distance from one another.

<a id="unreal.PCGCleanSplineSettings.colocation_distance_threshold"></a>

#### colocation_distance_threshold

```python
@colocation_distance_threshold.setter
def colocation_distance_threshold(value: float) -> None
```

<a id="unreal.PCGCleanSplineSettings.use_spline_local_space"></a>

#### use_spline_local_space

```python
@property
def use_spline_local_space() -> bool
```

(bool):  [Read-Write] Use spline local space for the distance calculation, rather than world space.

<a id="unreal.PCGCleanSplineSettings.use_spline_local_space"></a>

#### use_spline_local_space

```python
@use_spline_local_space.setter
def use_spline_local_space(value: bool) -> None
```

<a id="unreal.PCGCleanSplineSettings.fuse_mode"></a>

#### fuse_mode

```python
@property
def fuse_mode() -> PCGControlPointFuseMode
```

(PCGControlPointFuseMode):  [Read-Write] Controls how two co-located points will be fused together.

<a id="unreal.PCGCleanSplineSettings.fuse_mode"></a>

#### fuse_mode

```python
@fuse_mode.setter
def fuse_mode(value: PCGControlPointFuseMode) -> None
```

<a id="unreal.PCGCleanSplineSettings.remove_collinear_control_points"></a>

#### remove_collinear_control_points

```python
@property
def remove_collinear_control_points() -> bool
```

(bool):  [Read-Write] Remove control points on linear sections of the spline that would otherwise have no effect on the final spline calculation.

<a id="unreal.PCGCleanSplineSettings.remove_collinear_control_points"></a>

#### remove_collinear_control_points

```python
@remove_collinear_control_points.setter
def remove_collinear_control_points(value: bool) -> None
```

<a id="unreal.PCGCleanSplineSettings.collinear_angle_threshold"></a>

#### collinear_angle_threshold

```python
@property
def collinear_angle_threshold() -> float
```

(double):  [Read-Write] A control point will be considered collinear if it is within this angle from the segment between its previous and next control points.

<a id="unreal.PCGCleanSplineSettings.collinear_angle_threshold"></a>

#### collinear_angle_threshold

```python
@collinear_angle_threshold.setter
def collinear_angle_threshold(value: float) -> None
```

<a id="unreal.PCGCleanSplineSettings.use_radians"></a>

#### use_radians

```python
@property
def use_radians() -> bool
```

(bool):  [Read-Write] Use radians directly, instead of degrees. The current 'CollinearAngleThreshold' value will be automatically converted when toggled.

<a id="unreal.PCGCleanSplineSettings.use_radians"></a>

#### use_radians

```python
@use_radians.setter
def use_radians(value: bool) -> None
```

<a id="unreal.PCGClusterSettings"></a>