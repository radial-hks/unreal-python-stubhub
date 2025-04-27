## PCGCreatePointsSphereSettings Objects

```python
class PCGCreatePointsSphereSettings(PCGSettings)
```

Generate a grid of points along the surface of a sphere.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCreatePointsSphere.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``coordinate_space`` (PCGCoordinateSpace):  [Read-Write] Sets the generation referential of the points.
- ``cull_points_outside_volume`` (bool):  [Read-Write] Points are removed if they are outside the volume.
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
- ``geodesic_subdivisions`` (int32):  [Read-Write] Determines the number of subdivisions of the geodesic sphere. Becomes exponentially more expensive as it gets higher.
- ``jitter`` (double):  [Read-Write] Adds randomization (in the range of [-Jitter, Jitter]) of the angles of a generated point.
- ``latitudinal_end_angle`` (double):  [Read-Write] Points will cease to be generated on the sphere's surface after this equatorial angle.
- ``latitudinal_segments`` (int32):  [Read-Write] Will determine the latitudinal angle between segments needed to generate this number of latitudinal segments.
- ``latitudinal_start_angle`` (double):  [Read-Write] Points will be generated on the sphere's surface beginning at this equatorial angle.
- ``longitudinal_end_angle`` (double):  [Read-Write] Points will cease to be generated on the sphere's surface after this meridional angle.
- ``longitudinal_segments`` (int32):  [Read-Write] Will determine the longitudinal angle between segments needed to generate this number of longitudinal segments.
- ``longitudinal_start_angle`` (double):  [Read-Write] Points will be generated on the sphere's surface beginning at this meridional angle.
- ``origin`` (Vector):  [Read-Write] The sphere's origin, around which the points will be generated.
- ``phi`` (double):  [Read-Write] The longitudinal angle (in degrees) between generated segments on the standard sphere grid.
- ``point_orientation`` (PCGSpherePointOrientation):  [Read-Write] Will determine the points' orientation, once generated.
- ``point_steepness`` (float):  [Read-Write] Directly set as the output points' steepness value.
- ``poisson_distance`` (double):  [Read-Write] The maximum world distance between points sampled on the sphere's surface during a Poisson sampling, in cm.
- ``poisson_max_attempts`` (int32):  [Read-Write] Poisson sampling will continue to search for open positions until this limit is reached.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``radius`` (double):  [Read-Write] The sphere's radius.
- ``sample_count`` (int32):  [Read-Write] Determines the number of samples generated for the random generation and the poisson sampling.
- ``seed`` (int32):  [Read-Write]
- ``sphere_generation`` (PCGSphereGeneration):  [Read-Write] Determines the type of sphere generated.
- ``theta`` (double):  [Read-Write] The latitudinal angle (in degrees) between generated segments on the standard sphere grid.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGCreatePointsSphereSettings.sphere_generation"></a>

#### sphere_generation

```python
@property
def sphere_generation() -> PCGSphereGeneration
```

(PCGSphereGeneration):  [Read-Write] Determines the type of sphere generated.

<a id="unreal.PCGCreatePointsSphereSettings.sphere_generation"></a>

#### sphere_generation

```python
@sphere_generation.setter
def sphere_generation(value: PCGSphereGeneration) -> None
```

<a id="unreal.PCGCreatePointsSphereSettings.coordinate_space"></a>

#### coordinate_space

```python
@property
def coordinate_space() -> PCGCoordinateSpace
```

(PCGCoordinateSpace):  [Read-Write] Sets the generation referential of the points.

<a id="unreal.PCGCreatePointsSphereSettings.coordinate_space"></a>

#### coordinate_space

```python
@coordinate_space.setter
def coordinate_space(value: PCGCoordinateSpace) -> None
```

<a id="unreal.PCGCreatePointsSphereSettings.point_orientation"></a>

#### point_orientation

```python
@property
def point_orientation() -> PCGSpherePointOrientation
```

(PCGSpherePointOrientation):  [Read-Write] Will determine the points' orientation, once generated.

