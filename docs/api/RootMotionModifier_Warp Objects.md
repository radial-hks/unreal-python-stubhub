## RootMotionModifier_Warp Objects

```python
class RootMotionModifier_Warp(RootMotionModifier)
```

Root Motion Modifier Warp

**C++ Source:**

- **Plugin**: MotionWarping
- **Module**: MotionWarping
- **File**: RootMotionModifier.h

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

<a id="unreal.RootMotionModifier_Warp.warp_target_name"></a>

#### warp_target_name

```python
@property
def warp_target_name() -> Name
```

(Name):  [Read-Write] Name used to find the warp target for this modifier

<a id="unreal.RootMotionModifier_Warp.warp_target_name"></a>

#### warp_target_name

```python
@warp_target_name.setter
def warp_target_name(value: Name) -> None
```

<a id="unreal.RootMotionModifier_Warp.warp_point_anim_provider"></a>

#### warp_point_anim_provider

```python
@property
def warp_point_anim_provider() -> WarpPointAnimProvider
```

(WarpPointAnimProvider):  [Read-Write]

<a id="unreal.RootMotionModifier_Warp.warp_point_anim_provider"></a>

#### warp_point_anim_provider

```python
@warp_point_anim_provider.setter
def warp_point_anim_provider(value: WarpPointAnimProvider) -> None
```

<a id="unreal.RootMotionModifier_Warp.warp_point_anim_transform"></a>

#### warp_point_anim_transform

```python
@property
def warp_point_anim_transform() -> Transform
```

(Transform):  [Read-Write]
TODO:: Hide from the UI when Target != Static

<a id="unreal.RootMotionModifier_Warp.warp_point_anim_transform"></a>

#### warp_point_anim_transform

```python
@warp_point_anim_transform.setter
def warp_point_anim_transform(value: Transform) -> None
```

<a id="unreal.RootMotionModifier_Warp.warp_point_anim_bone_name"></a>

#### warp_point_anim_bone_name

```python
@property
def warp_point_anim_bone_name() -> Name
```

(Name):  [Read-Write]
TODO:: Hide from the UI when Target != Bone

<a id="unreal.RootMotionModifier_Warp.warp_point_anim_bone_name"></a>

#### warp_point_anim_bone_name

```python
@warp_point_anim_bone_name.setter
def warp_point_anim_bone_name(value: Name) -> None
```

<a id="unreal.RootMotionModifier_Warp.warp_translation"></a>

#### warp_translation

```python
@property
def warp_translation() -> bool
```

(bool):  [Read-Write] Whether to warp the translation component of the root motion

<a id="unreal.RootMotionModifier_Warp.warp_translation"></a>

#### warp_translation

```python
@warp_translation.setter
def warp_translation(value: bool) -> None
```

<a id="unreal.RootMotionModifier_Warp.ignore_z_axis"></a>

#### ignore_z_axis

```python
@property
def ignore_z_axis() -> bool
```

(bool):  [Read-Write] Whether to ignore the Z component of the translation. Z motion will remain untouched

<a id="unreal.RootMotionModifier_Warp.ignore_z_axis"></a>

#### ignore_z_axis

```python
@ignore_z_axis.setter
def ignore_z_axis(value: bool) -> None
```

<a id="unreal.RootMotionModifier_Warp.add_translation_easing_func"></a>

#### add_translation_easing_func

```python
@property
def add_translation_easing_func() -> AlphaBlendOption
```

(AlphaBlendOption):  [Read-Write] Easing function used when adding translation. Only relevant when there is no translation in the animation

<a id="unreal.RootMotionModifier_Warp.add_translation_easing_func"></a>

#### add_translation_easing_func

```python
@add_translation_easing_func.setter
def add_translation_easing_func(value: AlphaBlendOption) -> None
```

<a id="unreal.RootMotionModifier_Warp.add_translation_easing_curve"></a>

#### add_translation_easing_curve

```python
@property
def add_translation_easing_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] Custom curve used to add translation when there is none to warp. Only relevant when AddTranslationEasingFunc is set to Custom

<a id="unreal.RootMotionModifier_Warp.add_translation_easing_curve"></a>

#### add_translation_easing_curve

```python
@add_translation_easing_curve.setter
def add_translation_easing_curve(value: CurveFloat) -> None
```

<a id="unreal.RootMotionModifier_Warp.warp_rotation"></a>

#### warp_rotation

```python
@property
def warp_rotation() -> bool
```

(bool):  [Read-Write] Whether to warp the rotation component of the root motion

<a id="unreal.RootMotionModifier_Warp.warp_rotation"></a>

#### warp_rotation

```python
@warp_rotation.setter
def warp_rotation(value: bool) -> None
```

<a id="unreal.RootMotionModifier_Warp.rotation_type"></a>

#### rotation_type

```python
@property
def rotation_type() -> MotionWarpRotationType
```

(MotionWarpRotationType):  [Read-Write] Whether rotation should be warp to match the rotation of the sync point or to face the sync point

<a id="unreal.RootMotionModifier_Warp.rotation_type"></a>

#### rotation_type

```python
@rotation_type.setter
def rotation_type(value: MotionWarpRotationType) -> None
```

<a id="unreal.RootMotionModifier_Warp.rotation_method"></a>

#### rotation_method

```python
@property
def rotation_method() -> MotionWarpRotationMethod
```

(MotionWarpRotationMethod):  [Read-Write] The method of rotation to use

<a id="unreal.RootMotionModifier_Warp.rotation_method"></a>

#### rotation_method

```python
@rotation_method.setter
def rotation_method(value: MotionWarpRotationMethod) -> None
```

<a id="unreal.RootMotionModifier_Warp.warp_rotation_time_multiplier"></a>

#### warp_rotation_time_multiplier

```python
@property
def warp_rotation_time_multiplier() -> float
```

(float):  [Read-Write] Allow to modify how fast the rotation is warped.
e.g if the window duration is 2sec and this is 0.5, the target rotation will be reached in 1sec instead of 2sec

<a id="unreal.RootMotionModifier_Warp.warp_rotation_time_multiplier"></a>

#### warp_rotation_time_multiplier

```python
@warp_rotation_time_multiplier.setter
def warp_rotation_time_multiplier(value: float) -> None
```

<a id="unreal.RootMotionModifier_Warp.warp_max_rotation_rate"></a>

#### warp_max_rotation_rate

```python
@property
def warp_max_rotation_rate() -> float
```

(float):  [Read-Write] Maximum rotation rate in degrees/sec. Will be the value used in constant rotation rate

<a id="unreal.RootMotionModifier_Warp.warp_max_rotation_rate"></a>

#### warp_max_rotation_rate

```python
@warp_max_rotation_rate.setter
def warp_max_rotation_rate(value: float) -> None
```

<a id="unreal.RootMotionModifier_SimpleWarp"></a>