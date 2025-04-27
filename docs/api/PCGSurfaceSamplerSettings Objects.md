## PCGSurfaceSamplerSettings Objects

```python
class PCGSurfaceSamplerSettings(PCGSettings)
```

PCGSurface Sampler Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSurfaceSampler.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_density_to_points`` (bool):  [Read-Write]
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
- ``keep_zero_density_points`` (bool):  [Read-Write]
- ``looseness`` (float):  [Read-Write]
- ``point_extents`` (Vector):  [Read-Write]
- ``point_steepness`` (float):  [Read-Write] Each PCG point represents a discretized, volumetric region of world space. The points' Steepness value [0.0 to
  1.0] establishes how "hard" or "soft" that volume will be represented. From 0, it will ramp up linearly
  increasing its influence over the density from the point's center to up to two times the bounds. At 1, it will
  represent a binary box function with the size of the point's bounds.
- ``points_per_squared_meter`` (float):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``unbounded`` (bool):  [Read-Write] If no Bounding Shape input is provided, the actor bounds are used to limit the sample generation domain.
  This option allows ignoring the actor bounds and generating over the entire surface. Use with caution as this
  may generate a lot of points.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGSurfaceSamplerSettings.points_per_squared_meter"></a>

#### points_per_squared_meter

```python
@property
def points_per_squared_meter() -> float
```

(float):  [Read-Write]

<a id="unreal.PCGSurfaceSamplerSettings.points_per_squared_meter"></a>

#### points_per_squared_meter

```python
@points_per_squared_meter.setter
def points_per_squared_meter(value: float) -> None
```

<a id="unreal.PCGSurfaceSamplerSettings.point_extents"></a>

#### point_extents

```python
@property
def point_extents() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.PCGSurfaceSamplerSettings.point_extents"></a>

#### point_extents

```python
@point_extents.setter
def point_extents(value: Vector) -> None
```

<a id="unreal.PCGSurfaceSamplerSettings.looseness"></a>

#### looseness

```python
@property
def looseness() -> float
```

(float):  [Read-Write]

<a id="unreal.PCGSurfaceSamplerSettings.looseness"></a>

#### looseness

```python
@looseness.setter
def looseness(value: float) -> None
```

<a id="unreal.PCGSurfaceSamplerSettings.unbounded"></a>

#### unbounded

```python
@property
def unbounded() -> bool
```

(bool):  [Read-Write] If no Bounding Shape input is provided, the actor bounds are used to limit the sample generation domain.
This option allows ignoring the actor bounds and generating over the entire surface. Use with caution as this
may generate a lot of points.

<a id="unreal.PCGSurfaceSamplerSettings.unbounded"></a>

#### unbounded

```python
@unbounded.setter
def unbounded(value: bool) -> None
```

<a id="unreal.PCGSurfaceSamplerSettings.apply_density_to_points"></a>

#### apply_density_to_points

```python
@property
def apply_density_to_points() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGSurfaceSamplerSettings.apply_density_to_points"></a>

#### apply_density_to_points

```python
@apply_density_to_points.setter
def apply_density_to_points(value: bool) -> None
```

<a id="unreal.PCGSurfaceSamplerSettings.point_steepness"></a>

#### point_steepness

```python
@property
def point_steepness() -> float
```

(float):  [Read-Write] Each PCG point represents a discretized, volumetric region of world space. The points' Steepness value [0.0 to
1.0] establishes how "hard" or "soft" that volume will be represented. From 0, it will ramp up linearly
increasing its influence over the density from the point's center to up to two times the bounds. At 1, it will
represent a binary box function with the size of the point's bounds.

<a id="unreal.PCGSurfaceSamplerSettings.point_steepness"></a>

#### point_steepness

```python
@point_steepness.setter
def point_steepness(value: float) -> None
```

<a id="unreal.PCGSurfaceSamplerSettings.keep_zero_density_points"></a>

#### keep_zero_density_points

```python
@property
def keep_zero_density_points() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGSurfaceSamplerSettings.keep_zero_density_points"></a>

#### keep_zero_density_points

```python
@keep_zero_density_points.setter
def keep_zero_density_points(value: bool) -> None
```

<a id="unreal.PCGTextureSamplerSettings"></a>