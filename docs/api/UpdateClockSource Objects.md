## UpdateClockSource Objects

```python
class UpdateClockSource(EnumBase)
```

Enum used to define how to update to a particular time

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneFwd.h

<a id="unreal.UpdateClockSource.TICK"></a>

#### TICK

0: Use the default world tick delta for timing. Honors world and actor pause state, but is susceptible to accumulation errors

<a id="unreal.UpdateClockSource.PLATFORM"></a>

#### PLATFORM

1: Use the platform clock for timing. Does not honor world or actor pause state.

<a id="unreal.UpdateClockSource.AUDIO"></a>

#### AUDIO

2: Use the audio clock for timing. Does not honor world or actor pause state.

<a id="unreal.UpdateClockSource.RELATIVE_TIMECODE"></a>

#### RELATIVE_TIMECODE

3: Time relative to the timecode provider for timing. Does not honor world or actor pause state.

<a id="unreal.UpdateClockSource.TIMECODE"></a>

#### TIMECODE

4: Use current timecode provider for timing. Does not honor world or actor pause state.

<a id="unreal.UpdateClockSource.PLAY_EVERY_FRAME"></a>

#### PLAY_EVERY_FRAME

5: Debugging Tool: Hold on each whole frame for a Sequencer.SecondsPerFrame many wall-clock seconds before advancing to the next one. Does not honor world or actor pause state or time dilation and audio will be out of sync.

<a id="unreal.UpdateClockSource.CUSTOM"></a>

#### CUSTOM

6: Custom clock source created and defined externally.

<a id="unreal.MovieSceneGroupConditionOperator"></a>