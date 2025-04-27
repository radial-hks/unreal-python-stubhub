## DistanceDatum Objects

```python
class DistanceDatum(StructBase)
```

Distance Datum

**C++ Source:**

- **Module**: Engine
- **File**: SoundNodeDistanceCrossFade.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``fade_in_distance_end`` (float):  [Read-Write] The distance at which this sound has faded in completely.
- ``fade_in_distance_start`` (float):  [Read-Write] The FadeInDistance at which to start hearing this sound.
         * If you want to hear the sound up close then setting this to 0 might be a good option.
- ``fade_out_distance_end`` (float):  [Read-Write] The distance at which this sound is no longer audible.
- ``fade_out_distance_start`` (float):  [Read-Write] The distance at which this sound starts fading out.
- ``volume`` (float):  [Read-Write] The volume for which this Input should be played.

<a id="unreal.DistanceDatum.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.BPVariableMetaDataEntry"></a>