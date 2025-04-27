## RootMotionModifier_SkewWarp Objects

```python
class RootMotionModifier_SkewWarp(RootMotionModifier_Warp)
```

Root Motion Modifier Skew Warp

**C++ Source:**

- **Plugin**: MotionWarping
- **Module**: MotionWarping
- **File**: RootMotionModifier_SkewWarp.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actual_start_time`` (float):  [Read-Write] Actual playback time when the modifier becomes active
- ``add_translation_easing_curve`` (CurveFloat):  [Read-Write] Custom curve used to add translation when there is none to warp. Only relevant when AddTranslationEasingFunc is set to Custom
- ``add_translation_easing_func`` (AlphaBlendOption):  [Read-Write] Easing function used when adding translation. Only relevant when there is no translation in the animation
- ``animation`` (AnimSequenceBase):  [Read-Write] Source of the root motion we are warping
- ``current_position`` (float):  [Read-Write] Current playback time of the animation
- ``end_time`` (float):  [Read-Write] End time of the warping window
- ``ignore_z_axis`` (bool):  [Read-Write] Whether to ignore the Z component of the translation. Z motion will remain untouched
- ``previous_position`` (float):  [Read-Write] Previous playback time of the animation
- ``rotation_method`` (MotionWarpRotationMethod):  [Read-Write] The method of rotation to use
- ``rotation_type`` (MotionWarpRotationType):  [Read-Write] Whether rotation should be warp to match the rotation of the sync point or to face the sync point
- ``start_time`` (float):  [Read-Write] Start time of the warping window
- ``start_transform`` (Transform):  [Read-Write] Character owner transform at the time this modifier becomes active
- ``total_root_motion_within_window`` (Transform):  [Read-Write] Total root motion within the warping window
- ``warp_max_rotation_rate`` (float):  [Read-Write] Maximum rotation rate in degrees/sec. Will be the value used in constant rotation rate
- ``warp_point_anim_bone_name`` (Name):  [Read-Write]
  TODO:: Hide from the UI when Target != Bone
- ``warp_point_anim_provider`` (WarpPointAnimProvider):  [Read-Write]
- ``warp_point_anim_transform`` (Transform):  [Read-Write]
  TODO:: Hide from the UI when Target != Static
- ``warp_rotation`` (bool):  [Read-Write] Whether to warp the rotation component of the root motion
- ``warp_rotation_time_multiplier`` (float):  [Read-Write] Allow to modify how fast the rotation is warped.
  e.g if the window duration is 2sec and this is 0.5, the target rotation will be reached in 1sec instead of 2sec
- ``warp_target_name`` (Name):  [Read-Write] Name used to find the warp target for this modifier
- ``warp_translation`` (bool):  [Read-Write] Whether to warp the translation component of the root motion
- ``weight`` (float):  [Read-Write] Current blend weight of the animation

<a id="unreal.RootMotionModifier_SkewWarp.add_root_motion_modifier_skew_warp"></a>

#### add_root_motion_modifier_skew_warp

```python
@classmethod
def add_root_motion_modifier_skew_warp(
        cls,
        motion_warping_comp: MotionWarpingComponent,
        animation: AnimSequenceBase,
        start_time: float,
        end_time: float,
        warp_target_name: Name,
        warp_point_anim_provider: WarpPointAnimProvider,
        warp_point_anim_transform: Transform,
        warp_point_anim_bone_name: Name,
        warp_translation: bool = True,
        ignore_z_axis: bool = True,
        warp_rotation: bool = True,
        rotation_type: MotionWarpRotationType = MotionWarpRotationType.DEFAULT,
        rotation_method: MotionWarpRotationMethod = MotionWarpRotationMethod.
    SLERP,
        warp_rotation_time_multiplier: float = 1.000000,
        warp_max_rotation_rate: float = 0.000000
) -> RootMotionModifier_SkewWarp
```

X.add_root_motion_modifier_skew_warp(motion_warping_comp, animation, start_time, end_time, warp_target_name, warp_point_anim_provider, warp_point_anim_transform, warp_point_anim_bone_name, warp_translation=True, ignore_z_axis=True, warp_rotation=True, rotation_type=MotionWarpRotationType.DEFAULT, rotation_method=MotionWarpRotationMethod.SLERP, warp_rotation_time_multiplier=1.000000, warp_max_rotation_rate=0.000000) -> RootMotionModifier_SkewWarp
Add Root Motion Modifier Skew Warp

Args:
    motion_warping_comp (MotionWarpingComponent): 
    animation (AnimSequenceBase): 
    start_time (float): 
    end_time (float): 
    warp_target_name (Name): 
    warp_point_anim_provider (WarpPointAnimProvider): 
    warp_point_anim_transform (Transform): 
    warp_point_anim_bone_name (Name): 
    warp_translation (bool): 
    ignore_z_axis (bool): 
    warp_rotation (bool): 
    rotation_type (MotionWarpRotationType): 
    rotation_method (MotionWarpRotationMethod): 
    warp_rotation_time_multiplier (float): 
    warp_max_rotation_rate (float): 

Returns:
    RootMotionModifier_SkewWarp:

<a id="unreal.DNAAssetImportUI"></a>