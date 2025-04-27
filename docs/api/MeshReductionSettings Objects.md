## MeshReductionSettings Objects

```python
class MeshReductionSettings(StructBase)
```

Settings used to reduce a mesh.

**C++ Source:**

- **Module**: Engine
- **File**: MeshReductionSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_lod_model`` (int32):  [Read-Write]
- ``cull_occluded`` (bool):  [Read-Write]
- ``generate_unique_lightmap_u_vs`` (bool):  [Read-Write]
- ``hard_angle_threshold`` (float):  [Read-Write] Angle at which a hard edge is introduced between faces.
- ``keep_symmetry`` (bool):  [Read-Write]
- ``max_deviation`` (float):  [Read-Write] The maximum distance in object space by which the reduced mesh may deviate from the original mesh.
- ``max_num_of_triangles`` (uint32):  [Read-Write] The maximum number of triangles to retain when using percentage termination criterion. (Triangles criterion properties)
- ``max_num_of_verts`` (uint32):  [Read-Write] The maximum number of vertices to retain when using percentage termination criterion. (Vertices criterion properties)
- ``percent_triangles`` (float):  [Read-Write] Percentage of triangles to keep. 1.0 = no reduction, 0.0 = no triangles. (Triangles criterion properties)
- ``percent_vertices`` (float):  [Read-Write] Percentage of vertices to keep. 1.0 = no reduction, 0.0 = no vertices. (Vertices criterion properties)
- ``pixel_error`` (float):  [Read-Write] The amount of error in pixels allowed for this LOD.
- ``recalculate_normals`` (bool):  [Read-Write]
- ``shading_importance`` (MeshFeatureImportance):  [Read-Write] Higher values try to preserve normals better.
- ``silhouette_importance`` (MeshFeatureImportance):  [Read-Write] Higher values minimize change to border edges.
- ``termination_criterion`` (StaticMeshReductionTerimationCriterion):  [Read-Write] The method to use when optimizing static mesh LODs
- ``texture_importance`` (MeshFeatureImportance):  [Read-Write] Higher values reduce texture stretching.
- ``vertex_color_importance`` (MeshFeatureImportance):  [Read-Write] Higher values minimize change to vertex color data.
- ``visibility_aggressiveness`` (MeshFeatureImportance):  [Read-Write] Higher values generates fewer samples
- ``visibility_aided`` (bool):  [Read-Write]
- ``welding_threshold`` (float):  [Read-Write] Threshold in object space at which vertices are welded together.

<a id="unreal.MeshReductionSettings.__init__"></a>

#### __init__

```python
def __init__(
    percent_triangles: float = 0.000000,
    percent_vertices: float = 0.000000,
    max_deviation: float = 0.000000,
    pixel_error: float = 0.000000,
    welding_threshold: float = 0.000000,
    hard_angle_threshold: float = 0.000000,
    base_lod_model: int = 0,
    silhouette_importance: MeshFeatureImportance = MeshFeatureImportance.OFF,
    texture_importance: MeshFeatureImportance = MeshFeatureImportance.OFF,
    shading_importance: MeshFeatureImportance = MeshFeatureImportance.OFF,
    recalculate_normals: bool = False,
    generate_unique_lightmap_u_vs: bool = False,
    keep_symmetry: bool = False,
    visibility_aided: bool = False,
    cull_occluded: bool = False,
    termination_criterion:
    StaticMeshReductionTerimationCriterion = StaticMeshReductionTerimationCriterion
    .TRIANGLES,
    visibility_aggressiveness: MeshFeatureImportance = MeshFeatureImportance.
    OFF,
    vertex_color_importance: MeshFeatureImportance = MeshFeatureImportance.OFF
) -> None
```

<a id="unreal.MeshReductionSettings.percent_triangles"></a>

#### percent_triangles

```python
@property
def percent_triangles() -> float
```

(float):  [Read-Write] Percentage of triangles to keep. 1.0 = no reduction, 0.0 = no triangles. (Triangles criterion properties)

<a id="unreal.MeshReductionSettings.percent_triangles"></a>

#### percent_triangles

```python
@percent_triangles.setter
def percent_triangles(value: float) -> None
```

<a id="unreal.MeshReductionSettings.percent_vertices"></a>

#### percent_vertices

```python
@property
def percent_vertices() -> float
```

(float):  [Read-Write] Percentage of vertices to keep. 1.0 = no reduction, 0.0 = no vertices. (Vertices criterion properties)

<a id="unreal.MeshReductionSettings.percent_vertices"></a>

#### percent_vertices

```python
@percent_vertices.setter
def percent_vertices(value: float) -> None
```

<a id="unreal.MeshReductionSettings.max_deviation"></a>

#### max_deviation

```python
@property
def max_deviation() -> float
```

(float):  [Read-Write] The maximum distance in object space by which the reduced mesh may deviate from the original mesh.

<a id="unreal.MeshReductionSettings.max_deviation"></a>

#### max_deviation

```python
@max_deviation.setter
def max_deviation(value: float) -> None
```

<a id="unreal.MeshReductionSettings.pixel_error"></a>

#### pixel_error

```python
@property
def pixel_error() -> float
```

(float):  [Read-Write] The amount of error in pixels allowed for this LOD.

<a id="unreal.MeshReductionSettings.pixel_error"></a>

#### pixel_error

```python
@pixel_error.setter
def pixel_error(value: float) -> None
```

<a id="unreal.MeshReductionSettings.welding_threshold"></a>

#### welding_threshold

```python
@property
def welding_threshold() -> float
```

(float):  [Read-Write] Threshold in object space at which vertices are welded together.

