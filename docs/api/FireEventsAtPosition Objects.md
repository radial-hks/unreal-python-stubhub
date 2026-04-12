## FireEventsAtPosition Objects

```python
class FireEventsAtPosition(EnumBase)
```

Indicates at what point in the sequence evaluation events should fire

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneEventTrack.h

<a id="unreal.FireEventsAtPosition.AT_START_OF_EVALUATION"></a>

#### AT\_START\_OF\_EVALUATION

0: Fire events before anything else is evaluated in the sequence

<a id="unreal.FireEventsAtPosition.AT_END_OF_EVALUATION"></a>

#### AT\_END\_OF\_EVALUATION

1: Fire events after everything else has been evaluated in the sequence

<a id="unreal.FireEventsAtPosition.AFTER_SPAWN"></a>

#### AFTER\_SPAWN

2: Fire events right after any spawn tracks have been evaluated

<a id="unreal.TimecodeProviderSynchronizationState"></a>