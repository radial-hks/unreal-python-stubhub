## AimOffsetBlendSpace1D Objects

```python
class AimOffsetBlendSpace1D(BlendSpace1D)
```

An Aim Offset is an asset that stores a blendable series of poses to help a character aim a weapon.

**C++ Source:**

- **Module**: Engine
- **File**: AimOffsetBlendSpace1D.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_marker_based_sync`` (bool):  [Read-Write] Whether to allow marker based sync between the samples (it won't force sync if the markers don't exist)
- ``allow_mesh_space_blending`` (bool):  [Read-Write] If set then blending is performed in mesh space if there are per-bone sample smoothing overrides.

  Note that mesh space blending is significantly more expensive (slower) than normal blending when the
  samples are regular animations (i.e. not additive animations that are already set to apply in mesh
  space), and is typically only useful if you want some parts of the skeleton to achieve a pose
  in mesh space faster or slower than others - for example to make the head move faster than the
  body/arms when aiming, so the character looks at the target slightly before aiming at it.

  Note also that blend space assets with additive/mesh space samples will always blend in mesh space, and
  also that enabling this option with blend space graphs producing additive/mesh space samples may cause
  undesired results.
- ``analysis_properties`` (AnalysisProperties):  [Read-Write] Analysis properties for each axis. Note that these can be null. They will be created/set from
  FBlendSpaceDetails::HandleAnalysisFunctionChanged
- ``asset_mapping_table`` (AssetMappingTable):  [Read-Only] Asset mapping table when ParentAsset is set
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``axis_to_scale_animation`` (BlendSpaceAxis):  [Read-Write] If you have input smoothing, this specifies the axis on which to scale the animation playback speed. E.g. for
  locomotion animation, the speed axis will scale the animation speed in order to make up the difference
  between the target and the result of blending the samples.
- ``blend_parameters`` (BlendParameter):  [Read-Write] Blend Parameters for each axis. *
- ``interpolate_using_grid`` (bool):  [Read-Write] If true then interpolation is done via a grid at runtime. If false the interpolation uses the triangulation.
- ``interpolation_param`` (InterpolationParameter):  [Read-Write] Input Smoothing parameters for each input axis
- ``loop`` (bool):  [Read-Write] The default looping behavior of this blend space.
  Asset players can override this
- ``manual_per_bone_overrides`` (Array[PerBoneInterpolation]):  [Read-Write] Per bone sample smoothing settings, which affect the specified bone and all its descendants in the skeleton.
  These act as overrides to the global sample smoothing speed, which means the global sample smoothing speed does
  not affect these bones. Note that they also override each other - so a per-bone setting on the chest will not
  affect the hand if there is a per-bone setting on the arm.
- ``meta_data`` (Array[AnimMetaData]):  [Read-Write] Meta data that can be saved with the asset

  You can query by GetMetaData function
- ``notify_trigger_mode`` (NotifyTriggerMode):  [Read-Write] The current mode used by the BlendSpace to decide which animation notifies to fire. Valid options are:
        - AllAnimations: All notify events will fire
        - HighestWeightedAnimation: Notify events will only fire from the highest weighted animation
        - None: No notify events will fire from any animations
- ``parent_asset`` (AnimationAsset):  [Read-Only] Parent Asset, if set, you won't be able to edit any data in here but just mapping table

  During cooking, this data will be used to bake out to normal asset
- ``per_bone_blend_mode`` (BlendSpacePerBoneBlendMode):  [Read-Write] There are two ways to use per pone sample smoothing: Blend profiles and manually maintaining the per bone overrides.
- ``per_bone_blend_profile`` (BlendSpaceBlendProfile):  [Read-Write] Reference to a blend profile of the corresponding skeleton to be used for per bone smoothing in case the per bone blend mode is set to use a blend profile.
- ``preferred_triangulation_direction`` (PreferredTriangulationDirection):  [Read-Write] Preferred edge direction when the triangulation has to make an arbitrary choice
- ``preview_base_pose`` (AnimSequence):  [Read-Write] Preview Base pose for additive BlendSpace *
- ``preview_pose_asset`` (PoseAsset):  [Read-Write] The default skeletal mesh to use when previewing this asset - this only applies when you open Persona using this asset//
  todo:: note that this doesn't retarget right now
- ``sample_data`` (Array[BlendSample]):  [Read-Write] Sample animation data
- ``scale_animation`` (bool):  [Read-Write] If you have input smoothing, whether to scale the animation speed. E.g. for locomotion animation,
  the speed axis will scale the animation speed in order to make up the difference between the target
  and the result of blending the samples.
- ``skeleton`` (Skeleton):  [Read-Only] Pointer to the Skeleton this asset can be played on .
- ``target_weight_interpolation_ease_in_out`` (bool):  [Read-Write] If set then this eases in/out the sample weight adjustments, using the speed to determine how much smoothing to apply.
- ``target_weight_interpolation_speed_per_sec`` (float):  [Read-Write] If greater than zero, this is the speed at which the sample weights are allowed to change.

  A speed of 1 means a sample weight can change from zero to one (or one to zero) in one second.
  A speed of 2 means that this would take half a second.

  This allows the Blend Space to switch to new parameters without going through intermediate states,
  effectively blending between where it was and where the new target is. For example, imagine we have
  a blend space for locomotion, moving left, forward and right. Now if you interpolate the inputs of
  the blend space itself, from one extreme to the other, you will go from left, to forward, to right.
  As an alternative, by setting this Sample Weight Speed to a value higher than zero, it will go
  directly from left to right, without going through moving forward first.

  Smaller values mean slower adjustments of the sample weights, and thus more smoothing. However, a
  value of zero disables this smoothing entirely.
- ``thumbnail_info`` (ThumbnailInfo):  [Read-Only] Information for thumbnail rendering

<a id="unreal.AnimationSettings"></a>