<a id="unreal.MeshReductionSettings.welding_threshold"></a>

#### welding_threshold

```python
@welding_threshold.setter
def welding_threshold(value: float) -> None
```

<a id="unreal.MeshReductionSettings.hard_angle_threshold"></a>

#### hard_angle_threshold

```python
@property
def hard_angle_threshold() -> float
```

(float):  [Read-Write] Angle at which a hard edge is introduced between faces.

<a id="unreal.MeshReductionSettings.hard_angle_threshold"></a>

#### hard_angle_threshold

```python
@hard_angle_threshold.setter
def hard_angle_threshold(value: float) -> None
```

<a id="unreal.MeshReductionSettings.base_lod_model"></a>

#### base_lod_model

```python
@property
def base_lod_model() -> int
```

(int32):  [Read-Write]

<a id="unreal.MeshReductionSettings.base_lod_model"></a>

#### base_lod_model

```python
@base_lod_model.setter
def base_lod_model(value: int) -> None
```

<a id="unreal.MeshReductionSettings.silhouette_importance"></a>

#### silhouette_importance

```python
@property
def silhouette_importance() -> MeshFeatureImportance
```

(MeshFeatureImportance):  [Read-Write] Higher values minimize change to border edges.

<a id="unreal.MeshReductionSettings.silhouette_importance"></a>

#### silhouette_importance

```python
@silhouette_importance.setter
def silhouette_importance(value: MeshFeatureImportance) -> None
```

<a id="unreal.MeshReductionSettings.texture_importance"></a>

#### texture_importance

```python
@property
def texture_importance() -> MeshFeatureImportance
```

(MeshFeatureImportance):  [Read-Write] Higher values reduce texture stretching.

<a id="unreal.MeshReductionSettings.texture_importance"></a>

#### texture_importance

```python
@texture_importance.setter
def texture_importance(value: MeshFeatureImportance) -> None
```

<a id="unreal.MeshReductionSettings.shading_importance"></a>

#### shading_importance

```python
@property
def shading_importance() -> MeshFeatureImportance
```

(MeshFeatureImportance):  [Read-Write] Higher values try to preserve normals better.

<a id="unreal.MeshReductionSettings.shading_importance"></a>

#### shading_importance

```python
@shading_importance.setter
def shading_importance(value: MeshFeatureImportance) -> None
```

<a id="unreal.MeshReductionSettings.recalculate_normals"></a>

#### recalculate_normals

```python
@property
def recalculate_normals() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MeshReductionSettings.recalculate_normals"></a>

#### recalculate_normals

```python
@recalculate_normals.setter
def recalculate_normals(value: bool) -> None
```

<a id="unreal.MeshReductionSettings.generate_unique_lightmap_u_vs"></a>

#### generate_unique_lightmap_u_vs

```python
@property
def generate_unique_lightmap_u_vs() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MeshReductionSettings.generate_unique_lightmap_u_vs"></a>

#### generate_unique_lightmap_u_vs

```python
@generate_unique_lightmap_u_vs.setter
def generate_unique_lightmap_u_vs(value: bool) -> None
```

<a id="unreal.MeshReductionSettings.keep_symmetry"></a>

#### keep_symmetry

```python
@property
def keep_symmetry() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MeshReductionSettings.keep_symmetry"></a>

#### keep_symmetry

```python
@keep_symmetry.setter
def keep_symmetry(value: bool) -> None
```

<a id="unreal.MeshReductionSettings.visibility_aided"></a>

#### visibility_aided

```python
@property
def visibility_aided() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MeshReductionSettings.visibility_aided"></a>

#### visibility_aided

```python
@visibility_aided.setter
def visibility_aided(value: bool) -> None
```

<a id="unreal.MeshReductionSettings.cull_occluded"></a>

#### cull_occluded

```python
@property
def cull_occluded() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MeshReductionSettings.cull_occluded"></a>

#### cull_occluded

```python
@cull_occluded.setter
def cull_occluded(value: bool) -> None
```

<a id="unreal.MeshReductionSettings.termination_criterion"></a>

#### termination_criterion

```python
@property
def termination_criterion() -> StaticMeshReductionTerimationCriterion
```

(StaticMeshReductionTerimationCriterion):  [Read-Write] The method to use when optimizing static mesh LODs

<a id="unreal.MeshReductionSettings.termination_criterion"></a>

#### termination_criterion

```python
@termination_criterion.setter
def termination_criterion(
        value: StaticMeshReductionTerimationCriterion) -> None
```

<a id="unreal.MeshReductionSettings.visibility_aggressiveness"></a>

#### visibility_aggressiveness

```python
@property
def visibility_aggressiveness() -> MeshFeatureImportance
```

(MeshFeatureImportance):  [Read-Write] Higher values generates fewer samples

<a id="unreal.MeshReductionSettings.visibility_aggressiveness"></a>

#### visibility_aggressiveness

```python
@visibility_aggressiveness.setter
def visibility_aggressiveness(value: MeshFeatureImportance) -> None
```

<a id="unreal.MeshReductionSettings.vertex_color_importance"></a>

#### vertex_color_importance

```python
@property
def vertex_color_importance() -> MeshFeatureImportance
```

(MeshFeatureImportance):  [Read-Write] Higher values minimize change to vertex color data.

<a id="unreal.MeshReductionSettings.vertex_color_importance"></a>

#### vertex_color_importance

```python
@vertex_color_importance.setter
def vertex_color_importance(value: MeshFeatureImportance) -> None
```

<a id="unreal.MeshUVChannelInfo"></a>