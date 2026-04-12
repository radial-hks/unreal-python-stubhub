## QuartzCommandType Objects

```python
class QuartzCommandType(EnumBase)
```

An enumeration for specifying Quartz command types

**C++ Source:**

- **Module**: Engine
- **File**: QuartzQuantizationUtilities.h

<a id="unreal.QuartzCommandType.PLAY_SOUND"></a>

#### PLAY\_SOUND

0: Play a sound on a spample-accurate boundary (taking a voice slot immediately)

<a id="unreal.QuartzCommandType.QUEUE_SOUND_TO_PLAY"></a>

#### QUEUE\_SOUND\_TO\_PLAY

1: Queue a sound to play when it gets closer to its quantization boundary (avoids stealing a voice slot right away)

<a id="unreal.QuartzCommandType.RETRIGGER_SOUND"></a>

#### RETRIGGER\_SOUND

2: Quantized looping of the target sound (event tells the AudioComponent to play the sound again)

<a id="unreal.QuartzCommandType.TICK_RATE_CHANGE"></a>

#### TICK\_RATE\_CHANGE

3: Quantized change of the tick-rate (i.e. BPM change)

<a id="unreal.QuartzCommandType.TRANSPORT_RESET"></a>

#### TRANSPORT\_RESET

4: Quantized reset of the clocks transport (back to time = 0 on the boundary)

<a id="unreal.QuartzCommandType.START_OTHER_CLOCK"></a>

#### START\_OTHER\_CLOCK

5: Quantized start of another clock. Useful for sample accurate synchronization of clocks (i.e. to handle time signature changes)

<a id="unreal.QuartzCommandType.NOTIFY"></a>

#### NOTIFY

6: Command used only to get delegates for timing information (basically an empty command)

<a id="unreal.QuartzCommandType.CUSTOM"></a>

#### CUSTOM

7: Quantized custom command

<a id="unreal.ActorUpdateOverlapsMethod"></a>