## PCGSpatialNoiseSettings Objects

```python
class PCGSpatialNoiseSettings(PCGSettings)
```

Various fractal noises that can be used to filter points

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSpatialNoise.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``brightness`` (float):  [Read-Write]
- ``category`` (Text):  [Read-Write]
- ``contrast`` (float):  [Read-Write]
- ``debug`` (bool):  [Read-Write]
- ``debug_buffer_size`` (int32):  [Read-Write] Size (in number of floats) of the shader debug print buffer.
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``description`` (Text):  [Read-Write]
- ``determinism_settings`` (PCGDeterminismSettings):  [Read-Write]
- ``dump_cooked_hlsl`` (bool):  [Read-Write] Dump the cooked HLSL into the log after it is generated.
- ``dump_data_descriptions`` (bool):  [Read-Write] Dump the data descriptions of input/output pins to the log.
- ``edge_blend_curve_intensity`` (float):  [Read-Write] will makes the falloff harsher or softer
- ``edge_blend_curve_offset`` (float):  [Read-Write] Adjust the center point of the curve (where x = curve(x) crosses over)
- ``edge_blend_distance`` (float):  [Read-Write] if > 0, we blend to a tiling edge value
- ``edge_mask2d_mode`` (PCGSpatialNoiseMask2DMode):  [Read-Write]
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``iterations`` (int32):  [Read-Write] this is how many times the fractal method recurses. A higher number will mean more detail
- ``mode`` (PCGSpatialNoiseMode):  [Read-Write] The noise method used
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``random_offset`` (Vector):  [Read-Write] Adds a random amount of offset up to this amount
- ``seed`` (int32):  [Read-Write]
- ``tiled_voronoi_edge_blend_cell_count`` (int32):  [Read-Write] how many cells around the edge will tile
- ``tiled_voronoi_resolution`` (int32):  [Read-Write] The cell resolution of the tiled voronoi (across the bounds)
- ``tiling`` (bool):  [Read-Write] if true, will generate results that tile along the bounding box size of the
- ``transform`` (Transform):  [Read-Write] this will apply a transform to the points before calculating noise
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.
- ``value_target`` (PCGAttributePropertyOutputNoSourceSelector):  [Read-Write] The output attribute name to write, if not 'None'
- ``voronoi_cell_id_target`` (PCGAttributePropertyOutputNoSourceSelector):  [Read-Write] The output attribute name to write the voronoi cell id, if not 'None'
- ``voronoi_cell_randomness`` (double):  [Read-Write] the less random this is, the more it returns to being a grid
- ``voronoi_orient_samples_to_cell_edge`` (bool):  [Read-Write] If true it will orient the output points to point towards the cell edges, which can be used for effects

<a id="unreal.PCGSpatialNoiseSettings.mode"></a>

#### mode

```python
@property
def mode() -> PCGSpatialNoiseMode
```

(PCGSpatialNoiseMode):  [Read-Write] The noise method used

<a id="unreal.PCGSpatialNoiseSettings.mode"></a>

#### mode

```python
@mode.setter
def mode(value: PCGSpatialNoiseMode) -> None
```

<a id="unreal.PCGSpatialNoiseSettings.edge_mask2d_mode"></a>

#### edge_mask2d_mode

```python
@property
def edge_mask2d_mode() -> PCGSpatialNoiseMask2DMode
```

(PCGSpatialNoiseMask2DMode):  [Read-Write]

<a id="unreal.PCGSpatialNoiseSettings.edge_mask2d_mode"></a>

#### edge_mask2d_mode

```python
@edge_mask2d_mode.setter
def edge_mask2d_mode(value: PCGSpatialNoiseMask2DMode) -> None
```

<a id="unreal.PCGSpatialNoiseSettings.iterations"></a>

#### iterations

```python
@property
def iterations() -> int
```

(int32):  [Read-Write] this is how many times the fractal method recurses. A higher number will mean more detail

<a id="unreal.PCGSpatialNoiseSettings.iterations"></a>

#### iterations

```python
@iterations.setter
def iterations(value: int) -> None
```

<a id="unreal.PCGSpatialNoiseSettings.tiling"></a>

#### tiling

```python
@property
def tiling() -> bool
```

(bool):  [Read-Write] if true, will generate results that tile along the bounding box size of the

<a id="unreal.PCGSpatialNoiseSettings.tiling"></a>

#### tiling

```python
@tiling.setter
def tiling(value: bool) -> None
```

<a id="unreal.PCGSpatialNoiseSettings.brightness"></a>

#### brightness

```python
@property
def brightness() -> float
```

(float):  [Read-Write]

<a id="unreal.PCGSpatialNoiseSettings.brightness"></a>

#### brightness

```python
@brightness.setter
def brightness(value: float) -> None
```

<a id="unreal.PCGSpatialNoiseSettings.contrast"></a>

#### contrast

```python
@property
def contrast() -> float
```

(float):  [Read-Write]

<a id="unreal.PCGSpatialNoiseSettings.contrast"></a>

#### contrast

```python
@contrast.setter
def contrast(value: float) -> None
```

<a id="unreal.PCGSpatialNoiseSettings.value_target"></a>

#### value_target

```python
@property
def value_target() -> PCGAttributePropertyOutputNoSourceSelector
```

(PCGAttributePropertyOutputNoSourceSelector):  [Read-Write] The output attribute name to write, if not 'None'

