## MeshApproximationSettings Objects

```python
class MeshApproximationSettings(StructBase)
```

Mesh Approximation Settings

**C++ Source:**

- **Module**: Engine
- **File**: MeshApproximationSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_distance_field`` (bool):  [Read-Write] Whether to allow distance field to be computed for this mesh. Disable this to save memory if the generated mesh will only be rendered in the distance.
- ``approximation_accuracy`` (float):  [Read-Write] Approximation Accuracy in Meters, will determine (eg) voxel resolution
- ``attempt_auto_thickening`` (bool):  [Read-Write] if enabled, we will attempt to auto-thicken thin parts or flat sheets
- ``base_capping`` (MeshApproximationBaseCappingType):  [Read-Write] Optional methods to attempt to close off the bottom of open meshes
- ``capture_field_of_view`` (float):  [Read-Write]
- ``clamp_voxel_dimension`` (int32):  [Read-Write] Maximum allowable voxel count along main directions. This is a limit on ApproximationAccuracy. Max of 1290 (1290^3 is the last integer < 2^31, using a bigger number results in failures in TArray code & probably elsewhere)
- ``curvature_alignment`` (float):  [Read-Write] This parameter controls alignment of the initial patches to creases in the mesh
- ``emit_full_debug_mesh`` (bool):  [Read-Write] If true, write the full mesh triangle set (ie flattened, non-instanced) used for mesh generation. Warning: this asset may be extremely large!!
- ``enable_parallel_baking`` (bool):  [Read-Write] If false, texture capture and baking will be done serially after mesh generation, rather than in parallel when possible. This will reduce the maximum memory requirements of the process.
- ``enable_simplify_pre_pass`` (bool):  [Read-Write] If true, a faster mesh simplfication strategy will be used. This can significantly reduce computation time and memory usage, but potentially at the cost of lower quality output.
- ``estimate_hard_normals`` (bool):  [Read-Write] If true, normal angle will be used to estimate hard normals
- ``fill_gaps`` (bool):  [Read-Write] If true, topological expand/contract is used to try to fill small gaps between objects.
- ``gap_distance`` (float):  [Read-Write] Distance in Meters to expand/contract to fill gaps
- ``generate_nanite_enabled_mesh`` (bool):  [Read-Write] Whether to generate a nanite-enabled mesh
- ``geometric_deviation`` (float):  [Read-Write] Allowable Geometric Deviation in Meters when SimplifyMethod incorporates a Geometric Tolerance
- ``ground_clipping`` (MeshApproximationGroundPlaneClippingPolicy):  [Read-Write] Configure how the final mesh should be clipped with a ground plane, if desired
- ``ground_clipping_z_height`` (float):  [Read-Write] Z-Height for the ground clipping plane, if enabled
- ``hard_normal_angle`` (float):  [Read-Write]
- ``ignore_tiny_parts`` (bool):  [Read-Write] If enabled, tiny parts will be excluded from the mesh merging, which can improve performance
- ``initial_patch_count`` (int32):  [Read-Write] Number of initial patches mesh will be split into before computing island merging
- ``material_settings`` (MaterialProxySettings):  [Read-Write] Material generation settings
- ``max_angle_deviation`` (float):  [Read-Write] UV islands will not be merged if their average face normals deviate by larger than this amount
- ``merging_threshold`` (float):  [Read-Write] Distortion/Stretching Threshold for island merging - larger values increase the allowable UV stretching
- ``multi_sampling_aa`` (int32):  [Read-Write] If Value is > 1, Multisample output baked textures by this amount in each direction (eg 4 == 16x supersampling)
- ``nanite_fallback_percent_triangles`` (float):  [Read-Write] Percentage of triangles to keep from source Nanite mesh for fallback. 1.0 = no reduction, 0.0 = no triangles.
- ``nanite_fallback_relative_error`` (float):  [Read-Write] Reduce Nanite fallback mesh until at least this amount of error is reached relative to size of the mesh.
- ``nanite_fallback_target`` (NaniteFallbackTarget):  [Read-Write] Which heuristic to use when generating the Nanite fallback mesh.
- ``near_plane_dist`` (float):  [Read-Write]
- ``occlude_from_bottom`` (bool):  [Read-Write] If true, then the OcclusionMethod computation is configured to try to consider downward-facing "bottom" geometry as occluded
- ``occlusion_method`` (OccludedGeometryFilteringPolicy):  [Read-Write] Type of hidden geometry removal to apply
- ``output_type`` (MeshApproximationType):  [Read-Write] Type of output from mesh approximation process
- ``print_debug_messages`` (bool):  [Read-Write] If true, print out debugging messages
- ``render_capture_resolution`` (int32):  [Read-Write] If Value is zero, use MaterialSettings resolution, otherwise override the render capture resolution
- ``simplify_method`` (MeshApproximationSimplificationPolicy):  [Read-Write] Mesh Simplification criteria
- ``support_ray_tracing`` (bool):  [Read-Write] Whether ray tracing will be supported on this mesh. Disable this to save memory if the generated mesh will only be rendered in the distance.
- ``target_min_thickness_multiplier`` (float):  [Read-Write] Multiplier on Approximation Accuracy used for auto-thickening
- ``target_tri_count`` (int32):  [Read-Write] Target triangle count for Mesh Simplification, for SimplifyMethods that use a Count
- ``tiny_part_size_multiplier`` (float):  [Read-Write] Multiplier on Approximation Accuracy used to define tiny-part threshold, using maximum bounding-box dimension
- ``triangles_per_m`` (float):  [Read-Write] Approximate Number of triangles per Square Meter, for SimplifyMethods that use such a constraint
- ``use_render_lod_meshes`` (bool):  [Read-Write] If true, LOD0 Render Meshes (or Nanite Fallback meshes) are used instead of Source Mesh data. This can significantly reduce computation time and memory usage, but potentially at the cost of lower quality output.
- ``uv_generation_method`` (MeshApproximationUVGenerationPolicy):  [Read-Write] Mesh UV Generation Settings
- ``winding_threshold`` (float):  [Read-Write] Winding Threshold controls hole filling at open mesh borders. Smaller value means "more/rounder" filling

