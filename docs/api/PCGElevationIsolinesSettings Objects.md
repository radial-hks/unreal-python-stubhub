## PCGElevationIsolinesSettings Objects

```python
class PCGElevationIsolinesSettings(PCGSettings)
```

Compute the elevation isolines of a surface, can output either points or splines.
Currently only work for Z-up surfaces.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGElevationIsolines.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``add_tag_on_output_for_same_elevation`` (bool):  [Read-Write] Can add a tag (integer) to group output data that are at the same elevation.
- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``debug`` (bool):  [Read-Write]
- ``debug_buffer_size`` (int32):  [Read-Write] Size (in number of floats) of the shader debug print buffer.
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``description`` (Text):  [Read-Write]
- ``determinism_settings`` (PCGDeterminismSettings):  [Read-Write]
- ``dump_cooked_hlsl`` (bool):  [Read-Write] Dump the cooked HLSL into the log after it is generated.
- ``dump_data_descriptions`` (bool):  [Read-Write] Dump the data descriptions of input/output pins to the log.
- ``elevation_end`` (double):  [Read-Write] Maximum elevation of the isolines.
- ``elevation_increment`` (double):  [Read-Write] Increment elevation between each isolines.
- ``elevation_start`` (double):  [Read-Write] Minimum elevation of the isolines.
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``linear_spline`` (bool):  [Read-Write] Spline can either be curved or linear.
- ``output_as_spline`` (bool):  [Read-Write] Will output splines rather than points.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``project_surface_normal`` (bool):  [Read-Write] Option to either have Z up or project the surface normal at this position (similar to project rotations on the projection node).
- ``resolution`` (double):  [Read-Write] Resolution of the grid for the discretization of the surface. This is the size of one cell, in cm.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGElevationIsolinesSettings.elevation_start"></a>

#### elevation_start

```python
@property
def elevation_start() -> float
```

(double):  [Read-Write] Minimum elevation of the isolines.

<a id="unreal.PCGElevationIsolinesSettings.elevation_start"></a>

#### elevation_start

```python
@elevation_start.setter
def elevation_start(value: float) -> None
```

<a id="unreal.PCGElevationIsolinesSettings.elevation_end"></a>

#### elevation_end

```python
@property
def elevation_end() -> float
```

(double):  [Read-Write] Maximum elevation of the isolines.

<a id="unreal.PCGElevationIsolinesSettings.elevation_end"></a>

#### elevation_end

```python
@elevation_end.setter
def elevation_end(value: float) -> None
```

<a id="unreal.PCGElevationIsolinesSettings.elevation_increment"></a>

#### elevation_increment

```python
@property
def elevation_increment() -> float
```

(double):  [Read-Write] Increment elevation between each isolines.

<a id="unreal.PCGElevationIsolinesSettings.elevation_increment"></a>

#### elevation_increment

```python
@elevation_increment.setter
def elevation_increment(value: float) -> None
```

<a id="unreal.PCGElevationIsolinesSettings.resolution"></a>

#### resolution

```python
@property
def resolution() -> float
```

(double):  [Read-Write] Resolution of the grid for the discretization of the surface. This is the size of one cell, in cm.

<a id="unreal.PCGElevationIsolinesSettings.resolution"></a>

#### resolution

```python
@resolution.setter
def resolution(value: float) -> None
```

<a id="unreal.PCGElevationIsolinesSettings.add_tag_on_output_for_same_elevation"></a>

#### add_tag_on_output_for_same_elevation

```python
@property
def add_tag_on_output_for_same_elevation() -> bool
```

(bool):  [Read-Write] Can add a tag (integer) to group output data that are at the same elevation.

<a id="unreal.PCGElevationIsolinesSettings.add_tag_on_output_for_same_elevation"></a>

#### add_tag_on_output_for_same_elevation

```python
@add_tag_on_output_for_same_elevation.setter
def add_tag_on_output_for_same_elevation(value: bool) -> None
```

<a id="unreal.PCGElevationIsolinesSettings.project_surface_normal"></a>

#### project_surface_normal

```python
@property
def project_surface_normal() -> bool
```

(bool):  [Read-Write] Option to either have Z up or project the surface normal at this position (similar to project rotations on the projection node).

<a id="unreal.PCGElevationIsolinesSettings.project_surface_normal"></a>

#### project_surface_normal

```python
@project_surface_normal.setter
def project_surface_normal(value: bool) -> None
```

<a id="unreal.PCGElevationIsolinesSettings.output_as_spline"></a>

#### output_as_spline

```python
@property
def output_as_spline() -> bool
```

(bool):  [Read-Write] Will output splines rather than points.

<a id="unreal.PCGElevationIsolinesSettings.output_as_spline"></a>

#### output_as_spline

```python
@output_as_spline.setter
def output_as_spline(value: bool) -> None
```

<a id="unreal.PCGElevationIsolinesSettings.linear_spline"></a>

#### linear_spline

```python
@property
def linear_spline() -> bool
```

(bool):  [Read-Write] Spline can either be curved or linear.

<a id="unreal.PCGElevationIsolinesSettings.linear_spline"></a>

#### linear_spline

```python
@linear_spline.setter
def linear_spline(value: bool) -> None
```

<a id="unreal.PCGFilterDataBaseSettings"></a>