<a id="unreal.PCGSpatialNoiseSettings.value_target"></a>

#### value_target

```python
@value_target.setter
def value_target(value: PCGAttributePropertyOutputNoSourceSelector) -> None
```

<a id="unreal.PCGSpatialNoiseSettings.random_offset"></a>

#### random_offset

```python
@property
def random_offset() -> Vector
```

(Vector):  [Read-Write] Adds a random amount of offset up to this amount

<a id="unreal.PCGSpatialNoiseSettings.random_offset"></a>

#### random_offset

```python
@random_offset.setter
def random_offset(value: Vector) -> None
```

<a id="unreal.PCGSpatialNoiseSettings.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write] this will apply a transform to the points before calculating noise

<a id="unreal.PCGSpatialNoiseSettings.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.PCGSpatialNoiseSettings.voronoi_cell_randomness"></a>

#### voronoi_cell_randomness

```python
@property
def voronoi_cell_randomness() -> float
```

(double):  [Read-Write] the less random this is, the more it returns to being a grid

<a id="unreal.PCGSpatialNoiseSettings.voronoi_cell_randomness"></a>

#### voronoi_cell_randomness

```python
@voronoi_cell_randomness.setter
def voronoi_cell_randomness(value: float) -> None
```

<a id="unreal.PCGSpatialNoiseSettings.voronoi_cell_id_target"></a>

#### voronoi_cell_id_target

```python
@property
def voronoi_cell_id_target() -> PCGAttributePropertyOutputNoSourceSelector
```

(PCGAttributePropertyOutputNoSourceSelector):  [Read-Write] The output attribute name to write the voronoi cell id, if not 'None'

<a id="unreal.PCGSpatialNoiseSettings.voronoi_cell_id_target"></a>

#### voronoi_cell_id_target

```python
@voronoi_cell_id_target.setter
def voronoi_cell_id_target(
        value: PCGAttributePropertyOutputNoSourceSelector) -> None
```

<a id="unreal.PCGSpatialNoiseSettings.voronoi_orient_samples_to_cell_edge"></a>

#### voronoi_orient_samples_to_cell_edge

```python
@property
def voronoi_orient_samples_to_cell_edge() -> bool
```

(bool):  [Read-Write] If true it will orient the output points to point towards the cell edges, which can be used for effects

<a id="unreal.PCGSpatialNoiseSettings.voronoi_orient_samples_to_cell_edge"></a>

#### voronoi_orient_samples_to_cell_edge

```python
@voronoi_orient_samples_to_cell_edge.setter
def voronoi_orient_samples_to_cell_edge(value: bool) -> None
```

<a id="unreal.PCGSpatialNoiseSettings.tiled_voronoi_resolution"></a>

#### tiled_voronoi_resolution

```python
@property
def tiled_voronoi_resolution() -> int
```

(int32):  [Read-Write] The cell resolution of the tiled voronoi (across the bounds)

<a id="unreal.PCGSpatialNoiseSettings.tiled_voronoi_resolution"></a>

#### tiled_voronoi_resolution

```python
@tiled_voronoi_resolution.setter
def tiled_voronoi_resolution(value: int) -> None
```

<a id="unreal.PCGSpatialNoiseSettings.tiled_voronoi_edge_blend_cell_count"></a>

#### tiled_voronoi_edge_blend_cell_count

```python
@property
def tiled_voronoi_edge_blend_cell_count() -> int
```

(int32):  [Read-Write] how many cells around the edge will tile

<a id="unreal.PCGSpatialNoiseSettings.tiled_voronoi_edge_blend_cell_count"></a>

#### tiled_voronoi_edge_blend_cell_count

```python
@tiled_voronoi_edge_blend_cell_count.setter
def tiled_voronoi_edge_blend_cell_count(value: int) -> None
```

<a id="unreal.PCGSpatialNoiseSettings.edge_blend_distance"></a>

#### edge_blend_distance

```python
@property
def edge_blend_distance() -> float
```

(float):  [Read-Write] if > 0, we blend to a tiling edge value

<a id="unreal.PCGSpatialNoiseSettings.edge_blend_distance"></a>

#### edge_blend_distance

```python
@edge_blend_distance.setter
def edge_blend_distance(value: float) -> None
```

<a id="unreal.PCGSpatialNoiseSettings.edge_blend_curve_offset"></a>

#### edge_blend_curve_offset

```python
@property
def edge_blend_curve_offset() -> float
```

(float):  [Read-Write] Adjust the center point of the curve (where x = curve(x) crosses over)

<a id="unreal.PCGSpatialNoiseSettings.edge_blend_curve_offset"></a>

#### edge_blend_curve_offset

```python
@edge_blend_curve_offset.setter
def edge_blend_curve_offset(value: float) -> None
```

<a id="unreal.PCGSpatialNoiseSettings.edge_blend_curve_intensity"></a>

#### edge_blend_curve_intensity

```python
@property
def edge_blend_curve_intensity() -> float
```

(float):  [Read-Write] will makes the falloff harsher or softer

<a id="unreal.PCGSpatialNoiseSettings.edge_blend_curve_intensity"></a>

#### edge_blend_curve_intensity

```python
@edge_blend_curve_intensity.setter
def edge_blend_curve_intensity(value: float) -> None
```

<a id="unreal.PCGSpawnActorSettings"></a>