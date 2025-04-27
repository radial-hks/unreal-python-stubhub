## AnimSharingInstance Objects

```python
class AnimSharingInstance(Object)
```

Anim Sharing Instance

**C++ Source:**

- **Plugin**: AnimationSharing
- **Module**: AnimationSharing
- **File**: AnimationSharingManager.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``registered_actors`` (Array[Actor]):  [Read-Only] Actors currently registered to be animation driven by the AnimManager using this setup
- ``sharing_actor`` (Actor):  [Read-Only] Actor to which all the running SkeletalMeshComponents used for the sharing are attached to
- ``state_enum`` (Enum):  [Read-Only] Enum class set up by the user to 'describe' the animation states
- ``state_processor`` (AnimationSharingStateProcessor):  [Read-Write] (Blueprint)class instance used for determining the state enum value for each registered actor
- ``used_animation_sequences`` (Array[AnimSequence]):  [Read-Only]

<a id="unreal.CameraRigProxyAsset"></a>