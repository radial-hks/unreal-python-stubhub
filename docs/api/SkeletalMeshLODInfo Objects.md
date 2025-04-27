## SkeletalMeshLODInfo Objects

```python
class SkeletalMeshLODInfo(StructBase)
```

Struct containing information for a particular LOD level, such as materials and info for when to use it.

**C++ Source:**

- **Module**: Engine
- **File**: SkinnedAssetCommon.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_cpu_access`` (bool):  [Read-Write] Keeps this LODs data on the CPU so it can be used for things such as sampling in FX.
- ``allow_mesh_deformer`` (bool):  [Read-Write] Whether a Mesh Deformer applied to the mesh asset or Skinned Mesh Component should be used on this LOD or not
- ``bake_pose`` (AnimSequence):  [Read-Write] Pose which should be used to reskin vertex influences for which the bones will be removed in this LOD level, uses ref-pose by default
- ``bake_pose_override`` (AnimSequence):  [Read-Write] This is used when you are sharing the LOD settings, but you'd like to override the BasePose. This precedes prior to BakePose
- ``bones_to_prioritize`` (Array[BoneReference]):  [Read-Write] Bones which should be prioritized for the quality, this will be weighted toward keeping source data. Use WeightOfPrioritization to control the value.
- ``bones_to_remove`` (Array[BoneReference]):  [Read-Write] Bones which should be removed from the skeleton for the LOD level
- ``build_half_edge_buffers`` (bool):  [Read-Write] If true, we will cache/cook half edge data that provides vertex connectivity information across material sections, which
  may be useful for other systems like Mesh Deformer.
- ``build_settings`` (SkeletalMeshBuildSettings):  [Read-Write] build settings to apply when building render data.
- ``imported_morph_target_source_filename`` (Map[str, MorphTargetImportedSourceFileInfo]):  [Read-Only] Store the custom import morph target source file. The key of the map is the morph target name and the value is the source file path.
- ``lod_hysteresis`` (float):  [Read-Write] Used to avoid 'flickering' when on LOD boundary. Only taken into account when moving from complex->simple.
- ``morph_target_position_error_tolerance`` (float):  [Read-Write] The Morph target position error tolerance in microns. Larger values result in better compression and lower memory footprint, but also lower quality.
- ``reduction_settings`` (SkeletalMeshOptimizationSettings):  [Read-Write] Reduction settings to apply when building render data.
- ``screen_size`` (PerPlatformFloat):  [Read-Write] ScreenSize to display this LOD.
  The screen size is based around the projected diameter of the bounding
  sphere of the model. i.e. 0.5 means half the screen's maximum dimension.
- ``sections_to_prioritize`` (Array[SectionReference]):  [Read-Write] Sections which should be prioritized for the quality, this will be weighted toward keeping source data. Use WeightOfPrioritization to control the value.
- ``skin_cache_usage`` (SkinCacheUsage):  [Read-Write] How this LOD uses the skin cache feature. Auto will defer to the default project global option. If Support Ray Tracing is enabled on the mesh, will imply Enabled
- ``source_import_filename`` (str):  [Read-Only] The filename of the file tha was used to import this LOD if it was not auto generated.
- ``support_uniformly_distributed_sampling`` (bool):  [Read-Write] Mesh supports uniformly distributed sampling in constant time.
  Memory cost is 8 bytes per triangle.
  Example usage is uniform spawning of particles.
- ``vertex_attributes`` (Array[SkeletalMeshVertexAttributeInfo]):  [Read-Write] List of vertex attributes to include for rendering and what type they should be
- ``weight_of_prioritization`` (float):  [Read-Write] How much to consideration to give BonesToPrioritize and SectionsToPrioritize.  The weight is an additional vertex simplification penalty where 0 means nothing.

<a id="unreal.SkeletalMeshLODInfo.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.SkeletalMeshSamplingInfo"></a>