<a id="unreal.MeshApproximationSettings.__init__"></a>

#### __init__

```python
def __init__(
        output_type: MeshApproximationType = MeshApproximationType.
    MESH_AND_MATERIALS,
        approximation_accuracy: float = 0.000000,
        clamp_voxel_dimension: int = 0,
        attempt_auto_thickening: bool = False,
        target_min_thickness_multiplier: float = 0.000000,
        ignore_tiny_parts: bool = False,
        tiny_part_size_multiplier: float = 0.000000,
        base_capping:
    MeshApproximationBaseCappingType = MeshApproximationBaseCappingType.
    NO_BASE_CAPPING,
        winding_threshold: float = 0.000000,
        fill_gaps: bool = False,
        gap_distance: float = 0.000000,
        occlusion_method:
    OccludedGeometryFilteringPolicy = OccludedGeometryFilteringPolicy.
    NO_OCCLUSION_FILTERING,
        occlude_from_bottom: bool = False,
        simplify_method:
    MeshApproximationSimplificationPolicy = MeshApproximationSimplificationPolicy
    .FIXED_TRIANGLE_COUNT,
        target_tri_count: int = 0,
        triangles_per_m: float = 0.000000,
        geometric_deviation: float = 0.000000,
        ground_clipping:
    MeshApproximationGroundPlaneClippingPolicy = MeshApproximationGroundPlaneClippingPolicy
    .NO_GROUND_CLIPPING,
        ground_clipping_z_height: float = 0.000000,
        estimate_hard_normals: bool = False,
        hard_normal_angle: float = 0.000000,
        uv_generation_method:
    MeshApproximationUVGenerationPolicy = MeshApproximationUVGenerationPolicy.
    PREFER_UV_ATLAS,
        initial_patch_count: int = 0,
        curvature_alignment: float = 0.000000,
        merging_threshold: float = 0.000000,
        max_angle_deviation: float = 0.000000,
        generate_nanite_enabled_mesh: bool = False,
        nanite_fallback_target: NaniteFallbackTarget = NaniteFallbackTarget.
    AUTO,
        nanite_fallback_percent_triangles: float = 0.000000,
        nanite_fallback_relative_error: float = 0.000000,
        support_ray_tracing: bool = False,
        allow_distance_field: bool = False,
        multi_sampling_aa: int = 0,
        render_capture_resolution: int = 0,
        material_settings: MaterialProxySettings = [
            TextureSizingType.TEXTURE_SIZING_TYPE_USE_SINGLE_TEXTURE_SIZE,
            5.000000, 0.500000, 10000.000000, 4.000000, 0.000000, 0.500000,
            0.000000, 0.500000, 1.000000, 1.000000, 1.000000,
            BlendMode.BLEND_OPAQUE, True, True, False, False, False, False,
            False, False, False, False, False, [1024, 1024], [1024, 1024],
            [1024, 1024], [1024, 1024], [1024, 1024], [1024,
                                                       1024], [1024, 1024],
            [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024]
        ],
        capture_field_of_view: float = 0.000000,
        near_plane_dist: float = 0.000000,
        use_render_lod_meshes: bool = False,
        enable_simplify_pre_pass: bool = False,
        enable_parallel_baking: bool = False,
        print_debug_messages: bool = False,
        emit_full_debug_mesh: bool = False) -> None
```

