## AnimationSetup Objects

```python
class AnimationSetup(StructBase)
```

Animation Setup

**C++ Source:**

- **Plugin**: AnimationSharing
- **Module**: AnimationSharing
- **File**: AnimationSharingTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``anim_blueprint`` (type(Class)):  [Read-Write] Animation blueprint to use for playing back the Animation Sequence
- ``anim_sequence`` (AnimSequence):  [Read-Write] Animation Sequence to play for this particular setup
- ``enabled`` (PerPlatformBool):  [Read-Write] Whether or not this setup is enabled for specific platforms
- ``num_randomized_instances`` (PerPlatformInt):  [Read-Write] The number of randomized instances created from this setup, it will create instance with different start time offsets (Length / Number of Instance) * InstanceIndex

<a id="unreal.AnimationSetup.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.MetasoundFrontendClassMetadata"></a>