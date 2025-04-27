## AbcNormalGenerationSettings Objects

```python
class AbcNormalGenerationSettings(StructBase)
```

Abc Normal Generation Settings

**C++ Source:**

- **Plugin**: AlembicImporter
- **Module**: AlembicLibrary
- **File**: AbcImportSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``force_one_smoothing_group_per_object`` (bool):  [Read-Write] Whether or not to force smooth normals for each individual object rather than calculating smoothing groups
- ``hard_edge_angle_threshold`` (float):  [Read-Write] Threshold used to determine whether an angle between two normals should be considered hard, closer to 0 means more smooth vs 1
- ``ignore_degenerate_triangles`` (bool):  [Read-Write] Determines whether or not the degenerate triangles should be ignored when calculating tangents/normals
- ``recompute_normals`` (bool):  [Read-Write] Determines whether or not the normals should be forced to be recomputed
- ``skip_computing_tangents`` (bool):  [Read-Write] Determines whether tangents are computed for GeometryCache. Skipping them can improve streaming performance but may cause visual artifacts where they are required

<a id="unreal.AbcNormalGenerationSettings.__init__"></a>

#### __init__

```python
def __init__(force_one_smoothing_group_per_object: bool = False,
             hard_edge_angle_threshold: float = 0.000000,
             recompute_normals: bool = False,
             ignore_degenerate_triangles: bool = False,
             skip_computing_tangents: bool = False) -> None
```

<a id="unreal.AbcNormalGenerationSettings.force_one_smoothing_group_per_object"></a>

#### force_one_smoothing_group_per_object

```python
@property
def force_one_smoothing_group_per_object() -> bool
```

(bool):  [Read-Write] Whether or not to force smooth normals for each individual object rather than calculating smoothing groups

<a id="unreal.AbcNormalGenerationSettings.force_one_smoothing_group_per_object"></a>

#### force_one_smoothing_group_per_object

```python
@force_one_smoothing_group_per_object.setter
def force_one_smoothing_group_per_object(value: bool) -> None
```

<a id="unreal.AbcNormalGenerationSettings.hard_edge_angle_threshold"></a>

#### hard_edge_angle_threshold

```python
@property
def hard_edge_angle_threshold() -> float
```

(float):  [Read-Write] Threshold used to determine whether an angle between two normals should be considered hard, closer to 0 means more smooth vs 1

<a id="unreal.AbcNormalGenerationSettings.hard_edge_angle_threshold"></a>

#### hard_edge_angle_threshold

```python
@hard_edge_angle_threshold.setter
def hard_edge_angle_threshold(value: float) -> None
```

<a id="unreal.AbcNormalGenerationSettings.recompute_normals"></a>

#### recompute_normals

```python
@property
def recompute_normals() -> bool
```

(bool):  [Read-Write] Determines whether or not the normals should be forced to be recomputed

<a id="unreal.AbcNormalGenerationSettings.recompute_normals"></a>

#### recompute_normals

```python
@recompute_normals.setter
def recompute_normals(value: bool) -> None
```

<a id="unreal.AbcNormalGenerationSettings.ignore_degenerate_triangles"></a>

#### ignore_degenerate_triangles

```python
@property
def ignore_degenerate_triangles() -> bool
```

(bool):  [Read-Write] Determines whether or not the degenerate triangles should be ignored when calculating tangents/normals

<a id="unreal.AbcNormalGenerationSettings.ignore_degenerate_triangles"></a>

#### ignore_degenerate_triangles

```python
@ignore_degenerate_triangles.setter
def ignore_degenerate_triangles(value: bool) -> None
```

<a id="unreal.AbcNormalGenerationSettings.skip_computing_tangents"></a>

#### skip_computing_tangents

```python
@property
def skip_computing_tangents() -> bool
```

(bool):  [Read-Write] Determines whether tangents are computed for GeometryCache. Skipping them can improve streaming performance but may cause visual artifacts where they are required

<a id="unreal.AbcNormalGenerationSettings.skip_computing_tangents"></a>

#### skip_computing_tangents

```python
@skip_computing_tangents.setter
def skip_computing_tangents(value: bool) -> None
```

<a id="unreal.AbcMaterialSettings"></a>