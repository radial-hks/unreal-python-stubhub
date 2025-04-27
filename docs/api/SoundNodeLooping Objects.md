## SoundNodeLooping Objects

```python
class SoundNodeLooping(SoundNode)
```

Defines how a sound loops; either indefinitely, or for a set number of times.
Note: The Looping node should only be used for logical or procedural looping such as introducing a delay.
These sounds will not be played seamlessly. If you want a sound to loop seamlessly and indefinitely,
use the Looping flag on the Wave Player node for that sound.

**C++ Source:**

- **Module**: Engine
- **File**: SoundNodeLooping.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child_nodes`` (Array[SoundNode]):  [Read-Write]
- ``loop_count`` (int32):  [Read-Write] The amount of times to loop
- ``loop_indefinitely`` (bool):  [Read-Write] If enabled, the node will continue to loop indefinitely regardless of the Loop Count value.

<a id="unreal.SoundNodeMature"></a>