<a id="unreal.MeshApproximationSettings.output_type"></a>

#### output_type

```python
@property
def output_type() -> MeshApproximationType
```

(MeshApproximationType):  [Read-Write] Type of output from mesh approximation process

<a id="unreal.MeshApproximationSettings.output_type"></a>

#### output_type

```python
@output_type.setter
def output_type(value: MeshApproximationType) -> None
```

<a id="unreal.MeshApproximationSettings.approximation_accuracy"></a>

#### approximation_accuracy

```python
@property
def approximation_accuracy() -> float
```

(float):  [Read-Write] Approximation Accuracy in Meters, will determine (eg) voxel resolution

<a id="unreal.MeshApproximationSettings.approximation_accuracy"></a>

#### approximation_accuracy

```python
@approximation_accuracy.setter
def approximation_accuracy(value: float) -> None
```

<a id="unreal.MeshApproximationSettings.clamp_voxel_dimension"></a>

#### clamp_voxel_dimension

```python
@property
def clamp_voxel_dimension() -> int
```

(int32):  [Read-Write] Maximum allowable voxel count along main directions. This is a limit on ApproximationAccuracy. Max of 1290 (1290^3 is the last integer < 2^31, using a bigger number results in failures in TArray code & probably elsewhere)

<a id="unreal.MeshApproximationSettings.clamp_voxel_dimension"></a>

#### clamp_voxel_dimension

```python
@clamp_voxel_dimension.setter
def clamp_voxel_dimension(value: int) -> None
```

<a id="unreal.MeshApproximationSettings.attempt_auto_thickening"></a>

#### attempt_auto_thickening

```python
@property
def attempt_auto_thickening() -> bool
```

(bool):  [Read-Write] if enabled, we will attempt to auto-thicken thin parts or flat sheets

<a id="unreal.MeshApproximationSettings.attempt_auto_thickening"></a>

#### attempt_auto_thickening

```python
@attempt_auto_thickening.setter
def attempt_auto_thickening(value: bool) -> None
```

<a id="unreal.MeshApproximationSettings.target_min_thickness_multiplier"></a>

#### target_min_thickness_multiplier

```python
@property
def target_min_thickness_multiplier() -> float
```

(float):  [Read-Write] Multiplier on Approximation Accuracy used for auto-thickening

<a id="unreal.MeshApproximationSettings.target_min_thickness_multiplier"></a>

#### target_min_thickness_multiplier

```python
@target_min_thickness_multiplier.setter
def target_min_thickness_multiplier(value: float) -> None
```

<a id="unreal.MeshApproximationSettings.ignore_tiny_parts"></a>

#### ignore_tiny_parts

```python
@property
def ignore_tiny_parts() -> bool
```

(bool):  [Read-Write] If enabled, tiny parts will be excluded from the mesh merging, which can improve performance

<a id="unreal.MeshApproximationSettings.ignore_tiny_parts"></a>

#### ignore_tiny_parts

```python
@ignore_tiny_parts.setter
def ignore_tiny_parts(value: bool) -> None
```

<a id="unreal.MeshApproximationSettings.tiny_part_size_multiplier"></a>

#### tiny_part_size_multiplier

```python
@property
def tiny_part_size_multiplier() -> float
```

(float):  [Read-Write] Multiplier on Approximation Accuracy used to define tiny-part threshold, using maximum bounding-box dimension

