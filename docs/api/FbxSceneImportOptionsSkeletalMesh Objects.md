## FbxSceneImportOptionsSkeletalMesh Objects

```python
class FbxSceneImportOptionsSkeletalMesh(Object)
```

Fbx Scene Import Options Skeletal Mesh

**C++ Source:**

- **Module**: UnrealEd
- **File**: FbxSceneImportOptionsSkeletalMesh.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``animation_length`` (FBXAnimationLengthImportType):  [Read-Write] Type of asset to import from the FBX file
- ``create_physics_asset`` (bool):  [Read-Write] If checked, create new PhysicsAsset if it doesn't have it
- ``custom_sample_rate`` (int32):  [Read-Write] Sample fbx animation data at the specified sample rate, 0 find automaticaly the best sample rate
- ``delete_existing_custom_attribute_curves`` (bool):  [Read-Write] If true, all previous node attributes imported as Animation Curves will be deleted when doing a re-import.
- ``delete_existing_morph_target_curves`` (bool):  [Read-Write] Type of asset to import from the FBX file
- ``delete_existing_non_curve_custom_attributes`` (bool):  [Read-Write] If true, all previous node attributes imported as Animation Attributes will be deleted when doing a re-import.
- ``frame_import_range`` (Int32Interval):  [Read-Write] Frame range used when Set Range is used in Animation Length
- ``import_animations`` (bool):  [Read-Write] True to import animations from the FBX File
- ``import_custom_attribute`` (bool):  [Read-Write] If true, import node attributes as either Animation Curves or Animation Attributes
- ``import_meshes_in_bone_hierarchy`` (bool):  [Read-Write] If checked, meshes nested in bone hierarchies will be imported instead of being converted to bones.
- ``import_morph_targets`` (bool):  [Read-Write] If enabled, creates Unreal morph objects for the imported meshes
- ``import_vertex_attributes`` (bool):  [Read-Write] If enabled, import single-channel/weight/alpha vertex attributes
- ``keep_sections_separate`` (bool):  [Read-Write] If checked, sections with matching materials are kept separate and will not get combined.
- ``morph_threshold_position`` (float):  [Read-Write] Threshold to compare vertex position equality when computing morph target deltas.
- ``preserve_local_transform`` (bool):  [Read-Write] Type of asset to import from the FBX file
- ``preserve_smoothing_groups`` (bool):  [Read-Write] If checked, triangles with non-matching smoothing groups will be physically split.
- ``snap_to_closest_frame_boundary`` (bool):  [Read-Write] If enabled, snaps the animation to the closest frame boundary using the import sampling rate
- ``threshold_position`` (float):  [Read-Write] Threshold to compare vertex position equality.
- ``threshold_tangent_normal`` (float):  [Read-Write] Threshold to compare normal, tangent or bi-normal equality.
- ``threshold_uv`` (float):  [Read-Write] Threshold to compare UV equality.
- ``update_skeleton_reference_pose`` (bool):  [Read-Write] If enabled, update the Skeleton (of the mesh being imported)'s reference pose.
- ``use_default_sample_rate`` (bool):  [Read-Write] If enabled, samples all animation curves to 30 FPS

<a id="unreal.FbxSceneImportOptionsStaticMesh"></a>