<a id="unreal.PCGCreatePointsSphereSettings.point_orientation"></a>

#### point_orientation

```python
@point_orientation.setter
def point_orientation(value: PCGSpherePointOrientation) -> None
```

<a id="unreal.PCGCreatePointsSphereSettings.origin"></a>

#### origin

```python
@property
def origin() -> Vector
```

(Vector):  [Read-Write] The sphere's origin, around which the points will be generated.

<a id="unreal.PCGCreatePointsSphereSettings.origin"></a>

#### origin

```python
@origin.setter
def origin(value: Vector) -> None
```

<a id="unreal.PCGCreatePointsSphereSettings.radius"></a>

#### radius

```python
@property
def radius() -> float
```

(double):  [Read-Write] The sphere's radius.

<a id="unreal.PCGCreatePointsSphereSettings.radius"></a>

#### radius

```python
@radius.setter
def radius(value: float) -> None
```

<a id="unreal.PCGCreatePointsSphereSettings.geodesic_subdivisions"></a>

#### geodesic_subdivisions

```python
@property
def geodesic_subdivisions() -> int
```

(int32):  [Read-Write] Determines the number of subdivisions of the geodesic sphere. Becomes exponentially more expensive as it gets higher.

<a id="unreal.PCGCreatePointsSphereSettings.geodesic_subdivisions"></a>

#### geodesic_subdivisions

```python
@geodesic_subdivisions.setter
def geodesic_subdivisions(value: int) -> None
```

<a id="unreal.PCGCreatePointsSphereSettings.theta"></a>

#### theta

```python
@property
def theta() -> float
```

(double):  [Read-Write] The latitudinal angle (in degrees) between generated segments on the standard sphere grid.

<a id="unreal.PCGCreatePointsSphereSettings.theta"></a>

#### theta

```python
@theta.setter
def theta(value: float) -> None
```

<a id="unreal.PCGCreatePointsSphereSettings.phi"></a>

#### phi

```python
@property
def phi() -> float
```

(double):  [Read-Write] The longitudinal angle (in degrees) between generated segments on the standard sphere grid.

<a id="unreal.PCGCreatePointsSphereSettings.phi"></a>

#### phi

```python
@phi.setter
def phi(value: float) -> None
```

<a id="unreal.PCGCreatePointsSphereSettings.latitudinal_segments"></a>

#### latitudinal_segments

```python
@property
def latitudinal_segments() -> int
```

(int32):  [Read-Write] Will determine the latitudinal angle between segments needed to generate this number of latitudinal segments.

<a id="unreal.PCGCreatePointsSphereSettings.latitudinal_segments"></a>

#### latitudinal_segments

```python
@latitudinal_segments.setter
def latitudinal_segments(value: int) -> None
```

<a id="unreal.PCGCreatePointsSphereSettings.longitudinal_segments"></a>

#### longitudinal_segments

```python
@property
def longitudinal_segments() -> int
```

(int32):  [Read-Write] Will determine the longitudinal angle between segments needed to generate this number of longitudinal segments.

<a id="unreal.PCGCreatePointsSphereSettings.longitudinal_segments"></a>

#### longitudinal_segments

```python
@longitudinal_segments.setter
def longitudinal_segments(value: int) -> None
```

<a id="unreal.PCGCreatePointsSphereSettings.sample_count"></a>

#### sample_count

```python
@property
def sample_count() -> int
```

(int32):  [Read-Write] Determines the number of samples generated for the random generation and the poisson sampling.

<a id="unreal.PCGCreatePointsSphereSettings.sample_count"></a>

#### sample_count

```python
@sample_count.setter
def sample_count(value: int) -> None
```

<a id="unreal.PCGCreatePointsSphereSettings.poisson_distance"></a>

#### poisson_distance

```python
@property
def poisson_distance() -> float
```

(double):  [Read-Write] The maximum world distance between points sampled on the sphere's surface during a Poisson sampling, in cm.

<a id="unreal.PCGCreatePointsSphereSettings.poisson_distance"></a>

#### poisson_distance

