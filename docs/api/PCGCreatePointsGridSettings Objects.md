## PCGCreatePointsGridSettings Objects

```python
class PCGCreatePointsGridSettings(PCGSettings)
```

Creates a 2D or 3D grid of points.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCreatePointsGrid.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``cell_size`` (Vector):  [Read-Write]
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
- ``grid_extents`` (Vector):  [Read-Write]
- ``point_position`` (PCGPointPosition):  [Read-Write]
- ``point_steepness`` (float):  [Read-Write] Each PCG point represents a discretized, volumetric region of world space. The points' Steepness value [0.0 to
  1.0] establishes how "hard" or "soft" that volume will be represented. From 0, it will ramp up linearly
  increasing its influence over the density from the point's center to up to two times the bounds. At 1, it will
  represent a binary box function with the size of the point's bounds.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``set_points_bounds`` (bool):  [Read-Write] If true, the bounds of the points are set to 50.0, if false, 1.0
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGCreatePointsGridSettings.grid_extents"></a>

#### grid_extents

```python
@property
def grid_extents() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.PCGCreatePointsGridSettings.grid_extents"></a>

#### grid_extents

```python
@grid_extents.setter
def grid_extents(value: Vector) -> None
```

<a id="unreal.PCGCreatePointsGridSettings.cell_size"></a>

#### cell_size

```python
@property
def cell_size() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.PCGCreatePointsGridSettings.cell_size"></a>

#### cell_size

```python
@cell_size.setter
def cell_size(value: Vector) -> None
```

<a id="unreal.PCGCreatePointsGridSettings.point_steepness"></a>

#### point_steepness

```python
@property
def point_steepness() -> float
```

(float):  [Read-Write] Each PCG point represents a discretized, volumetric region of world space. The points' Steepness value [0.0 to
1.0] establishes how "hard" or "soft" that volume will be represented. From 0, it will ramp up linearly
increasing its influence over the density from the point's center to up to two times the bounds. At 1, it will
represent a binary box function with the size of the point's bounds.

<a id="unreal.PCGCreatePointsGridSettings.point_steepness"></a>

#### point_steepness

```python
@point_steepness.setter
def point_steepness(value: float) -> None
```

<a id="unreal.PCGCreatePointsGridSettings.coordinate_space"></a>

#### coordinate_space

```python
@property
def coordinate_space() -> PCGCoordinateSpace
```

(PCGCoordinateSpace):  [Read-Write] Sets the generation referential of the points

<a id="unreal.PCGCreatePointsGridSettings.coordinate_space"></a>

#### coordinate_space

```python
@coordinate_space.setter
def coordinate_space(value: PCGCoordinateSpace) -> None
```

<a id="unreal.PCGCreatePointsGridSettings.set_points_bounds"></a>

#### set_points_bounds

```python
@property
def set_points_bounds() -> bool
```

(bool):  [Read-Write] If true, the bounds of the points are set to 50.0, if false, 1.0

<a id="unreal.PCGCreatePointsGridSettings.set_points_bounds"></a>

#### set_points_bounds

```python
@set_points_bounds.setter
def set_points_bounds(value: bool) -> None
```

<a id="unreal.PCGCreatePointsGridSettings.cull_points_outside_volume"></a>

#### cull_points_outside_volume

```python
@property
def cull_points_outside_volume() -> bool
```

(bool):  [Read-Write] If true, points are removed if they are outside of the volume

<a id="unreal.PCGCreatePointsGridSettings.cull_points_outside_volume"></a>

#### cull_points_outside_volume

```python
@cull_points_outside_volume.setter
def cull_points_outside_volume(value: bool) -> None
```

<a id="unreal.PCGCreatePointsGridSettings.point_position"></a>

#### point_position

```python
@property
def point_position() -> PCGPointPosition
```

(PCGPointPosition):  [Read-Write]

<a id="unreal.PCGCreatePointsGridSettings.point_position"></a>

#### point_position

```python
@point_position.setter
def point_position(value: PCGPointPosition) -> None
```

<a id="unreal.PCGCullPointsOutsideActorBoundsSettings"></a>