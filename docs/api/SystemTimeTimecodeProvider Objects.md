## SystemTimeTimecodeProvider Objects

```python
class SystemTimeTimecodeProvider(TimecodeProvider)
```

Converts the current system time to timecode, relative to a provided frame rate.

**C++ Source:**

- **Module**: Engine
- **File**: SystemTimeTimecodeProvider.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frame_delay`` (float):  [Read-Write] Number of frames to subtract from the qualified frame time when GetDelayedQualifiedFrameTime or GetDelayedTimecode is called.
  see: GetDelayedQualifiedFrameTime, GetDelayedTimecode
- ``frame_rate`` (FrameRate):  [Read-Write] The frame rate at which the timecode value will be generated.
- ``generate_full_frame`` (bool):  [Read-Write] When generating frame time, should we generate full frame without subframe value.
- ``use_high_performance_clock`` (bool):  [Read-Write] Use the high performance clock instead of the system time to generate the timecode value.
  Using the high performance clock is faster but will make the value drift over time.

<a id="unreal.ViewportStatsSubsystem"></a>