```python
@poisson_distance.setter
def poisson_distance(value: float) -> None
```

<a id="unreal.PCGCreatePointsSphereSettings.poisson_max_attempts"></a>

#### poisson_max_attempts

```python
@property
def poisson_max_attempts() -> int
```

(int32):  [Read-Write] Poisson sampling will continue to search for open positions until this limit is reached.

<a id="unreal.PCGCreatePointsSphereSettings.poisson_max_attempts"></a>

#### poisson_max_attempts

```python
@poisson_max_attempts.setter
def poisson_max_attempts(value: int) -> None
```

<a id="unreal.PCGCreatePointsSphereSettings.latitudinal_start_angle"></a>

#### latitudinal_start_angle

```python
@property
def latitudinal_start_angle() -> float
```

(double):  [Read-Write] Points will be generated on the sphere's surface beginning at this equatorial angle.

<a id="unreal.PCGCreatePointsSphereSettings.latitudinal_start_angle"></a>

#### latitudinal_start_angle

```python
@latitudinal_start_angle.setter
def latitudinal_start_angle(value: float) -> None
```

<a id="unreal.PCGCreatePointsSphereSettings.latitudinal_end_angle"></a>

#### latitudinal_end_angle

```python
@property
def latitudinal_end_angle() -> float
```

(double):  [Read-Write] Points will cease to be generated on the sphere's surface after this equatorial angle.

<a id="unreal.PCGCreatePointsSphereSettings.latitudinal_end_angle"></a>

#### latitudinal_end_angle

```python
@latitudinal_end_angle.setter
def latitudinal_end_angle(value: float) -> None
```

<a id="unreal.PCGCreatePointsSphereSettings.longitudinal_start_angle"></a>

#### longitudinal_start_angle

```python
@property
def longitudinal_start_angle() -> float
```

(double):  [Read-Write] Points will be generated on the sphere's surface beginning at this meridional angle.

<a id="unreal.PCGCreatePointsSphereSettings.longitudinal_start_angle"></a>

#### longitudinal_start_angle

```python
@longitudinal_start_angle.setter
def longitudinal_start_angle(value: float) -> None
```

<a id="unreal.PCGCreatePointsSphereSettings.longitudinal_end_angle"></a>

#### longitudinal_end_angle

```python
@property
def longitudinal_end_angle() -> float
```

(double):  [Read-Write] Points will cease to be generated on the sphere's surface after this meridional angle.

<a id="unreal.PCGCreatePointsSphereSettings.longitudinal_end_angle"></a>

#### longitudinal_end_angle

```python
@longitudinal_end_angle.setter
def longitudinal_end_angle(value: float) -> None
```

<a id="unreal.PCGCreatePointsSphereSettings.jitter"></a>

#### jitter

```python
@property
def jitter() -> float
```

(double):  [Read-Write] Adds randomization (in the range of [-Jitter, Jitter]) of the angles of a generated point.

<a id="unreal.PCGCreatePointsSphereSettings.jitter"></a>

#### jitter

```python
@jitter.setter
def jitter(value: float) -> None
```

<a id="unreal.PCGCreatePointsSphereSettings.point_steepness"></a>

#### point_steepness

```python
@property
def point_steepness() -> float
```

(float):  [Read-Write] Directly set as the output points' steepness value.

<a id="unreal.PCGCreatePointsSphereSettings.point_steepness"></a>

#### point_steepness

```python
@point_steepness.setter
def point_steepness(value: float) -> None
```

<a id="unreal.PCGCreatePointsSphereSettings.cull_points_outside_volume"></a>

#### cull_points_outside_volume

```python
@property
def cull_points_outside_volume() -> bool
```

(bool):  [Read-Write] Points are removed if they are outside the volume.

<a id="unreal.PCGCreatePointsSphereSettings.cull_points_outside_volume"></a>

#### cull_points_outside_volume

```python
@cull_points_outside_volume.setter
def cull_points_outside_volume(value: bool) -> None
```

<a id="unreal.PCGCreateSplineSettings"></a>