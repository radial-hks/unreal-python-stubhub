## ChaosClothAsset Objects

```python
class ChaosClothAsset(SkinnedAsset)
```

Cloth asset for pattern based simulation.

**C++ Source:**

- **Plugin**: ChaosClothAsset
- **Module**: ChaosClothAssetEngine
- **File**: ClothAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dataflow_asset`` (Dataflow):  [Read-Write] Dataflow asset.
- ``dataflow_terminal`` (str):  [Read-Write] Dataflow Asset terminal node.
- ``disable_below_min_lod_stripping`` (PerPlatformBool):  [Read-Write]
- ``global_force_mip_levels_to_be_resident`` (bool):  [Read-Write] Global and serialized version of ForceMiplevelsToBeResident.
- ``lod_info`` (Array[SkeletalMeshLODInfo]):  [Read-Only] Struct containing information for each LOD level, such as materials to use, and when use the LOD. Not currently editable or customizable through the Dataflow.
- ``materials`` (Array[SkeletalMaterial]):  [Read-Write] List of materials for this cloth asset. Set by the Dataflow evaluation.
- ``min_lod`` (PerPlatformInt):  [Read-Write] Set the Minimum LOD by platform. This property is overriden by "Quality Level Minimum LOD" when "Use Cloth Asset Min LOD Per Quality Levels" is set at the Project level.
- ``min_quality_level_lod`` (PerQualityLevelInt):  [Read-Write] Set the Minimum LOD by Quality Level. This property is used when "Use Cloth Asset Min LOD Per Quality Levels" is set at the Project level. Otherwise, the (per platform) Minimum LOD value is used.
- ``never_stream`` (bool):  [Read-Write]
- ``num_cinematic_mip_levels`` (int32):  [Read-Write] Number of mip-levels to use for cinematic quality.
- ``physics_asset`` (PhysicsAsset):  [Read-Write] Physics asset used for collision. Set by the Dataflow evaluation.
- ``ray_tracing_min_lod`` (int32):  [Read-Write] Minimum raytracing LOD for this asset.
- ``shadow_physics_asset`` (PhysicsAsset):  [Read-Write] Physics asset whose shapes will be used for shadowing when components have bCastCharacterCapsuleDirectShadow or bCastCharacterCapsuleIndirectShadow enabled.
  Only spheres and sphyl shapes in the physics asset can be supported.  The more shapes used, the higher the cost of the capsule shadows will be.
- ``skeleton`` (Skeleton):  [Read-Write] Skeleton asset used at creation time.
  This is of limited use since this USkeleton's reference skeleton might not necessarily match the one created for this asset.
  Set by the Dataflow evaluation.
- ``support_ray_tracing`` (bool):  [Read-Write] Enable raytracing for this asset.

<a id="unreal.ChaosClothAsset.shadow_physics_asset"></a>

#### shadow_physics_asset

```python
@property
def shadow_physics_asset() -> PhysicsAsset
```

(PhysicsAsset):  [Read-Only] Physics asset whose shapes will be used for shadowing when components have bCastCharacterCapsuleDirectShadow or bCastCharacterCapsuleIndirectShadow enabled.
Only spheres and sphyl shapes in the physics asset can be supported.  The more shapes used, the higher the cost of the capsule shadows will be.

<a id="unreal.ChaosClothAssetInteractor"></a>