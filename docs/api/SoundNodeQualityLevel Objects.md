## SoundNodeQualityLevel Objects

```python
class SoundNodeQualityLevel(SoundNode)
```

This SoundNode uses GameUserSettings AudioQualityLevel (or the editor override) to choose which branch to play
and at runtime will only load in to memory sound waves connected to the branch that will be selected

**C++ Source:**

- **Module**: Engine
- **File**: SoundNodeQualityLevel.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child_nodes`` (Array[SoundNode]):  [Read-Write]

<a id="unreal.SoundNodeRandom"></a>