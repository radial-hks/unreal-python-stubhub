## SoundNodeGroupControl Objects

```python
class SoundNodeGroupControl(SoundNode)
```

Plays different sounds depending on the number of active sounds
Any time a new sound is played, the first group that has an available slot will be chosen

**C++ Source:**

- **Module**: Engine
- **File**: SoundNodeGroupControl.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child_nodes`` (Array[SoundNode]):  [Read-Write]
- ``group_sizes`` (Array[int32]):  [Read-Write] How many active sounds are allowed for each group

<a id="unreal.SoundNodeLooping"></a>