<a id="unreal.MeshApproximationSettings.tiny_part_size_multiplier"></a>

#### tiny_part_size_multiplier

```python
@tiny_part_size_multiplier.setter
def tiny_part_size_multiplier(value: float) -> None
```

<a id="unreal.MeshApproximationSettings.base_capping"></a>

#### base_capping

```python
@property
def base_capping() -> MeshApproximationBaseCappingType
```

(MeshApproximationBaseCappingType):  [Read-Write] Optional methods to attempt to close off the bottom of open meshes

<a id="unreal.MeshApproximationSettings.base_capping"></a>

#### base_capping

```python
@base_capping.setter
def base_capping(value: MeshApproximationBaseCappingType) -> None
```

<a id="unreal.MeshApproximationSettings.winding_threshold"></a>

#### winding_threshold

```python
@property
def winding_threshold() -> float
```

(float):  [Read-Write] Winding Threshold controls hole filling at open mesh borders. Smaller value means "more/rounder" filling

<a id="unreal.MeshApproximationSettings.winding_threshold"></a>

#### winding_threshold

```python
@winding_threshold.setter
def winding_threshold(value: float) -> None
```

<a id="unreal.MeshApproximationSettings.fill_gaps"></a>

#### fill_gaps

```python
@property
def fill_gaps() -> bool
```

(bool):  [Read-Write] If true, topological expand/contract is used to try to fill small gaps between objects.

<a id="unreal.MeshApproximationSettings.fill_gaps"></a>

#### fill_gaps

```python
@fill_gaps.setter
def fill_gaps(value: bool) -> None
```

<a id="unreal.MeshApproximationSettings.gap_distance"></a>

#### gap_distance

```python
@property
def gap_distance() -> float
```

(float):  [Read-Write] Distance in Meters to expand/contract to fill gaps

<a id="unreal.MeshApproximationSettings.gap_distance"></a>

#### gap_distance

```python
@gap_distance.setter
def gap_distance(value: float) -> None
```

<a id="unreal.MeshApproximationSettings.occlusion_method"></a>

#### occlusion_method

```python
@property
def occlusion_method() -> OccludedGeometryFilteringPolicy
```

(OccludedGeometryFilteringPolicy):  [Read-Write] Type of hidden geometry removal to apply

<a id="unreal.MeshApproximationSettings.occlusion_method"></a>

#### occlusion_method

```python
@occlusion_method.setter
def occlusion_method(value: OccludedGeometryFilteringPolicy) -> None
```

<a id="unreal.MeshApproximationSettings.occlude_from_bottom"></a>

#### occlude_from_bottom

```python
@property
def occlude_from_bottom() -> bool
```

(bool):  [Read-Write] If true, then the OcclusionMethod computation is configured to try to consider downward-facing "bottom" geometry as occluded

<a id="unreal.MeshApproximationSettings.occlude_from_bottom"></a>

#### occlude_from_bottom

```python
@occlude_from_bottom.setter
def occlude_from_bottom(value: bool) -> None
```

<a id="unreal.MeshApproximationSettings.simplify_method"></a>

#### simplify_method

```python
@property
def simplify_method() -> MeshApproximationSimplificationPolicy
```

(MeshApproximationSimplificationPolicy):  [Read-Write] Mesh Simplification criteria

<a id="unreal.MeshApproximationSettings.simplify_method"></a>

#### simplify_method

```python
@simplify_method.setter
def simplify_method(value: MeshApproximationSimplificationPolicy) -> None
```

<a id="unreal.MeshApproximationSettings.target_tri_count"></a>

#### target_tri_count

```python
@property
def target_tri_count() -> int
```

(int32):  [Read-Write] Target triangle count for Mesh Simplification, for SimplifyMethods that use a Count

<a id="unreal.MeshApproximationSettings.target_tri_count"></a>

#### target_tri_count

```python
@target_tri_count.setter
def target_tri_count(value: int) -> None
```

<a id="unreal.MeshApproximationSettings.triangles_per_m"></a>

#### triangles_per_m

```python
@property
def triangles_per_m() -> float
```

(float):  [Read-Write] Approximate Number of triangles per Square Meter, for SimplifyMethods that use such a constraint

<a id="unreal.MeshApproximationSettings.triangles_per_m"></a>

#### triangles_per_m

```python
@triangles_per_m.setter
def triangles_per_m(value: float) -> None
```

