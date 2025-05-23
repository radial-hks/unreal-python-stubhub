## SoundNodeDistanceCrossFade Objects

```python
class SoundNodeDistanceCrossFade(SoundNode)
```

SoundNodeDistanceCrossFade

This node's purpose is to play different sounds based on the distance to the listener.
The node mixes between the N different sounds which are valid for the distance.  One should
think of a SoundNodeDistanceCrossFade as Mixer node which determines the set of nodes to
"mix in" based on their distance to the sound.

Example:
You have a gun that plays a fire sound.  At long distances you want a different sound than
if you were up close.   So you use a SoundNodeDistanceCrossFade which will calculate the distance
a listener is from the sound and play either:  short distance, long distance, mix of short and long sounds.

A SoundNodeDistanceCrossFade differs from an SoundNodeAttenuation in that any sound is only going
be played if it is within the MinRadius and MaxRadius.  So if you want the short distance sound to be
heard by people close to it, the MinRadius should probably be 0

The volume curve for a SoundNodeDistanceCrossFade will look like this:

                         Volume (of the input)
   FadeInDistance.Max --> _________________ <-- FadeOutDistance.Min
                         /                 \
                        /                   \
                       /                     \
FadeInDistance.Min -->/                       \ <-- FadeOutDistance.Max

**C++ Source:**

- **Module**: Engine
- **File**: SoundNodeDistanceCrossFade.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child_nodes`` (Array[SoundNode]):  [Read-Write]
- ``cross_fade_input`` (Array[DistanceDatum]):  [Read-Write] Each input needs to have the correct data filled in so the SoundNodeDistanceCrossFade is able
  to determine which sounds to play

<a id="unreal.SoundNodeDoppler"></a>