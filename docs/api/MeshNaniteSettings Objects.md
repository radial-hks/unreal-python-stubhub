## MeshNaniteSettings Objects

```python
class MeshNaniteSettings(StructBase)
```

Settings applied when building Nanite data.

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``displacement_maps`` (Array[MeshDisplacementMap]):  [Read-Write]
- ``displacement_uv_channel`` (int32):  [Read-Write] UV channel used to sample displacement maps
- ``enabled`` (bool):  [Read-Write] If true, Nanite data will be generated.
- ``explicit_tangents`` (bool):  [Read-Write] Whether to store explicit tangents instead of using the implicitly derived ones.
- ``fallback_percent_triangles`` (float):  [Read-Write] Percentage of triangles to keep from source mesh for fallback. 1.0 = no reduction, 0.0 = no triangles.
- ``fallback_relative_error`` (float):  [Read-Write] Reduce until at least this amount of error is reached relative to size of the mesh
- ``fallback_target`` (NaniteFallbackTarget):  [Read-Write] Which heuristic to use when generating the fallback mesh.
- ``keep_percent_triangles`` (float):  [Read-Write] Percentage of triangles to keep from source mesh. 1.0 = no reduction, 0.0 = no triangles.
- ``lerp_u_vs`` (bool):  [Read-Write] Whether to interpolate UVs when simplifying.
  Should be enabled whenever possible.
  For real UV coordinates this allows calculating the lowest error optimal UVs for new vertices when simplifying,
  assuming the UVs are used as normal texture coordinates and will interpolate across the face of the triangles.

  Disable if data stored in UVs isn't valid to interpolate, for example if indexes are stored in UVs.
  Lerping an index doesn't make sense and would break the shader trying to use it.
  Note: If disabled, error from UVs is no longer accounted for when Nanite selects the LOD to render because
  error due to arbitrary vertex attributes that aren't interpolatable can't be generally reasoned about.
- ``max_edge_length_factor`` (float):  [Read-Write] Controls the maximum distance allowed between each vertex of the mesh on screen. Can be used to prevent oversimplification
  of meshes that are intended to be deformed (e.g. animation using World Position Offset, Spline Mesh Component, etc.).
  Should be left at default of 0 unless explicitly needed to fix oversimplification issues.
- ``normal_precision`` (int32):  [Read-Write] Normal Precision in bits. -1 is auto.
- ``position_precision`` (int32):  [Read-Write] Position Precision. Step size is 2^(-PositionPrecision) cm. MIN_int32 is auto.
- ``preserve_area`` (bool):  [Read-Write] Whether to try and maintain the same surface area at all distances. Useful for foliage that thins out otherwise.
- ``tangent_precision`` (int32):  [Read-Write] Tangent Precision in bits. -1 is auto.
- ``target_minimum_residency_in_kb`` (uint32):  [Read-Write] How much of the resource should always be resident (In KB). Approximate due to paging. 0: Minimum size (single page). MAX_uint32: Entire mesh.
- ``trim_relative_error`` (float):  [Read-Write] Reduce until at least this amount of error is reached relative to size of the mesh

<a id="unreal.MeshNaniteSettings.__init__"></a>

#### __init__

```python
def __init__(enabled: bool = False,
             preserve_area: bool = False,
             explicit_tangents: bool = False,
             lerp_u_vs: bool = False,
             position_precision: int = 0,
             normal_precision: int = 0,
             tangent_precision: int = 0,
             keep_percent_triangles: float = 0.000000,
             trim_relative_error: float = 0.000000,
             fallback_target: NaniteFallbackTarget = NaniteFallbackTarget.AUTO,
             fallback_percent_triangles: float = 0.000000,
             fallback_relative_error: float = 0.000000,
             max_edge_length_factor: float = 0.000000,
             displacement_uv_channel: int = 0) -> None
```

<a id="unreal.MeshNaniteSettings.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write] If true, Nanite data will be generated.

<a id="unreal.MeshNaniteSettings.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.MeshNaniteSettings.preserve_area"></a>

#### preserve_area

```python
@property
def preserve_area() -> bool
```

(bool):  [Read-Write] Whether to try and maintain the same surface area at all distances. Useful for foliage that thins out otherwise.

<a id="unreal.MeshNaniteSettings.preserve_area"></a>

#### preserve_area

```python
@preserve_area.setter
def preserve_area(value: bool) -> None
```

<a id="unreal.MeshNaniteSettings.explicit_tangents"></a>

#### explicit_tangents

```python
@property
def explicit_tangents() -> bool
```

(bool):  [Read-Write] Whether to store explicit tangents instead of using the implicitly derived ones.

<a id="unreal.MeshNaniteSettings.explicit_tangents"></a>

#### explicit_tangents

```python
@explicit_tangents.setter
def explicit_tangents(value: bool) -> None
```

<a id="unreal.MeshNaniteSettings.lerp_u_vs"></a>

#### lerp_u_vs

```python
@property
def lerp_u_vs() -> bool
```

(bool):  [Read-Write] Whether to interpolate UVs when simplifying.
Should be enabled whenever possible.
For real UV coordinates this allows calculating the lowest error optimal UVs for new vertices when simplifying,
assuming the UVs are used as normal texture coordinates and will interpolate across the face of the triangles.