<a id="unreal.MeshApproximationSettings.geometric_deviation"></a>

#### geometric_deviation

```python
@property
def geometric_deviation() -> float
```

(float):  [Read-Write] Allowable Geometric Deviation in Meters when SimplifyMethod incorporates a Geometric Tolerance

<a id="unreal.MeshApproximationSettings.geometric_deviation"></a>

#### geometric_deviation

```python
@geometric_deviation.setter
def geometric_deviation(value: float) -> None
```

<a id="unreal.MeshApproximationSettings.ground_clipping"></a>

#### ground_clipping

```python
@property
def ground_clipping() -> MeshApproximationGroundPlaneClippingPolicy
```

(MeshApproximationGroundPlaneClippingPolicy):  [Read-Write] Configure how the final mesh should be clipped with a ground plane, if desired

<a id="unreal.MeshApproximationSettings.ground_clipping"></a>

#### ground_clipping

```python
@ground_clipping.setter
def ground_clipping(value: MeshApproximationGroundPlaneClippingPolicy) -> None
```

<a id="unreal.MeshApproximationSettings.ground_clipping_z_height"></a>

#### ground_clipping_z_height

```python
@property
def ground_clipping_z_height() -> float
```

(float):  [Read-Write] Z-Height for the ground clipping plane, if enabled

<a id="unreal.MeshApproximationSettings.ground_clipping_z_height"></a>

#### ground_clipping_z_height

```python
@ground_clipping_z_height.setter
def ground_clipping_z_height(value: float) -> None
```

<a id="unreal.MeshApproximationSettings.estimate_hard_normals"></a>

#### estimate_hard_normals

```python
@property
def estimate_hard_normals() -> bool
```

(bool):  [Read-Write] If true, normal angle will be used to estimate hard normals

<a id="unreal.MeshApproximationSettings.estimate_hard_normals"></a>

#### estimate_hard_normals

```python
@estimate_hard_normals.setter
def estimate_hard_normals(value: bool) -> None
```

<a id="unreal.MeshApproximationSettings.hard_normal_angle"></a>

#### hard_normal_angle

```python
@property
def hard_normal_angle() -> float
```

(float):  [Read-Write]

<a id="unreal.MeshApproximationSettings.hard_normal_angle"></a>

#### hard_normal_angle

```python
@hard_normal_angle.setter
def hard_normal_angle(value: float) -> None
```

<a id="unreal.MeshApproximationSettings.uv_generation_method"></a>

#### uv_generation_method

```python
@property
def uv_generation_method() -> MeshApproximationUVGenerationPolicy
```

(MeshApproximationUVGenerationPolicy):  [Read-Write] Mesh UV Generation Settings

<a id="unreal.MeshApproximationSettings.uv_generation_method"></a>

#### uv_generation_method

```python
@uv_generation_method.setter
def uv_generation_method(value: MeshApproximationUVGenerationPolicy) -> None
```

<a id="unreal.MeshApproximationSettings.initial_patch_count"></a>

#### initial_patch_count

```python
@property
def initial_patch_count() -> int
```

(int32):  [Read-Write] Number of initial patches mesh will be split into before computing island merging

<a id="unreal.MeshApproximationSettings.initial_patch_count"></a>

#### initial_patch_count

```python
@initial_patch_count.setter
def initial_patch_count(value: int) -> None
```

<a id="unreal.MeshApproximationSettings.curvature_alignment"></a>

#### curvature_alignment

```python
@property
def curvature_alignment() -> float
```

(float):  [Read-Write] This parameter controls alignment of the initial patches to creases in the mesh

<a id="unreal.MeshApproximationSettings.curvature_alignment"></a>

#### curvature_alignment

```python
@curvature_alignment.setter
def curvature_alignment(value: float) -> None
```

<a id="unreal.MeshApproximationSettings.merging_threshold"></a>

#### merging_threshold

```python
@property
def merging_threshold() -> float
```

(float):  [Read-Write] Distortion/Stretching Threshold for island merging - larger values increase the allowable UV stretching

<a id="unreal.MeshApproximationSettings.merging_threshold"></a>

#### merging_threshold

```python
@merging_threshold.setter
def merging_threshold(value: float) -> None
```

<a id="unreal.MeshApproximationSettings.max_angle_deviation"></a>

