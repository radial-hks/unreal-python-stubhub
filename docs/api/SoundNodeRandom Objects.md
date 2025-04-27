## SoundNodeRandom Objects

```python
class SoundNodeRandom(SoundNode)
```

Selects sounds from a random set

**C++ Source:**

- **Module**: Engine
- **File**: SoundNodeRandom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child_nodes`` (Array[SoundNode]):  [Read-Write]
- ``preselect_at_level_load`` (int32):  [Read-Write] If greater than 0, then upon each level load such a number of inputs will be randomly selected
  and the rest will be removed. This can be used to cut down the memory usage of large randomizing
  cues.
- ``randomize_without_replacement`` (bool):  [Read-Write] Determines whether or not this SoundNodeRandom should randomize with or without
  replacement.

  WithoutReplacement means that only nodes left will be valid for
  selection.  So with that, you are guarenteed to have only one occurrence of the
  sound played until all of the other sounds in the set have all been played.

  WithReplacement means that a node will be chosen and then placed back into the set.
  So one could play the same sound over and over if the probabilities don't go your way :-)
- ``should_exclude_from_branch_culling`` (bool):  [Read-Write] If set to true, this random node will not be culled on load for platforms with a maximum amount of preloaded random branches
   set in project settings
- ``weights`` (Array[float]):  [Read-Write]

<a id="unreal.SoundNodeSoundClass"></a>