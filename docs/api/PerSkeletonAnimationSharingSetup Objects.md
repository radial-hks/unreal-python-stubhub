## PerSkeletonAnimationSharingSetup Objects

```python
class PerSkeletonAnimationSharingSetup(StructBase)
```

Per Skeleton Animation Sharing Setup

**C++ Source:**

- **Plugin**: AnimationSharing
- **Module**: AnimationSharing
- **File**: AnimationSharingTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additive_anim_blueprint`` (type(Class)):  [Read-Write] Animation blueprint used to apply additive animation on top of other states
- ``animation_states`` (Array[AnimationStateEntry]):  [Read-Write] Definition of different animation states
- ``blend_anim_blueprint`` (type(Class)):  [Read-Write] Animation blueprint used to perform the blending between states
- ``skeletal_mesh`` (SkeletalMesh):  [Read-Write] Skeletal mesh used to setup skeletal mesh components
- ``skeleton`` (Skeleton):  [Read-Write] Skeleton compatible with the animation sharing setup
- ``state_processor_class`` (type(Class)):  [Read-Write] Interface class used when determining which state an actor is in

<a id="unreal.PerSkeletonAnimationSharingSetup.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AnimationSharingScalability"></a>