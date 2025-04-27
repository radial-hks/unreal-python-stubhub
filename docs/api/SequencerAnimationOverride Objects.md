## SequencerAnimationOverride Objects

```python
class SequencerAnimationOverride(Interface)
```

Sequencer Animation Override

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: SequencerAnimationOverride.h

<a id="unreal.SequencerAnimationOverride.get_sequencer_anim_slot_names"></a>

#### get_sequencer_anim_slot_names

```python
def get_sequencer_anim_slot_names() -> Array[Name]
```

x.get_sequencer_anim_slot_names() -> Array[Name]
Should return a list of valid slot names for Sequencer to output to in the case that Sequencer is not permitted to nuke the anim instance.
Will be chosen by the user in drop down on the skeletal animation section properties. Should be named descriptively, as in some contexts (UEFN), the user
will not be able to view the animation blueprint itself to determine the mixing behavior of the slot.

Returns:
    Array[Name]:

<a id="unreal.SequencerAnimationOverride.allows_cinematic_override"></a>

#### allows_cinematic_override

```python
def allows_cinematic_override() -> bool
```

x.allows_cinematic_override() -> bool
Whether this animation blueprint allows Sequencer to nuke this anim instance and replace it during Sequencer playback.

Returns:
    bool:

<a id="unreal.AnimationStateMachineLibrary"></a>