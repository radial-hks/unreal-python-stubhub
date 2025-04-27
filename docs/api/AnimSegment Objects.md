## AnimSegment Objects

```python
class AnimSegment(StructBase)
```

this is anim segment that defines what animation and how *

**C++ Source:**

- **Module**: Engine
- **File**: AnimCompositeBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``anim_end_time`` (float):  [Read-Write] Time to end playing the AnimSequence at.
- ``anim_play_rate`` (float):  [Read-Write] Playback speed of this animation. If you'd like to reverse, set -1
- ``anim_reference`` (AnimSequenceBase):  [Read-Write] Anim Reference to play - only allow AnimSequence or AnimComposite *
- ``anim_start_time`` (float):  [Read-Write] Time to start playing AnimSequence at.
- ``cached_play_length`` (float):  [Read-Write]
- ``looping_count`` (int32):  [Read-Write]
- ``start_pos`` (float):  [Read-Only] Start Pos within this AnimCompositeBase

<a id="unreal.AnimSegment.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.CompositeSection"></a>