#### max_angle_deviation

```python
@property
def max_angle_deviation() -> float
```

(float):  [Read-Write] UV islands will not be merged if their average face normals deviate by larger than this amount

<a id="unreal.MeshApproximationSettings.max_angle_deviation"></a>

#### max_angle_deviation

```python
@max_angle_deviation.setter
def max_angle_deviation(value: float) -> None
```

<a id="unreal.MeshApproximationSettings.generate_nanite_enabled_mesh"></a>

#### generate_nanite_enabled_mesh

```python
@property
def generate_nanite_enabled_mesh() -> bool
```

(bool):  [Read-Write] Whether to generate a nanite-enabled mesh

<a id="unreal.MeshApproximationSettings.generate_nanite_enabled_mesh"></a>

#### generate_nanite_enabled_mesh

```python
@generate_nanite_enabled_mesh.setter
def generate_nanite_enabled_mesh(value: bool) -> None
```

<a id="unreal.MeshApproximationSettings.nanite_fallback_target"></a>

#### nanite_fallback_target

```python
@property
def nanite_fallback_target() -> NaniteFallbackTarget
```

(NaniteFallbackTarget):  [Read-Write] Which heuristic to use when generating the Nanite fallback mesh.

<a id="unreal.MeshApproximationSettings.nanite_fallback_target"></a>

#### nanite_fallback_target

```python
@nanite_fallback_target.setter
def nanite_fallback_target(value: NaniteFallbackTarget) -> None
```

<a id="unreal.MeshApproximationSettings.nanite_fallback_percent_triangles"></a>

#### nanite_fallback_percent_triangles

```python
@property
def nanite_fallback_percent_triangles() -> float
```

(float):  [Read-Write] Percentage of triangles to keep from source Nanite mesh for fallback. 1.0 = no reduction, 0.0 = no triangles.

<a id="unreal.MeshApproximationSettings.nanite_fallback_percent_triangles"></a>

#### nanite_fallback_percent_triangles

```python
@nanite_fallback_percent_triangles.setter
def nanite_fallback_percent_triangles(value: float) -> None
```

<a id="unreal.MeshApproximationSettings.nanite_fallback_relative_error"></a>

#### nanite_fallback_relative_error

```python
@property
def nanite_fallback_relative_error() -> float
```

(float):  [Read-Write] Reduce Nanite fallback mesh until at least this amount of error is reached relative to size of the mesh.

<a id="unreal.MeshApproximationSettings.nanite_fallback_relative_error"></a>

#### nanite_fallback_relative_error

```python
@nanite_fallback_relative_error.setter
def nanite_fallback_relative_error(value: float) -> None
```

<a id="unreal.MeshApproximationSettings.support_ray_tracing"></a>

#### support_ray_tracing

```python
@property
def support_ray_tracing() -> bool
```

(bool):  [Read-Write] Whether ray tracing will be supported on this mesh. Disable this to save memory if the generated mesh will only be rendered in the distance.

<a id="unreal.MeshApproximationSettings.support_ray_tracing"></a>

#### support_ray_tracing

```python
@support_ray_tracing.setter
def support_ray_tracing(value: bool) -> None
```

<a id="unreal.MeshApproximationSettings.allow_distance_field"></a>

#### allow_distance_field

```python
@property
def allow_distance_field() -> bool
```

(bool):  [Read-Write] Whether to allow distance field to be computed for this mesh. Disable this to save memory if the generated mesh will only be rendered in the distance.

<a id="unreal.MeshApproximationSettings.allow_distance_field"></a>

#### allow_distance_field

```python
@allow_distance_field.setter
def allow_distance_field(value: bool) -> None
```

<a id="unreal.MeshApproximationSettings.multi_sampling_aa"></a>

#### multi_sampling_aa

```python
@property
def multi_sampling_aa() -> int
```

(int32):  [Read-Write] If Value is > 1, Multisample output baked textures by this amount in each direction (eg 4 == 16x supersampling)

<a id="unreal.MeshApproximationSettings.multi_sampling_aa"></a>

#### multi_sampling_aa

```python
@multi_sampling_aa.setter
def multi_sampling_aa(value: int) -> None
```

<a id="unreal.MeshApproximationSettings.render_capture_resolution"></a>

#### render_capture_resolution

```python
@property
def render_capture_resolution() -> int
```

