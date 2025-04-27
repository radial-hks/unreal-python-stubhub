## ReOrientRootBoneModifier Objects

```python
class ReOrientRootBoneModifier(AnimationModifier)
```

Reorient root bone in the animation while maintaining mesh position and rotation

**C++ Source:**

- **Plugin**: AnimationModifierLibrary
- **Module**: AnimationModifierLibrary
- **File**: ReOrientRootBoneModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``reapply_post_owner_change`` (bool):  [Read-Write] If this is set to true then the animation modifier will call it's reapply function after any change made to the owning asset.
- ``rotator`` (Rotator):  [Read-Write] Rotation to apply to the root

<a id="unreal.ReOrientRootBoneModifier.rotator"></a>

#### rotator

```python
@property
def rotator() -> Rotator
```

(Rotator):  [Read-Only] Rotation to apply to the root

<a id="unreal.ZeroOutRootBoneModifier"></a>