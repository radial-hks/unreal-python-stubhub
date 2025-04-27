## AvaMarkRole Objects

```python
class AvaMarkRole(EnumBase)
```

EAva Mark Role

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheSequence
- **File**: AvaMarkShared.h

<a id="unreal.AvaMarkRole.NONE"></a>

#### NONE

0: Mark: Does nothing. Used for frame referencing

<a id="unreal.AvaMarkRole.STOP"></a>

#### STOP

1: Stop Point: Waits for 'Continue' input before resuming playback

<a id="unreal.AvaMarkRole.PAUSE"></a>

#### PAUSE

2: Pause Point: Waits a set amount of time before resuming playback

<a id="unreal.AvaMarkRole.JUMP"></a>

#### JUMP

3: Jump Point: Jumps to the nearest Marked Frame with the given Label, or continues playback if it doesn't exist

<a id="unreal.AvaMarkRole.REVERSE"></a>

#### REVERSE

4: Reverse Point: Reverses the Playback Direction

<a id="unreal.AvaMarkSearchDirection"></a>