(int32):  [Read-Write] If Value is zero, use MaterialSettings resolution, otherwise override the render capture resolution

<a id="unreal.MeshApproximationSettings.render_capture_resolution"></a>

#### render_capture_resolution

```python
@render_capture_resolution.setter
def render_capture_resolution(value: int) -> None
```

<a id="unreal.MeshApproximationSettings.material_settings"></a>

#### material_settings

```python
@property
def material_settings() -> MaterialProxySettings
```

(MaterialProxySettings):  [Read-Write] Material generation settings

<a id="unreal.MeshApproximationSettings.material_settings"></a>

#### material_settings

```python
@material_settings.setter
def material_settings(value: MaterialProxySettings) -> None
```

<a id="unreal.MeshApproximationSettings.capture_field_of_view"></a>

#### capture_field_of_view

```python
@property
def capture_field_of_view() -> float
```

(float):  [Read-Write]

<a id="unreal.MeshApproximationSettings.capture_field_of_view"></a>

#### capture_field_of_view

```python
@capture_field_of_view.setter
def capture_field_of_view(value: float) -> None
```

<a id="unreal.MeshApproximationSettings.near_plane_dist"></a>

#### near_plane_dist

```python
@property
def near_plane_dist() -> float
```

(float):  [Read-Write]

<a id="unreal.MeshApproximationSettings.near_plane_dist"></a>

#### near_plane_dist

```python
@near_plane_dist.setter
def near_plane_dist(value: float) -> None
```

<a id="unreal.MeshApproximationSettings.use_render_lod_meshes"></a>

#### use_render_lod_meshes

```python
@property
def use_render_lod_meshes() -> bool
```

(bool):  [Read-Write] If true, LOD0 Render Meshes (or Nanite Fallback meshes) are used instead of Source Mesh data. This can significantly reduce computation time and memory usage, but potentially at the cost of lower quality output.

<a id="unreal.MeshApproximationSettings.use_render_lod_meshes"></a>

#### use_render_lod_meshes

```python
@use_render_lod_meshes.setter
def use_render_lod_meshes(value: bool) -> None
```

<a id="unreal.MeshApproximationSettings.enable_simplify_pre_pass"></a>

#### enable_simplify_pre_pass

```python
@property
def enable_simplify_pre_pass() -> bool
```

(bool):  [Read-Write] If true, a faster mesh simplfication strategy will be used. This can significantly reduce computation time and memory usage, but potentially at the cost of lower quality output.

<a id="unreal.MeshApproximationSettings.enable_simplify_pre_pass"></a>

#### enable_simplify_pre_pass

```python
@enable_simplify_pre_pass.setter
def enable_simplify_pre_pass(value: bool) -> None
```

<a id="unreal.MeshApproximationSettings.enable_parallel_baking"></a>

#### enable_parallel_baking

```python
@property
def enable_parallel_baking() -> bool
```

(bool):  [Read-Write] If false, texture capture and baking will be done serially after mesh generation, rather than in parallel when possible. This will reduce the maximum memory requirements of the process.

<a id="unreal.MeshApproximationSettings.enable_parallel_baking"></a>

#### enable_parallel_baking

```python
@enable_parallel_baking.setter
def enable_parallel_baking(value: bool) -> None
```

<a id="unreal.MeshApproximationSettings.print_debug_messages"></a>

#### print_debug_messages

```python
@property
def print_debug_messages() -> bool
```

(bool):  [Read-Write] If true, print out debugging messages

<a id="unreal.MeshApproximationSettings.print_debug_messages"></a>

#### print_debug_messages

```python
@print_debug_messages.setter
def print_debug_messages(value: bool) -> None
```

<a id="unreal.MeshApproximationSettings.emit_full_debug_mesh"></a>

#### emit_full_debug_mesh

```python
@property
def emit_full_debug_mesh() -> bool
```

(bool):  [Read-Write] If true, write the full mesh triangle set (ie flattened, non-instanced) used for mesh generation. Warning: this asset may be extremely large!!

<a id="unreal.MeshApproximationSettings.emit_full_debug_mesh"></a>

#### emit_full_debug_mesh

```python
@emit_full_debug_mesh.setter
def emit_full_debug_mesh(value: bool) -> None
```

<a id="unreal.MaterialProxySettings"></a>