## AnimationStateEntry Objects

```python
class AnimationStateEntry(StructBase)
```

Animation State Entry

**C++ Source:**

- **Plugin**: AnimationSharing
- **Module**: AnimationSharing
- **File**: AnimationSharingTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additive`` (bool):  [Read-Write] Whether or not this state is an additive state
- ``animation_setups`` (Array[AnimationSetup]):  [Read-Write] Per state animation setup
- ``blend_time`` (float):  [Read-Write] Duration of blending when blending to this state
- ``maximum_number_of_concurrent_instances`` (PerPlatformInt):  [Read-Write] Number of instances that will be created for this state (platform-specific)
- ``next_state`` (uint8):  [Read-Write] State value to which the actors part of an on demand state should be set to when its animation has finished
- ``on_demand`` (bool):  [Read-Write] Flag whether or not this state is an on-demand state, this means that we kick off a unique animation when needed
- ``requires_curves`` (bool):  [Read-Write] Whether or not this animation requires curves or morphtargets to function correctly for follower components
- ``return_to_previous_state`` (bool):  [Read-Write] Flag whether or not we should return to the previous state, only used when this state is an on-demand one
- ``set_next_state`` (bool):  [Read-Write]
- ``state`` (uint8):  [Read-Write] Enum value linked to this state
- ``wiggle_time_percentage`` (float):  [Read-Write] Percentage of 'wiggle' frames, this is used when we run out of available entries in Components, if one of the on-demand animations has started SequenceLength * WiggleFramePercentage ago or earlier,
        it is used instead of a brand new one

<a id="unreal.AnimationStateEntry.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.MetasoundFrontendDocumentMetadata"></a>