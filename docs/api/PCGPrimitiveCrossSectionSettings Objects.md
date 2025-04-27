## PCGPrimitiveCrossSectionSettings Objects

```python
class PCGPrimitiveCrossSectionSettings(PCGSettings)
```

Creates spline cross-sections of one more primitives based on vertex features.

**C++ Source:**

- **Plugin**: PCGGeometryScriptInterop
- **Module**: PCGGeometryScriptInterop
- **File**: PCGPrimitiveCrossSection.h

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
- ``enable_min_area_culling`` (bool):  [Read-Write] Cull tiers that have a surface area smaller than a specified threshold.
- ``enable_tier_merging`` (bool):  [Read-Write] Cull tiers that are within a specified threshold.
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``extrusion_vector_attribute`` (PCGAttributePropertyOutputSelector):  [Read-Write] The attribute that will be populated with each cross-section's extrusion vector.
- ``max_mesh_vertex_count`` (int32):  [Read-Write] A safeguard to prevent finding features on an overly complex mesh.
- ``min_area_culling_threshold`` (double):  [Read-Write] If a tier is smaller in area than this threshold, it will be culled.
- ``minimum_coplanar_vertices`` (int32):  [Read-Write] The minimum required number of vertices that must be co-planar in order to be considered a tier "feature".
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``remove_redundant_sections`` (bool):  [Read-Write] If multiple tiers can be combined into a single tier without affecting the contour, remove the redundant one. Note: This will currently cull even if there are other unique tiers in between.
- ``seed`` (int32):  [Read-Write]
- ``slice_direction`` (Vector):  [Read-Write] Slicing will happen from the minimum vertex along this direction vector (normalized).
- ``tier_merging_threshold`` (double):  [Read-Write] If a tier is within this distance (in cm) of the previous tier, it will be culled.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGPrimitiveCrossSectionSettings.slice_direction"></a>

#### slice_direction

```python
@property
def slice_direction() -> Vector
```

(Vector):  [Read-Write] Slicing will happen from the minimum vertex along this direction vector (normalized).

<a id="unreal.PCGPrimitiveCrossSectionSettings.slice_direction"></a>

#### slice_direction

```python
@slice_direction.setter
def slice_direction(value: Vector) -> None
```

<a id="unreal.PCGPrimitiveCrossSectionSettings.extrusion_vector_attribute"></a>

#### extrusion_vector_attribute

```python
@property
def extrusion_vector_attribute() -> PCGAttributePropertyOutputSelector
```

(PCGAttributePropertyOutputSelector):  [Read-Write] The attribute that will be populated with each cross-section's extrusion vector.

<a id="unreal.PCGPrimitiveCrossSectionSettings.extrusion_vector_attribute"></a>

#### extrusion_vector_attribute

```python
@extrusion_vector_attribute.setter
def extrusion_vector_attribute(
        value: PCGAttributePropertyOutputSelector) -> None
```

<a id="unreal.PCGPrimitiveCrossSectionSettings.minimum_coplanar_vertices"></a>

#### minimum_coplanar_vertices

```python
@property
def minimum_coplanar_vertices() -> int
```

(int32):  [Read-Write] The minimum required number of vertices that must be co-planar in order to be considered a tier "feature".

<a id="unreal.PCGPrimitiveCrossSectionSettings.minimum_coplanar_vertices"></a>

#### minimum_coplanar_vertices

```python
@minimum_coplanar_vertices.setter
def minimum_coplanar_vertices(value: int) -> None
```

<a id="unreal.PCGPrimitiveCrossSectionSettings.max_mesh_vertex_count"></a>

#### max_mesh_vertex_count

```python
@property
def max_mesh_vertex_count() -> int
```

(int32):  [Read-Write] A safeguard to prevent finding features on an overly complex mesh.

<a id="unreal.PCGPrimitiveCrossSectionSettings.max_mesh_vertex_count"></a>

#### max_mesh_vertex_count

```python
@max_mesh_vertex_count.setter
def max_mesh_vertex_count(value: int) -> None
```

<a id="unreal.PCGPrimitiveCrossSectionSettings.enable_tier_merging"></a>

#### enable_tier_merging

```python
@property
def enable_tier_merging() -> bool
```

(bool):  [Read-Write] Cull tiers that are within a specified threshold.

<a id="unreal.PCGPrimitiveCrossSectionSettings.enable_tier_merging"></a>

#### enable_tier_merging

```python
@enable_tier_merging.setter
def enable_tier_merging(value: bool) -> None
```

<a id="unreal.PCGPrimitiveCrossSectionSettings.tier_merging_threshold"></a>

#### tier_merging_threshold

```python
@property
def tier_merging_threshold() -> float
```

(double):  [Read-Write] If a tier is within this distance (in cm) of the previous tier, it will be culled.

<a id="unreal.PCGPrimitiveCrossSectionSettings.tier_merging_threshold"></a>

#### tier_merging_threshold

```python
@tier_merging_threshold.setter
def tier_merging_threshold(value: float) -> None
```

<a id="unreal.PCGPrimitiveCrossSectionSettings.enable_min_area_culling"></a>

#### enable_min_area_culling

```python
@property
def enable_min_area_culling() -> bool
```

(bool):  [Read-Write] Cull tiers that have a surface area smaller than a specified threshold.

<a id="unreal.PCGPrimitiveCrossSectionSettings.enable_min_area_culling"></a>

#### enable_min_area_culling

```python
@enable_min_area_culling.setter
def enable_min_area_culling(value: bool) -> None
```

<a id="unreal.PCGPrimitiveCrossSectionSettings.min_area_culling_threshold"></a>

#### min_area_culling_threshold

```python
@property
def min_area_culling_threshold() -> float
```

(double):  [Read-Write] If a tier is smaller in area than this threshold, it will be culled.

<a id="unreal.PCGPrimitiveCrossSectionSettings.min_area_culling_threshold"></a>

#### min_area_culling_threshold

```python
@min_area_culling_threshold.setter
def min_area_culling_threshold(value: float) -> None
```

<a id="unreal.PCGPrimitiveCrossSectionSettings.remove_redundant_sections"></a>

#### remove_redundant_sections

```python
@property
def remove_redundant_sections() -> bool
```

(bool):  [Read-Write] If multiple tiers can be combined into a single tier without affecting the contour, remove the redundant one. Note: This will currently cull even if there are other unique tiers in between.

<a id="unreal.PCGPrimitiveCrossSectionSettings.remove_redundant_sections"></a>

#### remove_redundant_sections

```python
@remove_redundant_sections.setter
def remove_redundant_sections(value: bool) -> None
```

<a id="unreal.PCGSplineCrossSectionGeneratorSettings"></a>