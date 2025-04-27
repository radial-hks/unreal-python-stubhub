## FbxAnimSequenceImportData Objects

```python
class FbxAnimSequenceImportData(FbxAssetImportData)
```

Import data and options used when importing any mesh from FBX

**C++ Source:**

- **Module**: UnrealEd
- **File**: FbxAnimSequenceImportData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``add_curve_metadata_to_skeleton`` (bool):  [Read-Write] Whether to automatically add curve metadata to an animation's skeleton. If this is disabled, curve metadata will be added to skeletal meshes for morph targets, but no metadata entry will be created for general curves.
- ``animation_length`` (FBXAnimationLengthImportType):  [Read-Write] Which animation range to import. The one defined at Exported, at Animated time or define a range manually
- ``convert_scene`` (bool):  [Read-Write] Convert the scene from FBX coordinate system to UE coordinate system
- ``convert_scene_unit`` (bool):  [Read-Write] Convert the scene from FBX unit to UE unit (centimeter).
- ``custom_sample_rate`` (int32):  [Read-Write] Sample fbx animation data at the specified sample rate, 0 find automaticaly the best sample rate
- ``delete_existing_custom_attribute_curves`` (bool):  [Read-Write] If true, all previous node attributes imported as Animation Curves will be deleted when doing a re-import.
- ``delete_existing_morph_target_curves`` (bool):  [Read-Write] If enabled, this will delete this type of asset from the FBX
- ``delete_existing_non_curve_custom_attributes`` (bool):  [Read-Write] If true, all previous node attributes imported as Animation Attributes will be deleted when doing a re-import.
- ``do_not_import_curve_with_zero`` (bool):  [Read-Write] When importing custom attribute or morphtarget as curve, do not import if it doesn't have any value other than zero. This is to avoid adding extra curves to evaluate
- ``force_front_x_axis`` (bool):  [Read-Write] Convert the scene from FBX coordinate system to UE coordinate system with front X axis instead of -Y
- ``frame_import_range`` (Int32Interval):  [Read-Write] Frame range used when Set Range is used in Animation Length
- ``import_bone_tracks`` (bool):  [Read-Write] Import bone transform tracks. If false, this will discard any bone transform tracks. (useful for curves only animations)
- ``import_custom_attribute`` (bool):  [Read-Write] If true, import node attributes as either Animation Curves or Animation Attributes
- ``import_meshes_in_bone_hierarchy`` (bool):  [Read-Write] If checked, meshes nested in bone hierarchies will be imported instead of being converted to bones.
- ``import_rotation`` (Rotator):  [Read-Write]
- ``import_translation`` (Vector):  [Read-Write]
- ``import_uniform_scale`` (float):  [Read-Write]
- ``material_curve_suffixes`` (Array[str]):  [Read-Write] Set Material Curve Type for the custom attribute with the following suffixes. This doesn't matter if Set Material Curve Type is true
- ``preserve_local_transform`` (bool):  [Read-Write] If enabled, this will import a curve within the animation
- ``remove_redundant_keys`` (bool):  [Read-Write] When importing custom attribute as curve, remove redundant keys
- ``set_material_drive_parameter_on_custom_attribute`` (bool):  [Read-Write] Set Material Curve Type for all custom attributes that exists
- ``snap_to_closest_frame_boundary`` (bool):  [Read-Write] If enabled, snaps the animation to the closest frame boundary using the import sampling rate
- ``source_data`` (AssetImportInfo):  [Read-Only] Source file data describing the files that were used to import this asset.
- ``use_default_sample_rate`` (bool):  [Read-Write] If enabled, samples all animation curves to 30 FPS

<a id="unreal.FbxExportOption"></a>