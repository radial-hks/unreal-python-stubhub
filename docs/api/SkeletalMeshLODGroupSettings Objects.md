## SkeletalMeshLODGroupSettings Objects

```python
class SkeletalMeshLODGroupSettings(StructBase)
```

Skeletal Mesh LODGroup Settings

**C++ Source:**

- **Module**: Engine
- **File**: SkeletalMeshLODSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_mesh_deformer`` (bool):  [Read-Write] Whether a Mesh Deformer applied to the mesh asset or Skinned Mesh Component should be used on this LOD or not
- ``bake_pose`` (AnimSequence):  [Read-Write] Pose which should be used to reskin vertex influences for which the bones will be removed in this LOD level, uses ref-pose by default
- ``bone_filter_action_option`` (BoneFilterActionOption):  [Read-Write] Bones which should be removed from the skeleton for the LOD level
- ``bone_list`` (Array[BoneFilter]):  [Read-Write] Bones which should be removed from the skeleton for the LOD level
- ``bones_to_prioritize`` (Array[Name]):  [Read-Write] Bones which should be prioritized for the quality, this will be weighted toward keeping source data. Use WeightOfPrioritization to control the value.
- ``lod_hysteresis`` (float):  [Read-Write] Used to avoid 'flickering' when on LOD boundary. Only taken into account when moving from complex->simple.
- ``reduction_settings`` (SkeletalMeshOptimizationSettings):  [Read-Write] The optimization settings to use for the respective LOD level
- ``screen_size`` (PerPlatformFloat):  [Read-Write] The screen sizes to use for the respective LOD level
- ``sections_to_prioritize`` (Array[int32]):  [Read-Write] Sections which should be prioritized for the quality, this will be weighted toward keeping source data. Use WeightOfPrioritization to control the value.
- ``weight_of_prioritization`` (float):  [Read-Write] How much to consideration to give BonesToPrioritize and SectionsToPrioritize.  The weight is an additional vertex simplification penalty where 0 means nothing.

<a id="unreal.SkeletalMeshLODGroupSettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AudioEffectParameters"></a>