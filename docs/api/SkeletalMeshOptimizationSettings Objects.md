## SkeletalMeshOptimizationSettings Objects

```python
class SkeletalMeshOptimizationSettings(StructBase)
```

FSkeletalMeshOptimizationSettings - The settings used to optimize a skeletal mesh LOD.

**C++ Source:**

- **Module**: Engine
- **File**: SkeletalMeshReductionSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_lod`` (int32):  [Read-Write] Base LOD index to generate this LOD. By default, we generate from LOD 0
- ``enforce_bone_boundaries`` (bool):  [Read-Write] Penalize edge collapse between vertices that have different major bones.  This will help articulated segments like tongues but can lead to undesirable results under extreme simplification
- ``improve_triangles_for_cloth`` (bool):  [Read-Write] Better distribution of triangles on 2d meshes, such as flat cloth, but at the cost of potentially worse UVs in those areas.  This generally has little or no effect for mesh regions that aren't laid out on a plane intersecting the origin such as the xy-plane. When this is disabled, the planar regions may simplify to fewer large triangles.
- ``lock_color_bounaries`` (bool):  [Read-Write] Disallow edge collapse when the vertices do not have a common color
- ``lock_edges`` (bool):  [Read-Write] Preserve cuts in the mesh surface by locking vertices in place.  Increases the quality of the simplified mesh at edges at the cost of more triangles
- ``max_bones_per_vertex`` (int32):  [Read-Write] Maximum number of bones that can be assigned to each vertex.
- ``max_deviation_percentage`` (float):  [Read-Write] If ReductionMethod equals MaxDeviation this value is the maximum deviation from the base mesh as a percentage of the bounding sphere.
  In code, it ranges from [0, 1]. In the editor UI, it ranges from [0, 100]
- ``max_num_of_triangles`` (uint32):  [Read-Write] The maximum number of triangles to retain
- ``max_num_of_triangles_percentage`` (uint32):  [Read-Write] The maximum number of triangles to retain when using percentage termination criterion.
- ``max_num_of_verts`` (uint32):  [Read-Write] The maximum number of vertices to retain
- ``max_num_of_verts_percentage`` (uint32):  [Read-Write] The maximum number of vertices to retain when using percentage termination criterion.
- ``merge_coincident_vert_bones`` (bool):  [Read-Write] If enabled this option make sure vertices that share the same location (e.g. UV boundaries) have the same bone weights. This can fix cracks when the characters animate.
- ``normals_threshold`` (float):  [Read-Write] If the angle between two triangles are above this value, the normals will not be
        smooth over the edge between those two triangles. Set in degrees. This is only used when bRecalcNormals is set to true
- ``num_of_triangles_percentage`` (float):  [Read-Write] The percentage of triangles to retain as a ratio, e.g. 0.1 indicates 10 percent
- ``num_of_vert_percentage`` (float):  [Read-Write] The percentage of vertices to retain as a ratio, e.g. 0.1 indicates 10 percent
- ``recalc_normals`` (bool):  [Read-Write] Whether Normal smoothing groups should be preserved. If true then Hard Edge Angle (NormalsThreshold) is used *
- ``reduction_method`` (SkeletalMeshOptimizationType):  [Read-Write] The method to use when optimizing the skeletal mesh LOD
- ``remap_morph_targets`` (bool):  [Read-Write] Remap the morph targets from the base LOD onto the reduce LOD.
- ``shading_importance`` (SkeletalMeshOptimizationImportance):  [Read-Write] How important shading quality is.
- ``silhouette_importance`` (SkeletalMeshOptimizationImportance):  [Read-Write] How important the shape of the geometry is.
- ``skinning_importance`` (SkeletalMeshOptimizationImportance):  [Read-Write] How important skinning quality is.
- ``termination_criterion`` (SkeletalMeshTerminationCriterion):  [Read-Write] The method to use when optimizing the skeletal mesh LOD
- ``texture_importance`` (SkeletalMeshOptimizationImportance):  [Read-Write] How important texture density is.
- ``volume_importance`` (float):  [Read-Write] Default value of 1 attempts to preserve volume.  Smaller values will loose volume by flattening curved surfaces, and larger values will accentuate curved surfaces.
- ``welding_threshold`` (float):  [Read-Write] The welding threshold distance. Vertices under this distance will be welded.

<a id="unreal.SkeletalMeshOptimizationSettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.SectionReference"></a>