## ZeroOutRootBoneModifier Objects

```python
class ZeroOutRootBoneModifier(AnimationModifier)
```

Adjust root motion to be relative to the first frame. Optionally cut the start and end sections of the animation that don't have motion on the root.
      This was written to be used when capturing Character Movement motion via Take Recorder. Take Recorder outputs an animation captured from
      a character moving in game in world space, and this modifier zeroes out the root. The animation can then be exported to fbx to be animated against.

**C++ Source:**

- **Plugin**: AnimationModifierLibrary
- **Module**: AnimationModifierLibrary
- **File**: ZeroOutRootBoneModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``clip_end_frames_with_no_motion`` (bool):  [Read-Write] Clip frames at the end of the animation that have no root motion.
- ``clip_start_frames_with_no_motion`` (bool):  [Read-Write] Clip frames at the start of the animation that have no root motion.
- ``reapply_post_owner_change`` (bool):  [Read-Write] If this is set to true then the animation modifier will call it's reapply function after any change made to the owning asset.

<a id="unreal.ZeroOutRootBoneModifier.clip_start_frames_with_no_motion"></a>

#### clip_start_frames_with_no_motion

```python
@property
def clip_start_frames_with_no_motion() -> bool
```

(bool):  [Read-Only] Clip frames at the start of the animation that have no root motion.

<a id="unreal.ZeroOutRootBoneModifier.clip_end_frames_with_no_motion"></a>

#### clip_end_frames_with_no_motion

```python
@property
def clip_end_frames_with_no_motion() -> bool
```

(bool):  [Read-Only] Clip frames at the end of the animation that have no root motion.

<a id="unreal.MotionExtractorModifier"></a>