Disable if data stored in UVs isn't valid to interpolate, for example if indexes are stored in UVs.
Lerping an index doesn't make sense and would break the shader trying to use it.
Note: If disabled, error from UVs is no longer accounted for when Nanite selects the LOD to render because
error due to arbitrary vertex attributes that aren't interpolatable can't be generally reasoned about.

<a id="unreal.MeshNaniteSettings.lerp_u_vs"></a>

#### lerp_u_vs

```python
@lerp_u_vs.setter
def lerp_u_vs(value: bool) -> None
```

<a id="unreal.MeshNaniteSettings.position_precision"></a>

#### position_precision

```python
@property
def position_precision() -> int
```

(int32):  [Read-Write] Position Precision. Step size is 2^(-PositionPrecision) cm. MIN_int32 is auto.

<a id="unreal.MeshNaniteSettings.position_precision"></a>

#### position_precision

```python
@position_precision.setter
def position_precision(value: int) -> None
```

<a id="unreal.MeshNaniteSettings.normal_precision"></a>

#### normal_precision

```python
@property
def normal_precision() -> int
```

(int32):  [Read-Write] Normal Precision in bits. -1 is auto.

<a id="unreal.MeshNaniteSettings.normal_precision"></a>

#### normal_precision

```python
@normal_precision.setter
def normal_precision(value: int) -> None
```

<a id="unreal.MeshNaniteSettings.tangent_precision"></a>

#### tangent_precision

```python
@property
def tangent_precision() -> int
```

(int32):  [Read-Write] Tangent Precision in bits. -1 is auto.

<a id="unreal.MeshNaniteSettings.tangent_precision"></a>

#### tangent_precision

```python
@tangent_precision.setter
def tangent_precision(value: int) -> None
```

<a id="unreal.MeshNaniteSettings.keep_percent_triangles"></a>

#### keep_percent_triangles

```python
@property
def keep_percent_triangles() -> float
```

(float):  [Read-Write] Percentage of triangles to keep from source mesh. 1.0 = no reduction, 0.0 = no triangles.

<a id="unreal.MeshNaniteSettings.keep_percent_triangles"></a>

#### keep_percent_triangles

```python
@keep_percent_triangles.setter
def keep_percent_triangles(value: float) -> None
```

<a id="unreal.MeshNaniteSettings.trim_relative_error"></a>

#### trim_relative_error

```python
@property
def trim_relative_error() -> float
```

(float):  [Read-Write] Reduce until at least this amount of error is reached relative to size of the mesh

<a id="unreal.MeshNaniteSettings.trim_relative_error"></a>

#### trim_relative_error

```python
@trim_relative_error.setter
def trim_relative_error(value: float) -> None
```

<a id="unreal.MeshNaniteSettings.fallback_target"></a>

#### fallback_target

```python
@property
def fallback_target() -> NaniteFallbackTarget
```

(NaniteFallbackTarget):  [Read-Write] Which heuristic to use when generating the fallback mesh.

<a id="unreal.MeshNaniteSettings.fallback_target"></a>

#### fallback_target

```python
@fallback_target.setter
def fallback_target(value: NaniteFallbackTarget) -> None
```

<a id="unreal.MeshNaniteSettings.fallback_percent_triangles"></a>

#### fallback_percent_triangles

```python
@property
def fallback_percent_triangles() -> float
```

(float):  [Read-Write] Percentage of triangles to keep from source mesh for fallback. 1.0 = no reduction, 0.0 = no triangles.

<a id="unreal.MeshNaniteSettings.fallback_percent_triangles"></a>

#### fallback_percent_triangles

```python
@fallback_percent_triangles.setter
def fallback_percent_triangles(value: float) -> None
```

<a id="unreal.MeshNaniteSettings.fallback_relative_error"></a>

#### fallback_relative_error

```python
@property
def fallback_relative_error() -> float
```

(float):  [Read-Write] Reduce until at least this amount of error is reached relative to size of the mesh

<a id="unreal.MeshNaniteSettings.fallback_relative_error"></a>

#### fallback_relative_error

```python
@fallback_relative_error.setter
def fallback_relative_error(value: float) -> None
```

<a id="unreal.MeshNaniteSettings.max_edge_length_factor"></a>

#### max_edge_length_factor

```python
@property
def max_edge_length_factor() -> float
```

(float):  [Read-Write] Controls the maximum distance allowed between each vertex of the mesh on screen. Can be used to prevent oversimplification
of meshes that are intended to be deformed (e.g. animation using World Position Offset, Spline Mesh Component, etc.).
Should be left at default of 0 unless explicitly needed to fix oversimplification issues.

<a id="unreal.MeshNaniteSettings.max_edge_length_factor"></a>

#### max_edge_length_factor

```python
@max_edge_length_factor.setter
def max_edge_length_factor(value: float) -> None
```

<a id="unreal.MeshNaniteSettings.displacement_uv_channel"></a>

#### displacement_uv_channel

```python
@property
def displacement_uv_channel() -> int
```

(int32):  [Read-Write] UV channel used to sample displacement maps

<a id="unreal.MeshNaniteSettings.displacement_uv_channel"></a>

#### displacement_uv_channel

```python
@displacement_uv_channel.setter
def displacement_uv_channel(value: int) -> None
```

<a id="unreal.DisplacementScaling"></a>