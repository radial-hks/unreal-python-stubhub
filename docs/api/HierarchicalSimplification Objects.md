## HierarchicalSimplification Objects

```python
class HierarchicalSimplification(StructBase)
```

Hierarchical Simplification

**C++ Source:**

- **Module**: Engine
- **File**: HLODSetup.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_specific_exclusion`` (bool):  [Read-Write]
- ``approximate_settings`` (MeshApproximationSettings):  [Read-Write] Approximate settings, used if SimplificationMethod is Approximate
- ``desired_bound_radius`` (float):  [Read-Write] Desired Bounding Radius for clustering - this is not guaranteed but used to calculate filling factor for auto clustering
- ``desired_filling_percentage`` (float):  [Read-Write] Desired Filling Percentage for clustering - this is not guaranteed but used to calculate filling factor  for auto clustering
- ``merge_setting`` (MeshMergingSettings):  [Read-Write] Merge settings, used if SimplificationMethod is Merge
- ``min_number_of_actors_to_build`` (int32):  [Read-Write] Min number of actors to build LODActor
- ``only_generate_clusters_for_volumes`` (bool):  [Read-Write] Only generate clusters for HLOD volumes
- ``override_draw_distance`` (float):  [Read-Write]
- ``proxy_setting`` (MeshProxySettings):  [Read-Write] Simplification settings, used if SimplificationMethod is Simplify
- ``reuse_previous_level_clusters`` (bool):  [Read-Write] Will reuse the clusters generated for the previous (lower) HLOD level
- ``simplification_method`` (HierarchicalSimplificationMethod):  [Read-Write]
- ``simplify_mesh`` (bool):  [Read-Write]
  deprecated: Property 'bSimplifyMesh' is deprecated.
- ``transition_screen_size`` (float):  [Read-Write] The screen radius an mesh object should reach before swapping to the LOD actor, once one of parent displays, it won't draw any of children.
- ``use_override_draw_distance`` (bool):  [Read-Write]

<a id="unreal.HierarchicalSimplification.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.HierarchicalSimplification.simplify_mesh"></a>

#### simplify_mesh

```python
@property
def simplify_mesh() -> bool
```

(bool):  [Read-Write]
deprecated: Property 'bSimplifyMesh' is deprecated.

<a id="unreal.HierarchicalSimplification.simplify_mesh"></a>

#### simplify_mesh

```python
@simplify_mesh.setter
def simplify_mesh(value: bool) -> None
```

<a id="unreal.CustomInput"></a>