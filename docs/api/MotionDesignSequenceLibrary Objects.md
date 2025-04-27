## MotionDesignSequenceLibrary Objects

```python
class MotionDesignSequenceLibrary(BlueprintFunctionLibrary)
```

Ava Sequence Library

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheSequence
- **File**: AvaSequenceLibrary.h

<a id="unreal.MotionDesignSequenceLibrary.make_single_frame_play_settings"></a>

#### make_single_frame_play_settings

```python
@classmethod
def make_single_frame_play_settings(
        cls, target_time: AvaSequenceTime,
        play_mode: AvaSequencePlayMode) -> AvaSequencePlayParams
```

X.make_single_frame_play_settings(target_time, play_mode) -> AvaSequencePlayParams
Helper function to build Play Settings for Single Frame Playback

Args:
    target_time (AvaSequenceTime): 
    play_mode (AvaSequencePlayMode): 

Returns:
    AvaSequencePlayParams:

<a id="unreal.MotionDesignSequenceLibrary.get_playback_object"></a>

#### get_playback_object

```python
@classmethod
def get_playback_object(
        cls, world_context_object: Object) -> AvaSequencePlaybackObject
```

X.get_playback_object(world_context_object) -> AvaSequencePlaybackObject
Get Playback Object

Args:
    world_context_object (Object): 

Returns:
    AvaSequencePlaybackObject:

<a id="unreal.AvaSequencePlaybackActor"></a>